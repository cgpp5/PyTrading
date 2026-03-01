"""Tests for data_store.market_repo — Paso 2: Contrato JSON de features."""

from __future__ import annotations

import math

import numpy as np
import pandas as pd
import pytest

from data_store.core import DataStoreCore
from data_store.market_repo import (
    load_market_data,
    save_features,
    save_market_data,
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


def _make_df(n: int = 3, start: str = "2026-03-01") -> pd.DataFrame:
    """Build a minimal canonical OHLCV DataFrame."""
    idx = pd.date_range(start, periods=n, freq="D", tz="UTC", name="timestamp")
    return pd.DataFrame(
        {
            "open": np.arange(100.0, 100.0 + n),
            "high": np.arange(101.0, 101.0 + n),
            "low": np.arange(99.0, 99.0 + n),
            "close": np.arange(100.5, 100.5 + n),
            "volume": np.arange(1000.0, 1000.0 + n),
            "source": "yfinance",
            "quality": "normal",
            "is_gap": False,
            "latency_sec": 0.42,
        },
        index=idx,
    )


def _ts_iso(df: pd.DataFrame, i: int) -> str:
    """Return ISO 8601 string for the i-th row's timestamp."""
    return df.index[i].isoformat()


# ------------------------------------------------------------------
# Tests — Save & load features
# ------------------------------------------------------------------


class TestFeatureRoundTrip:
    """Save features on one row, load the full DataFrame, verify columns."""

    def test_features_appear_as_columns(self, conn):
        """Inject features on candle 2 and verify columns on load."""
        df = _make_df(3)
        save_market_data(conn, "SPY", "1d", df)

        features = {
            "returns@1.0": {"value": 0.0023, "quality": "ready"},
            "sma_50@1.0": {"value": 398.1, "quality": "warmup"},
        }
        save_features(conn, "SPY", "1d", _ts_iso(df, 1), features)

        loaded = load_market_data(conn, "SPY", "1d")

        # Feature columns exist
        assert "returns@1.0" in loaded.columns
        assert "sma_50@1.0" in loaded.columns

        # Candle 2 has correct values
        assert loaded["returns@1.0"].iloc[1] == pytest.approx(0.0023)
        assert loaded["sma_50@1.0"].iloc[1] == pytest.approx(398.1)

    def test_rows_without_features_are_nan(self, conn):
        """Candles 1 and 3 (no features) should have NaN in feature cols."""
        df = _make_df(3)
        save_market_data(conn, "SPY", "1d", df)

        features = {
            "returns@1.0": {"value": 0.0023, "quality": "ready"},
        }
        save_features(conn, "SPY", "1d", _ts_iso(df, 1), features)

        loaded = load_market_data(conn, "SPY", "1d")

        assert math.isnan(loaded["returns@1.0"].iloc[0])
        assert math.isnan(loaded["returns@1.0"].iloc[2])

    def test_null_value_loads_as_nan(self, conn):
        """A feature with value=null, quality=missing should load as NaN."""
        df = _make_df(1)
        save_market_data(conn, "SPY", "1d", df)

        features = {
            "rsi_14@1.0": {"value": None, "quality": "missing"},
        }
        save_features(conn, "SPY", "1d", _ts_iso(df, 0), features)

        loaded = load_market_data(conn, "SPY", "1d")
        assert "rsi_14@1.0" in loaded.columns
        assert math.isnan(loaded["rsi_14@1.0"].iloc[0])


# ------------------------------------------------------------------
# Tests — Validation failures
# ------------------------------------------------------------------


class TestValidationRejects:
    """save_features must reject malformed feature dicts."""

    def test_key_without_at(self, conn):
        """Key without '@' → ValueError."""
        df = _make_df(1)
        save_market_data(conn, "SPY", "1d", df)

        with pytest.raises(ValueError, match="must contain '@'"):
            save_features(
                conn, "SPY", "1d", _ts_iso(df, 0),
                {"sma50": {"value": 1.0, "quality": "ready"}},
            )

    def test_invalid_quality_value(self, conn):
        """quality='COMPUTED' (not in valid set) → ValueError."""
        df = _make_df(1)
        save_market_data(conn, "SPY", "1d", df)

        with pytest.raises(ValueError, match="quality"):
            save_features(
                conn, "SPY", "1d", _ts_iso(df, 0),
                {"sma@1.0": {"value": 1.0, "quality": "COMPUTED"}},
            )

    def test_missing_quality_field(self, conn):
        """Entry without 'quality' key → ValueError."""
        df = _make_df(1)
        save_market_data(conn, "SPY", "1d", df)

        with pytest.raises(ValueError, match="missing"):
            save_features(
                conn, "SPY", "1d", _ts_iso(df, 0),
                {"sma@1.0": {"value": 1.0}},
            )

    def test_missing_value_field(self, conn):
        """Entry without 'value' key → ValueError."""
        df = _make_df(1)
        save_market_data(conn, "SPY", "1d", df)

        with pytest.raises(ValueError, match="missing"):
            save_features(
                conn, "SPY", "1d", _ts_iso(df, 0),
                {"sma@1.0": {"quality": "ready"}},
            )


# ------------------------------------------------------------------
# Tests — Canonical columns untouched
# ------------------------------------------------------------------


class TestCanonicalColumnsPreserved:
    """Features should not interfere with base OHLCV columns."""

    def test_ohlcv_unchanged_after_feature_injection(self, conn):
        df = _make_df(3)
        save_market_data(conn, "SPY", "1d", df)

        save_features(
            conn, "SPY", "1d", _ts_iso(df, 1),
            {"returns@1.0": {"value": 0.5, "quality": "ready"}},
        )

        loaded = load_market_data(conn, "SPY", "1d")

        # OHLCV values unchanged
        assert loaded["close"].iloc[1] == pytest.approx(101.5)
        assert loaded["volume"].iloc[1] == pytest.approx(1001.0)
        assert loaded["source"].iloc[1] == "yfinance"
