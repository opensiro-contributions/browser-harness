# DRAFT — NOT SENT — possible comment on existing browser-use/browser-harness#582

**Destination:** https://github.com/browser-use/browser-harness/issues/582  
**Action:** external issue comment only after separate exact publication approval. **NOT APPROVED / NOT SENT.**

I'm testing whether Opensiro's VSM-informed specification can help standardize useful harness improvements and potentially lower development and maintenance cost. This is an unmeasured hypothesis, not a request to adopt VSM.

Your #582 report of one agent closing other agents' tabs gives a concrete safety problem. The current skill already recommends task-owned target IDs, serialization on one local daemon and isolated remote sessions for concurrent work. Open PRs #760 (target multiplexing), #846 (tab guard), #911 (owned-target preflight) and #1034 (reconnection) may cover parts; none is assumed merged.

Would a minimal first-party owner/lease enforcement path be more useful than the existing per-agent tab-ID convention? Separately, do maintainers see a real need for an operator to choose among *current* competing browser jobs (admit/defer/hold) and observe the later effect, or would a simple host queue be the better boundary? Opensiro has a dependent, unpublished S3 priority-admission experiment, but its earlier fake-CDP/unit tests do not prove a real Chrome benefit.

Research: https://github.com/opensiro-contributions/browser-harness/blob/opensiro/meta/.opensiro/issues/browser-resource-control-20261117/README.md

AI-assisted drafting; no independent human code review certification claimed.
