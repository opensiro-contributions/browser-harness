"""Fail-closed durable action intent for browser tasks across CLI restarts.

This coordinates calls to the *action callback*, not transactions on websites.
The caller supplies a site-specific, independently observed postcondition.
"""

from __future__ import annotations

import hashlib
import os
import sqlite3
import time
from pathlib import Path
from typing import Callable, TypeVar

from . import paths

T = TypeVar("T")


class ActionOutcomeUnknown(RuntimeError):
    """Action may have happened; refusing to repeat it without read-back."""


class ActionIdentityMismatch(ValueError):
    """This action key has already been used with a different expected outcome."""


def _identity(value: str, label: str) -> str:
    if not isinstance(value, str) or not value.strip() or len(value) > 512:
        raise ValueError(f"{label} must be a nonempty string of at most 512 characters")
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _observe(verify: Callable[[], bool], wait_seconds: float) -> bool:
    end = time.monotonic() + wait_seconds
    while True:
        observed = verify()
        if type(observed) is not bool:
            raise TypeError("verify() must return an actual bool, not a truthy value")
        if observed:
            return True
        remain = end - time.monotonic()
        if remain <= 0:
            return False
        time.sleep(min(0.2, remain))


def _commit_verified(conn: sqlite3.Connection, key_hash: str) -> None:
    conn.execute("BEGIN IMMEDIATE")
    try:
        conn.execute(
            "UPDATE action_intents SET state='verified', verified_at=? WHERE key_hash=?",
            (time.time(), key_hash),
        )
        conn.commit()
    except Exception:
        conn.rollback()
        raise


def guarded_action(
    key: str,
    *,
    expected: str,
    action: Callable[[], T],
    verify: Callable[[], bool],
    workspace: str | Path | None = None,
    wait_seconds: float = 5.0,
) -> dict[str, bool | str]:
    """Execute a task action at most once per action key in one persistent workspace.

    Commit an intent to local SQLite *before* invoking action(). A fresh CLI
    invocation can reconcile that intent only when verify() proves the expected
    site-specific outcome; otherwise it fails closed without calling action()
    again. Verifier results must be actual bool values. There are no automatic
    retries and no guarantee of exactly-once execution at the remote website.

    The key and expected outcome must identify one concrete task side effect.
    Do not treat the local database as an authorization/ownership boundary.
    """
    key_hash = _identity(key, "key")
    expected_hash = _identity(expected, "expected")
    if not callable(action) or not callable(verify):
        raise TypeError("action and verify must be callables")
    if not isinstance(wait_seconds, (int, float)) or not (0 <= wait_seconds <= 120):
        raise ValueError("wait_seconds must be between 0 and 120")

    root = Path(workspace).expanduser().resolve() if workspace is not None else paths.workspace_dir()
    state_dir = paths.ensure_private_dir(root / ".browser-harness")
    db = state_dir / "action-intents.sqlite3"
    conn = sqlite3.connect(db, timeout=5.0, isolation_level=None)
    try:
        if os.name != "nt":
            try:
                os.chmod(db, 0o600)
            except PermissionError:
                pass
        conn.execute(
            "CREATE TABLE IF NOT EXISTS action_intents ("
            "key_hash TEXT PRIMARY KEY, expected_hash TEXT NOT NULL,"
            "state TEXT NOT NULL CHECK(state IN ('intent','verified')),"
            "created_at REAL NOT NULL, verified_at REAL)"
        )
        conn.execute("BEGIN IMMEDIATE")
        try:
            row = conn.execute(
                "SELECT expected_hash, state FROM action_intents WHERE key_hash=?",
                (key_hash,),
            ).fetchone()
            fresh = row is None
            if row is None:
                conn.execute(
                    "INSERT INTO action_intents(key_hash, expected_hash, state, created_at)"
                    " VALUES (?,?, 'intent', ?)",
                    (key_hash, expected_hash, time.time()),
                )
            elif row[0] != expected_hash:
                raise ActionIdentityMismatch(
                    "action key already belongs to a different expected result; "
                    "use the original task identity or inspect the persisted intent"
                )
            conn.commit()
        except Exception:
            conn.rollback()
            raise

        # Recovery never invokes action again, even if a previous attempt died
        # before any effect or a completed receipt is no longer observable.
        if not fresh:
            try:
                observed = _observe(verify, wait_seconds)
            except Exception as exc:
                raise ActionOutcomeUnknown(
                    "saved intent exists; its outcome could not be verified; "
                    "action was NOT repeated"
                ) from exc
            if not observed:
                raise ActionOutcomeUnknown(
                    "saved intent exists but the postcondition is not confirmed; "
                    "action was NOT repeated"
                )
            _commit_verified(conn, key_hash)
            return {"state": "verified", "executed": False}

        # Even before the first action, a trustworthy exact postcondition may
        # prove the operation was completed elsewhere. Do not duplicate it.
        try:
            if _observe(verify, 0):
                _commit_verified(conn, key_hash)
                return {"state": "verified", "executed": False}
        except Exception as exc:
            raise ActionOutcomeUnknown(
                "pre-action postcondition check failed; action was NOT executed"
            ) from exc

        try:
            action()
        except Exception as exc:
            raise ActionOutcomeUnknown(
                "action raised after intent was persisted; outcome is uncertain"
            ) from exc
        try:
            observed = _observe(verify, wait_seconds)
        except Exception as exc:
            raise ActionOutcomeUnknown(
                "post-action verification failed; outcome is uncertain"
            ) from exc
        if not observed:
            raise ActionOutcomeUnknown(
                "postcondition not confirmed; action will NOT be repeated automatically"
            )
        _commit_verified(conn, key_hash)
        return {"state": "verified", "executed": True}
    finally:
        conn.close()
