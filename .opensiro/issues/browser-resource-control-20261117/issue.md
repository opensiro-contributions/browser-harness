# Browser Harness — S3=— -> S3=C (OpenSiro fork-local Human roadmap)

**PLAN_ONLY · proposal-stage GO · research NEEDS_EVIDENCE · DRAFT — NOT PUBLISHED**

**One-sentence proposal:** At existing BU_NAME, current-tab and cloud provision/stop seams, add an optional bounded task-admission decision with an owned resource snapshot, capability-limited lease and proven task-action/release feedback.

**Canonical decision receipt:** [roadmap.md](roadmap.md) — source of truth for historical assessment, canonical target, P0/P1/P2, decision and research state.
**Technical companion:** [constructor-sufficiency.md](constructor-sufficiency.md) — source-native controls and future test contract.
**Working fork:** opensiro-contributions/browser-harness on opensiro/meta.
**Case:** .opensiro/issues/browser-resource-control-20261117/.

## 1. Why Opensiro and central accepted VSM assessment

OpenSiro explores whether VSM-informed organizational construction helps agent harness engineering. It is a **research hypothesis**, not product certification, cost savings or a maintainer adoption request.

### Central starting point — accepted Index, not the target

> **ACCEPTED HISTORICAL INDEX — not current-HEAD grades or proposed after-states**
>
> **S1=A · S2=C · S3=— · S3*=— · S4=— · S5=—**
>
> [Pinned accepted Index assessment](https://github.com/opensiro/vsm-harness-index/blob/394ce776e6945115891b8f7cc459f5a7f7d7aa39/assessments/br/browser-harness.md); blob SHA 7522febc97e2eff75e78ad781cec9ac64f480a94; historical review ref afbcc381b963040c19627d788e40c7e7663171ee; reviewed 2026-09-18; historical Profile/Skills versions retained in the canonical [roadmap.md](roadmap.md).

**Repository-wide audit:** The present same-case v0.18.2 follow-up used browser-use/browser-harness original HEAD 22ecf8545d67c474fa024643632d70af28b7fa0e, checked first-party source at [SKILL.md](https://github.com/browser-use/browser-harness/blob/22ecf8545d67c474fa024643632d70af28b7fa0e/SKILL.md) and [src/browser_harness/daemon.py](https://github.com/browser-use/browser-harness/blob/22ecf8545d67c474fa024643632d70af28b7fa0e/src/browser_harness/daemon.py), original repository https://github.com/browser-use/browser-harness/issues/1022 (OPEN, agent-owned tabs). Historical fork case references other issue proposals, not assumed merged; original PR #626 CLOSED_UNMERGED (daemon lifecycle hardening)., prior accepted assessment and published protocol. The system in focus is the installed first-party agent harness and its supported components; separate host provider, original maintainer policy, repo CI and external services are not automatically in-boundary autonomous owners. Prior fork-case evidence was opened only after the source-first #58 [checkpoint](https://github.com/opensiro/upstream/issues/58#issuecomment-7047329680). This was a bounded source review, not exhaustive source classification or a fresh accepted Index grade.

| Function / plain-language role | Historical Index state | Current source-backed owner/closure | Candidate / justified no-target / uncertainty and rank |
| --- | --- | --- | --- |
| **S1 · Operations** | A | First-party SKILL.md describes one mutable attached tab and required serialization, named daemon fallback and cloud browser isolation. Daemon has session-scoped locks; deterministic tab isolation already covers S2, not autonomous whole-task admission. | ALREADY_A — external autonomous agent chooses browser operations with first-party helpers and receives page observations; no new C selected |
| **S2 · Coordination** | C | First-party SKILL.md describes one mutable attached tab and required serialization, named daemon fallback and cloud browser isolation. Daemon has session-scoped locks; deterministic tab isolation already covers S2, not autonomous whole-task admission. | ALREADY_C — serial local lane or separate remote browsers regulates observed inter-agent tab conflicts; #1022 OPEN PR improves owned-tab isolation but does not create S3 management |
| **S3 · Current management** | — | First-party SKILL.md describes one mutable attached tab and required serialization, named daemon fallback and cloud browser isolation. Daemon has session-scoped locks; deterministic tab isolation already covers S2, not autonomous whole-task admission. | P0 conditional: One-tab collision safety and a separate optional resource allocation decision are different functions. A lock alone does not give an autonomous whole-task priority choice; proof is needed that enforcement covers all relevant browser entrypoints. |
| **S3* · Independent review** | — | S1 agent browsing and S2 tab isolation are already covered. The conditional S3 target is whole-task competing resource allocation; S3* audit and S4 foresight have no separate verified candidate, S5 remains user policy. | DEFER — recorder/video/telemetry do not independently challenge S1 claims and return a corrective judgment to S3; not a minimal first construction |
| **S4 · Future adaptation** | — | S1 agent browsing and S2 tab isolation are already covered. The conditional S3 target is whole-task competing resource allocation; S3* audit and S4 foresight have no separate verified candidate, S5 remains user policy. | DEFER — agent-written domain skills and OPEN #1025 saved-script drift detection do not create an outside-and-future adaptation owner that returns to S3 |
| **S5 · Identity/policy** | — | Legitimate parent/user controls ultimate policy, approval and publication, not the proposed auditor or controller. | NO_TARGET_PARENT — Chrome consent, cloud budget and ultimate identity legitimately belong to user/host; no intentional product omission inferred from missing source |

**Interpretation:** A, C, P and — denote ownership categories, **not quality ranks**; a historical dash is not proof work is necessary and A is not inferior to C. Unsupported current-HEAD functions stay UNKNOWN rather than silently regraded.

**Priority rationale:** S1 agent browsing and S2 tab isolation are already covered. The conditional S3 target is whole-task competing resource allocation; S3* audit and S4 foresight have no separate verified candidate, S5 remains user policy. The selected S3 target is the only conditional P0 in this existing case. Utility and actual independent operation remain unmeasured.

**Deliberate exclusions / methodology challenge:** No first-party independent actor has been shown to ship the complete optional link. Do not promote the historical grade or treat a proposed design as installed. No new S5 delegation or additional automatically generated Sx. Separate Profile/Skills review is required for any real classification counterexample.

**Contributor / maintainer interests:** NOT_STATED as approval for this construction. An original Issue is not maintainer acceptance.

## 2. Selected construction hypothesis and operator outcome

**Target transition:** S3=— -> S3=C

**Function-specific disturbance:** Two simultaneous agent browser tasks compete for one mutable attached tab or scarce isolated cloud capacity; specific race is documented in first-party SKILL.

**Proposed C capability (P0):** At existing BU_NAME, current-tab and cloud provision/stop seams, add an optional bounded task-admission decision with an owned resource snapshot, capability-limited lease and proven task-action/release feedback.

**Best native operator alternative:** Prefer the documented SKILL serialization, existing named daemon and isolated remote browser when adequate; do not vendor a general scheduler. Native source: [SKILL.md](https://github.com/browser-use/browser-harness/blob/22ecf8545d67c474fa024643632d70af28b7fa0e/SKILL.md) and [src/browser_harness/daemon.py](https://github.com/browser-use/browser-harness/blob/22ecf8545d67c474fa024643632d70af28b7fa0e/src/browser_harness/daemon.py).

**Expected user benefit:** HYPOTHETICAL. HYPOTHETICAL; dynamic priority and constrained cost decisions among browser jobs, not proven faster, cheaper or requested by original maintainers No native implementation or matched benefit test has occurred.

**Architectural sufficiency argument:** The first-party baseline already provides part of the path: First-party SKILL.md describes one mutable attached tab and required serialization, named daemon fallback and cloud browser isolation. Daemon has session-scoped locks; deterministic tab isolation already covers S2, not autonomous whole-task admission. The proposed developer-installed decision owner adds the strictly scoped capability: Choose serialize this task, grant isolated named daemon, defer, or provision an authorized cloud lane while respecting quota and ownership. A lawful effect and later feedback are required: The selected task receives only its scoped browser lane and a later real operation/closure event changes available lane state; unauthorized cross-lane use fails closed. This is a conditional complete design, not a shipped C witness.

## 3. Existing native work versus missing construction

**Track A — native coverage:** SHIPPED first-party source: [SKILL.md](https://github.com/browser-use/browser-harness/blob/22ecf8545d67c474fa024643632d70af28b7fa0e/SKILL.md) and [src/browser_harness/daemon.py](https://github.com/browser-use/browser-harness/blob/22ecf8545d67c474fa024643632d70af28b7fa0e/src/browser_harness/daemon.py). Existing original evidence: https://github.com/browser-use/browser-harness/issues/1022 (OPEN, agent-owned tabs). Historical fork case references other issue proposals, not assumed merged; original PR #626 CLOSED_UNMERGED (daemon lifecycle hardening).. Issue or PR is never treated as deployed simply by title.

**Track B — independent on-top C construction:** At existing BU_NAME, current-tab and cloud provision/stop seams, add an optional bounded task-admission decision with an owned resource snapshot, capability-limited lease and proven task-action/release feedback. Keep the original's native terminology, identities, state and permission checks.

| C-sufficiency requirement | Already present / original status (A) | Smallest conditional first-party delta (B) |
| --- | --- | --- |
| Scoped independent owner choice | First-party SKILL.md describes one mutable attached tab and required serialization, named daemon fallback and cloud browser isolation. Daemon has session-scoped locks; deterministic tab isolation already covers S2, not autonomous whole-task admission. | Choose serialize this task, grant isolated named daemon, defer, or provision an authorized cloud lane while respecting quota and ownership. |
| Enforced effect and later observation | SKILL.md, src/browser_harness/daemon.py provide candidate entrypoints, not a proven new C | The selected task receives only its scoped browser lane and a later real operation/closure event changes available lane state; unauthorized cross-lane use fails closed. |

**Distinctness and falsifier:** One-tab collision safety and a separate optional resource allocation decision are different functions. A lock alone does not give an autonomous whole-task priority choice; proof is needed that enforcement covers all relevant browser entrypoints. With manager removed, there must be no independent autonomous whole-current priority choice; an unauthorized lease, bypassable raw CDP action or missing later real-action return defeats the proposed C chain Historic prior decision remains the canonical baseline; no new unrelated function is implied.

## 4. Priorities and minimum sufficient result

- **P0:** Opt-in first-party browser-resource-admission API with current workload snapshot, bounded local/defer/authorized-cloud options, developer-composed autonomous S3 decision owner, atomic scoped lease enforcement, and real subsequent browser action/commitment feedback returned to owner
- **P1:** Establish permitted host-supplied current task commitments and priority envelope; check #1022 and #911 owner scope overlap; add lease/epoch enforcement before opted-in CDP effects; prove later task feedback, CLI/MCP distribution and safe cloud budget; compare simple host queue under matched tasks
- **P2:** NONE — no second function or obligatory parent-governed mode

**Proposed C-sufficiency verdict:** PROPOSED_C_SUFFICIENT at a conditional architectural proposal stage only. No native build, cost proof, Index regrade or external consent.

## 5. Proposed acceptance and stop gates

**Future positive test:** With two real browser-task requests, verify the installed owner can lawfully choose local serialization versus permitted isolated lane, and the next browser operation plus release shows the choice.

**Future negative test:** No lease, cross-lane ownership mismatch, stale tab, exhausted cloud budget or owner outage blocks forbidden action and preserves existing single-agent behavior.

**Proposed falsifier:** A shipped equivalent C already exists, or native host queue plus isolated remote browsers achieve the same task and owner outcome with lower/equal total engineering and maintenance cost, or safe first-party return cannot be implemented

**Validation state:** NOT_RUN; only document structural validation will be performed on fork-local artifacts, not native tests.

## 6. Independent paths

**Original-native contribution:** Prefer the documented SKILL serialization, existing named daemon and isolated remote browser when adequate; do not vendor a general scheduler. Third-party code PR, Issue or comment requires separate owner approval and normal project rules.

**Profile / Skills:** No forced methodology change; raise an independent correction only for a reproducible semantics/ownership conflict.

**Domain fork:** Optional licensed and permission-checked test only, not performed or authorized here.

## 7. Cost hypothesis

Matched native A versus optional new B would measure actual engineering, review, integration, runtime and maintenance effort alongside the named operator outcome. **Cost status: NOT_MEASURED.** Cost reduction is not asserted.

## 8. Decision / handoff

**Proposal-stage decision:** GO

**Research disposition:** NEEDS_EVIDENCE

**Decision reason / next permitted step:** Canonical proposal remains GO / NEEDS_EVIDENCE based on the earlier source-pinned receipt. This v0.18.2 source-first follow-up found One-tab collision safety and a separate optional resource allocation decision are different functions. A lock alone does not give an autonomous whole-task priority choice; proof is needed that enforcement covers all relevant browser entrypoints. and does not claim newly shipped capabilities or five independent isolated chat contexts. Compare the cheapest native alternative, source drift and lawful C feedback before product implementation.

**Agent/developer handoff:** [constructor-sufficiency.md](constructor-sufficiency.md) and [roadmap.md](roadmap.md), with reservations and prior-independent checkpoint at [Upstream #58](https://github.com/opensiro/upstream/issues/58#issuecomment-7047108048).

**Rights and publication:** MIT original LICENSE; matched fork opensiro/meta owner state was ACTIVE / ALLOW at preflight; recheck before effect. **No public fork Issue**, original Issue/comment/PR, implementation, changed Index grade or new S5 authority is authorized. PAUSE/STOP must block. This draft is not externally published.

**AI disclosure:** Prepared with AI assistance. No native tests, independent human validation or measured benefit claimed.
