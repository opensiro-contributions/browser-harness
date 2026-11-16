# Native test and GitHub readback — 2026-11-16

Original source `browser-use/browser-harness@8ec26f6974015a78eaf5494fe35bb9ba1f6b3598`. Parent unmerged PR #911 `c2de9b79115ca38c19c43385b232c83fc0fbd875`. Experiment `opensiro-contributions/browser-harness@6160b0eebde89aaab40c1cbb284e32b89c91907c`.

Test executor: dev-alpha-2 isolated workspace, Python 3.12, pytest in existing virtual environment; mock browser/CDP, no headed or headless Chrome present.

Commands run against exact remote experiment head, fetched into clean detached worktree:

```sh
PYTHONPATH=src python -m pytest tests/unit -q
git diff --check
git merge-base --is-ancestor c2de9b79115ca38c19c43385b232c83fc0fbd875 HEAD
```

Reported: **344 passed, 1 skipped** (12.82 s), diff-check PASS, parent ancestry PASS. Original main separately: 266 passed, 1 skipped. Parent #911 previously: 335 passed, 1 skipped. These are different test sets and not a comparative score of product quality.

Own commit vs parent #911: six files only — `SKILL.md`, `src/browser_harness/admin.py`, `daemon.py`, `owned_scope.py`, `tests/unit/test_owned_scope.py`, `tests/unit/test_run.py`. First-party GitHub [compare](https://github.com/opensiro-contributions/browser-harness/compare/c2de9b79115ca38c19c43385b232c83fc0fbd875...6160b0eebde89aaab40c1cbb284e32b89c91907c) returned one commit, no behind. Exact [implementation commit](https://github.com/opensiro-contributions/browser-harness/commit/6160b0eebde89aaab40c1cbb284e32b89c91907c) read back after publication to fork branch.

Critical exclusions: No live Chrome, browser restart, 300-task load or cross-platform race test. No external original PR, no fork-local review PR, no human technical correctness certification. This report is an AI-assisted native test receipt, not deployment evidence.
