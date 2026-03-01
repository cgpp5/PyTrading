"""data_store.core — Motor físico de la base de datos.

Responsabilidades:
  - Abrir conexión a SQLite con PRAGMAs de rendimiento.
  - Crear el esquema de tablas si no existen.
  - Proveer conexiones configuradas a los repositorios.
"""

from __future__ import annotations

import itertools
import logging
import sqlite3
from pathlib import Path

logger = logging.getLogger(__name__)

# Monotonic counter to guarantee unique in-memory DB names even if
# Python reuses object ids after garbage collection.
_mem_counter = itertools.count()

# ---------------------------------------------------------------------------
# DDL
# ---------------------------------------------------------------------------

_DDL_MARKET_DATA = """
CREATE TABLE IF NOT EXISTS market_data (
    symbol      TEXT NOT NULL,
    timeframe   TEXT NOT NULL,
    timestamp   TEXT NOT NULL,
    open        REAL,
    high        REAL,
    low         REAL,
    close       REAL,
    volume      REAL,
    source      TEXT,
    quality     TEXT,
    is_gap      INTEGER DEFAULT 0,
    latency_sec REAL,
    features    JSON,
    PRIMARY KEY (symbol, timeframe, timestamp)
);
"""

_DDL_MARKET_REQUESTS = """
CREATE TABLE IF NOT EXISTS market_requests (
    symbol          TEXT NOT NULL,
    timeframe       TEXT NOT NULL,
    requested_at    TEXT NOT NULL,
    provider_used   TEXT NOT NULL,
    fallback_used   INTEGER DEFAULT 0,
    start_ts        TEXT NOT NULL,
    end_ts          TEXT NOT NULL,
    coverage_ratio  REAL,
    gap_count       INTEGER,
    quality         TEXT,
    notes           TEXT,
    PRIMARY KEY (symbol, timeframe, requested_at)
);
"""

_DDL_SYSTEM_STATE = """
CREATE TABLE IF NOT EXISTS system_state (
    key        TEXT PRIMARY KEY,
    value      JSON NOT NULL,
    updated_at TEXT NOT NULL
);
"""


class DataStoreCore:
    """Motor físico de la base de datos.

    Maneja la conexión optimizada para concurrencia (WAL) y la
    inicialización del esquema.

    Para bases de datos ``":memory:"``, se usa internamente un URI con
    shared-cache para que todas las conexiones de la misma instancia
    compartan la misma base de datos en memoria.
    """

    def __init__(self, db_path: str = "trading_data.sqlite") -> None:
        self.db_path = db_path
        self._keeper_conn: sqlite3.Connection | None = None

        if db_path == ":memory:":
            # Cada sqlite3.connect(":memory:") crea una DB independiente.
            # Un URI con shared cache permite que todas las conexiones de
            # esta instancia compartan la misma DB en memoria.
            self._db_uri = (
                f"file:memdb_{next(_mem_counter)}?mode=memory&cache=shared"
            )
            self._use_uri = True
            # Mantener una conexión viva para que la DB no se destruya
            # al cerrar todas las demás conexiones.
            self._keeper_conn = self._raw_connect()
        else:
            self._db_uri = db_path
            self._use_uri = False
            Path(db_path).parent.mkdir(parents=True, exist_ok=True)

        self._initialize_schema()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def get_connection(self) -> sqlite3.Connection:
        """Devuelve una conexión configurada con PRAGMAs de rendimiento.

        Los PRAGMAs ``synchronous`` y ``temp_store`` son **per-connection**
        y deben establecerse cada vez.  ``journal_mode=WAL`` es per-database
        pero se reafirma por seguridad.
        """
        conn = self._raw_connect()
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA synchronous=NORMAL")
        conn.execute("PRAGMA temp_store=MEMORY")
        return conn

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _raw_connect(self) -> sqlite3.Connection:
        """Conexión sin PRAGMAs ni row_factory — uso interno."""
        if self._use_uri:
            return sqlite3.connect(self._db_uri, uri=True, timeout=10.0)
        return sqlite3.connect(self.db_path, timeout=10.0)

    def _initialize_schema(self) -> None:
        """Crea las tablas si no existen."""
        conn = self.get_connection()
        try:
            conn.execute(_DDL_MARKET_DATA)
            conn.execute(_DDL_MARKET_REQUESTS)
            conn.execute(_DDL_SYSTEM_STATE)
            conn.commit()
            logger.debug(
                "DataStore schema initialised in %s (WAL mode).", self.db_path
            )
        finally:
            conn.close()