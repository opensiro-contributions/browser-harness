"""Real daemon-socket + real CLI admission canary; CDP is deliberately fake.

This exercises concurrent subprocess IPC, owned-target lifecycle and priority
without claiming a live Chrome or deployed-browser result. Linux/POSIX only.

    python tests/integration/owned_admission_ipc_canary.py
"""

import asyncio
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tempfile
import time


class FakeCDP:
    def __init__(self):
        self.counter = 0

    async def send_raw(self, method, params=None, session_id=None):
        self.counter += 1
        if method == "Target.createBrowserContext":
            return {"browserContextId": f"context-{self.counter}"}
        if method == "Target.createTarget":
            return {"targetId": f"target-{self.counter}"}
        if method == "Target.attachToTarget":
            return {"sessionId": f"session-{self.counter}"}
        if method == "Target.getTargetInfo":
            return {"targetInfo": {"targetId": params["targetId"],
                                   "url": "about:blank", "title": "owned",
                                   "type": "page"}}
        return {}


async def run_fake_daemon():
    from browser_harness import daemon

    d = daemon.Daemon()
    d.cdp = FakeCDP()
    d.stop = asyncio.Event()
    monitor_path = Path(os.environ["BH_TEST_WAITERS_PATH"])

    async def monitor():
        while True:
            tmp = monitor_path.with_suffix(".tmp")
            tmp.write_text(str(len(d.scopes._waiters)))
            tmp.replace(monitor_path)
            await asyncio.sleep(0.02)

    watcher = asyncio.create_task(monitor())
    try:
        await daemon.serve(d)
    finally:
        watcher.cancel()
        try:
            await watcher
        except asyncio.CancelledError:
            pass


def request(ipc, name, payload, timeout=10):
    sock, token = ipc.connect(name, timeout=timeout)
    try:
        return ipc.request(sock, token, payload)
    finally:
        sock.close()


def launch_client(env, priority):
    child_env = dict(env, BH_OWNED_TARGET="1", BH_OWNED_WAIT_SECONDS="8",
                     BH_OWNED_PRIORITY=str(priority))
    child = subprocess.Popen(
        [sys.executable, "-m", "browser_harness.run"], stdin=subprocess.PIPE,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=child_env,
    )
    child.stdin.write("print('completed', current_tab()['targetId'])\n")
    child.stdin.close()
    return child


def read_client(child):
    # communicate() flushes stdin unless it has been cleared after close.
    child.stdin = None
    out, err = child.communicate(timeout=15)
    assert child.returncode == 0, (child.returncode, out, err)
    assert out.strip().startswith("completed target-"), (out, err)
    return out.strip()


def run_canary():
    if os.name != "posix":
        raise SystemExit("POSIX socket canary; Windows is not tested")
    root = Path(tempfile.mkdtemp(prefix="bh-admission-ipc-", dir="/tmp"))
    env = dict(os.environ)
    env.update(
        BU_NAME="bh-admission-ipc-canary", BH_RUNTIME_DIR=str(root / "runtime"),
        BH_TMP_DIR=str(root / "tmp"), BH_RECORD="0",
        BH_TELEMETRY="0", BH_UPDATE_CHECK="0",
        BH_TEST_WAITERS_PATH=str(root / "waiters"),
    )
    for key in ("BH_OWNED_TARGET", "BH_OWNED_WAIT_SECONDS", "BH_OWNED_PRIORITY",
                "BH_REQUIRE_EXISTING_DAEMON", "BU_CDP_WS", "BU_CDP_URL"):
        env.pop(key, None)
    # Import ipc only after the isolated runtime/name environment is set.
    os.environ.update({k: env[k] for k in ("BU_NAME", "BH_RUNTIME_DIR", "BH_TMP_DIR")})
    from browser_harness import _ipc as ipc

    daemon = subprocess.Popen(
        [sys.executable, __file__, "--daemon"], env=env,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
    )
    clients = []
    leases = []
    try:
        deadline = time.monotonic() + 10
        while True:
            if daemon.poll() is not None:
                raise RuntimeError("daemon exited before IPC listening")
            try:
                resp = request(ipc, env["BU_NAME"], {"meta": "ping"}, timeout=0.2)
                if resp.get("pong"):
                    break
            except (OSError, TimeoutError, ValueError):
                pass
            if time.monotonic() > deadline:
                raise TimeoutError("daemon IPC did not become available")
            time.sleep(0.05)

        for _ in range(8):
            resp = request(ipc, env["BU_NAME"], {"meta": "begin_owned_target"})
            assert "owned_target" in resp, resp
            leases.append(resp["owned_target"]["scope_id"])
        assert request(ipc, env["BU_NAME"], {"meta": "begin_owned_target"}) == {
            "error": "owned-scope: capacity",
        }

        # A real CLI closing its socket must cancel its queued admission.
        canceled = launch_client(env, priority=5)
        clients.append(canceled)
        waiters_path = root / "waiters"
        deadline = time.monotonic() + 5
        while time.monotonic() < deadline and (
            not waiters_path.exists() or waiters_path.read_text().strip() != "1"
        ):
            time.sleep(0.02)
        assert waiters_path.exists() and waiters_path.read_text().strip() == "1"
        canceled.kill()
        canceled.wait(timeout=5)
        deadline = time.monotonic() + 1.5
        while time.monotonic() < deadline and waiters_path.read_text().strip() != "0":
            time.sleep(0.02)
        assert waiters_path.read_text().strip() == "0", (
            "daemon retained a canceled CLI's admission waiter"
        )

        low = launch_client(env, priority=1)
        clients.append(low)
        high = launch_client(env, priority=9)
        clients.append(high)
        deadline = time.monotonic() + 7
        waiters_path = root / "waiters"
        while time.monotonic() < deadline:
            if low.poll() is not None or high.poll() is not None:
                raise AssertionError("a waiting CLI exited before release")
            try:
                if waiters_path.read_text().strip() == "2":
                    break
            except FileNotFoundError:
                pass
            time.sleep(0.02)
        else:
            raise TimeoutError("two client tasks did not simultaneously queue")

        assert request(ipc, env["BU_NAME"], {
            "scope": leases.pop(), "meta": "end_owned_target",
        })["ok"]
        high_result = read_client(high)
        # The high-priority CLI disposes its scope when its script completes.
        # That release can legitimately admit low before this assertion runs,
        # so compare assigned target sequence instead of process completion time.
        low_result = read_client(low)
        assert high_result != low_result, "two client tasks received one target"
        high_target = int(high_result.rsplit("target-", 1)[1])
        low_target = int(low_result.rsplit("target-", 1)[1])
        assert high_target < low_target, (high_result, low_result)

        for scope in leases:
            assert request(ipc, env["BU_NAME"], {
                "scope": scope, "meta": "end_owned_target",
            })["ok"]
        assert request(ipc, env["BU_NAME"], {"meta": "shutdown"})["ok"]
        daemon.wait(timeout=8)
        assert daemon.returncode == 0, daemon.stderr.read()
        print("real IPC + fake CDP canary: PASS")
        print("priority 9:", high_result)
        print("priority 1:", low_result)
        print("no live browser was executed")
    finally:
        for child in clients:
            if child.poll() is None:
                child.kill()
                child.wait(timeout=3)
            for fd in (child.stdout, child.stderr, child.stdin):
                if fd:
                    fd.close()
        if daemon.poll() is None:
            daemon.send_signal(signal.SIGTERM)
            try:
                daemon.wait(timeout=5)
            except subprocess.TimeoutExpired:
                daemon.kill()
                daemon.wait(timeout=3)
        for fd in (daemon.stdout, daemon.stderr):
            fd.close()
        shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    if "--daemon" in sys.argv:
        asyncio.run(run_fake_daemon())
    else:
        run_canary()
