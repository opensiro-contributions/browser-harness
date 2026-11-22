# Browser Harness — independent six-function capability roadmap receipt

**Plan-only second independent pass · 2026-11-19 · GO / NEEDS_EVIDENCE · NOT IMPLEMENTED.**
The first-pass independent decision was recorded before reading the previous fork-local case. Prior NO_GO remains in Git history and is compared only at the end.

## Identity and pins

- Original repository: browser-use/browser-harness
- Original HEAD: fe4a2cd3dd308e8de929621e64e7f284d7a124d7
- Observed at: 2026-11-19
- Accepted Index assessment: https://github.com/opensiro/vsm-harness-index/blob/394ce776e6945115891b8f7cc459f5a7f7d7aa39/assessments/br/browser-harness.md
- Accepted assessment blob SHA: 7522febc97e2eff75e78ad781cec9ac64f480a94
- Accepted review ref: afbcc381b963040c19627d788e40c7e7663171ee
- Accepted reviewed at: 2026-09-18
- Accepted Profile version: 0.2.2
- Accepted Methodology version: 0.3.1
- System in focus: First-party Browser Harness standard CLI, daemon, CDP helpers, skill and MCP plus optional local/cloud browser modes; external coding agents act as S1 workers, while private Cloud management and repo development governance are excluded
- Receipt contract: proposal-gate
- Repository-wide source map: 267 tracked original files; README, AGENTS, LICENSE, CONTRIBUTING, SKILL, interaction/domain skills, Python CLI/daemon/admin/helpers/IPC/recorder/telemetry/video/MCP, unit/integration tests, release workflow, active Issues and exact open PR patches
- Accepted VSM vector: S1=A · S2=C · S3=— · S3*=— · S4=— · S5=—
- S1 disposition: ALREADY_A — external autonomous agent chooses browser operations with first-party helpers and receives page observations; no new C selected
- S2 disposition: ALREADY_C — serial local lane or separate remote browsers regulates observed inter-agent tab conflicts; #1022 OPEN PR improves owned-tab isolation but does not create S3 management
- S3 disposition: P0 — whole-current task capacity, priority and commitments currently remain host-controlled; compose a bounded first-party decision/authority/effect/return interface for an external autonomous resource manager
- S3* disposition: DEFER — recorder/video/telemetry do not independently challenge S1 claims and return a corrective judgment to S3; not a minimal first construction
- S4 disposition: DEFER — agent-written domain skills and OPEN #1025 saved-script drift detection do not create an outside-and-future adaptation owner that returns to S3
- S5 disposition: NO_TARGET_PARENT — Chrome consent, cloud budget and ultimate identity legitimately belong to user/host; no intentional product omission inferred from missing source
- Target transition: S3=— -> S3=C
- Priority rationale: Only S3 has both source-evidenced multi-worker current resource contention and concrete first-party local/cloud actuation primitives; S1/S2 already have accepted positive states, S3*/S4 need distinct independent returns and S5 remains parent authority
- P1 dependencies: Establish permitted host-supplied current task commitments and priority envelope; check #1022 and #911 owner scope overlap; add lease/epoch enforcement before opted-in CDP effects; prove later task feedback, CLI/MCP distribution and safe cloud budget; compare simple host queue under matched tasks
- P2 optional: NONE — no second function or obligatory parent-governed mode
- Proposed C construction: Opt-in first-party browser-resource-admission API with current workload snapshot, bounded local/defer/authorized-cloud options, developer-composed autonomous S3 decision owner, atomic scoped lease enforcement, and real subsequent browser action/commitment feedback returned to owner
- C sufficiency falsifier: With manager removed, there must be no independent autonomous whole-current priority choice; an unauthorized lease, bypassable raw CDP action or missing later real-action return defeats the proposed C chain
- Scenario basis: HYPOTHETICAL
- Proposal-stage decision: GO
- Research disposition: NEEDS_EVIDENCE
- Proposed validation: Two independently driven browser tasks competing for local lane and authorized remote capacity; verify different lawful decisions and later actions, missing/stale/unauthorized owner negatives, default CLI/MCP compatibility, and matched host queue versus S3 costs
- Validation state: NOT_RUN
- Proposal falsifier: A shipped equivalent C already exists, or native host queue plus isolated remote browsers achieve the same task and owner outcome with lower/equal total engineering and maintenance cost, or safe first-party return cannot be implemented
- Evaluation object: Whole-current multi-task resource admission at the Browser Harness first-party runtime, not narrower S2 tab ownership or generic cloud startup
- Existing-work overlap: Shipped SKILL serial lane/cloud isolation; original Issues #375/#582/#901; OPEN #1022 agent-owned tabs, #760 shared-target coordination, #911 owned-target scope, #1025 script replay and #1039 self-report
- Our on-top contribution: Function-specific optional S3 task-state/options/manager/lease/effect/feedback path built on native daemon and cloud APIs, without competing against open S2 tab-protection work
- Incremental benefit: HYPOTHETICAL; dynamic priority and constrained cost decisions among browser jobs, not proven faster, cheaper or requested by original maintainers
- Decision scope: Bounded proposal GO for S3 developer-composable construction and future experiments; not implementation, Index regrade, project endorsement or publication

## Rights and authority

[MIT license](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/LICENSE) permits reuse with notice; [CONTRIBUTING](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/CONTRIBUTING.md) welcomes focused PRs. Additional CLA/DCO/AI contributor obligations are UNVERIFIED. The matched fork's opensiro/meta state was read as ALLOW / ACTIVE on 2026-11-19 before effect; re-read and enforce before persistence. User/parent must grant Chrome attachment and explicit cloud authentication/cost/volume bounds. No manager right to mint authority, inspect unrelated tabs or provision chargeable cloud without consent. Fork case metadata is not external publication consent.

## Existing work / overlap

**Current source-first reconciliation (2026-11-20; Upstream v0.18.2)**

A source-first same-case check was sealed at [Upstream #58](https://github.com/opensiro/upstream/issues/58#issuecomment-7047329680) before the prior fork record was read. Current public original default HEAD 22ecf8545d67c474fa024643632d70af28b7fa0e (distinct from receipt historical Original HEAD fe4a2cd3dd308e8de929621e64e7f284d7a124d7) was read at [SKILL.md](https://github.com/browser-use/browser-harness/blob/22ecf8545d67c474fa024643632d70af28b7fa0e/SKILL.md) and [src/browser_harness/daemon.py](https://github.com/browser-use/browser-harness/blob/22ecf8545d67c474fa024643632d70af28b7fa0e/src/browser_harness/daemon.py); status of issue/PR overlap: https://github.com/browser-use/browser-harness/issues/1022 (OPEN, agent-owned tabs). Historical fork case references other issue proposals, not assumed merged; original PR #626 CLOSED_UNMERGED (daemon lifecycle hardening).

**Deep current-source resource boundary:** [SKILL.md](https://github.com/browser-use/browser-harness/blob/22ecf8545d67c474fa024643632d70af28b7fa0e/SKILL.md) describes one mutable attached tab per daemon; named `BU_NAME` daemons still share the same Chrome profile and process, and are not resource-isolated browsers. [admin.py](https://github.com/browser-use/browser-harness/blob/22ecf8545d67c474fa024643632d70af28b7fa0e/src/browser_harness/admin.py) contains an explicit spawn lock, so OPEN [#692](https://github.com/browser-use/browser-harness/issues/692) cannot alone prove that historical daemon-start race still reproduces. [daemon.py](https://github.com/browser-use/browser-harness/blob/22ecf8545d67c474fa024643632d70af28b7fa0e/src/browser_harness/daemon.py) still invokes synchronous `get_ws_url()` from async `start()`, relevant to OPEN [#893](https://github.com/browser-use/browser-harness/issues/893) as S2 operational overlap, not independent S3 resource prioritization. [PR #1039](https://github.com/browser-use/browser-harness/pull/1039) is OPEN telemetry/feedback, not a shipped autonomous pool manager. Native baseline `test_auth.py` + `test_ipc.py`: **20 PASS**, but concurrent browser resource / lease / cloud acceptance tests and P0 implementation remain **NOT_RUN**. The proposal is opt-in S3=C only if real enforceable allocation and returned resource-use feedback exist beyond deterministic tab serialization.

The scoped new-source first pass asks: One-tab collision safety and a separate optional resource allocation decision are different functions. A lock alone does not give an autonomous whole-task priority choice; proof is needed that enforcement covers all relevant browser entrypoints. **No newly demonstrated changed C ownership or Index regrade** is asserted. Previous canonical proposal remains **GO / NEEDS_EVIDENCE**, `S3=— -> S3=C`, with native tests `NOT_RUN`, cost `NOT_MEASURED`. This is a Human/AI template-compliance repair and bounded current-source note, **not a duplicate independent original research case, code implementation, or public outreach**. The old receipt/head and first-attempt lineage remain readable in Git history and in the existing fields above.


**Original shipped at HEAD.** [SKILL](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/SKILL.md) treats default local daemon as one mutable attached-tab lane and recommends serialization or distinct cloud browsers for simultaneous tasks. [helpers](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/helpers.py) sends CDP actions through IPC. [daemon](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/daemon.py) holds browser/session state, [admin](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/admin.py) provides start_remote_daemon and stop_remote_daemon. [CLI](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/run.py) and [MCP](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/mcp_server.py) expose supported entry points. [recorder](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/recorder.py), video, telemetry, domain skills and tests are supporting or adjacent to the selected current S3 constructor.

**Observed need and open work.** [#375](https://github.com/browser-use/browser-harness/issues/375) reports subagent concurrency conflicts and seeks parallelism; [#582](https://github.com/browser-use/browser-harness/issues/582) documents a task closing three other agents' tabs; [#901](https://github.com/browser-use/browser-harness/issues/901) documents exact target ownership/metadata concerns. [PR #1022](https://github.com/browser-use/browser-harness/pull/1022) OPEN @ 06e4d7ca0d7327a0b5b886604ba7d35547f0a728 implements proposed agent-owned tabs, tested by authors but NOT shipped; it resolves S2 interference rather than whole-task priority selection. [#760](https://github.com/browser-use/browser-harness/pull/760) and [#911](https://github.com/browser-use/browser-harness/pull/911) remain OPEN coordination/owner-scope alternatives. [PR #1025](https://github.com/browser-use/browser-harness/pull/1025) OPEN @ 4479c8973f68d012ec6ffa310b4736b81ac708a6 proposes saved-script drift detection, and [PR #1039](https://github.com/browser-use/browser-harness/pull/1039) OPEN @ 50c31e859cd1977184a8bac88fb853c209607dae proposes task self-feedback. Their PR diffs and scope were inspected before prioritization. No open PR is credited as shipped original main.

## Function ownership

S1 agent decides local browser task actions and consumes page observations. S2 host composes serial or isolated lanes to attenuate actual tab collision. Proposed S3 differs: an independent developer-composed actor would choose and revise resource commitments and task priorities for the whole current browser-work organization under parent constraints. The deterministic daemon only enforces that right, and a subsequent task action/result returns to the same manager. S3* requires complementary independent evidence beyond routine action traces. S4 requires prospective outside change analysis and S3 return, not merely stored scripts. S5 ultimate purpose/approval belongs to a legitimate higher-recursion human/host, not to a browser permission popup. No adjacent CI or maintainer organization is counted as product S5.

## Capability priority

**P0: S3=— -> S3=C.** Required first-party path: scoped current task snapshot → legitimate local/defer/remote alternatives → composed autonomous S3 agent decides → server-side versioned owner/task lease enforces later CDP browser action/provision → actual browser action and task release/error receipt returns to manager for subsequent decisions.

**P1:** prove owner-safe task identity and scope before any current/remote action, opt-in cloud budget and availability, no unauthorized tab enumeration, no bypass through raw cdp() or MCP; capture real downstream effects rather than a queue log; verify two different lawful S3 choices, recover stale waiting clients, compare host queue/remote isolation, preserve default CLI/MCP. Reuse #1022 where compatible or build minimal standalone lease when it remains unmerged.

**P2: NONE.** No independent extra VSM upgrade or optional parent mode is justified now.

**Confidence:** MEDIUM in source-native constructibility, LOW in unmeasured incremental value or maintainer desire. Historical Index reviewed 62 days ago; recommend independent source-pinned Index reassessment without substituting an unmerged proposal for accepted evidence.

## Parallel contribution-on-top review

| S3 link | Track A native shipped/open | Track B remaining minimal first-party constructor | Falsifier |
| --- | --- | --- | --- |
| Current-work state | Daemon knows tabs/sessions; admin provisions remote browser; #1022 OPEN owner-scoped tabs | Task/lane/principal current commitments, authorized capacity and lease epoch snapshot | Browser tabs without multi-task state are only S2 support |
| Alternatives/decision owner | Host currently chooses serialization/remote manually | First-party bounded choices and CLI/MCP port for independently composed agent manager under delegated decision right | Hardcoded FIFO/remote default is not S3 C |
| Enforcement | Existing IPC and CDP effects, OPEN #911 owner-scoped guard | Opt-in daemon-side atomic task/lane/epoch checks before all side-effecting CDP and cloud provisioning | Stale owner or raw CDP bypass invalidates path |
| Return | CLI operation errors, recorder/logs, OPEN #1039 self-report | decision_id → actual later browser action status → manager-visible task completion/release and fresh commitments | Advisory/log alone not S3 closure |
| Parent and legacy mode | Chrome consent, cloud auth/billing warnings, current default serial mode | Explicit user budget and no cloud calls without permission, no secret/liveUrl leaks, opt-in default-off | Scope leak or changed normal behavior stops construction |

## Implementation options

Plan-only: build a small proof contract against fake IPC and current tests, not an unrelated orchestrator; integrate with #1022 without treating it as main. Test real Chrome only with appropriate browser consent; test cloud provisioning only with separately authorized cost and authentication. If the simple native host scheduler matches cost and reliability, abandon the S3 feature and focus on existing original-native S2 fixes.

## Specification and domain alternatives

A separate Profile/Skills method proposal may address classification of S2 coordination versus S3 whole-work control if new genuine evidence challenges semantics. It does not authorize a new Index state, special domain fork or original-maintainer engagement.

## Cost experiment

Use identical A/B tasks: two subagents competing for one local browser, one remote-eligible, both with bounded priority/deadline and user-authorized cloud budget. Compare simple host queue/explicit remote invocation against S3 admission. Observe correct-tab changes, task completion, remote charges, lost/stale tasks, engineering/integration/review/test hours and maintenance regression cost.
- Cost status: NOT_MEASURED

## Delivery and publication

- Human: [issue.md](issue.md). AI: [constructor-sufficiency.md](constructor-sufficiency.md). Canonical receipt: [roadmap.md](roadmap.md).
- Result: PLAN_ONLY
- External issue: DRAFT — NOT PUBLISHED
- Native validation: NOT_RUN; the inspected dev-alpha-2 Python 3.12 environment did not have pytest or uv. Python AST parse of 33 source/test files passed but is not a functional test.
- Historical comparison (only after independent outcome): previous [NO_GO case revision](https://github.com/opensiro-contributions/browser-harness/commit/c6df76d4eee6190a65623c85f76147f0ba7f87c1) chose NO_QUALIFIED_C_TARGET / DECISION_READY for this original HEAD. The new first-pass verdict found a source-grounded bounded S3 decision + lease + later return chain and gives proposal GO + NEEDS_EVIDENCE without claiming measured utility or retroactively invalidating the prior evidence.
- No product source edits, public fork Issue/PR, original Issue/comment/PR, Index change, charged browser call or external communication. Separate exact approval required for publication.
