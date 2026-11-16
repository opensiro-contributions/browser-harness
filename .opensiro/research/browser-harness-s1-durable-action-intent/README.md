# Browser Harness S1  durable action intent / capability-delta receipt

**Original:** browser-use/browser-harness@8ec26f6974015a78eaf5494fe35bb9ba1f6b3598
**Product commit:** opensiro-contributions/browser-harness@0be45c484fe3a7a721bad48f37dc288ca9ee0fbc
**Gate (human report only):** MATERIAL_DELTA_SUPPORTED for this bounded delayed-commit/restart scenario, not general exactly-once or production reliability.
**Origin:** ASSESSMENT_INFORMED; no Index-first prediction established.

## Actor, task and VSM mechanism

A browser-task agent may submit a non-idempotent operation then terminate before server acknowledgement; blindly rerunning it creates duplicate side effects. browser-harness#675 reports falsely successful writes, issue #662 reports silent input no-ops, and #998 reports lost tab attachment. The pinned Sep 18 VSM assessment locates agent action selection and read-back closure in S1 and identifies the agent-editable workspace. This informed a first-party S1 durable-intent/reconciliation contract, not a new VSM function or grade.

## Baseline / best workaround

Original main supplies js/page_info checks and an agent-writable agent_helpers.py; expert users can build their own durable log. But an immediate count=0 while a remote commit is in flight does not prove retry safety. This is more than a generic wait_for_element helper.

Pre-code source-pinned loopback fixture SHA256: 7f6023f72de194b0296b9c051704f6c94498b3b0d9d0aa4cce59aa229e190c72. Slow actions have a 1.5-second server commit delay. Two sequential unmodified Browser Harness CLI invocations for task slowb yielded TWO server-side receipts: 7aff7a932816 and bf69ac7c31cc. The baseline represents a naive retry, not the strongest hand-built application checkpoint.

## After-state and independent feedback

Candidate saves an SQLite intent before running the callback and reconciles existing intent by rechecking the app. It never automatically repeats on an unknown result. Native Chrome 157 and separate CLI processes produced:
- slowguard: process exit 71 after click; independent new CLI verified the remote result without rerunning action; server count=1 (receipt b02307b3058e).
- slowmissing: process exit 72 before callback; new CLI refused execution with ActionOutcomeUnknown; server count=0.
- slownormal: normal completion verified on server, executed=True; count=1.
- Native same-environment unit suites: original 266 passed, 1 skipped; candidate 272 passed, 1 skipped. Compile and diff checks passed.

## Overlap and limits

Pending #768 covers conditional wait, #791 Input delivery, #1034 tab reconnection and #1022/#1031 tab ownership. None provides this persistent action-intent guard. Verification is a caller-supplied boolean and must read a trustworthy server-backed outcome. No general exactly-once guarantee, site transaction, authorization, tab isolation, autonomous agent benchmark, production effectiveness or VSM grade change is claimed. Lost SQLite/workspace or an incorrect verifier removes the protection. Unknown outcome requires explicit operator reconciliation; no automatic retry.

**Publication:** product branch tested; fork-local and third-party PRs NOT CREATED pending exact proposal approval. No OpenSiro-only files on the product branch.
