# Browser Harness — independent architecture-first roadmap (Human)

**PLAN_ONLY · proposal-stage NO_GO · research DECISION_READY · DRAFT — NOT PUBLISHED**

**One-sentence decision:** after examining the entire first-party harness and native alternatives, no additional complete, differentiated function-specific `C` constructor is currently qualified.

**Canonical decision receipt:** [roadmap.md](roadmap.md) is the single case-local authority for the accepted starting vector, source pins, dispositions and priorities.
**AI/developer contract:** [constructor-sufficiency.md](constructor-sufficiency.md) owns source-specific Track A/B and future test contract.

## 1. Why Opensiro and central accepted VSM assessment

OpenSiro investigates whether VSM-informed composable organizational interfaces reduce the engineering effort for agent harnesses. That value proposition is a **hypothesis**, not demonstrated cost reduction, product certification, or a demand to change Browser Harness.

**HISTORICAL Index, not current HEAD/target:** `S1=A · S2=C · S3=— · S3*=— · S4=— · S5=—`. [Accepted assessment](https://github.com/opensiro/vsm-harness-index/blob/394ce776e6945115891b8f7cc459f5a7f7d7aa39/assessments/br/browser-harness.md), Index `394ce776e6945115891b8f7cc459f5a7f7d7aa39`, blob `7522febc97e2eff75e78ad781cec9ac64f480a94`, review `afbcc381b963040c19627d788e40c7e7663171ee` at 2026-09-18, Profile 0.2.2 / Methodology 0.3.1.

**Repository-wide current boundary:** [original HEAD](https://github.com/browser-use/browser-harness/commit/fe4a2cd3dd308e8de929621e64e7f284d7a124d7); first-party CLI, CDP helpers, daemon, MCP, local/cloud browser integration, skill, domain/interaction recipes, tests and release CI. Claude/Codex task agents, Browser Use Cloud management and repo-maintainer governance do not automatically become in-boundary metasystem owners.

| Function / plain-language role | Historical Index state | Current observed ownership / feedback | Candidate / ranking |
| --- | --- | --- | --- |
| **S1 · Operations** — browser task execution | A | External autonomous agent chooses [CDP helper](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/helpers.py) actions, observes browser output | ALREADY_A; no mandatory C work |
| **S2 · Coordination** — avoid competing tab operations | C | [SKILL](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/SKILL.md) directs shared-lane serialization or isolated remote browsers, composed by host | ALREADY_C; open #1022 is not shipped |
| **S3 · Current management** — task/resource priorities | — | [daemon](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/daemon.py) handles CDP lifecycle, not current whole-work commitments | NO_TARGET; proposed allocator crosses unproved host boundary |
| **S3* · Independent audit** — corrective separate channel | — | [recorder](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/recorder.py) logs events and screenshot traces, without independent S3 judgment | NO_TARGET; mere instrumentation insufficient |
| **S4 · Adaptation** — prospective changes | — | [domain skills](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/SKILL.md) and agent-written helpers; #1025 proposes script drift replay | NO_TARGET; no lawful prospective decision returned via S3 |
| **S5 · Policy** — identity and ultimate purpose | — | Chrome user consent and host policy are outside the harness's local decision loop | NO_TARGET; parent boundary, intention UNVERIFIED |

The historical states are categorical agent/constructor/parent ownership claims, **not quality scores or six feature requests**. `A` means autonomous ownership, `C` means composable first-party constructor, `P` means parent-supported authority for eligible functions, and `—` is a bounded absence of a material local path; `?` means unresolved. Parent ownership or deliberately narrow scope is legitimate, but intentional omissions are not inferred from missing code. Maintainer issues document real tab-safety requests; a demand for S3/S4 is **NOT_STATED**.

## 2. Selected construction hypothesis and user outcome

**Target transition:** NO_QUALIFIED_C_TARGET
**Proposal-stage decision:** NO_GO
**Research disposition:** DECISION_READY

**P0: NO_QUALIFIED_C_TARGET.** There is no lawful minimal first-party C chain clearly distinct from native solutions. An operator currently has documented serial local execution or isolated remote browsers for competing agent tasks. The observed wrong-tab concern in [#582](https://github.com/browser-use/browser-harness/issues/582) and concurrency demand [#375](https://github.com/browser-use/browser-harness/issues/375) qualify narrower S2 protection and host coordination; they do not establish an S3 autonomous allocator.

**Hypothetical rejected S3:** a developer-composed actor deciding `admit/defer/hold` across multiple browser-worker commitments would additionally need authoritative task state, safe enforced effect and later task feedback. The source cannot supply the entire chain merely by adding a tab guard or callback. **No claim** this construction is useless to a different organizational boundary.

## 3. Track A existing work versus Track B missing C

| Function-specific consideration | Track A: native current source and open work | Track B: minimum on-top candidate | Finding |
| --- | --- | --- | --- |
| Shared-task coordination / candidate S3 | [SKILL](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/SKILL.md) shipped serial/isolated lanes; [#1022](https://github.com/browser-use/browser-harness/pull/1022) OPEN PR agent-owned tabs | Autonomous whole-work allocator with lawful actor, enforcement and return | INCOMPLETE_CHAIN, new management boundary unjustified |
| Replay drift / candidate S4 | [#1025](https://github.com/browser-use/browser-harness/pull/1025) OPEN PR saved scripts and output drift | Authorized autonomous later-capability adaptation through S3 | INCOMPLETE_CHAIN; replay is not S4 ownership |
| Separate review / candidate S3* | [recorder](https://github.com/browser-use/browser-harness/blob/fe4a2cd3dd308e8de929621e64e7f284d7a124d7/src/browser_harness/recorder.py) shipped; [#1039](https://github.com/browser-use/browser-harness/pull/1039) OPEN PR self-feedback | Independent reviewer with corrective decision to S3 | INCOMPLETE_CHAIN; unsupported separate authority |
| Ultimate policy / S5 | Host identity and Chrome consent | Local autonomous policy | NO_TARGET; outside chosen recursion |

Related [#901](https://github.com/browser-use/browser-harness/issues/901), [#998](https://github.com/browser-use/browser-harness/issues/998), [#911](https://github.com/browser-use/browser-harness/pull/911), [#1034](https://github.com/browser-use/browser-harness/pull/1034) cover narrow caller scope, reconnection and protection; none alone supplies whole-system C. Open original PRs are **not shipped**. Developer contract links pinned heads.

## 4. Priorities and minimum sufficient result

**P0:** `NO_QUALIFIED_C_TARGET`, rather than manufacturing six missing controllers. **P1:** `NONE`, since no qualified P0; first prove a new bounded need and lawful actor/return. **P2:** `NONE`, no independent optional constructor demand.

**Proposed C-sufficiency verdict:** `NO_QUALIFIED_C_TARGET`; the existing optional S3 and S4 notions remain hypotheses, not selected implementation plans.

## 5. Acceptance and stop

**Future positive (NOT_RUN):** same browser-work tasks demonstrate a developer-composed rightful management choice affecting a later real operation with feedback to that manager. **Negative (NOT_RUN):** stale/absent/unauthorized owner must fail closed, without touching another user's tab. **Falsifier:** show a source-native complete C chain or a fully specified minimal on-top first-party actor/authority/action/feedback loop whose outcome is not matched by host queue and remote isolation at equivalent effort.

## 6. Independent paths

Native maintainers may proceed with existing tab safety, task ownership and script-replay PRs without adopting VSM. Profile/Skills questions about recursive boundaries require separate evidence and owner review; no domain fork or independent feature is requested here. Prior OpenSiro S3 experiment exists but does not confer accepted first-party S3 and does not supersede independent original-source decisions.

## 7. Cost hypothesis

Engineering, integration, review, test, maintenance, browser and task-success costs would need matched native-alternative measurement. **NOT_MEASURED**, no claimed savings or completed performance trials.

## 8. Decision and handoff

**Proposal-stage decision:** NO_GO
**Research disposition:** DECISION_READY

**Target transition:** NO_QUALIFIED_C_TARGET

**Historic comparison (read after independent decision):** old [2026-11-18 case](https://github.com/opensiro-contributions/browser-harness/commit/bc5e0fd8128af7637e074430fe0a93f25a49bfef) proposed *conditional* S3 and left `PLAN_ONLY / NEEDS_EVIDENCE` without a terminal proposal verdict. This independently reviewed case now explicitly closes current boundary with scoped `NO_GO / DECISION_READY`, not a judgment on the original harness.

**Handoff:** retain [roadmap.md](roadmap.md) and [constructor-sufficiency.md](constructor-sufficiency.md) as synchronized canonical evidence and future falsification test contract. Fork metadata readback was `ALLOW / ACTIVE` on 2026-11-19; MIT original. **No public fork Issue**, original Issue/comment/PR, product implementation or Index regrade. Public contact needs separate exact approval; prepared with AI assistance, no independent human technical audit or native tests claimed.
