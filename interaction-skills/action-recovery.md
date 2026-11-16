# Durable task actions (opt-in)

Use `guarded_action()` for non-idempotent browser operations (submit, publish,
create, send) when a CLI process may stop before receiving a server receipt.
A successful click/CDP response is not proof that a task completed.

```python
# Run in browser-harness; imported automatically from the helper module.
def saved():
    # Site-specific verification: read a server-backed receipt or persisted record.
    return bool(js("document.querySelector('[data-server-receipt=\"ticket-123\"]')"))

try:
    result = guarded_action(
        "ticket-123/create",
        expected="ticket-123:created-by-current-task",
        action=lambda: click_at_xy(420, 320),
        verify=saved,
        wait_seconds=10,
    )
    print(result)  # {'state': 'verified', 'executed': True or False}
except ActionOutcomeUnknown as exc:
    print(f"STOP: uncertain outcome, do not submit again: {exc}")
```

The helper commits a hashed action identity and intent to
`$BH_AGENT_WORKSPACE/.browser-harness/action-intents.sqlite3`
*before* calling the action callback. On the next invocation with the same key
and persistent workspace, it runs the verifier first. A confirmed site
postcondition returns verified without invoking the action again. Otherwise
it raises `ActionOutcomeUnknown` and fails closed. Concurrent callers
using the same workspace and key share one SQLite intent.

Limits and responsibilities:

- Choose a stable unique key and expected-outcome description for exactly one
  side effect; reused keys with different expected identities are rejected.
- The verification callback must return an actual bool backed by the site's
  authoritative application state, not an optimistic notification, a click
  return value or an unverified UI label.
- The caller still chooses the correct browser target and owns it separately.
  This is not an authorization, tab-ownership or isolation system.
- This provides at-most-one **callback invocation per key and intact workspace**,
  not exactly-once behavior at the remote website. A callback may never
  execute, remain in flight, or cause server-side duplication.
- If the outcome is unknown, stop and reconcile with the operator/application;
  do not delete the DB, change the key, or retry to bypass the guard.
- Preserving the same `BH_AGENT_WORKSPACE` is essential across CLI
  invocations. Losing or replacing the DB removes historical intent evidence.
- No page content, receipts, secrets, or callback source are persisted. Do not
  use secret values as identifiers. Local SQLite is not a security boundary.
