# Proposal: opt-in task-level browser resource admission for Browser Harness

This is a **plan-only, optional architecture proposal**, adapted from one existing OpenSiro Roadmap case. It is not a report of a shipped feature or a request to replace Browser Harness's current concurrency guidance.

## Proposal in the project's own terms

### Before submitting

- [ ] I searched existing issues and discussions.
- [ ] This is a feature request, not a bug.

### Problem

Browser Harness already documents that parallel agents using the same local Chrome instance can interfere with tabs and focus. The supported answer is to serialize local work or use separately authenticated cloud browsers when tasks genuinely need parallel isolation. What is not established at the current first-party boundary is an **optional task-level admission decision**: given two pending browser jobs, current local availability and an operator-authorized cloud allowance, which task should use the local lane, wait, or receive a separate cloud browser, and when is that capacity really released?

This is a **hypothetical workflow** rather than a measured user incident attributable to a missing scheduler. A developer may reasonably choose existing serialization or cloud isolation instead of introducing new coordination.

### Proposal

Explore an opt-in, first-party, developer-composable **browser-task resource admission** seam using existing CLI/daemon and cloud lifecycle primitives. An application-provided decision actor would receive a bounded current-work snapshot and choose **admit to an available local lane / defer / admit to an explicitly authorized isolated cloud lane**. A short-lived, task-scoped authorization or lease would have to be enforced on subsequent browser operations; actual task completion, failure, cancellation, and browser release would return to that decision owner for its next choice.

The default Browser Harness flow must remain unchanged with no configured manager. This does **not** authorize cloud purchases, browser access, extra model calls, or changes to the user's ultimate policy. Cloud authentication, capacity ceilings, billed-session lifetime and cancellation remain under existing user/application authority. The suggested API shape is exploratory, not a claim that its implementation is straightforward or required.

### Alternatives considered

1. **Use the documented local serial lane.** The simplest supported option when tasks need not run simultaneously.
2. **Use one authenticated cloud browser per concurrent task.** Already supported and often preferable; the operator chooses and bears any cost.
3. **Use named daemons / agent-owned tabs.** Existing named-daemon behavior and open tab-isolation proposals address target interference, not a whole-task, feedback-driven allocation decision.
4. **Keep task priority entirely in the host application.** Likely the lowest-cost approach; the proposed first-party seam is justified only if a developer demonstrates that host-only admission cannot enforce or observe the relevant effects consistently.

**What exists today:** [SKILL.md](https://github.com/browser-use/browser-harness/blob/797f2d05e30e58b217ff621a99d302d712dc38da/SKILL.md) documents sequential local work and isolated cloud browsers; [daemon.py](https://github.com/browser-use/browser-harness/blob/797f2d05e30e58b217ff621a99d302d712dc38da/src/browser_harness/daemon.py) manages attached browser state and session locks; [admin.py](https://github.com/browser-use/browser-harness/blob/797f2d05e30e58b217ff621a99d302d712dc38da/src/browser_harness/admin.py) exposes cloud browser start/stop. Existing mechanisms are useful and must be reused where they suffice.

**What may be missing:** A supported optional first-party **task commitment → bounded admission choice → enforceable browser effect → later task/resource feedback** interface across permitted local and cloud routes. Its absence and product value have not been proven by an end-to-end experiment.

**Closest existing project-native solution:** Serialize requests through the default local daemon or explicitly provision isolated cloud browsers using the existing APIs; compare this baseline before implementing a new manager.

**Existing discussion:** [Issue #375](https://github.com/browser-use/browser-harness/issues/375) (parallel subagents), [#582](https://github.com/browser-use/browser-harness/issues/582) (tab protection) and [#901](https://github.com/browser-use/browser-harness/issues/901) (caller-owned target scope) are open. [PR #760](https://github.com/browser-use/browser-harness/pull/760), [#911](https://github.com/browser-use/browser-harness/pull/911) and [#1022](https://github.com/browser-use/browser-harness/pull/1022) are open/unmerged at review time. These are primarily S2 isolation/ownership alternatives. The related older Issues and comments have been re-read; no identical task-level resource-admission proposal was found in targeted Issue/PR searches, but this is not a claim of exhaustive discussion coverage.

## How we reached this proposal — Opensiro VSM assessment

OpenSiro uses Stafford Beer's Viable System Model as a **research lens for organizational functions and decision ownership**, not as a product-quality, maturity or safety ranking. This proposal preserves its accepted *historical* assessment separately from code on the current original branch.

**Historical assessment:** [Accepted Browser Harness Index record](https://github.com/opensiro/vsm-harness-index/blob/394ce776e6945115891b8f7cc459f5a7f7d7aa39/assessments/br/browser-harness.md), Index commit `394ce776e6945115891b8f7cc459f5a7f7d7aa39`, assessment blob `7522febc97e2eff75e78ad781cec9ac64f480a94`, reviewed 2026-09-18, original `review_ref` `afbcc381b963040c19627d788e40c7e7663171ee`, Profile `0.2.2`, Skills Methodology `0.3.1`; accepted `status: included`, catalog identity and revision verified.

**Boundary:** First-party Browser Harness CLI/daemon/CDP helpers, editable skill/workspace and MCP used by external autonomous coding/browser agents. Browser Use Cloud credentials and billing, the host application's priority policy, user Chrome consent and original maintainer governance remain separate decision owners.

**Current original HEAD:** [browser-use/browser-harness@797f2d05e30e58b217ff621a99d302d712dc38da](https://github.com/browser-use/browser-harness/commit/797f2d05e30e58b217ff621a99d302d712dc38da), observed 2026-11-22 UTC. The historical `review_ref` is not rewritten; this current source check does not produce a new Index grade.

| Key | Organizational function, in plain language | Historical state | Evidence or limitation |
| --- | --- | --- | --- |
| **S1 · Operations** | Agents performing browser work | A | Agents select CLI/helper actions and use returned page observations; Browser Harness enables these operational loops. |
| **S2 · Coordination** | Attenuating interference between workers | C | Documented serialization, daemon/session isolation and browser routing are first-party conflict mitigations; open tab-ownership PRs are not shipped proof. |
| **S3 · Current management** | Choosing current priorities, capacity and commitments | — | Historical Index did not establish a distinct whole-task priority owner and feedback closure; an optional construction is proposed here, not evidenced as shipped. |
| **S3* · Independent audit** | Independent challenge of operational claims | — | Logs/recording or an agent's self-report do not alone provide independent corrective audit with return to S3. |
| **S4 · Future adaptation** | External and prospective intelligence feeding current decisions | — | Saved scripts or future drift detection do not establish a first-party future adaptation owner with closed return. |
| **S5 · Identity and policy** | Ultimate identity, policy and authority | — | Cloud spend, Chrome permission and user/application policy are parent-owned, not delegated through this proposal. |

The notation describes **ownership, not a ranked score**: `A` means agent-owned closure; `C` a first-party developer-composable function-specific path; `P` a parent-governed function where applicable; `A(P)` and `C(P)` combine evidenced parent governance with A/C (S3–S5); `—` means no material path established within the bounded historical review; `?` means insufficient evidence. Neither an absent state nor `A` implies a product defect or an automatic design priority.

## Why this particular construction?

**Whole-repository prioritization:** S1 operations and S2 isolation already have positive historical states. S3 is the only selected conditional P0 because multiple agent tasks may compete for one mutable local lane or separately billed remote capacity. S3* audit, S4 adaptation and S5 policy are not additional targets here. Maintainer demand for this proposed S3 manager is **NOT_STATED**.

**Construction hypothesis:** `S3=— -> S3=C`. This is a prospective, falsifiable, function-specific constructor and leaves the accepted historical vector unchanged.

**Native building blocks:** Default and named daemon routing, existing daemon state/locks, explicit browser helpers/CLI/MCP paths, [cloud start/stop](https://github.com/browser-use/browser-harness/blob/797f2d05e30e58b217ff621a99d302d712dc38da/src/browser_harness/admin.py), and user opt-in Cloud authentication. Existing PRs #760/#911/#1022 should be reassessed for possible overlap immediately before implementation.

**Minimal proposed addition:** An optional workload snapshot and lawful set of options, separately composed manager decision, revision/lease-bound enforcement at *all supported browser action entry points*, and real subsequent release/action feedback. A recommendation-only prompt, lock without an independent owner, or unguarded direct CDP bypass would not supply S3 closure.

**Scope exclusions:** No second scheduler by default, automatic Cloud spending, stealth bypass, new parent S5 authority, replacement of agent tab-ownership work, independent S3* review, outside-and-future S4 controller, or mandatory VSM terminology in Browser Harness.

## Proposed approach and validation

1. **Prove native coverage first.** Compare a host-side serial queue and manual/authorized cloud-per-task baseline against any proposed first-party seam. Check whether newer tab ownership/Cloud work already meets the same operator requirement.
2. **Specify authority and effect.** Give a developer-composed manager only scoped pending/current job facts and host-approved local/cloud options. It may admit, defer or request an already authorized isolated lane; a versioned lease must prevent stale decisions or bypass via CLI, helpers, raw CDP, and MCP.
3. **Prove the return and negative cases.** Run competing tasks, observe actual admitted operations and release/stop, and feed receipts to the same manager. Reject missing/stale leases, unauthorized Cloud starts, wrong task/target, cancelled work, lost owners, replayed decisions, and unreleased billed sessions. With the feature disabled, existing behavior must remain intact.

**Hypothesized benefit:** A developer could coordinate task-level browser capacity and defer or isolate work under explicit cost and ownership bounds, rather than relying on ad hoc external scheduling. No throughput, reliability or savings improvement is asserted.

**How to falsify:** Show that the existing host queue and native isolation provide the same safe task decisions/observations with less complexity, or that first-party enforcement/feedback cannot be complete across supported entry points without prohibited authority. Either result should stop or narrow this proposal.

**Cost status:** NOT_MEASURED. No task-admission implementation or native positive/negative acceptance tests were run for this proposal (`NOT_RUN`); previous source/structural checks are not an S3=C runtime proof.

## Feedback requested

Would this optional task-admission seam be useful beyond the documented serial/local and cloud-isolation options? Is it already addressed by native code or another Issue/PR? Could it be kept solely in the host application? Which existing interface would maintainers prefer, if any? Corrections to the VSM mapping, authority boundary and the decision not to build are all welcome.

This request does **not** ask the maintainers to adopt VSM or commit to implementation.

## Three independent ways to participate

- **Improve Browser Harness:** If maintainers see a concrete use case, narrow a first-party extension or experiment around existing daemon/Cloud APIs and their acceptance tests.
- **Challenge the public assessment:** Explain where the historical ownership mapping or proposed boundary misreads existing first-party behavior; methodology changes belong to the public OpenSiro Profile/Skills project.
- **Explore a domain-specific fork:** Compare the host-only baseline with the proposed S3 closure in a legally permitted, explicitly opt-in experimental fork without burdening the original maintainers.

## Research attribution and AI disclosure

[OpenSiro Upstream](https://github.com/opensiro/upstream) · [VSM Profile](https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md) · [VSM assessment Skills](https://github.com/opensiro/vsm-harness-skills/blob/main/skills/assess-vsm-harness/references/autonomy-states.md) · [accepted VSM Index](https://github.com/opensiro/vsm-harness-index).

**AI involvement:** This proposal and its public source-evidence map were prepared with AI assistance as a plan-only design hypothesis. There is no claim of independent human source audit, product adoption, maintainer endorsement, shipped `S3=C`, native acceptance-test PASS, or measured cost improvement.
