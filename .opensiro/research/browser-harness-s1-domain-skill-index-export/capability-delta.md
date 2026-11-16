# Pre-implementation capability-delta and overlap receipt — Browser Harness S1 skill discovery

Recorded 2026-11-16. **Selected original:** browser-use/browser-harness @ `8ec26f6974015a78eaf5494fe35bb9ba1f6b3598` (MIT). This is a *distinct feature hypothesis* from the blocked autonomous-learned-regulator experiment and the earlier exact-target preflight. No model performance improvements are claimed.

## Actor, need and observable new task

Actor: a user of a lazy-loaded SKILL.md-indexing coding-agent environment (e.g., Hermes Agent) that has enabled browser-harness and wants to discover a site-specific Browser Harness domain skill *without* reading the primary Browser Harness skill or manually searching its workspace.

Original request: https://github.com/browser-use/browser-harness/issues/155 . That issue was closed in May 2026, but the precise structural gap remains present at this pinned current original: 174 existing `agent-workspace/domain-skills/**/*.md` inputs, **zero** `SKILL.md` entry points in that tree, while the primary `SKILL.md` only instructs users after its body is already loaded to read the matching directory. Closed issue does not imply a currently accepted patch.

Task: export existing site-specific operational instructions into independently discoverable, conventional `SKILL.md` entries for an explicit agent skill directory, then retrieve a named workflow by the target system's filename/frontmatter scanner in a fresh process. This is an **S1 operational-repertoire accessibility** mechanism, not agent learning or S3/S4.

## Existing supported alternative

Today the user can search `agent-workspace/domain-skills` manually, read a site file after first loading browser-harness, or hand-copy and convert each file to SKILL.md with frontmatter and an appropriate skill directory. `BH_DOMAIN_SKILLS=1` only returns matching **filenames on navigation**, after the Browser Harness agent already runs; it cannot make the external lazy-loader index all relevant site skills before browser work. Hand-copy is real but repeatedly manual and may be stale, and a one-sentence prompt cannot run when the primary skill has not loaded.

## Predeclared native counterfactual

- Input: an unmodified, source-pinned Browser Harness workspace with `github/repo-actions.md` and other site skill files.
- Before: a real SKILL.md-entrypoint-style scanner over the workspace finds 0 source site-skill entries.
- After: an explicit `browser-harness domain-skills export --output DIR` produces one independently indexable SKILL.md per existing site-workflow file, with YAML `name`/`description` and the exact source-body text. A fresh scanner process finds at least one correctly named workflow and retrieves its actual original instructions **without a browser daemon or model call**.
- Negatives: empty source is no-op; malformed/colliding names fail before write; never traverse source symlinks or output symlinks; do not overwrite user-controlled or modified target SKILL.md; repeated export is idempotent; unrelated existing browser-harness CLI and the source files are unchanged.
- Scope: deterministic discoverability and content preservation only. No claim of LLM choosing a skill, succeeding at domain tasks, autonomously generating new rules, or verified trust of untrusted source Markdown.

## Materiality and VSM boundary

This adds a *previously unavailable supported integration task* for agent systems that only index SKILL.md entrypoints. It changes the agent's addressable S1 repertoire, not its canonical autonomous grade. It is meaningfully different from another health flag, a diagnostic, or a text-only prompt: independently discoverable site skills are an actual new input/API surface. Still, this does not show end-user task success, which needs an additional outcome study.

## Overlap and source ownership

- PR https://github.com/browser-use/browser-harness/pull/1025: saves/reruns Python scripts per host, not agent-visible SKILL.md indexing — distinct.
- PR https://github.com/browser-use/browser-harness/pull/908: rewrites/moves primary SKILL.md and improves Cloud uploads, not export of domain-skills — distinct.
- PR https://github.com/browser-use/browser-harness/pull/163: closed unmerged documentation-only advice; no structural exporter — does not implement.
- Issue #155: closed completed; user/maintainer requirement exists historically but maintainer admission of this implementation is **not established**.
- Original current main still has the first-party files and no matching export API. This does not imply maintainer will accept the change.

**Disposition pre-implementation:** `MATERIAL_DELTA_SUPPORTED` *for the narrow discoverability capability only*, conditional on actual independent before/after integration results and negative controls. `ASSESSMENT_INFORMED` only: the pinned 2026-09-18 Index S1=A assessment and 2026-09-22 S1 learned-regulator note are context for S1 extension affordance, not a prior causal prediction. No `ASSESSMENT_DERIVED` claim. Native need/mechanism/counterfactual/scope are source-supported and should be reevaluated after tests; no external PR without exact consent.
