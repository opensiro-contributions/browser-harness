# Dependent Browser Harness S3 admission — current-main merge proof (2026-11-16)

Original and fork main: `browser-use/browser-harness@8ec26f6974015a78eaf5494fe35bb9ba1f6b3598`. Native open dependency [PR #911](https://github.com/browser-use/browser-harness/pull/911): `c2de9b79115ca38c19c43385b232c83fc0fbd875`, **not merged**. Earlier OpenSiro experimental head `7eba11415aac4dcbf703516f170db6d4e22b24ba`.

The source clone was initially shallow; an early attempt to merge reported `fatal: refusing to merge unrelated histories` due to missing local ancestor. After fetching complete history, common ancestor `dbf0e4f3a37ebc31aaeaf9d378ab1760b5776c15` was present and an uncommitted merge of current main completed **without conflicts**. A GitHub tree was constructed against the latest fork `main`; its SHA `d1c8078cb640c4ad4228c5d9914391fc0f059919` exactly matched the locally tested merged tree.

The resulting first-party [integration commit](https://github.com/opensiro-contributions/browser-harness/commit/ef5c5bcd92196d33a5b5463a64cfc20f0363895e) has both parents: experiment `7eba114` and original main `8ec26f6`. It is on [OpenSiro integration branch](https://github.com/opensiro-contributions/browser-harness/tree/opensiro/exp-s3-admission-main-integrated-20261116). Verified GitHub compare `main...integration`: **ahead 12 commits, behind 0, 12 changed files**, all within `SKILL.md`, `src/browser_harness/`, and `tests/`. Changes include the *entire unmerged PR #911 prerequisite*, not just OpenSiro's two incremental commits.

The exact remote integrated head was checked out into a clean detached worktree and validated:

```sh
PYTHONPATH=src python -m pytest tests/unit -q
# 344 passed, 1 skipped (14.06 s)
PYTHONPATH=src python tests/integration/owned_admission_ipc_canary.py
# PASS; real subprocess IPC, fake CDP
git diff origin/main --check
# PASS
```

One broad `git diff --cached --check` during merge reported trailing whitespace in unrelated upstream domain-skill files when comparing the older feature branch to newer main. That check is **not** evidence of new patch whitespace: the correct diff against current `main` passed. No upstream domain-skill files are altered by the integrated feature diff.

**Not proven:** real Chrome/browser visible actions, human technical review, user-level gains over external orchestration queue, independent S3 whole-system decision ownership, S4 future-environment adaptation, or acceptance/merge of PR #911. No fork-local review PR or third-party PR was created. First-party meta state remains independently gated.
