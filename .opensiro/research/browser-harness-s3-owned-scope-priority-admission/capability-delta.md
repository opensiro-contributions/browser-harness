# Browser Harness — capability-delta and overlap receipt (2026-11-16)

**Scope lock:** original `browser-use/browser-harness@8ec26f6974015a78eaf5494fe35bb9ba1f6b3598`, verified working fork `opensiro-contributions/browser-harness`. This is a dependency-bound experiment, not a published external PR, current assessment revision, or autonomous S3 certification.

## Historical assessment and VSM mechanism

- Canonical Index: [Browser Harness assessment](https://github.com/opensiro/vsm-harness-index/blob/854c6e5441709b014c01f803c23311fdf366a354/assessments/br/browser-harness.md); `reviewed_at=2026-09-18`, assessed `afbcc381b963040c19627d788e40c7e7663171ee`. Historical `S3=—`, `S4=—` do not classify current PR heads.
- Normative [Profile S3](https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md): requires whole-system present view plus real resource/priority/commitment decision right; routing, static cap, health checks alone do not establish ownership.
- Prototype allocates scoped task starts by live daemon capacity and operator-assigned priority. Parent host controls priorities; daemon enforces bounded admission. **This is S3-informed supporting enforcement; first-party autonomous S3 closure/grade is NOT claimed.**

## Actor, native task and best alternative

- Original [#375](https://github.com/browser-use/browser-harness/issues/375): Claude Code subagents need to work on many independent browser sites concurrently; serial browsing was the reported workaround.
- Original [#637](https://github.com/browser-use/browser-harness/issues/637): detached named daemons accumulated tabs/processes and exhausted a real host's process budget; issue is now closed, but its resource-pressure evidence is not erased.
- Parent [PR #911](https://github.com/browser-use/browser-harness/pull/911), `c2de9b79115ca38c19c43385b232c83fc0fbd875`, adds invocation-owned contexts with **8** live-scope cap, 9th immediately returns `owned-scope: capacity`. This protects against uncontrolled growth but rejects a burst rather than admitting it when a slot is freed. Its own test `test_begin_refuses_past_capacity_without_cdp` reproduces this branch-local behavior.
- Best available alternatives: the host manually schedules fewer than eight subagents, retries failed invocations, serializes the workload, or uses separately provisioned browsers. A host may implement a queue outside the harness; no claim of impossibility is made. The proposed feature reduces that orchestration requirement for **bounded bursts**, not arbitrary 300-at-once submissions.

## Existing-work overlap

| Source | Actual supported/proposed mechanism | Function coverage conclusion |
| --- | --- | --- |
| Original `main@8ec26f6` | Shared attached tab and manual serialization/remote isolation | S2 coordination, not S3 controller |
| [PR #746](https://github.com/browser-use/browser-harness/pull/746) | Per-target session routing and parallel tabs | S2; no verified resource/priority owner |
| [PR #911](https://github.com/browser-use/browser-harness/pull/911) | Scope enforcement, static cap eight, fail-closed foreign target accesses | S2 enforcement and S3-supporting resource cap only |
| [PR #1008](https://github.com/browser-use/browser-harness/pull/1008) | Opt-in idle daemon/browser cleanup | Lifecycle support, not S3 discretion |
| [OpenSiro experiment](https://github.com/opensiro-contributions/browser-harness/commit/6160b0eebde89aaab40c1cbb284e32b89c91907c) | Opt-in bounded wait and priority admission on PR #911 | S3-informed support; full S3 still unproven |

Disposition: `PARTIAL_OVERLAP` for S3 mechanisms; **not** `OVERLAP_CONFIRMED`. The original and PR #746 don't establish dynamic whole-system resource arbitration.

## Predeclared matched test and outcome

At eight existing scopes, the source PR #911 immediately rejects a ninth. In the experimental branch, the ninth starts waiting, a live scope is disposed, and that ninth receives its own scoped target and completes a fake CDP task. With two pending requests, higher operator priority enters first. Negative checks cover cancellation, timeout, capacity conservation, no `Target.getTargets` enumeration, default fail-fast compatibility and malformed settings. 344 unit tests passed, 1 skipped on exact published experiment head, with mock CDP rather than Chrome. This is a bounded matched **test-proxy** for task completion, not live browser validation or deployed user benefit.

## S4 source-local follow-up

Current `src/browser_harness/helpers.py` exposes up to ten domain-skill filenames when `BH_DOMAIN_SKILLS=1`, but it doesn't inspect prospective site changes, create adaptation options, or feed an S3 decision loop. [Original issue #934](https://github.com/browser-use/browser-harness/issues/934) contains 58 manually found problems across 48 example files, proving a maintenance need but not a prospective adaptation mechanism or material delta. **S4 candidate: `DELTA_PENDING`; no feature-code write for this separate hypothesis.**

## Limitation and authority

Dependency [PR #911](https://github.com/browser-use/browser-harness/pull/911) is unmerged as checked 2026-11-16; the experiment is one dependent commit on its head, not a minimal PR diff against original main. No live Chrome/CDP is installed in the checked executor. No original/fork-local PR was created, and the fork meta owner attention remained `WATCHING` (`owner_control=ALLOW`); the preflight requiring `ACTIVE` blocks review handoff. The read-only aggregator's GitHub call returned HTTP 403 in the executor: report `UNKNOWN`, not zero. Publication requires exact current-conversation owner consent and independent source/dependency/CI recheck.
