# Browser Harness — source-native S3 construction contract (AI/developer)

**PLAN_ONLY · proposal-stage GO · research NEEDS_EVIDENCE · NOT IMPLEMENTED · DRAFT — NOT PUBLISHED**

**Human decision:** [issue.md](issue.md). **Canonical receipt and historical accepted vector:** [roadmap.md](roadmap.md). Do not treat this proposed target as a changed Index assessment.

**Target transition:** S3=— -> S3=C
**Proposal-stage decision:** GO
**Research disposition:** NEEDS_EVIDENCE

## 1. First-party boundary, function and owner

Pinned original: [browser-use/browser-harness@fe4a2cd3dd308e8de929621e64e7f284d7a124d7](https://github.com/browser-use/browser-harness/commit/fe4a2cd3dd308e8de929621e64e7f284d7a124d7). This is the standard-distribution browser control layer: Python CLI, CDP helpers, daemon, admin, MCP and skill. External Codex/Claude/Cursor workers are S1 browser actors; private Browser Use Cloud service, an arbitrary host's own manager, and repo CI/maintainer organization are not attributed as already-shipped first-party S3.

**Disturbance:** competing browser task commitments across one serialized local lane, isolated remote lanes and browser-budget/permission restrictions. [Issue #375](https://github.com/browser-use/browser-harness/issues/375) and [#582](https://github.com/browser-use/browser-harness/issues/582) show real multi-task interference, but not proven need for dynamic autonomous whole-work decisions. S2 already attenuates collision. S3 would decide **which current tasks and commitments obtain authorized resources under priorities/caps**. This is not task decomposition or individual tab ownership.

**Decisive right:** developer-composed autonomous resource manager chooses from allowed admit_local, defer, or admit_remote options. **Authority:** parent host/user grants eligible task identities, available lanes and cloud budget; manager cannot alter parent identity/policy. **Supporting mechanism:** daemon and admin enforce the selected decision. **Return:** a later real browser action result, denial or task completion tied to decision_id and observed by the SAME S3 manager, changing later priorities/commitments.

**Counterfactual:** remove the agent manager: the normal host can still serially operate the browser, but opt-in S3 resource-choice discretion does not exist; deterministic checks simply deny or use an explicitly authorized fallback. No S3=A is claimed.

## 2. Source-pinned Track A vs Track B

| Needed S3-specific property | Track A original native / issue or PR | Track B first-party delta | Refutation |
| --- | --- | --- | --- |
| Present commitments and resources | [SKILL](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/SKILL.md) one mutable local lane vs separate remote; [daemon](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/daemon.py) attached session; [admin](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/admin.py) cloud provisioning | Opt-in scoped task/lane commitments, capacity/budget, live epoch and priority snapshot, never enumerate unrelated tabs | If only tab IDs exist, this is S2 substrate, not S3 view |
| Bounded lawful alternatives | Existing host chooses serialization or cloud; open [#1022](https://github.com/browser-use/browser-harness/pull/1022) at 06e4d7ca0d7327a0b5b886604ba7d35547f0a728 prevents cross-agent tab races | Produce permitted admit_local/defer/admit_remote options under parent caps | Hardcoded transport scheduling not discretionary control |
| Composed S3 owner | [CLI](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/run.py) and [MCP](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/mcp_server.py) have generic browser calls, not this S3 port | First-party request/decision API specifically for resource/commitment selection; developer binds autonomous manager actor | No actor-choice or authorization leads to generic callback, not C |
| Enforcement and scope | [helpers](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/helpers.py) raw cdp() and IPC; [#911](https://github.com/browser-use/browser-harness/pull/911) and [#760](https://github.com/browser-use/browser-harness/pull/760) OPEN owner scope proposals | Server-side atomic lease/epoch check before opted-in CDP attach, input, navigate, close and cloud provisioning | Client-side check, stale lease or raw CDP bypass |
| Subsequent corrective feedback | Daemon returns action status; [recorder](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/recorder.py) logs; [#1039](https://github.com/browser-use/browser-harness/pull/1039) OPEN run self-report | decision_id ↔ actual later browser action/denial ↔ bounded task release/failure event, manager sees new snapshot | Queue receipt or unverified S1 success claim is insufficient |
| Other functions | [#1025](https://github.com/browser-use/browser-harness/pull/1025) OPEN saved-script drift detection, video/privacy review and host permission | NONE for S3*/S4/S5 in this P0; keep existing functions/parent separate | No cargo-cult upgrade to all six |

All referenced original PRs were open when inspected and NOT included in pinned main. In particular #1022 belongs to tab ownership/S2; it is a reusable safety dependency and not an S3 decision actor. #1025 and #1039 cannot be silently treated as shipped. The user/operator request for autonomous resource management is HYPOTHETICAL; the S2 shared-work pressure itself is OBSERVED.

## 3. Minimum complete first-party C design

The necessary design may use one resource-admission module under src/browser_harness, exposed at supported CLI/MCP and enforced by the daemon, rather than a new standalone management framework. Exact physical port count is not prescribed.

**Source-native proposed flow:**

1. First-party opt-in host submits scoped task_id, principal, current commitment, priority/deadline, permitted lanes and parent-signed/validated budget. A snapshot returns bounded current capacity/leases and versions; it must NOT reveal other agents' pages or credentials.
2. First-party S3 interface returns valid options local/admit, defer, remote/admit only if separately authorized; developer-supplied autonomous manager decides. No manager means explicit safe abstention, not fictitious autonomy.
3. Manager submits decision with snapshot version. The daemon (and remote-provisioning path in admin) atomically verifies principal, lane, lease and epoch before browser side effects. Stale, lost or revoked owners cannot act, including through raw CDP/MCP.
4. First-party return path correlates decision_id with later browser operation result, error/denial and bounded task completion/release; the manager receives that changed commitment state and can exercise a new current-resource decision.
5. Existing single-agent local workflow remains default when opt-in not configured; cloud keys, liveUrl and nontrivial billing stay under parent budget and authentication. A manager cannot self-authorize them.

**Why this is proposed C, not already A or a generic hook:** original first-party substrate includes action and cloud lifecycle endpoints, but lacks a resource-specific discretionary owner port and feedback. A developer must compose an independent autonomous S3 manager with real bounded authority. The proposed native port is function-specific, reaches later S1 behaviour, and provides return; it would be eligible for independent Index assessment **only after** original first-party implementation and evidence, never from this plan.

**P0:** S3=— -> S3=C. **P1:** scoped state, #1022 interoperability, lease enforcement at IPC edge, permission/billing guards, real feedback, native modes and matched A/B tests. **P2:** NONE. No S3*/S4/S5 policy agents or unrequested parent modes.

## 4. Derived future acceptance (NOT_RUN)

Source-native test command in [AGENTS.md](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/AGENTS.md): uv run --with pytest python -m pytest tests/unit -q. Python 3.12.3 was present in the inspected dev-alpha-2 runner; neither uv nor pytest was installed. Python AST-only parse of 33 tracked source/test Python files succeeded; **no native pytest was executed**. Integration tests may require a live browser/CDP.

| Test | Setup | Positive/negative witness |
| --- | --- | --- |
| Competing tasks and alternative decisions | Two task identities A/B, one shared local lane, independent supplied manager | Manager chooses admit A/defer B, browser actually executes A and denies B; alternate lawful choice reverses results; decision-aware feedback changes subsequent manager snapshot |
| Authorized capacity expansion | Task A requires local signed-in Chrome, B allows remote; explicit max_cloud=1 and authenticated cloud | Manager chooses A local/B remote; correct later browser instances/actions; max_cloud=0 or missing credentials fails closed before remote API or charges |
| Stale/revoked owner and race | Concurrent clients, same tab URL, task identity mismatch, stale epoch, dead waiter | No action or tab metadata leakage across owners; invalid lease denied before attach/navigate/close; released capacity returns to manager |
| Missing manager and default compatibility | No S3 composition and standard CLI/MCP existing modes | No fabricated choice, opt-in fails closed; default single-agent behaviour unchanged |
| Native economic counterfactual | Same work and browser-budget constraints under host FIFO/priority queue and cloud isolation | Compare complete task outcome, right-tab effects, engineering/review/maintenance cost and cloud bill; stop if simpler path is at least as useful and cheaper |

**Falsifier:** if no distinct lawful whole-current decision and server effect/feedback can be established, the design is not a complete S3=C constructor. If an existing host queue accomplishes the same with less total cost or the upstream maintainer rejects the scope, decline to implement despite proposal-stage GO. No numeric benefit, PASS count, user demand or release claims inferred.

## 5. Ownership, prior comparison and handoff

**Proposal-stage decision:** GO
**Research disposition:** NEEDS_EVIDENCE
**Target transition:** S3=— -> S3=C

**Validation state:** NOT_RUN. **Cost status:** NOT_MEASURED.

Index owns accepted assessment and regrading; Profile and Skills own VSM semantics/method; original owns code and PR decisions; fork-local [roadmap.md](roadmap.md) owns this proposal and [issue.md](issue.md) its Human rendering. Prior [2026-11-19 NO_GO revision](https://github.com/opensiro-contributions/browser-harness/commit/c6df76d4eee6190a65623c85f76147f0ba7f87c1) was read only after independently selecting this C path and remains an attributed historical decision.

**No product source edit, public fork Issue, original Issue/comment/PR, charged cloud call or Index grade is claimed.** Implementation and outward publication need independent permissions. AI-generated plan, not independently human-reviewed code.
