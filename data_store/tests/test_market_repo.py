"""Tests for data_store.market_repo — Paso 1: UPSERT y OHLCV."""

from __future__ import annotations

import math

import numpy as np
import pandas as pd
import pytest

from data_store.core import DataStoreCore
from data_store.market_repo import (
    load_market_data,
    load_request_meta,
    save_market_data,
    save_request_meta,
)


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


def _make_df(
    n: int = 3,
    start: str = "2026-03-01",
    freq: str = "D",
    source: str = "yfinance",
    quality: str = "normal",
    is_gap: bool = False,
    latency_sec: float = 0.42,
) -> pd.DataFrame:
    """Build a minimal canonical OHLCV DataFrame with *n* rows."""
    idx = pd.date_range(start, periods=n, freq=freq, tz="UTC", name="timestamp")
    df = pd.DataFrame(
        {
            "open": np.arange(100.0, 100.0 + n),
            "high": np.arange(101.0, 101.0 + n),
            "low": np.arange(99.0, 99.0 + n),
            "close": np.arange(100.5, 100.5 + n),
            "volume": np.arange(1000.0, 1000.0 + n),
            "source": source,
            "quality": quality,
            "is_gap": is_gap,
            "latency_sec": latency_sec,
        },
        index=idx,
    )
    df["is_gap"] = df["is_gap"].astype(bool)
    return df


# ------------------------------------------------------------------
# Tests — Save & Load round-trip
# ------------------------------------------------------------------


class TestSaveAndLoad:
    """Basic save/load and type fidelity."""

    def test_save_and_load_3_candles(self, conn):
        """Save 3 SPY/1d candles and load them back with correct types."""
        df = _make_df(n=3)
        written = save_market_data(conn, "SPY", "1d", df)
        assert written == 3

        loaded = load_market_data(conn, "SPY", "1d")
        assert len(loaded) == 3

        # Index type
        assert isinstance(loaded.index, pd.DatetimeIndex)
        assert str(loaded.index.tz) == "UTC"
        assert loaded.index.name == "timestamp"

        # OHLCV dtypes
        for col in ["open", "high", "low", "close", "volume"]:
            assert loaded[col].dtype == np.float64

        # Control column dtypes
        assert loaded["is_gap"].dtype == bool
        assert loaded["latency_sec"].dtype == np.float64

        # Values
        assert loaded["source"].iloc[0] == "yfinance"
        assert loaded["quality"].iloc[0] == "normal"
        assert loaded["is_gap"].iloc[0] is np.bool_(False)
        assert loaded["latency_sec"].iloc[0] == pytest.approx(0.42)


class TestIdempotency:
    """UPSERT: writing the same data twice produces no duplicates."""

    def test_upsert_updates_volume(self, conn):
        """Modify candle 2's volume, re-save all 3, verify 3 rows."""
        df = _make_df(n=3)
        save_market_data(conn, "SPY", "1d", df)

        # Modify candle 2
        df.iloc[1, df.columns.get_loc("volume")] = 9999.0
        save_market_data(conn, "SPY", "1d", df)

        loaded = load_market_data(conn, "SPY", "1d")
        assert len(loaded) == 3
        assert loaded["volume"].iloc[1] == pytest.approx(9999.0)


class TestGapAndNaN:
    """Edge case: gap rows with is_gap=True and NaN latency."""

    def test_gap_row_roundtrip(self, conn):
        """Save a candle with is_gap=True and NaN latency_sec."""
        df = _make_df(n=1, is_gap=True, latency_sec=float("nan"))
        save_market_data(conn, "SPY", "1d", df)

        loaded = load_market_data(conn, "SPY", "1d")
        assert len(loaded) == 1
        assert loaded["is_gap"].iloc[0] is np.bool_(True)
        assert math.isnan(loaded["latency_sec"].iloc[0])


class TestEmptyLoad:
    """Loading non-existent data returns an empty canonical DataFrame."""

    def test_empty_result_has_correct_schema(self, conn):
        loaded = load_market_data(conn, "AAPL", "1h")
        assert len(loaded) == 0
        assert isinstance(loaded.index, pd.DatetimeIndex)
        assert loaded.index.name == "timestamp"
        for col in ["open", "high", "low", "close", "volume"]:
            assert col in loaded.columns


class TestTimeFiltering:
    """Optional start/end filters on load."""

    def test_filter_by_start_and_end(self, conn):
        df = _make_df(n=5, start="2026-03-01")
        save_market_data(conn, "SPY", "1d", df)

        start = "2026-03-02T00:00:00+00:00"
        end = "2026-03-04T00:00:00+00:00"
        loaded = load_market_data(conn, "SPY", "1d", start=start, end=end)
        assert len(loaded) == 3


# ------------------------------------------------------------------
# Tests — Request metadata
# ------------------------------------------------------------------


class TestRequestMeta:
    """save_request_meta / load_request_meta round-trip."""

    def test_save_and_load_meta(self, conn):
        meta = {
            "provider_used": "yfinance",
            "fallback_used": True,
            "start": "2026-03-01T00:00:00+00:00",
            "end": "2026-03-05T00:00:00+00:00",
            "coverage_ratio": 0.95,
            "gap_count": 2,
            "quality": "degraded",
            "notes": "Tier 3 fallback",
        }
        save_request_meta(conn, "SPY", "1d", meta)

        loaded = load_request_meta(conn, "SPY", "1d")
        assert loaded is not None
        assert loaded["provider_used"] == "yfinance"
        assert loaded["fallback_used"] is True
        assert loaded["start"] == "2026-03-01T00:00:00+00:00"
        assert loaded["end"] == "2026-03-05T00:00:00+00:00"
        assert loaded["coverage_ratio"] == pytest.approx(0.95)
        assert loaded["gap_count"] == 2
        assert loaded["quality"] == "degraded"
        assert loaded["notes"] == "Tier 3 fallback"

    def test_load_meta_nonexistent(self, conn):
        result = load_request_meta(conn, "AAPL", "1h")
        assert result is None
