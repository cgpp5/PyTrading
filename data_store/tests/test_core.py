"""Tests for data_store.core — Paso 0: Fundaciones y conexión."""

from __future__ import annotations

import sqlite3

import pytest

from data_store.core import DataStoreCore


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------

def _table_names(conn: sqlite3.Connection) -> set[str]:
    """Return the set of user-created table names in the database."""
    rows = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()
    return {row["name"] for row in rows}


# ------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------


class TestSchemaCreation:
    """Verificar que las 3 tablas se crean correctamente."""

    def test_tables_exist_in_memory(self):
        """Instanciar con :memory: y comprobar que las 3 tablas existen."""
        core = DataStoreCore(":memory:")
        conn = core.get_connection()
        try:
            tables = _table_names(conn)
            assert "market_data" in tables
            assert "market_requests" in tables
            assert "system_state" in tables
        finally:
            conn.close()

    def test_no_redundant_indexes(self):
        """No debe existir un índice explícito sobre la PK."""
        core = DataStoreCore(":memory:")
        conn = core.get_connection()
        try:
            rows = conn.execute(
                "SELECT name FROM sqlite_master WHERE type='index' "
                "AND sql IS NOT NULL"  # excluye índices autoindex de PK
            ).fetchall()
            index_names = {row["name"] for row in rows}
            assert len(index_names) == 0, (
                f"Unexpected explicit indexes: {index_names}"
            )
        finally:
            conn.close()


class TestPragmas:
    """Verificar que los PRAGMAs se configuran correctamente."""

    def test_wal_mode_on_disk(self, tmp_path):
        """WAL mode funciona con bases de datos en disco."""
        db_file = str(tmp_path / "test.sqlite")
        core = DataStoreCore(db_file)
        conn = core.get_connection()
        try:
            mode = conn.execute("PRAGMA journal_mode").fetchone()[0]
            assert mode == "wal"
        finally:
            conn.close()

    def test_synchronous_per_connection(self):
        """synchronous=NORMAL (1) se aplica en cada get_connection()."""
        core = DataStoreCore(":memory:")

        # Primera conexión
        conn1 = core.get_connection()
        try:
            sync1 = conn1.execute("PRAGMA synchronous").fetchone()[0]
            assert sync1 == 1  # NORMAL
        finally:
            conn1.close()

        # Segunda conexión — debe tener el mismo PRAGMA
        conn2 = core.get_connection()
        try:
            sync2 = conn2.execute("PRAGMA synchronous").fetchone()[0]
            assert sync2 == 1  # NORMAL
        finally:
            conn2.close()

    def test_temp_store_per_connection(self):
        """temp_store=MEMORY (2) se aplica en cada get_connection()."""
        core = DataStoreCore(":memory:")
        conn = core.get_connection()
        try:
            temp = conn.execute("PRAGMA temp_store").fetchone()[0]
            assert temp == 2  # MEMORY
        finally:
            conn.close()


class TestConnectionFactory:
    """Verificar que get_connection() produce conexiones funcionales."""

    def test_row_factory_is_row(self):
        """Las filas deben ser accesibles por nombre de columna."""
        core = DataStoreCore(":memory:")
        conn = core.get_connection()
        try:
            conn.execute(
                "INSERT INTO system_state (key, value, updated_at) "
                "VALUES ('test_key', '{}', '2026-03-01T00:00:00+00:00')"
            )
            row = conn.execute(
                "SELECT key, value FROM system_state WHERE key='test_key'"
            ).fetchone()
            assert row["key"] == "test_key"
        finally:
            conn.close()

    def test_schema_idempotent(self):
        """Instanciar dos veces sobre la misma DB no falla."""
        core1 = DataStoreCore(":memory:")
        # Crear un segundo core apuntando al mismo :memory: no es posible
        # (cada :memory: es independiente), pero podemos re-ejecutar el init.
        core1._initialize_schema()  # segunda llamada — no debe fallar
        conn = core1.get_connection()
        try:
            tables = _table_names(conn)
            assert len(tables) == 3
        finally:
            conn.close()
