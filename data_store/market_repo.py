"""data_store.market_repo — Repositorio de mercado.

Traduce DataFrames OHLCV canónicos a sentencias SQL y viceversa.
Gestiona también la persistencia de MarketDataMeta (tabla market_requests).

No importa nada de market_feed ni de feature_engine.
"""

from __future__ import annotations

import json
import math
import sqlite3
from datetime import datetime, timezone
from typing import Any, Optional

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Canonical schema (mirrors market_feed.normalize without importing it)
# ---------------------------------------------------------------------------

_PRICE_COLS = ["open", "high", "low", "close", "volume"]
_CONTROL_COLS = ["source", "quality", "is_gap", "latency_sec"]
_CANONICAL_COLS = _PRICE_COLS + _CONTROL_COLS

# Structural validation — no imports from feature_engine.
_VALID_QUALITIES = {"ready", "warmup", "degraded", "missing"}

# ---------------------------------------------------------------------------
# Write helpers
# ---------------------------------------------------------------------------


def _to_iso(ts: pd.Timestamp) -> str:
    """Convert a pandas Timestamp to ISO 8601 UTC string."""
    return ts.isoformat()


def _bool_to_int(val: Any) -> int:
    """Convert a Python/numpy bool to SQLite integer (0/1)."""
    return int(bool(val))


def _float_or_none(val: Any) -> Optional[float]:
    """Convert a float to Python float, mapping NaN → None for SQLite."""
    if val is None:
        return None
    try:
        if math.isnan(val):
            return None
    except (TypeError, ValueError):
        pass
    return float(val)


# ---------------------------------------------------------------------------
# Public API — market_data
# ---------------------------------------------------------------------------


def save_market_data(
    conn: sqlite3.Connection,
    symbol: str,
    timeframe: str,
    df: pd.DataFrame,
) -> int:
    """Persist an OHLCV DataFrame into the market_data table.

    Uses INSERT OR REPLACE for idempotency.

    Args:
        conn: An open SQLite connection (from DataStoreCore.get_connection).
        symbol: Ticker symbol (e.g. ``"SPY"``).
        timeframe: Timeframe literal (e.g. ``"1d"``).
        df: DataFrame with DatetimeIndex[UTC] and canonical OHLCV + control
            columns.

    Returns:
        Number of rows written.
    """
    rows_written = 0
    cursor = conn.cursor()

    for ts, row in df.iterrows():
        cursor.execute(
            """
            INSERT OR REPLACE INTO market_data
                (symbol, timeframe, timestamp,
                 open, high, low, close, volume,
                 source, quality, is_gap, latency_sec, features)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL)
            """,
            (
                symbol,
                timeframe,
                _to_iso(ts),
                _float_or_none(row.get("open")),
                _float_or_none(row.get("high")),
                _float_or_none(row.get("low")),
                _float_or_none(row.get("close")),
                _float_or_none(row.get("volume")),
                row.get("source"),
                row.get("quality"),
                _bool_to_int(row.get("is_gap", False)),
                _float_or_none(row.get("latency_sec")),
            ),
        )
        rows_written += 1

    conn.commit()
    return rows_written


def load_market_data(
    conn: sqlite3.Connection,
    symbol: str,
    timeframe: str,
    *,
    start: Optional[str] = None,
    end: Optional[str] = None,
) -> pd.DataFrame:
    """Load OHLCV data from the market_data table.

    Args:
        conn: An open SQLite connection.
        symbol: Ticker symbol.
        timeframe: Timeframe literal.
        start: Optional ISO 8601 lower bound (inclusive).
        end: Optional ISO 8601 upper bound (inclusive).

    Returns:
        DataFrame with DatetimeIndex[ns, UTC] named ``"timestamp"`` and
        canonical columns.  Empty DataFrame with correct schema if no rows.
    """
    query = (
        "SELECT timestamp, open, high, low, close, volume, "
        "source, quality, is_gap, latency_sec, features "
        "FROM market_data "
        "WHERE symbol = ? AND timeframe = ?"
    )
    params: list[Any] = [symbol, timeframe]

    if start is not None:
        query += " AND timestamp >= ?"
        params.append(start)
    if end is not None:
        query += " AND timestamp <= ?"
        params.append(end)

    query += " ORDER BY timestamp"

    rows = conn.execute(query, params).fetchall()

    if not rows:
        return _empty_canonical_df()

    records = []
    feature_data: list[dict[str, Any]] = []  # per-row feature dicts

    for row in rows:
        records.append({
            "timestamp": row["timestamp"],
            "open": row["open"],
            "high": row["high"],
            "low": row["low"],
            "close": row["close"],
            "volume": row["volume"],
            "source": row["source"],
            "quality": row["quality"],
            "is_gap": bool(row["is_gap"]),
            "latency_sec": row["latency_sec"],
        })
        # Deserialize features JSON (may be NULL)
        raw_features = row["features"]
        if raw_features:
            parsed = json.loads(raw_features)
            feature_data.append(
                {k: v["value"] for k, v in parsed.items()}
            )
        else:
            feature_data.append({})

    df = pd.DataFrame(records)

    # Reconstruct DatetimeIndex[ns, UTC]
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
    df = df.set_index("timestamp")
    df.index.name = "timestamp"

    # Enforce strict dtypes
    for col in _PRICE_COLS:
        df[col] = df[col].astype("float64")
    df["latency_sec"] = df["latency_sec"].astype("float64")
    df["is_gap"] = df["is_gap"].astype("bool")

    # Unpack feature columns (union of all keys across rows)
    all_feature_keys = sorted(
        {k for fd in feature_data for k in fd}
    )
    if all_feature_keys:
        feat_df = pd.DataFrame(feature_data, index=df.index)
        for key in all_feature_keys:
            df[key] = feat_df[key].astype("float64") if key in feat_df.columns else np.nan

    return df


# ---------------------------------------------------------------------------
# Public API — market_requests (MarketDataMeta persistence)
# ---------------------------------------------------------------------------


def save_request_meta(
    conn: sqlite3.Connection,
    symbol: str,
    timeframe: str,
    meta: dict[str, Any],
) -> None:
    """Persist request-level metadata into the market_requests table.

    Args:
        conn: An open SQLite connection.
        symbol: Ticker symbol.
        timeframe: Timeframe literal.
        meta: Dictionary with keys matching market_requests columns:
            ``provider_used``, ``fallback_used``, ``start``, ``end``,
            ``coverage_ratio``, ``gap_count``, ``quality``, ``notes``.
    """
    requested_at = datetime.now(timezone.utc).isoformat()
    conn.execute(
        """
        INSERT OR REPLACE INTO market_requests
            (symbol, timeframe, requested_at,
             provider_used, fallback_used,
             start_ts, end_ts,
             coverage_ratio, gap_count, quality, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            symbol,
            timeframe,
            requested_at,
            meta["provider_used"],
            int(bool(meta.get("fallback_used", False))),
            meta["start"],
            meta["end"],
            meta.get("coverage_ratio"),
            meta.get("gap_count"),
            meta.get("quality"),
            meta.get("notes"),
        ),
    )
    conn.commit()


def load_request_meta(
    conn: sqlite3.Connection,
    symbol: str,
    timeframe: str,
) -> Optional[dict[str, Any]]:
    """Load the most recent request metadata for a symbol/timeframe pair.

    Returns:
        Dictionary with metadata fields, or ``None`` if no record exists.
    """
    row = conn.execute(
        """
        SELECT * FROM market_requests
        WHERE symbol = ? AND timeframe = ?
        ORDER BY requested_at DESC
        LIMIT 1
        """,
        (symbol, timeframe),
    ).fetchone()

    if row is None:
        return None

    return {
        "symbol": row["symbol"],
        "timeframe": row["timeframe"],
        "requested_at": row["requested_at"],
        "provider_used": row["provider_used"],
        "fallback_used": bool(row["fallback_used"]),
        "start": row["start_ts"],
        "end": row["end_ts"],
        "coverage_ratio": row["coverage_ratio"],
        "gap_count": row["gap_count"],
        "quality": row["quality"],
        "notes": row["notes"],
    }


# ---------------------------------------------------------------------------
# Public API — features JSON
# ---------------------------------------------------------------------------


def validate_features_dict(features: dict[str, Any]) -> None:
    """Validate the structural contract of a features dictionary.

    Rules:
        1. Each key must contain ``@`` (format ``name@version``).
        2. Each value must be a dict with exactly ``value`` and ``quality``.
        3. ``value`` must be ``float``, ``int``, or ``None``.
        4. ``quality`` must be in ``_VALID_QUALITIES``.

    Raises:
        ValueError: If any entry violates the contract.
    """
    for key, entry in features.items():
        if "@" not in key:
            raise ValueError(
                f"Feature key {key!r} must contain '@' "
                f"(expected format: name@version)"
            )
        if not isinstance(entry, dict):
            raise ValueError(
                f"Feature {key!r}: value must be a dict, got {type(entry).__name__}"
            )
        if set(entry.keys()) != {"value", "quality"}:
            missing = {"value", "quality"} - set(entry.keys())
            extra = set(entry.keys()) - {"value", "quality"}
            raise ValueError(
                f"Feature {key!r}: expected keys {{'value', 'quality'}}, "
                f"missing={missing or '{}'}, extra={extra or '{}'}"  
            )
        val = entry["value"]
        if val is not None and not isinstance(val, (int, float)):
            raise ValueError(
                f"Feature {key!r}: 'value' must be float, int, or null, "
                f"got {type(val).__name__}"
            )
        quality = entry["quality"]
        if quality not in _VALID_QUALITIES:
            raise ValueError(
                f"Feature {key!r}: quality {quality!r} not in "
                f"{sorted(_VALID_QUALITIES)}"
            )


def save_features(
    conn: sqlite3.Connection,
    symbol: str,
    timeframe: str,
    timestamp: str,
    features: dict[str, Any],
) -> None:
    """Save feature values into the features JSON column of an existing row.

    Validates the features dict structurally before writing.

    Args:
        conn: An open SQLite connection.
        symbol: Ticker symbol.
        timeframe: Timeframe literal.
        timestamp: ISO 8601 UTC timestamp identifying the row.
        features: Dictionary following the FeatureValue contract::

            {"returns@1.0": {"value": 0.0023, "quality": "ready"}, ...}

    Raises:
        ValueError: If the features dict violates the structural contract.
    """
    validate_features_dict(features)

    features_json = json.dumps(features)
    conn.execute(
        "UPDATE market_data SET features = ? "
        "WHERE symbol = ? AND timeframe = ? AND timestamp = ?",
        (features_json, symbol, timeframe, timestamp),
    )
    conn.commit()


# ---------------------------------------------------------------------------
# Private helpers
# ---------------------------------------------------------------------------


def _empty_canonical_df() -> pd.DataFrame:
    """Return an empty DataFrame with the canonical OHLCV schema."""
    df = pd.DataFrame(columns=_CANONICAL_COLS)
    df.index = pd.DatetimeIndex([], dtype="datetime64[ns, UTC]", name="timestamp")
    for col in _PRICE_COLS:
        df[col] = df[col].astype("float64")
    df["latency_sec"] = df["latency_sec"].astype("float64")
    df["is_gap"] = df["is_gap"].astype("bool")
    return df
