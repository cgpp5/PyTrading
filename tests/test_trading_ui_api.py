"""Tests for trading_ui.server — FastAPI endpoints.

Uses an in-memory DataStoreCore so tests do not touch disk.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest
from fastapi.testclient import TestClient

from data_store.core import DataStoreCore
from data_store.market_repo import save_features, save_market_data
from trading_ui.server import app, set_store


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture()
def store():
    """In-memory DataStoreCore with seeded test data."""
    s = DataStoreCore(":memory:")
    conn = s.get_connection()

    # -- 5 daily candles for TEST --
    dates = pd.date_range("2026-01-05", periods=5, freq="B", tz="UTC")
    df = pd.DataFrame(
        {
            "open": [100.0, 101.0, 102.0, 103.0, 104.0],
            "high": [105.0, 106.0, 107.0, 108.0, 109.0],
            "low": [95.0, 96.0, 97.0, 98.0, 99.0],
            "close": [102.0, 103.0, 104.0, 105.0, 106.0],
            "volume": [1000.0, 2000.0, 3000.0, 4000.0, 5000.0],
            "source": ["yfinance"] * 5,
            "quality": ["normal"] * 5,
            "is_gap": [False] * 5,
            "latency_sec": [0.1] * 5,
        },
        index=dates,
    )
    df.index.name = "timestamp"
    save_market_data(conn, "TEST", "1d", df)

    # -- Inject feature sma_50@1.0 in rows 1, 2, 3 (0-indexed) --
    for i in [1, 2, 3]:
        ts_iso = dates[i].isoformat()
        save_features(conn, "TEST", "1d", ts_iso, {
            "sma_50@1.0": {"value": 100.0 + i, "quality": "ready"},
        })

    conn.close()
    return s


@pytest.fixture()
def client(store):
    """FastAPI TestClient wired to the in-memory store."""
    set_store(store)
    with TestClient(app) as c:
        yield c
    set_store(None)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_get_symbols(client):
    resp = client.get("/api/symbols")
    assert resp.status_code == 200
    data = resp.json()
    assert data == {"symbols": ["TEST"]}


def test_get_timeframes(client):
    resp = client.get("/api/timeframes")
    assert resp.status_code == 200
    tfs = resp.json()["timeframes"]
    assert len(tfs) == 4
    assert "1d" in tfs
    assert "15m" in tfs


def test_get_ohlcv(client):
    resp = client.get("/api/ohlcv", params={"symbol": "TEST", "timeframe": "1d"})
    assert resp.status_code == 200
    data = resp.json()

    assert data["symbol"] == "TEST"
    assert data["timeframe"] == "1d"
    assert len(data["candles"]) == 5
    assert len(data["volume"]) == 5

    # Each candle has the required fields
    c = data["candles"][0]
    assert isinstance(c["time"], int)
    assert all(k in c for k in ("open", "high", "low", "close"))

    # Volume entries have time + value
    v = data["volume"][0]
    assert isinstance(v["time"], int)
    assert isinstance(v["value"], (int, float))

    # Times are ascending
    times = [x["time"] for x in data["candles"]]
    assert times == sorted(times)


def test_get_ohlcv_nonexistent_symbol(client):
    resp = client.get("/api/ohlcv", params={"symbol": "NONEXIST", "timeframe": "1d"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["candles"] == []
    assert data["volume"] == []


def test_get_available_features(client):
    resp = client.get(
        "/api/available-features",
        params={"symbol": "TEST", "timeframe": "1d"},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["features"] == ["sma_50@1.0"]


def test_get_available_features_no_data(client):
    resp = client.get(
        "/api/available-features",
        params={"symbol": "NONEXIST", "timeframe": "1d"},
    )
    assert resp.status_code == 200
    assert resp.json()["features"] == []


def test_get_features(client):
    resp = client.get(
        "/api/features",
        params={"symbol": "TEST", "timeframe": "1d", "feature": "sma_50@1.0"},
    )
    assert resp.status_code == 200
    data = resp.json()

    assert data["symbol"] == "TEST"
    assert data["timeframe"] == "1d"
    assert data["feature"] == "sma_50@1.0"

    # Only 3 rows have the feature (rows 1, 2, 3)
    assert len(data["data"]) == 3

    # Each entry has time (int) + value (float)
    for entry in data["data"]:
        assert isinstance(entry["time"], int)
        assert isinstance(entry["value"], float)


def test_get_features_nonexistent(client):
    resp = client.get(
        "/api/features",
        params={"symbol": "TEST", "timeframe": "1d", "feature": "nope@1.0"},
    )
    assert resp.status_code == 200
    assert resp.json()["data"] == []


def test_get_features_no_symbol(client):
    resp = client.get(
        "/api/features",
        params={"symbol": "NONEXIST", "timeframe": "1d", "feature": "sma_50@1.0"},
    )
    assert resp.status_code == 200
    assert resp.json()["data"] == []
