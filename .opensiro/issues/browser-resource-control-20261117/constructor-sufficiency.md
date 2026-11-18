# Browser Harness — proposed developer-composable S3 current control

**AI/developer contract · PLAN_ONLY / NEEDS_EVIDENCE · NOT IMPLEMENTED.** [Human decision](issue.md) · [Roadmap receipt](roadmap.md).

## Functional scope: S2 vs S3 vs S4 vs S5

S2 regulates collisions between existing S1 agents (tab switches, concurrent access) through serialized work, per-target identity and isolation. S3 would additionally choose among *current* shared browser resource and task commitments with authority and later observed feedback. S3* requires independent corrective audit; logs/video are insufficient. S4 concerns outside/future change options returned to current capacity. S5 owns ultimate identity/policy and is not created by a consent prompt or a static guard.

## 1. Boundary, state, user and developer counterfactual

> **HISTORICAL ACCEPTED INDEX:** \`S1=A · S2=C · S3=— · S3*=— · S4=— · S5=—\` — [pinned assessment](https://github.com/opensiro/vsm-harness-index/blob/d7d07e2f6db17d8ca9bc6c9c6c6d07892c611e1d/assessments/br/browser-harness.md), SHA \`7522febc97e2eff75e78ad781cec9ac64f480a94\`, 2026-09-18 at \`afbcc381b963040c19627d788e40c7e7663171ee\`, Profile 0.2.2 / Methodology 0.3.1. Proposed re-review [#3219](https://github.com/opensiro/vsm-harness-index/pull/3219) remains unmerged. The vector is historical, **not current \`main\`**, nor target state.

Current original public Browser Harness [main@4cccf3b8](https://github.com/browser-use/browser-harness/commit/4cccf3b8daf992227a6c9019ffbce5f7a2844280) offers a single mutable local daemon attached tab, host serialization and remote browser isolation in [SKILL.md](https://github.com/browser-use/browser-harness/blob/4cccf3b8daf992227a6c9019ffbce5f7a2844280/SKILL.md); [helpers.py](https://github.com/browser-use/browser-harness/blob/4cccf3b8daf992227a6c9019ffbce5f7a2844280/src/browser_harness/helpers.py) exposes tab primitives. System in focus: CLI/daemon/skills/MCP used by independently controlled browser task agents, excluding private Cloud backend. [#582](https://github.com/browser-use/browser-harness/issues/582) reports unintended closing of other agents' tabs; [#375](https://github.com/browser-use/browser-harness/issues/375) describes collision from subagents.

**Best current workaround:** host-side serial scheduler with task-owned \`targetId\` list, no closing tabs by URL/title, or one remote browser per simultaneous job. Developer counterfactual: can an independently supplied **S3 current-manager agent** use a first-party bounded decision/action/feedback port for multiple ongoing jobs and produce demonstrably different, useful outcomes beyond that workaround? A need for S2 tab safety alone does not answer yes.

## 2. Verified existing baseline versus still-proposed change

| Source native / proposed | Lifecycle, evidence boundary | Residual need |
| --- | --- | --- |
| [SKILL](https://github.com/browser-use/browser-harness/blob/4cccf3b8daf992227a6c9019ffbce5f7a2844280/SKILL.md) / [helpers](https://github.com/browser-use/browser-harness/blob/4cccf3b8daf992227a6c9019ffbce5f7a2844280/src/browser_harness/helpers.py) | **SHIPPED** tab identity and native serialization/isolation conventions | No verified first-party current-task commitment decision port |
| [#760](https://github.com/browser-use/browser-harness/pull/760) @ \`e285724fabac1cd7cc949a0038013d80055a7aab\` | **OPEN_PR** target-specific multiplexing | S2 interference, not independent manager selection |
| [#846](https://github.com/browser-use/browser-harness/pull/846) @ \`b1e0b7a9a0219a75e9ca6c36338530860da75423\` | **OPEN_PR** tab authorization/guard | Candidate enforcement dependency, not S3 actor |
| [#911](https://github.com/browser-use/browser-harness/pull/911) @ \`c2de9b79115ca38c19c43385b232c83fc0fbd875\` | **OPEN_PR** owned-target preflight | Proposed scope authority, unmerged, may need revision |
| [#1034](https://github.com/browser-use/browser-harness/pull/1034) @ \`4056c5aece6e4a83ea999d60e42482b84f9eed7b\` | **OPEN_PR** exact-tab reconnection | Explicitly does not prevent a concurrent same-daemon race |
| [#765](https://github.com/browser-use/browser-harness/pull/765), [#713](https://github.com/browser-use/browser-harness/pull/713), [#1020](https://github.com/browser-use/browser-harness/pull/1020) | **OPEN_PR** target persistence, safe cleanup, dialog isolation respectively | Inspect differences/test coverage; don't duplicate |
| [Opensiro S3 experiment](https://github.com/opensiro-contributions/browser-harness/blob/opensiro/meta/.opensiro/contributions/browser-harness-s3-owned-scope-priority-admission.json) integrated at [\`ef5c5bc\`](https://github.com/opensiro-contributions/browser-harness/commit/ef5c5bcd92196d33a5b5463a64cfc20f0363895e) | **EXPERIMENT**, includes full unmerged #911 changes; 344 unit PASS/1 SKIP + real-IPC fake-CDP canary previously recorded, NOT rerun here | Real Chrome E2E, independently composed actor, baseline material delta and full owner return unproved |

Do not treat any open PR head as accepted \`main\`; do not manufacture a new contribution record for this plan. Original PR #911 ownership and all proposed state have to be reconsidered at new source HEAD before actual code.

## 3. Proposed minimum S3 first-party construction ports

For a future **genuine C candidate**, require **all five linked first-party properties**, not just interface names:

1. **Current demand observation:** bounded, source-attributed view of authorized \`task_id\`, \`lane_id\`, current task commitment, capacity, principal, target ownership, lease epoch. Do not expose unrelated Chrome targets in health/bootstrap.
2. **Permitted options:** compute real \`admit\`, \`defer\`, \`hold\` and possibly \`safe_reassign\` proposals under versioned current resource pressure, not merely deterministic tab forwarding.
3. **Independent developer-composed decision owner:** documented first-party port for an independently supplied autonomous manager/callback able to select a bounded current-control option; do not hardcode the answer or call an S1 browser agent S3. No installed actor → no fabricated autonomous S3 choice.
4. **Enforced application:** daemon-side atomic owner/lease/version CAS checked before actual attach, action, close, retry and return paths; deny lost/stale scope, unrelated tabs, unauthorized assignment and stale waiting clients. An advisory marker, helper-only check or client-side filtering is insufficient.
5. **Return to later work:** record \`decision_id\`, selected action, effective/denied result and **actual subsequent task/CLI/MCP outcome** consumed by the manager to revise current commitments. A successful mock/fake-CDP queue test does not establish browser/task return.

**Authority:** parent/operator grants authorized users/lanes and retains ultimate policy. S3 decides only within permitted current-control envelope. Existing S2 guard, S1 browser actions, private Cloud rights and downstream task results remain separate. Integration should be reachable through first-party public CLI/MCP and preserve opt-in/default compatibility. A real S3 agent is not obligatory for a simpler native safety fix.

## 4. Priority and dependency decisions

**P0 conditional S3=C:** only if a real multi-job resource choice is materially unmet by host scheduling and the above five-link closure can be built. **P1 first:** reproduce #582-like collision with synthetic tabs, audit original PR heads and current original main, validate existing Opensiro experiment and \`#911\` dependency, test owner/epoch enforcement and real Chrome/CLI, compare native host queue using matched tasks and cost. **P2: NONE:** no independently justified separate parent mode, S4/S5/S3* construction or C→A upgrade.

## 5. Additional optional constructor proposal — NONE

No optional S3 parent-mode or secondary-function constructor is supported by current evidence. Do not infer autonomous/parent grade from generic permissions.

## 6. S3 example acceptance scenarios — adapt to repository (not executed)

These are illustrative, **NOT EXECUTED**, and do not mandate a particular test count/name.

| Example | Real stimulus / choice | Required observable first-party result | Negative / counterfactual |
| --- | --- | --- | --- |
| AC-01 positive | Two owned tasks contend for one browser lane; composed manager admits A, defers B | Actual subsequent A operation on authorized tab; B prevented until release; task outcome/receipt returns to S3 | Queue log only or wrong-tab mutation is not closure |
| AC-02 lawful alternative | Same state, independent manager selects \`hold\` or B | A genuinely different permitted future task outcome | Hardcoded FIFO presented as developer-controlled decision |
| AC-03 missing actor | S3 adapter not installed | No invented autonomous decision; default host/skill S2 behavior remains | Generic hook does not become C |
| AC-04 scope and stale owner | Wrong principal, revoked task, expired epoch, duplicate URL/tab | Fail closed **before** attachment/action/close; do not enumerate unrelated browser metadata | Client-side marker-only check fails |
| AC-05 dead waiter | Client dies waiting on shared resource | Queue slot reclaimed; later eligible action proceeds without wrong reassignment | Prior experiment found and fixed a waiter leak; record is historical, not real Chrome proof |
| AC-06 baseline/compatibility | Existing single agent and two tasks on current CLI/MCP | No regression in normal safe serial mode; no forced new Cloud auth | Requiring controller for every user is invalid |
| AC-07 matched native outcome | Same synthetic two-agent race using plain host queue, isolated remote browser, proposed constructor | Compare observed wrong-tab rate, task outcome and engineering+maintenance cost | If no extra real value, \`NO_USEFUL_CHANGE\` |

No fresh tests are run by this plan. Existing [fork event/experiment](https://github.com/opensiro-contributions/browser-harness/blob/opensiro/meta/.opensiro/contributions/browser-harness-s3-owned-scope-priority-admission.json) has prior 344/1 native unit and fake-CDP socket evidence only.

## 7. Falsification, exclusions and evidence ownership

If source-native host scheduler and task-owned target IDs prevent the observed harm with equal or better cost, conclude **NO_USEFUL_CHANGE** for new S3 API. If independently delegated manager rights, enforced state transition or later task feedback remain unproved, conclude **NEEDS_EVIDENCE** (the current disposition). If rights, source policy, fork PAUSE/STOP or original PR dependencies block a later implementation, report **IMPLEMENTATION_BLOCKED** without bypass.

[Original Browser Harness](https://github.com/browser-use/browser-harness) owns shipped code and maintainer decisions; [Index](https://github.com/opensiro/vsm-harness-index/blob/d7d07e2f6db17d8ca9bc6c9c6c6d07892c611e1d/assessments/br/browser-harness.md) owns the accepted historical assessment; [fork S3 record](https://github.com/opensiro-contributions/browser-harness/blob/opensiro/meta/.opensiro/contributions/browser-harness-s3-owned-scope-priority-admission.json) owns independent experimental tests/branch history; this \`.opensiro/issues\` case owns *only* planning. No external issue/comment/PR or Index regrade is implied. Costs **NOT_MEASURED**; compare matched host queue versus proposed constructor before claiming reduced effort.
