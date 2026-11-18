# Browser Harness — Shared browser resource control (S3) capability roadmap

**PLAN_ONLY / NEEDS_EVIDENCE · 2026-11-18 · DRAFT — NOT PUBLISHED**

## 1. Why Opensiro and central accepted VSM assessment

Opensiro tests whether VSM-informed reusable organizational specifications and source-native integration can standardize AI agent harnesses and lower development, integration, review and maintenance costs. **This is an unmeasured hypothesis**, not an obligation for Browser Use maintainers to adopt VSM. Prefer a cheaper native solution if it delivers the same real user outcome.

> **ACCEPTED HISTORICAL INDEX — NOT THE ROADMAP TARGET:** \`S1=A · S2=C · S3=— · S3*=— · S4=— · S5=—\`.  
> [Frozen accepted assessment](https://github.com/opensiro/vsm-harness-index/blob/d7d07e2f6db17d8ca9bc6c9c6c6d07892c611e1d/assessments/br/browser-harness.md); assessment file SHA \`7522febc97e2eff75e78ad781cec9ac64f480a94\`; \`review_ref=afbcc381b963040c19627d788e40c7e7663171ee\`; reviewed 2026-09-18; **historical** Profile 0.2.2 / Methodology 0.3.1. Now 61 days old; [Index re-review PR #3219](https://github.com/opensiro/vsm-harness-index/pull/3219) is **OPEN / unaccepted**. New original main is [\`4cccf3b8\`](https://github.com/browser-use/browser-harness/commit/4cccf3b8daf992227a6c9019ffbce5f7a2844280), observed 2026-11-18.

| Function | Accepted historical state | Meaning / roadmap consequence |
| --- | --- | --- |
| S1 · Browser operations | A | Task agents act autonomously using browser helpers, with observation return |
| S2 · Cross-agent coordination | C | Shared mutable tab needs serialization or isolation; first-party rules allow host composition |
| S3 · Current resource control | — | No accepted whole-task resource/priority decision actor and feedback; conditional C candidate only |
| S3* · Complementary audit | — | Screenshots/video/logs are not independent corrective audit |
| S4 · Future adaptation | — | Current-task helper expansion does not prove prospective environment-adaptation closure |
| S5 · Identity/policy | — | Chrome consent and maintainer policies are not runtime ultimate-policy governance |

**System boundary:** public Browser Harness CLI, daemon, CDP helpers, skill and MCP with multiple external coding-agent S1 tasks; not Browser Use Cloud's private management or the upstream maintainers' own organization. The [current README](https://github.com/browser-use/browser-harness/blob/4cccf3b8daf992227a6c9019ffbce5f7a2844280/README.md) notes Browser Harness is also the engine inside Browser Use CLI.

## 2. Proposed user capabilities and decision

[Issue #582](https://github.com/browser-use/browser-harness/issues/582) describes one agent closing **three other agents' browser tabs** during cleanup. [#375](https://github.com/browser-use/browser-harness/issues/375) describes concurrently operating subagents fighting over tabs. These establish a real shared-work safety/coordination need but **not by themselves a new S3=C requirement**.

Conditional question: does an operator supervising several current browser jobs need a *first-party developer-composable* S3 controller that can inspect present task commitments, authorize \`admit/defer/hold/safe_reassign\` and get a later outcome receipt? Or is a simple host queue with per-task target ID ownership and remote-browser isolation sufficient?

**Decision today:** investigate native materiality and overlapping PRs before any implementation. See [AI construction contract](constructor-sufficiency.md) and [source receipt](roadmap.md).

## 3. Existing native work vs missing capability

- **SHIPPED:** [SKILL.md](https://github.com/browser-use/browser-harness/blob/4cccf3b8daf992227a6c9019ffbce5f7a2844280/SKILL.md) directs serialization on one mutable local daemon or independent remote-browser lanes; [helpers.py](https://github.com/browser-use/browser-harness/blob/4cccf3b8daf992227a6c9019ffbce5f7a2844280/src/browser_harness/helpers.py) provides \`list_tabs/current_tab/switch_tab/new_tab/close_tab\`. [Merged #618](https://github.com/browser-use/browser-harness/pull/618) added named-daemon background tabs, [merged #744](https://github.com/browser-use/browser-harness/pull/744) clarified cleanup. These support S2; no S3 decision/return evidence follows.
- **OPEN original issues:** [#582](https://github.com/browser-use/browser-harness/issues/582) ownership/protection, [#895](https://github.com/browser-use/browser-harness/issues/895) browser/start-tab choice, [#901](https://github.com/browser-use/browser-harness/issues/901) caller-owned metadata preflight, [#998](https://github.com/browser-use/browser-harness/issues/998) reconnection; [#375](https://github.com/browser-use/browser-harness/issues/375) parallel need.
- **OPEN original PRs (unmerged):** [#760](https://github.com/browser-use/browser-harness/pull/760) target-scoped concurrency, [#846](https://github.com/browser-use/browser-harness/pull/846) tab guard, [#911](https://github.com/browser-use/browser-harness/pull/911) owned-target preflight, [#1034](https://github.com/browser-use/browser-harness/pull/1034) fail-closed reconnection, [#765](https://github.com/browser-use/browser-harness/pull/765) durable owner binding, [#713](https://github.com/browser-use/browser-harness/pull/713) owned cleanup. None may be treated as shipped.
- **Existing OpenSiro experiment:** [S3 assessment-informed record](https://github.com/opensiro-contributions/browser-harness/blob/opensiro/meta/.opensiro/contributions/browser-harness-s3-owned-scope-priority-admission.json), [integrated commit](https://github.com/opensiro-contributions/browser-harness/commit/ef5c5bcd92196d33a5b5463a64cfc20f0363895e), dependent on **unmerged #911**. Historical record reports **344 unit passes, 1 skipped and IPC fake-CDP canary**; real Chrome, full independent S3 decision owner and material advantage to a host queue remain **UNPROVEN**. This case is not a new contribution.

## 4. Proposed priority and minimum sufficient result

| Priority | Outcome | Minimum construction/evidence |
| --- | --- | --- |
| **P0 conditional S3=C** | An independently developer-composed current-resource decision actor, only if native need is unmet | Actual current capacity/commitments → bounded options → delegated autonomous S3 actor chooses → first-party versioned lease/owner enforcement → **later real task action and feedback to S3** |
| **P1 prerequisite** | Verify native benefit and safe authority | Inspect all relevant current PR diffs, reproduce #582-like synthetic collision, audit #911 dependency, compare historical experiment with current original main, enforce stale/unowned/missing actor negatives, test real Chrome and normal CLI/MCP compatibility |
| **P2: NONE** | No independent optional parent \`C(P)\` or \`A(P)\` demand yet | Do not force a maturity ladder or add S3*/S4/S5 on missing grades |

**S3 sufficiency is not established by a tab guard, policy text, raw CDP hook, generic plugin or passing mock tests.** Source-native materiality and all function-specific decision/authority/return links must be demonstrated before claiming a C-ready implementation.

## 5. Acceptance / stop gates

**Proposed, NOT EXECUTED:** two competing agents on one local lane; \`admit A/defer B\` with later observed correct-tab execution; different lawful \`hold\` choice; unauthorized/stale owner denial before any CDP effect; lost waiting client cleanup; default single-agent compatibility; same tasks compared against host serialization/remote isolation. If simpler native operation meets the task with less total cost, choose \`NO_USEFUL_CHANGE\`; if owner/feedback/benefit proof is missing, retain \`NEEDS_EVIDENCE\`.

## 6. Independent paths

Original maintainers can prioritize [#582](https://github.com/browser-use/browser-harness/issues/582), [#901](https://github.com/browser-use/browser-harness/issues/901) or existing PRs natively without adopting VSM. Any Profile/Skills semantic proposal requires independent evidence. A separate domain experiment needs separate scope and approval. Do not open a duplicate external Issue for the #582 need; [maintainer comment draft](maintainer-comment-draft.md) remains **NOT SENT**.

## 7. Cost hypothesis

Matched native baseline: simple host serialization and task-owned target whitelist (or independent remote browsers). Candidate: first-party bounded, composable S3 current allocation with enforced return. Measure engineering/review/integration/maintenance hours, false denial, unauthorized tab changes, task throughput/completion and ongoing costs. **NOT_MEASURED**; no developer savings, quality gain or grade change claimed.

## 8. Decision / handoff

**PLAN_ONLY / NEEDS_EVIDENCE.** The [technical construction contract](constructor-sufficiency.md) is a proposal, not tested source code. No new product branch, external Issue/comment/PR, fork public Issue, native tests or Index regrade arises from this update. \`ACTIVE / ALLOW\` for metadata is not blanket public publication consent.
