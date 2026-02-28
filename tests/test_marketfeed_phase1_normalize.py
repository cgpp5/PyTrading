from __future__ import annotations

from datetime import datetime, timezone

import numpy as np
import pandas as pd
import pytest

from marketfeed.normalize import normalize_ohlcv, CANONICAL_COLS


def test_normalize_sets_utc_index_from_timestamp_column():
    start = datetime(2026, 2, 1, 12, 0, tzinfo=timezone.utc)
    raw = pd.DataFrame(
        {
            "timestamp": [start],
            "open": [1],
            "high": [2],
            "low": [0.5],
            "close": [1.5],
            "volume": [100],
        }
    )

    df = normalize_ohlcv(raw, provider_name="p", quality="normal")

    assert df.index.name == "timestamp"
    assert str(df.index.tz) == "UTC"
    assert list(df.columns) == CANONICAL_COLS


def test_normalize_sets_utc_index_from_index():
    start = datetime(2026, 2, 1, 12, 0, tzinfo=timezone.utc)
    raw = pd.DataFrame(
        {
            "open": [1],
            "high": [2],
            "low": [0.5],
            "close": [1.5],
            "volume": [100],
        },
        index=[start],
    )

    df = normalize_ohlcv(raw, provider_name="p", quality="normal")

    assert df.index.name == "timestamp"
    assert str(df.index.tz) == "UTC"
    assert list(df.columns) == CANONICAL_COLS


def test_normalize_dedupes_keep_last():
    t = datetime(2026, 2, 1, 12, 0, tzinfo=timezone.utc)
    raw = pd.DataFrame(
        {
            "timestamp": [t, t],
            "open": [1, 10],
            "high": [2, 20],
            "low": [0.5, 5],
            "close": [1.5, 15],
            "volume": [100, 999],
        }
    )

    df = normalize_ohlcv(raw, provider_name="p", quality="normal")

    assert len(df) == 1
    assert df.loc[t, "open"] == 10.0
    assert df.loc[t, "volume"] == 999.0


def test_normalize_ignores_extra_columns():
    t = datetime(2026, 2, 1, 12, 0, tzinfo=timezone.utc)
    raw = pd.DataFrame(
        {
            "timestamp": [t],
            "open": [1],
            "high": [2],
            "low": [0.5],
            "close": [1.5],
            "volume": [100],
            "foo": ["bar"],
        }
    )

    df = normalize_ohlcv(raw, provider_name="p", quality="normal")

    assert "foo" not in df.columns
    assert list(df.columns) == CANONICAL_COLS


def test_normalize_types_are_float64_and_control_cols_present():
    t = datetime(2026, 2, 1, 12, 0, tzinfo=timezone.utc)
    raw = pd.DataFrame(
        {
            "timestamp": [t],
            "open": [1],
            "high": [2],
            "low": [0.5],
            "close": [1.5],
            "volume": [100],
        }
    )

    df = normalize_ohlcv(raw, provider_name="alpaca", quality="normal")

    assert df["open"].dtype == "float64"
    assert df["volume"].dtype == "float64"
    assert df.loc[t, "source"] == "alpaca"
    assert df.loc[t, "quality"] == "normal"
    assert df.loc[t, "is_gap"] == False
    assert np.isnan(df.loc[t, "latency_sec"])


def test_normalize_missing_required_columns_raises():
    t = datetime(2026, 2, 1, 12, 0, tzinfo=timezone.utc)
    raw = pd.DataFrame({"timestamp": [t], "open": [1.0]})

    with pytest.raises(ValueError):
        normalize_ohlcv(raw, provider_name="p", quality="normal")
