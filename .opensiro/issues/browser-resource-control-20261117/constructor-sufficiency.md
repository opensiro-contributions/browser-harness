# Browser Harness — source-native S3 C-construction technical contract

**Canonical storage:** opensiro-contributions/browser-harness@opensiro/meta:.opensiro/issues/browser-resource-control-20261117/constructor-sufficiency.md.
**Level 1 / Human decision Issue:** [issue.md](issue.md).
**Canonical decision receipt:** [roadmap.md](roadmap.md), authoritative for Index vector, case pins, priority and verdict.
**Stage:** PLAN_ONLY / HYPOTHESIS, current v0.18.2 template synchronization; **DRAFT — NOT PUBLISHED**. Native validation NOT_RUN.

## 1. Function-specific construction boundary and methodology checks

**Source and mode boundary:** Original browser-use/browser-harness at current original HEAD 22ecf8545d67c474fa024643632d70af28b7fa0e, first-party entrypoints [SKILL.md](https://github.com/browser-use/browser-harness/blob/22ecf8545d67c474fa024643632d70af28b7fa0e/SKILL.md) and [src/browser_harness/daemon.py](https://github.com/browser-use/browser-harness/blob/22ecf8545d67c474fa024643632d70af28b7fa0e/src/browser_harness/daemon.py). The canonical historical research HEAD remains fe4a2cd3dd308e8de929621e64e7f284d7a124d7; accepted historical Index https://github.com/opensiro/vsm-harness-index/blob/394ce776e6945115891b8f7cc459f5a7f7d7aa39/assessments/br/browser-harness.md reviewed at afbcc381b963040c19627d788e40c7e7663171ee. The supported local first-party runtime and its explicit optional modes are the unit of analysis. Original project's own CI, third-party provider, external management and parent owner are not silently counted as agent functions.

**Target transition:** S3=— -> S3=C

**Six-function dependencies (S1/S2/S3/S3*/S4/S5):** S1 agent browsing and S2 tab isolation are already covered. The conditional S3 target is whole-task competing resource allocation; S3* audit and S4 foresight have no separate verified candidate, S5 remains user policy. Reuse historical S1=A · S2=C · S3=— · S3*=— · S4=— · S5=— without changing the Index. Supporting runtime permissions and transport are not themselves autonomous decisions.

**Function witness:** Two simultaneous agent browser tasks compete for one mutable attached tab or scarce isolated cloud capacity; specific race is documented in first-party SKILL. The legitimate independent choice and owner: a developer-composed current browser-task resource owner chooses when several agents may share a bounded local daemon versus receive a named isolated daemon/cloud browser. Choose serialize this task, grant isolated named daemon, defer, or provision an authorized cloud lane while respecting quota and ownership. The effect and feedback must be The selected task receives only its scoped browser lane and a later real operation/closure event changes available lane state; unauthorized cross-lane use fails closed..

**Counterfactual owner test:** Remove the optional developer-composed S3 decision actor but keep current source machinery: First-party SKILL.md describes one mutable attached tab and required serialization, named daemon fallback and cloud browser isolation. Daemon has session-scoped locks; deterministic tab isolation already covers S2, not autonomous whole-task admission. The specific extra choice would then be missing: One-tab collision safety and a separate optional resource allocation decision are different functions. A lock alone does not give an autonomous whole-task priority choice; proof is needed that enforcement covers all relevant browser entrypoints.. A mere generic hook or another model call does not count.

**Possible methodological negative control:** If baseline first-party code already closes the exact owner/choice/effect/return at the supported boundary, or only a human parent may choose, report native equivalence and withdraw the new C design rather than regrade.

**Contributor / maintainer priorities:** NOT_STATED as approval of this exact VSM construction; third-party product direction remains the maintainer's.

## 2. Source-pinned baseline and parallel native Track A / on-top Track B

**Original native workflow:** First-party SKILL.md describes one mutable attached tab and required serialization, named daemon fallback and cloud browser isolation. Daemon has session-scoped locks; deterministic tab isolation already covers S2, not autonomous whole-task admission. First-party pinned source: [SKILL.md](https://github.com/browser-use/browser-harness/blob/22ecf8545d67c474fa024643632d70af28b7fa0e/SKILL.md) and [src/browser_harness/daemon.py](https://github.com/browser-use/browser-harness/blob/22ecf8545d67c474fa024643632d70af28b7fa0e/src/browser_harness/daemon.py).

**Closest existing solution:** Prefer the documented SKILL serialization, existing named daemon and isolated remote browser when adequate; do not vendor a general scheduler.

**Relevant original Issues/PRs:** https://github.com/browser-use/browser-harness/issues/1022 (OPEN, agent-owned tabs). Historical fork case references other issue proposals, not assumed merged; original PR #626 CLOSED_UNMERGED (daemon lifecycle hardening).. Labels such as OPEN or CLOSED are current at this follow-up only where checked; unverified heads are not treated as merged.

| Required C link or operator outcome | Track A: shipped/current source | Track B: minimum integration | Falsifier |
| --- | --- | --- | --- |
| Bounded whole-function decision | First-party SKILL.md describes one mutable attached tab and required serialization, named daemon fallback and cloud browser isolation. Daemon has session-scoped locks; deterministic tab isolation already covers S2, not autonomous whole-task admission. | Choose serialize this task, grant isolated named daemon, defer, or provision an authorized cloud lane while respecting quota and ownership. | One-tab collision safety and a separate optional resource allocation decision are different functions. A lock alone does not give an autonomous whole-task priority choice; proof is needed that enforcement covers all relevant browser entrypoints. |
| Lawful downstream effect | Source entrypoints at SKILL.md and src/browser_harness/daemon.py | The selected task receives only its scoped browser lane and a later real operation/closure event changes available lane state; unauthorized cross-lane use fails closed. | No lease, cross-lane ownership mismatch, stale tab, exhausted cloud budget or owner outage blocks forbidden action and preserves existing single-agent behavior. |

**On-top distinctness:** One-tab collision safety and a separate optional resource allocation decision are different functions. A lock alone does not give an autonomous whole-task priority choice; proof is needed that enforcement covers all relevant browser entrypoints. First prefer the exact native solution; a copied supervisor abstraction is insufficient.

**Source ambiguity / rights blockers:** Future source HEAD/PR changes, reviewer identity, permission of the original owner, and tests are unverified. A matched fork research write does not authorize external original actions or code changes. No evidence-free demand assumption.

## 3. Minimal complete S3 first-party C construction

**Required property:** A first-party S3-specific path to install a legitimate autonomous decision owner, enforce its selected lawful alternative, and return later operational evidence.

| Necessary native component or port | Existing first-party source | Smallest proposed change / integration | Legitimate owner, effect, return |
| --- | --- | --- | --- |
| Decision evidence and invocation | [SKILL.md](https://github.com/browser-use/browser-harness/blob/22ecf8545d67c474fa024643632d70af28b7fa0e/SKILL.md) | At existing BU_NAME, current-tab and cloud provision/stop seams, add an optional bounded task-admission decision with an owned resource snapshot, capability-limited lease and proven task-action/release feedback. | a developer-composed current browser-task resource owner chooses when several agents may share a bounded local daemon versus receive a named isolated daemon/cloud browser |
| Bound decision and later feedback | [src/browser_harness/daemon.py](https://github.com/browser-use/browser-harness/blob/22ecf8545d67c474fa024643632d70af28b7fa0e/src/browser_harness/daemon.py) | The selected task receives only its scoped browser lane and a later real operation/closure event changes available lane state; unauthorized cross-lane use fails closed. | Choose serialize this task, grant isolated named daemon, defer, or provision an authorized cloud lane while respecting quota and ownership. |

**Architectural C-sufficiency argument:** Native baseline: First-party SKILL.md describes one mutable attached tab and required serialization, named daemon fallback and cloud browser isolation. Daemon has session-scoped locks; deterministic tab isolation already covers S2, not autonomous whole-task admission. The key residual is One-tab collision safety and a separate optional resource allocation decision are different functions. A lock alone does not give an autonomous whole-task priority choice; proof is needed that enforcement covers all relevant browser entrypoints. The strongest scoped optional solution is At existing BU_NAME, current-tab and cloud provision/stop seams, add an optional bounded task-admission decision with an owned resource snapshot, capability-limited lease and proven task-action/release feedback. Alternative one: use native/manual Prefer the documented SKILL serialization, existing named daemon and isolated remote browser when adequate; do not vendor a general scheduler. Alternative two: avoid building if protected authority or actual feedback cannot be established. This proposal claims constructibility, not new implemented grade.

**Explicit non-goals:** No unrelated function upgrades, blanket task guardian, unrequested S5 authority, generic provider dependency, automatic external PR, or forced adoption.

**Implementation dependency graph:** Verify pinned current source and accepted assessment -> resolve P1 native rights/overlap/feedback proof -> implement minimal P0 only with separately authorized product work -> run native positive/negative closure tests -> reconsider adoption based on measured benefit.

## 4. Priorities, optional alternative and stopping rules

**P0 and P1:** P0 is Opt-in first-party browser-resource-admission API with current workload snapshot, bounded local/defer/authorized-cloud options, developer-composed autonomous S3 decision owner, atomic scoped lease enforcement, and real subsequent browser action/commitment feedback returned to owner P1 is Establish permitted host-supplied current task commitments and priority envelope; check #1022 and #911 owner scope overlap; add lease/epoch enforcement before opted-in CDP effects; prove later task feedback, CLI/MCP distribution and safe cloud budget; compare simple host queue under matched tasks. Priorities are inherited, not newly changed.

**P2:** NONE — no second function or obligatory parent-governed mode. No forced second VSM function.

**Alternative path:** Prefer the documented SKILL serialization, existing named daemon and isolated remote browser when adequate; do not vendor a general scheduler.. Prefer this if it closes the same operator outcome with no independent C need.

**Stop:** Complete native equivalence, impossible independent actor right, no enforced return, policy veto or missing indispensable evidence triggers NO_GO/BLOCKED under the parent protocol. A missing measured saving is not by itself NO_GO.

## 5. Future source-native acceptance — derive tests, do not copy a matrix

**Native test commands and entry points:** Original tests/unit/test_daemon.py and tests/unit/test_admin.py are native test entrypoints; a Python test suite exists. No tests executed in this run.

**Positive functional closure:** With two real browser-task requests, verify the installed owner can lawfully choose local serialization versus permitted isolated lane, and the next browser operation plus release shows the choice.

**Independent alternative (where applicable):** Choose serialize this task, grant isolated named daemon, defer, or provision an authorized cloud lane while respecting quota and ownership. A genuine owner should be able to make two lawful different choices under different bounded contexts, not simply follow an always-grant rule.

**Negative authority and compatibility (where applicable):** No lease, cross-lane ownership mismatch, stale tab, exhausted cloud budget or owner outage blocks forbidden action and preserves existing single-agent behavior.

**Matched native alternative:** Prefer the documented SKILL serialization, existing named daemon and isolated remote browser when adequate; do not vendor a general scheduler. Execute the same task once with current native behavior and once with conditional construction. No results or economics have yet been collected.

## 6. Proposal verdict, falsification, evidence ownership and handoff

**Proposal-stage decision:** GO

**Research disposition:** NEEDS_EVIDENCE

**Primary falsifier:** With manager removed, there must be no independent autonomous whole-current priority choice; an unauthorized lease, bypassable raw CDP action or missing later real-action return defeats the proposed C chain

**Validation state:** NOT_RUN; proposal only, no native tests.

**Ownership of truth:** Profile owns semantics; Skills owns assessment method; Index owns historical accepted classification; original browser-use/browser-harness owns product change and maintainer choice; the [roadmap.md](roadmap.md) case receipt owns these decisions.

**Cost status:** NOT_MEASURED.

**Next permitted action:** Source-verify the narrow A/B comparison at current original HEAD and test scope under new explicit permission, or keep this as an unpublished research case.

**Human backlink:** [issue.md](issue.md); **case receipt:** [roadmap.md](roadmap.md).

**AI disclosure:** Drafted with AI; no native execution, maintainer consent, economic proof or independently verified value claimed.
