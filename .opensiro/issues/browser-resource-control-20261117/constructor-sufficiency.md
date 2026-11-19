# Browser Harness — independent source-native constructor sufficiency review (AI)

**Level 2 · PLAN_ONLY · NO_GO / DECISION_READY · NOT IMPLEMENTED · NOT PUBLISHED.** [Human decision](issue.md) · canonical [roadmap.md](roadmap.md).

**Target transition:** NO_QUALIFIED_C_TARGET
**Proposal-stage decision:** NO_GO
**Research disposition:** DECISION_READY

## 1. Boundary, owners, six-function dependencies

Original `browser-use/browser-harness@fe4a2cd3dd308e8de929621e64e7f284d7a124d7` [source commit](https://github.com/browser-use/browser-harness/commit/fe4a2cd3dd308e8de929621e64e7f284d7a124d7). The deployed first-party scope is CLI -> browser daemon -> CDP, editable agent helpers, skill and MCP. Agents execute tasks via a host and can call first-party functions; host agents are not a bundled S3 managerial actor. Browser Use Cloud service and maintainer development governance are excluded. The complete **historical** accepted VSM vector and current six-function dispositions are recorded only in [roadmap.md](roadmap.md) and rendered once in [issue.md](issue.md).

Observed problem: concurrent browser actors can close or access the wrong tab ([#582](https://github.com/browser-use/browser-harness/issues/582), [#375](https://github.com/browser-use/browser-harness/issues/375)). It is an S2 interaction. The [SKILL](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/SKILL.md) already proposes serialized local operations or isolated remote browsers; the daemon implements transport and CDP connections. S3 would instead make legitimate discretionary decisions on the organization-wide *current task/capacity/commitments*, not merely tab forwarding. No independent whole-work decision right is established inside original first-party code.

**Counterfactual owner test:** with no proposed developer-composed resource manager, the supported host may still serialize or isolate and all browser work proceeds. No source proof of a distinct required S3 decision or first-party return channel is present. Parent/user consent is not a new S5. Proposed S4 future change cannot be inferred from an agent-written current-task helper.

## 2. Track A native source/Issues/PRs vs Track B

| Required organizational link | Track A shipped / ISSUE / OPEN_PR (not merged) | Candidate B on-top and rejection | Refutation criterion |
| --- | --- | --- | --- |
| State/disturbance | Shipped [helpers](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/helpers.py) expose `list_tabs`, `current_tab`, `switch_tab`, `close_tab`; [daemon](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/daemon.py) holds mutable session; [#1022](https://github.com/browser-use/browser-harness/pull/1022) OPEN PR agent ownership | Proposed new task-commitment/resource state is absent, and would change the native host boundary | Real shipping authoritative task state under the same first-party recursion |
| Options and decisive authority | Shipped host skill specifies serial/isolated lanes; [#375](https://github.com/browser-use/browser-harness/issues/375) asks parallel use; [#760](https://github.com/browser-use/browser-harness/pull/760) OPEN PR target concurrency @ `e285724fabac1cd7cc949a0038013d80055a7aab` | Proposed `admit/defer/hold` by independent S3 composed actor has no established first-party rightful owner | Demonstrated native owner executing genuinely alternative lawful current-management choices |
| Enforcement and negative safety | [#911](https://github.com/browser-use/browser-harness/pull/911) OPEN PR scoped owned target @ `c2de9b79115ca38c19c43385b232c83fc0fbd875`, [#846](https://github.com/browser-use/browser-harness/pull/846) OPEN PR guard @ `b1e0b7a9a0219a75e9ca6c36338530860da75423`, [#1034](https://github.com/browser-use/browser-harness/pull/1034) OPEN PR reconnect @ `4056c5aece6e4a83ea999d60e42482b84f9eed7b`; original [#901](https://github.com/browser-use/browser-harness/issues/901) scope need | Any lease/CAS actor enforcement must be original-native, not caller title marker; current PR solutions remain S2 safety features | Evidence existing complete first-party S3 enforcement and authority with later operation |
| Feedback return | Shipped [recorder](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/recorder.py) action trail; [#1039](https://github.com/browser-use/browser-harness/pull/1039) OPEN PR agent self-feedback @ `50c31e859cd1977184a8bac88fb853c209607dae` | No source-backed later real task outcome fed to an independent S3 manager for reconsideration | Actual multi-task choice → browser effect → manager receives result and changes commitment |
| S4 alternative | Agent-written domain skills under optional `BH_DOMAIN_SKILLS`; [#1025](https://github.com/browser-use/browser-harness/pull/1025) OPEN PR saved scripts/drift @ `4479c8973f68d012ec6ffa310b4736b81ac708a6` | Future site drift adaptation would need owned option generation, authorization and S3 return; merely detecting drift cannot close S4 | Pinned complete future-oriented choice returned lawfully to later operations |
| S3* / S5 exclusions | Recording is not independent audit; Chrome consent belongs to user/host | No legitimate new local independent judge or ultimate-policy owner identified | A genuine owner with corrective feedback at the same recursion |

The first-party source tree at the pinned commit was enumerated (454 entries, not truncated), covering Python runtime, docs/skills, tests, release CI, policy/config and sample domain recipes. The original [CONTRIBUTING](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/CONTRIBUTING.md) permits relevant improvements and does not establish a specific request for S3. Maintainer support for this autonomous construction is **NOT_STATED**. A matching Issue alone is not a veto; the missing authorization and closure are decisive.

## 3. Construction sufficiency / no qualified ports

There is **no selected P0 C transition**, hence no invented interface count or claimed constructor. A *future* S3 hypothesis would require a bounded task/resource snapshot with authorized actors; permissible competing current-resource choices; independently composed autonomous manager port; atomic first-party enforcement before CDP effect; and subsequent real task outcome returned to manager. A *future* S4 hypothesis would need independently authorized prospective drift adaptation with S3 handoff. In neither case does Track A+B presently yield the minimum justified source-native construction *inside* the claimed Browser Harness ownership boundary.

**P0:** NO_QUALIFIED_C_TARGET. **P1:** NONE. **P2:** NONE. Reuse existing native solutions rather than building a parallel framework, policy engine or unrequested new recursion. The prior fork [S3 experimental record](https://github.com/opensiro-contributions/browser-harness/blob/opensiro/meta/.opensiro/contributions/browser-harness-s3-owned-scope-priority-admission.json) depends on unmerged #911 and has historical unit/fake-CDP results, not verified current-original real task value.

## 4. Native acceptance if new evidence reopens one function

Command supported in [original AGENTS](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/AGENTS.md): `uv run --with pytest python -m pytest tests/unit -q` for unit tests; original integration tests may require a real Chrome/CDP, and release CI currently does not run unit suite automatically. **No native tests executed in this rerun**.

| Proposed scenario, NOT_RUN | Native comparison with same actor/task | Decisive observable outcome |
| --- | --- | --- |
| Authorized current-resource choice | Two agent processes compete for local shared Chrome; compare serial host queue and remote isolated browsers with candidate opt-in manager | Two distinct lawful options, agent manager decision, enforced next CDP operation and returned task outcome |
| Missing/revoked/stale owner | Identical tabs and work, absent manager or revoked lease | Default mode remains safe; unauthorized tab access/close fails before effect; no fabricated autonomous S3 |
| Future drift adaptation | Same stored script task and changed page condition, native helper or open PR #1025 vs proposed S4 | Independent future selection, lawful application and observable subsequent operational return, not just script failure report |
| Compatibility and cost | Default single-agent CLI/MCP, unit/integration tests, native serial lane vs optional construction | No default regression, and measurable task benefit/total engineering cost comparison |

**Falsifier:** a current-source equivalent complete first-party C decision/right/action/feedback path, or a minimal *new* authoritatively bounded path delivering a genuinely distinct real task outcome vs the shipped native alternatives, disproves this particular NO_QUALIFIED_C_TARGET. Missing measured ROI alone is not a reason for NO_GO; here the missing first-party actor/scope and complete lawful chain are the problem.

## 5. Decision, evidence ownership and publication

**Proposal-stage decision:** NO_GO
**Research disposition:** DECISION_READY
**Target transition:** NO_QUALIFIED_C_TARGET

**Validation state:** NOT_RUN. **Cost status:** NOT_MEASURED. Confidence medium for bounded decision, not a verified proof of product-wide feature irrelevance. Index retains accepted historical grading; Profile/Skills own normative semantics; original upstream owns its code and PR/Issue outcomes; [roadmap.md](roadmap.md) owns case decisions, and [issue.md](issue.md) displays those to humans.

Historical [previous metadata commit](https://github.com/opensiro-contributions/browser-harness/commit/bc5e0fd8128af7637e074430fe0a93f25a49bfef) was inspected only after independent first-pass determination. It left a conditional S3 proposal and `NEEDS_EVIDENCE` without new-protocol terminal verdict. This update records a separate scoped NO_GO. No native implementation, public fork Issue, original Issue/comment/PR, additional VSM grade or independent human review is implied. AI assistance disclosed.
