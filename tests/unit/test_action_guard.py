import os
import sqlite3
import subprocess
import sys
import threading
import time

import pytest

from browser_harness.action_guard import guarded_action, ActionOutcomeUnknown, ActionIdentityMismatch


def test_first_and_recovery(tmp_path):
    state = {"n": 0}
    def action():
        state["n"] += 1
    verify = lambda: state["n"] == 1
    assert guarded_action("x", expected="one", action=action, verify=verify, workspace=tmp_path, wait_seconds=0)["executed"]
    assert not guarded_action("x", expected="one", action=lambda: pytest.fail("duplicate"), verify=verify, workspace=tmp_path, wait_seconds=0)["executed"]
    assert state["n"] == 1


def test_uncertain_never_retries(tmp_path):
    seen = []
    with pytest.raises(ActionOutcomeUnknown):
        guarded_action("uncertain", expected="outcome", action=lambda: seen.append(1), verify=lambda: False, workspace=tmp_path, wait_seconds=0)
    with pytest.raises(ActionOutcomeUnknown):
        guarded_action("uncertain", expected="outcome", action=lambda: seen.append(2), verify=lambda: False, workspace=tmp_path, wait_seconds=0)
    assert seen == [1]
    assert not guarded_action("uncertain", expected="outcome", action=lambda: pytest.fail("duplicate"), verify=lambda: True, workspace=tmp_path, wait_seconds=0)["executed"]


def test_process_crash_persists_intent(tmp_path):
    script = ("import os;from browser_harness.action_guard import guarded_action;"
              f"guarded_action('crash',expected='task-1',workspace={str(tmp_path)!r},"
              "action=lambda:os._exit(71),verify=lambda:False,wait_seconds=0)")
    result = subprocess.run([sys.executable, "-c", script], capture_output=True)
    assert result.returncode == 71
    with sqlite3.connect(tmp_path / ".browser-harness" / "action-intents.sqlite3") as conn:
        assert conn.execute("select state from action_intents").fetchone() == ("intent",)
    with pytest.raises(ActionOutcomeUnknown):
        guarded_action("crash", expected="task-1", action=lambda: pytest.fail("replayed"), verify=lambda: False, workspace=tmp_path, wait_seconds=0)
    assert not guarded_action("crash", expected="task-1", action=lambda: pytest.fail("replayed"), verify=lambda: True, workspace=tmp_path, wait_seconds=0)["executed"]


def test_mismatched_identity_or_bad_verifier(tmp_path):
    with pytest.raises(ActionOutcomeUnknown):
        guarded_action("same", expected="a", action=lambda: None, verify=lambda: False, workspace=tmp_path, wait_seconds=0)
    with pytest.raises(ActionIdentityMismatch):
        guarded_action("same", expected="b", action=lambda: pytest.fail("mismatch"), verify=lambda: True, workspace=tmp_path, wait_seconds=0)
    with pytest.raises(ActionOutcomeUnknown):
        guarded_action("bad", expected="a", action=lambda: pytest.fail("truthy is not evidence"), verify=lambda: "yes", workspace=tmp_path, wait_seconds=0)


def test_concurrent_callers_execute_once(tmp_path):
    barrier = threading.Barrier(2)
    success = threading.Event()
    executed = []
    outputs = []
    def action():
        executed.append(1)
        time.sleep(0.1)
        success.set()
    def worker():
        barrier.wait()
        outputs.append(guarded_action("shared", expected="one", action=action, verify=success.is_set, workspace=tmp_path, wait_seconds=1))
    ts = [threading.Thread(target=worker) for _ in range(2)]
    for t in ts: t.start()
    for t in ts: t.join(timeout=4)
    assert not any(t.is_alive() for t in ts)
    assert executed == [1]
    assert sorted(v["executed"] for v in outputs) == [False, True]


def test_completed_result_disappears_without_replaying(tmp_path):
    state = [False]
    def action(): state[0] = True
    assert guarded_action("change", expected="one", action=action, verify=lambda: state[0], workspace=tmp_path, wait_seconds=0)["executed"]
    state[0] = False
    with pytest.raises(ActionOutcomeUnknown):
        guarded_action("change", expected="one", action=lambda: pytest.fail("must not repeat"), verify=lambda: False, workspace=tmp_path, wait_seconds=0)
