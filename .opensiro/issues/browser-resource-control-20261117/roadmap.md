# Browser Harness — independent six-function roadmap receipt

**Plan-only independent re-run · 2026-11-19.** This receipt supersedes the previous conditional S3 proposal as the current case decision; the 2026-11-18 revision is retained in Git history. Neither the Index vector nor product code is changed.

## Identity and pins

- Original repository: browser-use/browser-harness
- Original HEAD: fe4a2cd3dd308e8de929621e64e7f284d7a124d7
- Observed at: 2026-11-19
- Accepted Index assessment: https://github.com/opensiro/vsm-harness-index/blob/394ce776e6945115891b8f7cc459f5a7f7d7aa39/assessments/br/browser-harness.md
- Accepted assessment blob SHA: 7522febc97e2eff75e78ad781cec9ac64f480a94
- Accepted review ref: afbcc381b963040c19627d788e40c7e7663171ee
- Accepted reviewed at: 2026-09-18
- System in focus: first-party Browser Harness CLI/daemon/CDP helper/skill/MCP and authorized optional local/remote browser modes; external coding agents are task actors, Browser Use Cloud management and maintainer governance are excluded
- Receipt contract: proposal-gate
- Repository-wide source map: README, AGENTS, SKILL, CONTRIBUTING, LICENSE, pyproject, core Python source, browser daemon/admin, helper, recorder, telemetry, MCP, domain and interaction skills, native tests/integration, release CI, current Issues and PR heads (see below)
- Accepted VSM vector: S1=A · S2=C · S3=— · S3*=— · S4=— · S5=—
- Target transition: NO_QUALIFIED_C_TARGET
- Priority rationale: S1 already autonomous and S2 already composable; S3 management lacks a justified native first-party authority/return boundary beyond host scheduling, S3* lacks independent corrective authority, S4 lacks a complete lawful prospective adaptation return via S3, and S5 is host/user reserved
- S1 disposition: ALREADY_A — external agent chooses browser interactions via first-party helpers, page observations return to later task actions; no additional C is required
- S2 disposition: ALREADY_C — serialization of one mutable daemon tab and separate remote browser isolation are first-party protocols assembled with the external host; open agent-owned-tab PR is not shipped
- S3 disposition: NO_TARGET — no current whole-work autonomous allocator; hypothesized lane controller requires introducing task/resource commitments and authority beyond this thin browser transport; host queue and isolated browsers are the simpler same-task baseline
- S3* disposition: NO_TARGET — recorder and diagnostics observe operations but do not supply an independently authorized corrective judgment returning to S3
- S4 disposition: NO_TARGET — agent-authored helpers/domain skills and open saved-script PR concern task/replay support, not a source-supported future environment-intelligence decision and operational return
- S5 disposition: PARENT_RESERVED_UNVERIFIED — Chrome user permission and external host choices are outside harness ultimate-policy ownership; no maintainer declaration proves intentional omission
- Target transition: NO_QUALIFIED_C_TARGET
- P1 dependencies: NONE — no selected P0; new evidence can reopen a scoped experiment after independent admission and authority review
- P2 optional: NONE — no evidenced independent optional constructor
- Proposed C construction: NONE — no qualified source-grounded distinct complete C actor/authority/effect/feedback chain at the selected first-party boundary
- C sufficiency falsifier: A supported first-party C actor port with lawful whole-system decisions and later actual task feedback, not replicable at similar cost with native serial or isolated lanes, would overturn S3 no-target
- Scenario basis: HYPOTHETICAL
- Proposal-stage decision: NO_GO
- Research disposition: DECISION_READY
- Proposed validation: If newly scoped, compare two concurrent task agents using native host serialization/isolation against opt-in first-party resource-manager controller with lawful choices, fail-closed scope and downstream feedback; alternatively test independently authorized S4 drift adaptation into later operations
- Validation state: NOT_RUN
- Proposal falsifier: Demonstrate a current-source native first-party complete differentiated C chain for one named function, at the same recursion and with legitimate owner and feedback, or a minimal fully source-grounded on-top chain that uniquely supplies it
- Evaluation object: Incremental first-party C construction on the current Browser Harness boundary, screened neutrally across all six VSM functions
- Existing-work overlap: shipped tab helpers and skill S2 conventions; open PR #1022 owns multi-agent tabs, #1025 saved scripts, #1039 feedback; Issues #375, #582, #901, #998 and PR #1034 narrow native outcomes
- Our on-top contribution: NONE qualified; optional S3 allocation and S4 adaptation were independently considered but each lacks a defensible minimal complete first-party actor and authority/return chain at this boundary
- Incremental benefit: NOT_MEASURED; no claimed gain beyond native host queue or remote-browser isolation
- Decision scope: NO_GO only for additional C construction in this original and operating boundary; does not reject current issues, existing PRs or independent future projects

## Rights and authority

- MIT license at [pinned LICENSE](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/LICENSE); [CONTRIBUTING](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/CONTRIBUTING.md) welcomes scoped fixes and skill contributions. CLA/DCO/AI-specific terms beyond these read documents remain UNVERIFIED, not waived.
- Verified fork `opensiro-contributions/browser-harness`, parent `browser-use/browser-harness`, default `main`; `opensiro/meta` state on 2026-11-19: `owner_control=ALLOW`, `attention=ACTIVE`. Recheck state and HEAD before edits; this permits fork-local case metadata only, not external publication.
- The selected evaluation is NOT an Index reassessment, product implementation authority, new external Issue/PR or grade award.

## Existing work / overlap

- **SHIPPED**, pinned `fe4a2cd3dd308e8de929621e64e7f284d7a124d7`: [SKILL](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/SKILL.md) describes one mutable attached tab and serial local operations, remote isolated browsers and bounded local fallback; [daemon](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/daemon.py), [helpers](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/helpers.py), [CLI](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/run.py) and [MCP](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/mcp_server.py) provide browser actions and transport. [recorder](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/recorder.py) and [telemetry](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/telemetry.py) are supporting observation, not independent S3*/S4 decision loops.
- **OPEN ISSUE:** [#375](https://github.com/browser-use/browser-harness/issues/375) parallel subagents, [#582](https://github.com/browser-use/browser-harness/issues/582) observed cross-agent wrong-tab closure, [#901](https://github.com/browser-use/browser-harness/issues/901) caller-owned metadata boundary and [#998](https://github.com/browser-use/browser-harness/issues/998) fail-closed reconnect. These support S2 safety problems, not automatic S3.
- **OPEN PR, not shipped:** [#1022](https://github.com/browser-use/browser-harness/pull/1022) agent-owned tabs @ `06e4d7ca0d7327a0b5b886604ba7d35547f0a728`, [#1025](https://github.com/browser-use/browser-harness/pull/1025) saved scripts/drift @ `4479c8973f68d012ec6ffa310b4736b81ac708a6`, [#1039](https://github.com/browser-use/browser-harness/pull/1039) feedback @ `50c31e859cd1977184a8bac88fb853c209607dae`, [#1034](https://github.com/browser-use/browser-harness/pull/1034) fail-closed reconnect @ `4056c5aece6e4a83ea999d60e42482b84f9eed7b` from an Opensiro fork; [#911](https://github.com/browser-use/browser-harness/pull/911) opted-in owned target, [#760](https://github.com/browser-use/browser-harness/pull/760) one browser per multiple tabs, [#846](https://github.com/browser-use/browser-harness/pull/846) guarded authorization remain open.
- **Governance boundary:** [CONTRIBUTING](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/CONTRIBUTING.md) and [AGENTS](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/AGENTS.md) concern developer workflows, not deployed S5; [release workflow](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/.github/workflows/release.yml) does not prove runtime governance. Optional `agent-workspace/domain-skills` are reference recipes and agent-authored material, not autonomous future strategy ownership.
- Current README explicitly says Browser Harness is the browser engine inside Browser Use; do not import decisions from the separate Browser Use CLI/cloud organization into this assessed recursion.
- **Prior OpenSiro experiment (historical only, read after independent outcome):** [S3 owned scope record](https://github.com/opensiro-contributions/browser-harness/blob/opensiro/meta/.opensiro/contributions/browser-harness-s3-owned-scope-priority-admission.json), older dependent on open #911, cannot establish a native S3 controller here without real task return and matched native benefit.

## Function ownership

All six dispositions above are qualitative *current-source research*, not replacement grades. S1 task agent decides navigation/clicks via CDP with page observation; S2 host composes serialization/isolation between agents; S3 resource allocation and priorities remain host/operator decisions, with the daemon managing connection lifecycle only; S3* recording and run feedback are not independent control correction; S4 agent-written current-task skills and prospective PR replay detection lack an S3-coupled adaptation owner; S5 end-user Chrome approval and parent host policy are outside the assessed boundary. No omission is called intentional solely because code is absent.

## Capability priority

- **P0: NO_QUALIFIED_C_TARGET** — six-function screen yields no scoped complete differentiated minimum C construction.
- **P1: NONE** — no qualified P0 dependencies. Future narrowly selected research could test an owner-authorized S3 allocator using the same task against host serialization, but is not currently scheduled or specified as C.
- **P2: NONE** — no independent optional C(P)/A(P) mode or secondary-function obligation.
- Confidence: medium for scoped NO_GO; high for dated source/Index provenance; no real-browser intervention/ROI experiment executed.
- Maintainer interest: issues #375 and #582 evidence problems with parallel tasks and tab safety, NOT a request for autonomous S3 or S4; contributor-specific interest: NOT_STATED.

## Parallel contribution-on-top review

| C-sufficiency link | Track A native source and current PR/Issue | Track B minimal on-top candidate | Result and falsifier |
| --- | --- | --- | --- |
| S3 present-wide state and lawful options | Tab lists, mutable current tab and optional daemon selection; #1022 offers per-agent isolation in OPEN_PR | Hypothetical scoped resource/commitment state and `admit/defer/hold` policy | NO_TARGET: this requires new task-organization ownership not established in current harness; native queue is adequate baseline until proven otherwise |
| S3 developer-composed decision, enforcement and returned task outcome | External agent hosts decide tasks; #911/#846 address owner-scoped security in OPEN_PR; daemon executes CDP only | Hypothetical S3 adapter plus lease/CAS, later action and feedback | No minimal lawful existing actor/authority/return path established; lack is architectural not just missing measurements |
| S3* independent corrective audit | Recorder, trace and #1039 self-report OPEN_PR | Independent reviewer with separate decision authority returning to S3 | Excluded: entire independent control loop added beyond recorder, no S3 return owner |
| S4 future adaptation and operational return | Agent-created domain skills, #1025 drift detection OPEN_PR, CLI reuse | Autonomous choose/validate/apply changes to future task-capability under owner authority | Excluded: S3 return and legitimate owner missing; replay test alone not prospective S4 |
| S5 ultimate identity/policy | Chrome permission and host user decisions | Local policy engine | Excluded: would cross parent-reserved authority; no source-backed independent user benefit |

**Simplest alternative:** serialize on local daemon using documented [SKILL](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/SKILL.md); for truly parallel tasks create isolated remote browsers where authenticated. A future proposal must beat this matched baseline and supply an actual discretionary decisive owner, legal effect and feedback, not just a convenience API or identical host job queue. No mandatory implementation follows from a missing historical `—`.

## Implementation options

1. NOW: no new C constructor; preserve native/maintainer-owned Issues and open PR review, with no duplicate external request.
2. Future research only if new first-party authority/recursion evidence exists: design a bounded S3 choice that survives independent agent omission and has actual downstream task feedback; test against host queue/remote isolation. The current NO_GO would then be reconsidered.
3. Separate native fixes for wrong tabs or reconnection can proceed through their own approved Upgrade route; this roadmap grants no implementation or communication authority.

## Specification and domain alternatives

A Profile/Skills question about composable host S2 versus real in-boundary S3, or about prospective S4 return, is a separate methodological proposal with its own evidence. No Profile/Skills change or external original issue is authorized. No separate domain fork is created.

## Cost experiment

- Same-task counterfactual: two agents competing for browser tabs, preserving task-owned targets and valid returns, host serialization/cloud isolation versus first-party optional manager.
- Measure actual wrong-tab effects, legitimate alternative allocation choices, feedback closure, completion, engineering+review+maintenance effort and platform/browser costs.
- Cost status: NOT_MEASURED
- Proposed tests and benefit measurements: NOT_RUN. Existing prior fork experiment results are historical, not rerun or independently validated here.

## Delivery and publication

- Human: [issue.md](issue.md); AI: [constructor-sufficiency.md](constructor-sufficiency.md); canonical receipt: [roadmap.md](roadmap.md).
- Result: PLAN_ONLY
- External issue: DRAFT — NOT PUBLISHED
- Fork public Issue, fork/original PR, original comment or issue, and product source change: NONE.
- Previous case before independent rerun: 2026-11-18 conditional S3 `PLAN_ONLY / NEEDS_EVIDENCE`, no terminal GO/NO_GO/BLOCKED; [prior Git commit](https://github.com/opensiro-contributions/browser-harness/commit/bc5e0fd8128af7637e074430fe0a93f25a49bfef). Read only AFTER independent current-source conclusion.
- Independent rerun: `NO_GO / NO_QUALIFIED_C_TARGET / DECISION_READY` with `NOT_RUN` validation. This is a new scoped proposal judgement and does not retroactively invalidate a prior plan or source issue.
- This source-pinned fork-local metadata update is not external publication; fork `owner_control=ALLOW` is not third-party permission.
