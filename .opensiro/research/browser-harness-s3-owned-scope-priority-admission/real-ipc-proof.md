# Real IPC cancellation regression and bounded admission — 2026-11-16

Selected original: `browser-use/browser-harness@8ec26f6974015a78eaf5494fe35bb9ba1f6b3598`. Canonical Index assessment historical date 2026-09-18, source `afbcc381b963040c19627d788e40c7e7663171ee`. Open dependency: [browser-use/browser-harness PR #911](https://github.com/browser-use/browser-harness/pull/911) at `c2de9b79115ca38c19c43385b232c83fc0fbd875`; no merge or human acceptance claimed.

## Before/after result

The dependent experiment [6160b0e](https://github.com/opensiro-contributions/browser-harness/commit/6160b0eebde89aaab40c1cbb284e32b89c91907c) passed its original 344 unit tests but a new *real local UNIX socket / real CLI process* canary reproduced an abandoned waiting scope after a CLI process was killed: `AssertionError: daemon retained a canceled CLI's admission waiter`. A separate nondeterministic draft assertion initially raced with the second process's queue registration; the canary was corrected to wait until both remote waiters appeared before releasing a slot.

The revised [7eba114](https://github.com/opensiro-contributions/browser-harness/commit/7eba11415aac4dcbf703516f170db6d4e22b24ba) cancels pending daemon admission when the peer disconnects. If client disconnect races with admission completion, the daemon disposes the newly allocated scope before returning; if result write fails, it likewise attempts scoped cleanup. This is a bounded lifecycle fix, **not** a claim that all post-admission process crashes or resource failures are automatically repaired.

Native verification on dev-alpha-2 in a **clean detached worktree of exact remote head**:

```sh
PYTHONPATH=src python -m pytest tests/unit -q
# 344 passed, 1 skipped (11.06 s)
PYTHONPATH=src python tests/integration/owned_admission_ipc_canary.py
# PASS, repeated 3 times on remote exact head;
# 5 other PASS repeats during local development
git diff --check
# PASS
```

The canary proves that eight scopes occupy the shared budget, a ninth immediately refuses by default, a killed waiting CLI loses its queue slot, two live waiting CLI processes are admitted by operator priority 9 before priority 1, each CLI gets a different target, and all contexts release via IPC. The test uses **real Unix sockets, real daemon server and real CLI subprocesses**, but deliberately substitutes `FakeCDP`: no real Chrome page, navigation or external site was tested.

Available Playwright Chromium headless in dev-alpha-2 could not start due to missing system shared libraries (including `libglib-2.0.so.0`, `libnss3.so`). There is no live browser proof and no 300-task user-level test. An external host's own queue remains a plausible alternative, so **material comparative benefit is not yet independently established**. S3 decision priority remains parent/operator-assigned, not autonomous first-party S3. S4 adaptation remains `DELTA_PENDING`.

**Publication boundaries:** only the existing `opensiro-contributions/browser-harness` product branch was updated. No fork-local review PR, original upstream PR, comments or changes to author PR #911 were made. All OpenSiro state/proof remains on `opensiro/meta`. Fork-wide state ACTIVE/ALLOW is preserved as last independently verified; it is not consent to public publication.
