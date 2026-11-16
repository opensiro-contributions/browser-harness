# Browser Harness S1 learned-regulator: bounded experiment (2026-11-16)

**Result:** EVIDENCE_INSUFFICIENT. Independent agent-learning experiment NOT EXECUTED. No material Upgrade qualified. Do not claim S1 self-organization, task-quality benefit, Index reassessment or permission for a fork-local/external PR.

## Frozen sources
- Original: browser-use/browser-harness @ 8ec26f6974015a78eaf5494fe35bb9ba1f6b3598. Pristine worktree, no product changes.
- Case: .opensiro/contributions/browser-harness-s1-learned-regulator-reuse.json.
- Pinned assessment: https://github.com/opensiro/vsm-harness-index/blob/854c6e5441709b014c01f803c23311fdf366a354/assessments/br/browser-harness.md (2026-09-18, S1=A).
- Existing source-native mechanisms: SKILL.md, agent_helpers.py, helpers.py already support agent-editable helpers and BH_DOMAIN_SKILLS. Existing Expedia learned workflow: https://github.com/browser-use/browser-harness/pull/218.
- Preregistered.json SHA256: 42f333fdd131cbd6c9168751e8b0326e8a8e0aa70bcf30ff43e07acbb127ddae.
- Local fixture.py SHA256: 4634214ee203ecdf031de9caa465b464a79b973be9f1db15fe735300c11c86c0. Training case learn; held-out a-e. First three calendar submissions fail, a site-linked alternative is discoverable.

## Real native checks, NOT learning proof
- Original source at exact SHA, clean detached worktree: pytest -q tests/unit => 266 passed, 1 skipped.
- Headless Chrome for Testing 157.0.8103.78 and original Browser Harness 0.1.13 communicated via CDP.
- On task a, a real Chrome-side form submission returned the page message "Calendar lost selected date".
- An evaluator manually wrote domain-skills/localhost/evaluator-placeholder.md. Original goto_url then reported that filename; it was NOT agent-discovered or agent-generated.
- A manually constructed legitimate URL for task b returned server-verified ID 99181c9ba463, and the server audit logged the Chrome user-agent and correct query.
- Same fixture reached through 127.0.0.1 did NOT surface a skill under localhost. This is hostname matching only, not safety or autonomy.
- Native receipts: native-unit-tests.log, pristine-cold-smoke.log, pristine-manual-control.log.

## Independent-agent failure boundary
Cold trial cold-a was launched as a fresh Codex CLI 0.145.0 agent. Its authentication refresh returned HTTP 403 unsupported_country_region_territory before any browser-task action. The process was stopped. Independent cold/learning/held-out/ablation completions: 0/0/0/0. No attempt was made to bypass the service restriction. This is a runner authorization blocker, NOT evidence of agent failure.

## Gate and next step
Neither an endogenous learned rule nor a fresh-agent reuse, held-out counterfactual, negative control, independently verified quality gain, or original-repository unmet material capability is demonstrated. Passing tests and evaluator-authored artifacts cannot qualify an Upgrade. Decision: DELTA_PENDING and EVIDENCE_INSUFFICIENT, NOT MATERIAL_DELTA_SUPPORTED.

Only with an authorized working independent-agent runtime: repeat five cold tasks, training, five learned tasks, ablation/negative controls, source-native need/alternative check and exact immutable provenance. If no material new outcome, close without code changes. No fork-local or third-party PR for this prototype.
