# Browser Harness — composable current browser resource control (Human)

**PLAN_ONLY · proposal-stage GO · research NEEDS_EVIDENCE · DRAFT — NOT PUBLISHED**

**Proposal:** Make it possible to supply an autonomous S3 manager that chooses which of several current browser tasks should be admitted locally, deferred, or assigned an explicitly authorized remote lane; enforce its decision and report later real actions.

**Canonical case decision:** [roadmap.md](roadmap.md). **Technical AI/developer handoff:** [constructor-sufficiency.md](constructor-sufficiency.md).

## 1. Why Opensiro and the historical accepted VSM baseline

OpenSiro studies whether VSM-informed first-party constructors can make multi-agent harnesses cheaper and safer to develop and integrate. This is a research proposition, **not a proven saving** or a demand that Browser Use adopt VSM.

**Accepted historical general Index (NOT a new HEAD assessment):** S1=A · S2=C · S3=— · S3*=— · S4=— · S5=—. [Pinned accepted assessment](https://github.com/opensiro/vsm-harness-index/blob/394ce776e6945115891b8f7cc459f5a7f7d7aa39/assessments/br/browser-harness.md), blob 7522febc97e2eff75e78ad781cec9ac64f480a94, 2026-09-18 at afbcc381b963040c19627d788e40c7e7663171ee; Profile 0.2.2, Methodology 0.3.1. Current original [HEAD fe4a2cd3dd308e8de929621e64e7f284d7a124d7](https://github.com/browser-use/browser-harness/commit/fe4a2cd3dd308e8de929621e64e7f284d7a124d7) observed 2026-11-19. Assessment is 62 days old and a separate Index recheck is advised, not required for this plan.

**Assessed boundary:** Standard Browser Harness CLI/daemon/helpers/skill/MCP and optional local/cloud browser control used by external autonomous model agents. An external host's work planning, Browser Use private cloud service, and the original repository's CI/maintainer organization are not silently included. These letters classify *ownership*, not feature quality or maturity.

| Function and plain-language role | Historical Index state | Current first-party operating relation | Selection |
| --- | --- | --- | --- |
| **S1 · Operations** — execute browser tasks | A | Agent chooses browser actions and sees results through [helpers](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/helpers.py) | ALREADY_A; no new C |
| **S2 · Coordination** — reduce tab interference | C | [SKILL](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/SKILL.md) prescribes serial local or isolated cloud lanes; original [PR #1022](https://github.com/browser-use/browser-harness/pull/1022) is still open | ALREADY_C; reuse |
| **S3 · Current management** — allocate resources and priorities for the whole | — | Daemon/host can run local and cloud tasks, but the discretionary cross-task manager interface is missing | **P0: S3→C** |
| **S3* · Complementary audit** — check reality independently | — | Recordings and telemetry are not separate corrective judgment | DEFER |
| **S4 · Outside-and-future adaptation** — respond to evolving environment | — | Agent-created domain recipes and open script-drift PR are not a prospective S3-coupled decision loop | DEFER |
| **S5 · Ultimate identity and policy** — authorized higher-order direction | — | Chrome approval and cloud budget remain with user/host, not an autonomous harness governor | Parent boundary; no target |

A historical absence does not imply a defect. S3* or S4 would need independent authority/return not presently established. Intentional omission is NOT VERIFIED merely because a module is absent. Maintainer request for a new S3 actor is NOT STATED; source issues establish only underlying shared-work pressure.

## 2. User/operator outcome and selected C hypothesis

**Target transition:** S3=— -> S3=C
**Proposal-stage decision:** GO
**Research disposition:** NEEDS_EVIDENCE

[Original #375](https://github.com/browser-use/browser-harness/issues/375) requests simultaneous subagents but reports tab interference; [original #582](https://github.com/browser-use/browser-harness/issues/582) reports erroneous closure of other agents' tabs. Native [SKILL](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/SKILL.md) already offers serial local work or independent remote browsers. Those issues show real S2 coordination pressure, **not independently proven demand for S3**.

The distinct S3 task is a whole-work choice: given tasks A and B, their commitments, budget and browser constraints, a composed manager may admit A into the local lane and defer B; with explicit cloud budget it could place B on an isolated remote browser. It must have a bounded decision right, an enforced outcome on later browser operations, and feedback about those operations. It cannot create parent permissions or expose someone else's browser tabs.

## 3. Track A original-native work versus Track B on-top

| Required S3 property | Track A: shipped and open original work | Track B: proposed minimal additional C |
| --- | --- | --- |
| Current whole-work view | [admin](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/admin.py) provisions cloud browsers, daemon tracks attached session; open #1022 proposes scoped tab owners | Opt-in tasks, commitments, capacity, priority and versioned leases, never unauthorized tab enumeration |
| Decision with alternatives | Host currently serializes or chooses remote manually | First-party legal choices local/defer/remote exposed to independently composed autonomous manager |
| Effect + return | [daemon](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/daemon.py) handles IPC/CDP; CLI/MCP have operational results | Enforce lease at browser side-effect boundary and send later action/task status to the SAME manager |

Do not duplicate [PR #1022](https://github.com/browser-use/browser-harness/pull/1022) owner-safe tabs, [PR #911](https://github.com/browser-use/browser-harness/pull/911) scoped target preflight, or [PR #760](https://github.com/browser-use/browser-harness/pull/760) multiplexing. They address S2 and owner safety, not whole-current resource commitments. [PR #1025](https://github.com/browser-use/browser-harness/pull/1025) is an unmerged script-replay alternative for S4 investigation, not a shipped S3 owner.

## 4. Priorities and minimum sufficiency

**P0:** Design a first-party opt-in S3 state/options/decision/lease/actual feedback constructor for a developer-provided autonomous actor. **P1:** verify owner scope, parent capacity and cloud authority, atomic server enforcement, actual return, and CLI/MCP compatibility against current and open PR code. **P2:** NONE.

**Proposed C-sufficiency verdict:** PROPOSED_C_SUFFICIENT at proposal level, NOT IMPLEMENTED and NOT INDEX-CLASSIFIED. A queue, generic hook, daemon or tab lock alone cannot earn S3=C. Details and falsifiable test scenarios belong in [constructor-sufficiency.md](constructor-sufficiency.md).

## 5. Acceptance and stop

**Positive (NOT_RUN):** two concurrent browser tasks, one lane; a manager legitimately admits A/defers B; an alternative manager decision admits B/defers A; a later CDP operation is permitted/denied accordingly and outcome flows back to manager to update commitments. Under explicit cloud authorization a remote option can also be selected.

**Negative (NOT_RUN):** wrong/stale/revoked lease, absent autonomous manager, missing cloud grant or expired capacity cannot cause another agent's tab action or paid browser creation. Default non-opt-in use remains unchanged.

**Falsifier:** first-party lease/effect/feedback proves impossible, management remains hardcoded FIFO, or a minimal host queue plus documented isolation solves the same operator problem with lower/equal total effort. In that case stop this proposed S3 change even if other original fixes remain worthwhile.

## 6. Independent paths and permissions

Original maintainers can merge existing safe-tab/remote PRs without an S3 proposal. Profile/Skills discussion requires separate normative evidence; a domain-specific experiment requires its own permission. Current [MIT license](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/LICENSE) is readable; further contributor AI/CLA/DCO requirements are UNVERIFIED. OpenSiro fork metadata ALLOW permits this research document, not public fork GitHub Issue or original PR/comment. No paid browser was started.

## 7. Cost hypothesis

Compare matched tasks, operator permissions, correct browser outcomes, test/integration/review hours, ongoing maintenance and cloud spend between a simple host queue and proposed S3 management. **Cost status: NOT_MEASURED.**

## 8. Proposal verdict and handoff

**Target transition:** S3=— -> S3=C
**Proposal-stage decision:** GO
**Research disposition:** NEEDS_EVIDENCE

The previous [NO_GO case revision](https://github.com/opensiro-contributions/browser-harness/commit/c6df76d4eee6190a65623c85f76147f0ba7f87c1) was inspected *only after* independently forming this proposal. That review did not establish a qualified C path; this one proposes a bounded full actor→authority→action→return chain and reserves empirical benefit for validation. Both remain traceable. See [canonical roadmap.md](roadmap.md) and [AI contract](constructor-sufficiency.md).

**Disclosure:** AI-assisted plan-only research; no native suite pass, independent human review, new Index classification, implementation or external/public publication claimed.
