# Browser Harness — source-pinned architecture-first roadmap pilot

**Snapshot:** 2026-11-18. **Status:** `PLAN_ONLY / NEEDS_EVIDENCE · DRAFT — NOT PUBLISHED`. Read-only, non-authoritative example for the [OpenSiro roadmap procedure](https://github.com/opensiro/upstream/blob/main/docs/CAPABILITY_ROADMAP.md); all GitHub statuses below can change. **This is metadata-only on the OpenSiro fork; it does not alter the original project, fork product code, accepted Index, or Profile.**

## Identity and pins

- Original repository: browser-use/browser-harness
- Original HEAD: 4cccf3b8daf992227a6c9019ffbce5f7a2844280
- Observed at: 2026-11-18
- Accepted Index assessment: https://github.com/opensiro/vsm-harness-index/blob/d7d07e2f6db17d8ca9bc6c9c6c6d07892c611e1d/assessments/br/browser-harness.md
- Accepted assessment blob SHA: 7522febc97e2eff75e78ad781cec9ac64f480a94
- Accepted review ref: afbcc381b963040c19627d788e40c7e7663171ee
- Accepted reviewed at: 2026-09-18
- System in focus: shipped Browser Harness CLI, browser daemon, CDP/tab helpers, skill and MCP mode, with external agent actors; **not** Browser Use's separate maintainer organization or host product
- Assessment vector: `A C — — — —` (historical accepted Index, **not** a current-ref reassessment)
- Proposed Index re-review: [PR #3219](https://github.com/opensiro/vsm-harness-index/pull/3219), **open/unmerged at observation**, result `reassessed-unchanged` is **not canonical**.
- Historical assessed Profile: 0.2.2. Current semantic reference: [Profile 0.2.4](https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md) (current semantic reference, not a retroactive source review)
- Historical assessed Methodology: 0.3.1. Current methodology reference: [Methodology 0.3.8](https://github.com/opensiro/vsm-harness-skills/blob/main/skills/assess-vsm-harness/references/autonomy-states.md)

## Rights and authority

- [MIT license](https://github.com/browser-use/browser-harness/blob/bc274a297d893e94ee05b4901898809651876a2d/LICENSE) permits copying/modifying subject to retained notice; third-party site terms and imported examples remain separate constraints.
- [CONTRIBUTING.md](https://github.com/browser-use/browser-harness/blob/bc274a297d893e94ee05b4901898809651876a2d/CONTRIBUTING.md) says focused improvements/PRs welcome and uncertain ideas may be proposed via issue. CLA/AI-specific attestations are **NOT VERIFIED** by this document, not presumed waived.
- Matching [fork](https://github.com/opensiro-contributions/browser-harness) and [fork metadata](https://github.com/opensiro-contributions/browser-harness/blob/opensiro/meta/.opensiro/state.json) were observed with `owner_control=ALLOW` and `attention=ACTIVE`; these are **not** a blanket approval to publish public issues, comments, fork PRs or external PRs. The fork may have advanced since this snapshot.
- External-publication route: separate exact owner approval for the concrete destination, full issue body/diff and action is **NOT GRANTED** by this pilot.

## Existing work / overlap

| Source work | 2026-11-18 observation | Functional overlap and remaining task |
| --- | --- | --- |
| [Upstream #582](https://github.com/browser-use/browser-harness/issues/582) | OPEN ISSUE, real wrong-tab cleanup of 3 other agents' tabs | Source-backed S2 ownership harm, not automatic S3 necessity |
| [#375](https://github.com/browser-use/browser-harness/issues/375), [#895](https://github.com/browser-use/browser-harness/issues/895), [#901](https://github.com/browser-use/browser-harness/issues/901), [#998](https://github.com/browser-use/browser-harness/issues/998) | OPEN original issues | Parallel subagents, browser/target choice, scoped metadata and reconnection |
| [Current SKILL](https://github.com/browser-use/browser-harness/blob/4cccf3b8daf992227a6c9019ffbce5f7a2844280/SKILL.md), [helpers](https://github.com/browser-use/browser-harness/blob/4cccf3b8daf992227a6c9019ffbce5f7a2844280/src/browser_harness/helpers.py), [merged #618](https://github.com/browser-use/browser-harness/pull/618), [merged #744](https://github.com/browser-use/browser-harness/pull/744) | SHIPPED first-party S2 serial/remote isolation and tab helper/cleanup conventions | Does not prove distinct first-party S3 manager |
| [PR #760](https://github.com/browser-use/browser-harness/pull/760) @ \`e285724fabac1cd7cc949a0038013d80055a7aab\` | OPEN/unmerged | Target-specific shared connection/coordination |
| [PR #846](https://github.com/browser-use/browser-harness/pull/846) @ \`b1e0b7a9a0219a75e9ca6c36338530860da75423\` | OPEN/unmerged | Tab authorization guard, not manager closure |
| [PR #911](https://github.com/browser-use/browser-harness/pull/911) @ \`c2de9b79115ca38c19c43385b232c83fc0fbd875\` | OPEN/unmerged | Owned-target preflight; unmerged dependency of OpenSiro experiment |
| [PR #1034](https://github.com/browser-use/browser-harness/pull/1034) @ \`4056c5aece6e4a83ea999d60e42482b84f9eed7b\` | OPEN/unmerged | Reconnection helper, same-daemon concurrent race remains |
| [PR #765](https://github.com/browser-use/browser-harness/pull/765), [PR #713](https://github.com/browser-use/browser-harness/pull/713), [PR #1020](https://github.com/browser-use/browser-harness/pull/1020) | OPEN/unmerged | Durable binding, owned cleanup, dialog isolation; review exact diff before new code |
| [Existing OpenSiro S3 admission record](https://github.com/opensiro-contributions/browser-harness/blob/opensiro/meta/.opensiro/contributions/browser-harness-s3-owned-scope-priority-admission.json), [experiment commit](https://github.com/opensiro-contributions/browser-harness/commit/ef5c5bcd92196d33a5b5463a64cfc20f0363895e) | BUILD/EXPERIMENT on prior original main, includes full unmerged #911 | Earlier **344 unit pass, 1 skipped** and real IPC with fake CDP; no real Chrome, independently composed S3 actor, current-main coverage or materiality proof |
| [#637](https://github.com/browser-use/browser-harness/issues/637) | Historical issue CLOSED | Resource-pressure report; issue closure is not independent proof of shipped fix |

**Source/PR distinction:** original code heads above were observed on 2026-11-18. The latest first-party [main commit](https://github.com/browser-use/browser-harness/commit/4cccf3b8daf992227a6c9019ffbce5f7a2844280) differs from the fork experiment's earlier original base. An OPEN_PR or fork EXPERIMENT is never SHIPPED in original main. Examine exact head/diff/test overlap before any engineering.

## Function ownership

- S1 browser actions: external task agent chooses navigation/interaction through first-party helpers; actual browser observations return to its next task action.
- S2: simultaneous external agents sharing one local daemon can interfere through tab switching; existing first-party skill prescribes serialization or isolated browser lane; host composes the coordinating actor.
- Candidate S3: **not established**. Host/operator may choose browsers and agent commitments, but source issue #895/#901 and a tab API do not demonstrate a whole-system allocator/decision owner with returned controls across tasks.
- S3*: video review checks media/source artifacts; no independent S3 corrective channel evidenced.
- S4: maintainer decisions on domain skills occur at another recursion; no first-party prospective options that return to S3 evidenced.
- S5: ordinary consent/preferences and maintainer PR policy are **not** a shipped identity/ultimate-policy decision and return loop; no inferred S5=P.

## Capability priority

**Observed user counterfactual:** [#582](https://github.com/browser-use/browser-harness/issues/582) documents one agent closing other agents' shared Chrome tabs; [#375](https://github.com/browser-use/browser-harness/issues/375) asks for subagent parallelism. Existing task-owned \`targetId\` whitelist, serial host browser queue and isolated remote browsers are the **native baseline**. A task owner may benefit from composable *current* resource/commitment decisions, but this is **not yet a proved demand for S3=C**.

- **P0 conditional S3=C constructor:** current scoped lane state/commitments → resource pressure and permitted \`admit/defer/hold/reassign\` → independently developer-composed bounded autonomous S3 decision actor → enforced first-party lease/owner/CAS/version update → **actual later task operation receipt and feedback** for further current decisions. Only if this produces a materially useful task outcome beyond host scheduling; a guard or one-tab router alone is not S3.
- **P1 prerequisites before P0:** safely reproduce synthetic #582-style collision; compare original PR #760/#846/#911/#1034 exact current diffs; reconcile [existing OpenSiro S3 experiment](https://github.com/opensiro-contributions/browser-harness/blob/opensiro/meta/.opensiro/contributions/browser-harness-s3-owned-scope-priority-admission.json) and its unmerged #911 dependency; prove no unauthorized target enumeration/close, stale lease safety, cancellation cleanup, compatibility, real Chrome task feedback and native queue baseline. No new contribution ID for this plan.
- **P2: NONE:** no independent optional \`C(P)\`/\`A(P)\` parent mode or S3*/S4/S5 expansion is justified now.
- **Stop:** if existing/original-native host approaches fully close the same user need with lower/equal total effort, report \`NO_USEFUL_CHANGE\`; if the independently composed decision owner and later run feedback are not established, \`NEEDS_EVIDENCE\` is the correct result.

[Human decision](issue.md) · [AI five-link sufficiency/acceptance](constructor-sufficiency.md).

## Implementation options

1. **Plan only first:** reorganize #895, #901, #998 and #1034 by current native user outcomes, distinguish overlap and choose no-code/integration or actual S3 constructor only if maintainers agree. This is not permission to edit those PRs.
2. **If qualified, small product PR:** a minimal host-composable shared-resource decision/feedback interface; keep S2 tab correctness work separate; each actual implementation follows full `upstream upgrade` tests, classification, fork-local review/publication gates.
3. **Native counterfactual:** compare a minimal external host scheduler using existing APIs against the proposed constructor under the same two-agent browser lane collision scenario. If new API does not improve a real task, omit it.

## Specification and domain alternatives

- Profile feedback: if the case reveals a real ambiguity in function-specific ownership/recursion/closure, propose evidence and counterexamples to [VSM Profile](https://github.com/opensiro/vsm-harness-profile) as a **separate normative review**, not a mandatory original project dependency.
- Skills feedback: if construction evidence / parent-mode calibration is ambiguous, send a separately scoped proposal to [VSM Skills](https://github.com/opensiro/vsm-harness-skills).
- Optional domain experiment: only with independent permission, explore an explicitly bounded **multi-tenant browser-work** fork; compare the smallest native scheduler to a VSM-informed constructor. This fork has **NOT BEEN CREATED** by this roadmap.

## Cost experiment

- Matched task: two external agents competing for one mutable browser lane while preserving each agent's tab ownership.
- Native baseline: simple host-side serialization and explicit isolated browser setup.
- Hypothetical variant: a verified first-party, composable current-control constructor with owner/feedback/closure.
- Costs to measure: engineering hours, integration/review/test effort, regressions and maintenance; task success and isolation correctness.
- Cost status: NOT_MEASURED
- No quantified developer saving, quality superiority, new VSM grade or maintainer endorsement is claimed.

## Delivery and publication

- Canonical Human Issue decision: [issue.md](issue.md)
- AI/developer technical sufficiency contract: [constructor-sufficiency.md](constructor-sufficiency.md)
- Optional [original #582 comment draft](maintainer-comment-draft.md): NOT SENT; no new original issue
- Existing fork S3 assessment-informed experiment: [record](https://github.com/opensiro-contributions/browser-harness/blob/opensiro/meta/.opensiro/contributions/browser-harness-s3-owned-scope-priority-admission.json); this roadmap creates no new contribution

- Result: NEEDS_EVIDENCE
- External issue: DRAFT — NOT PUBLISHED
- Case metadata: dated, **non-authoritative source-pinned plan**, with an append-only fork event; not a new independent implementation or original Issue.
- External maintainer communication, original PR, public fork-local review PR, domain fork publication and normative Profile/Skills PR: **NONE CREATED** by this pilot.

**Storage provenance:** Moved from [Upstream's previously checked-in example](https://github.com/opensiro/upstream/blob/c870a6a756bea774012c48877ad5a12aa991e656/docs/examples/browser-harness-roadmap-20261117.md) to `.opensiro/issues/` under this matched fork on `opensiro/meta`. Migration is not an upstream code change, assessment re-grade, or external maintainer communication.
