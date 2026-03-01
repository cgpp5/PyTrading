"""data_store.state_repo — Repositorio de estado transversal.

KV store persistente para variables de sistema: cooldowns, flags,
multiplicadores y cualquier estado que deba sobrevivir entre ciclos
de ejecución.

No importa nada de módulos de dominio.
"""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from typing import Any, Optional


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def save_state(
    conn: sqlite3.Connection,
    key: str,
    value: Any,
) -> None:
    """Persist a state entry (INSERT OR REPLACE).

    ``updated_at`` is set automatically to the current UTC timestamp.

    Args:
        conn: An open SQLite connection.
        key: Unique identifier for the state entry.
        value: Any JSON-serialisable value (dict, list, scalar).
    """
    updated_at = datetime.now(timezone.utc).isoformat()
    conn.execute(
        "INSERT OR REPLACE INTO system_state (key, value, updated_at) "
        "VALUES (?, ?, ?)",
        (key, json.dumps(value), updated_at),
    )
    conn.commit()


def load_state(
    conn: sqlite3.Connection,
    key: str,
) -> Optional[Any]:
    """Load a state entry by key.

    Returns:
        The deserialised value, or ``None`` if the key does not exist.
    """
    row = conn.execute(
        "SELECT value FROM system_state WHERE key = ?",
        (key,),
    ).fetchone()

    if row is None:
        return None

    return json.loads(row["value"])


def delete_state(
    conn: sqlite3.Connection,
    key: str,
) -> None:
    """Delete a state entry by key (no-op if it doesn't exist)."""
    conn.execute(
        "DELETE FROM system_state WHERE key = ?",
        (key,),
    )
    conn.commit()


def list_keys(conn: sqlite3.Connection) -> list[str]:
    """Return a sorted list of all state keys."""
    rows = conn.execute(
        "SELECT key FROM system_state ORDER BY key"
    ).fetchall()
    return [row["key"] for row in rows]
