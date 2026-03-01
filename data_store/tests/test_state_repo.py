"""Tests for data_store.state_repo — Paso 3: Repositorio de estado."""

from __future__ import annotations

import pytest

from data_store.core import DataStoreCore
from data_store.state_repo import delete_state, list_keys, load_state, save_state


# ------------------------------------------------------------------
# Fixtures
# ------------------------------------------------------------------


@pytest.fixture()
def conn():
    """Yield a connection to a fresh in-memory DataStore."""
    core = DataStoreCore(":memory:")
    connection = core.get_connection()
    yield connection
    connection.close()


# ------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------


class TestSaveAndLoad:
    """Basic round-trip for state entries."""

    def test_save_and_load_dict(self, conn):
        """Save a dict, load it back, verify all fields."""
        value = {"active": True, "since": "2026-03-01T10:00:00+00:00"}
        save_state(conn, "cb_active", value)

        loaded = load_state(conn, "cb_active")
        assert loaded == value

    def test_load_nonexistent_returns_none(self, conn):
        """Loading a key that doesn't exist returns None."""
        assert load_state(conn, "no_such_key") is None


class TestIdempotency:
    """UPSERT: updating a key replaces the value without duplicating rows."""

    def test_update_replaces_value(self, conn):
        """Update cb_active, verify 1 row with new value."""
        save_state(conn, "cb_active", {"active": True, "since": "2026-03-01T10:00:00+00:00"})
        save_state(conn, "cb_active", {"active": False, "since": "2026-03-01T14:00:00+00:00"})

        loaded = load_state(conn, "cb_active")
        assert loaded["active"] is False
        assert loaded["since"] == "2026-03-01T14:00:00+00:00"

        # Only 1 row in the table for this key
        count = conn.execute(
            "SELECT COUNT(*) FROM system_state WHERE key = 'cb_active'"
        ).fetchone()[0]
        assert count == 1


class TestListKeys:
    """list_keys returns a sorted list of all keys."""

    def test_list_multiple_keys(self, conn):
        save_state(conn, "cb_active", {"active": True})
        save_state(conn, "dca_multiplier", {"value": 1.5})

        keys = list_keys(conn)
        assert keys == ["cb_active", "dca_multiplier"]

    def test_list_empty(self, conn):
        assert list_keys(conn) == []


class TestDelete:
    """delete_state removes an entry cleanly."""

    def test_delete_existing_key(self, conn):
        save_state(conn, "cb_active", {"active": True})
        save_state(conn, "dca_multiplier", {"value": 1.5})

        delete_state(conn, "cb_active")

        assert load_state(conn, "cb_active") is None
        assert list_keys(conn) == ["dca_multiplier"]

    def test_delete_nonexistent_is_noop(self, conn):
        """Deleting a key that doesn't exist should not raise."""
        delete_state(conn, "no_such_key")  # no error
