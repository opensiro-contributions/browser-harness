# Browser Harness S1 domain-skill export — native functional proof

Recorded 2026-11-16 UTC. Original source and fork `main`: `8ec26f6974015a78eaf5494fe35bb9ba1f6b3598`. Code on `opensiro-contributions/browser-harness@opensiro/upgrade-s1-domain-skill-export-20261116`, head `13c404281b89003c3675d64a903cdc98b2139a96`.

## Observed baseline before adding the feature

The existing source has **174** `agent-workspace/domain-skills/**/*.md` files and **zero** conventional `SKILL.md` entrypoints in that directory. The existing `BH_DOMAIN_SKILLS=1` returns names only after the harness navigates; it does not populate an external lazy skill index. A manual prompt/file conversion remains a workaround. The original feature request is [browser-harness #155](https://github.com/browser-use/browser-harness/issues/155), closed completed in May 2026; this does **not** imply maintainer approval for the proposed implementation.

## Functional experiment on native CLI

The original workspace was explicitly selected with `BH_AGENT_WORKSPACE`. Export output went to a separate disposable directory, not the original repo:

```
browser-harness domain-skills export --output ../browser-runtime/s1-export-e2e
# domain-skills: exported=174 unchanged=0 total=174

browser-harness domain-skills export --output ../browser-runtime/s1-export-e2e
# domain-skills: exported=0 unchanged=174 total=174
```

A subsequent independent Python process scanned `**/SKILL.md` under the output, checked frontmatter name/description, and returned `FRESH_SCANNER_COUNT 174`. It verified the name `browser-harness-github-repo-actions` and confirmed the entire original `github/repo-actions.md` body survived in that exported entry. No browser daemon, model or third-party application was invoked.

This demonstrates the **functional task** of converting formerly invisible site workflows into per-skill indexed entries. It is **not** evidence that Hermes or any other full third-party agent runtime actually loaded or selected these entries, and cannot establish LLM task-quality improvement.

## Native checks

- Pristine original worktree: `PYTHONPATH=browser-harness-clean/src python -m pytest -q browser-harness-clean/tests/unit` — **266 passed, 1 skipped**.
- New product branch source: `PYTHONPATH=src python -m pytest -q tests/unit` — **274 passed, 1 skipped**; 8 additional tests cover positive export, source updating, conflict preflight, unmanaged/edited output refusal, symbolic links, collisions and no-daemon CLI behavior.
- `python3 -m compileall -q src/browser_harness/domain_skills.py tests/unit/test_domain_skills.py` — PASS.
- `git diff --cached --check` — PASS before local commit.
- GitHub compare of fork `main` to head `13c4042...`: one commit, five changed files, no `.opensiro/` in product diff; original main matches fork main.

## Capability-delta decision and scope

- Actor: user/coding agent with a SKILL.md-based lazy skill loader; native feature's decision owner is the invoking user selecting the export target.
- **S1 mechanism:** make the first-party agent-edited local operating repertoire indexable by another agent invocation, independently of an already running browser session.
- **Material supported delta:** an explicit first-party export route now creates fully indexed per-site skills, whereas the original exposes only manual reading and navigation-time file-name hints.
- **Does not establish:** autonomous skill construction, actual model skill selection or browser task outcome gains, canonical S1 grade changes, trustworthiness of agent- or website-written Markdown, automatic registration into any particular agent, removal of stale exported files or adoption by original maintainers.
- Existing work screened: source PR [#1025](https://github.com/browser-use/browser-harness/pull/1025) saves/reruns scripts; [#908](https://github.com/browser-use/browser-harness/pull/908) refactors primary SKILL.md; [#163](https://github.com/browser-use/browser-harness/pull/163) closed unmerged docs-only advice. No equivalent exporter observed at those inspected revisions.
- Admission: `MATERIAL_DELTA_SUPPORTED` **only for file-based skill discoverability**, with end-user LLM improvement `NOT_TESTED`. This is an `ASSESSMENT_INFORMED` new S1 capability, not an `ASSESSMENT_DERIVED` causal claim.

## Public communication boundary

Implementation branch and this internal research record may be public GitHub code/evidence. **No fork-local review PR or external original PR has been created by this task.** Creating a public fork-local PR requires the owner's exact current-conversation approval of its full title/body and verified diff; submitting to `browser-use/browser-harness` requires separate fresh permission.
