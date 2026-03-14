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
            "sma_osc_20@1.0": {"value": 2.5 + i, "quality": "ready"},
            "atr_14@1.0": {"value": 1.5 + i, "quality": "ready"},
            "adx_14@1.0": {"value": 20.0 + i, "quality": "ready"},
            "plus_di_14@1.0": {"value": 25.0 + i, "quality": "ready"},
            "minus_di_14@1.0": {"value": 15.0 + i, "quality": "ready"},
            "bollinger_middle_20@1.0": {"value": 101.0 + i, "quality": "ready"},
            "bollinger_upper_20_2@1.0": {"value": 103.0 + i, "quality": "ready"},
            "bollinger_lower_20_2@1.0": {"value": 99.0 + i, "quality": "ready"},
            "macd_line_12_26_9_close@1.0": {"value": 0.5 + i, "quality": "ready"},
            "macd_signal_12_26_9_close@1.0": {"value": 0.25 + i, "quality": "ready"},
            "macd_histogram_12_26_9_close@1.0": {"value": 0.25, "quality": "ready"},
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
    assert data["features"] == [
        "adx_14@1.0",
        "atr_14@1.0",
        "bollinger_lower_20_2@1.0",
        "bollinger_middle_20@1.0",
        "bollinger_upper_20_2@1.0",
        "macd_histogram_12_26_9_close@1.0",
        "macd_line_12_26_9_close@1.0",
        "macd_signal_12_26_9_close@1.0",
        "minus_di_14@1.0",
        "plus_di_14@1.0",
        "sma_50@1.0",
        "sma_osc_20@1.0",
    ]


def test_get_available_indicators_groups_bollinger(client):
    resp = client.get(
        "/api/available-indicators",
        params={"symbol": "TEST", "timeframe": "1d"},
    )
    assert resp.status_code == 200

    indicators = resp.json()["indicators"]
    assert [indicator["key"] for indicator in indicators] == [
        "adx_family_14@1.0",
        "atr_14@1.0",
        "bollinger_bands_20_2@1.0",
        "macd_12_26_9_close@1.0",
        "sma_osc_20@1.0",
        "sma_50@1.0",
    ]
    assert indicators[0]["pane"] == "separate"
    assert indicators[0]["kind"] == "adx"
    assert indicators[0]["name"] == "ADX (14)"
    assert [series["label"] for series in indicators[0]["series"]] == [
        "ADX",
        "+DI",
        "-DI",
    ]
    assert indicators[1]["pane"] == "separate"
    assert indicators[1]["kind"] == "atr"
    assert indicators[1]["name"] == "ATR (14)"
    assert indicators[2]["name"] == "Bollinger Bands (20, 2)"
    assert [series["label"] for series in indicators[2]["series"]] == [
        "Middle",
        "Upper",
        "Lower",
    ]
    assert indicators[3]["pane"] == "separate"
    assert [series["seriesType"] for series in indicators[3]["series"]] == [
        "line",
        "line",
        "histogram",
    ]
    assert indicators[4]["kind"] == "sma_osc"
    assert indicators[4]["pane"] == "separate"
    assert indicators[4]["name"] == "SMA Osc (20)"


def test_get_available_features_includes_simple_keys(store):
    conn = store.get_connection()
    try:
        ts_iso = pd.date_range("2026-01-05", periods=1, freq="B", tz="UTC")[0].isoformat()
        save_features(conn, "TEST", "1d", ts_iso, {
            "mcclellan_oscillator": {"value": 12.3, "quality": "ready"},
        })
    finally:
        conn.close()

    set_store(store)
    with TestClient(app) as client:
        resp = client.get(
            "/api/available-features",
            params={"symbol": "TEST", "timeframe": "1d"},
        )

    assert resp.status_code == 200
    assert resp.json()["features"] == [
        "adx_14@1.0",
        "atr_14@1.0",
        "bollinger_lower_20_2@1.0",
        "bollinger_middle_20@1.0",
        "bollinger_upper_20_2@1.0",
        "macd_histogram_12_26_9_close@1.0",
        "macd_line_12_26_9_close@1.0",
        "macd_signal_12_26_9_close@1.0",
        "mcclellan_oscillator",
        "minus_di_14@1.0",
        "plus_di_14@1.0",
        "sma_50@1.0",
        "sma_osc_20@1.0",
    ]

    set_store(None)


def test_get_available_indicators_includes_simple_scalar_keys(store):
    conn = store.get_connection()
    try:
        ts_iso = pd.date_range("2026-01-05", periods=1, freq="B", tz="UTC")[0].isoformat()
        save_features(conn, "TEST", "1d", ts_iso, {
            "mcclellan_oscillator": {"value": 12.3, "quality": "ready"},
        })
    finally:
        conn.close()

    set_store(store)
    with TestClient(app) as client:
        resp = client.get(
            "/api/available-indicators",
            params={"symbol": "TEST", "timeframe": "1d"},
        )

    assert resp.status_code == 200
    assert [indicator["key"] for indicator in resp.json()["indicators"]] == [
        "adx_family_14@1.0",
        "atr_14@1.0",
        "bollinger_bands_20_2@1.0",
        "macd_12_26_9_close@1.0",
        "mcclellan_oscillator",
        "sma_osc_20@1.0",
        "sma_50@1.0",
    ]

    set_store(None)


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


def test_get_indicator_returns_grouped_bollinger_series(client):
    resp = client.get(
        "/api/indicator",
        params={"symbol": "TEST", "timeframe": "1d", "indicator": "bollinger_bands_20_2@1.0"},
    )
    assert resp.status_code == 200

    data = resp.json()
    assert data["indicator"] == "bollinger_bands_20_2@1.0"
    assert data["name"] == "Bollinger Bands (20, 2)"
    assert data["kind"] == "bollinger_bands"
    assert len(data["series"]) == 3
    assert [series["label"] for series in data["series"]] == [
        "Middle",
        "Upper",
        "Lower",
    ]
    assert all(len(series["data"]) == 3 for series in data["series"])


def test_get_indicator_returns_atr_scalar_in_separate_pane(client):
    resp = client.get(
        "/api/indicator",
        params={"symbol": "TEST", "timeframe": "1d", "indicator": "atr_14@1.0"},
    )
    assert resp.status_code == 200

    data = resp.json()
    assert data["indicator"] == "atr_14@1.0"
    assert data["name"] == "ATR (14)"
    assert data["kind"] == "atr"
    assert data["pane"] == "separate"
    assert len(data["series"]) == 1
    assert data["series"][0]["seriesType"] == "line"
    assert len(data["series"][0]["data"]) == 3


def test_get_indicator_returns_grouped_adx_series(client):
    resp = client.get(
        "/api/indicator",
        params={"symbol": "TEST", "timeframe": "1d", "indicator": "adx_family_14@1.0"},
    )
    assert resp.status_code == 200

    data = resp.json()
    assert data["indicator"] == "adx_family_14@1.0"
    assert data["name"] == "ADX (14)"
    assert data["kind"] == "adx"
    assert data["pane"] == "separate"
    assert len(data["series"]) == 3
    assert [series["label"] for series in data["series"]] == [
        "ADX",
        "+DI",
        "-DI",
    ]
    assert [series["seriesType"] for series in data["series"]] == [
        "line",
        "line",
        "line",
    ]
    assert all(len(series["data"]) == 3 for series in data["series"])


def test_get_indicator_returns_grouped_macd_series(client):
    resp = client.get(
        "/api/indicator",
        params={"symbol": "TEST", "timeframe": "1d", "indicator": "macd_12_26_9_close@1.0"},
    )
    assert resp.status_code == 200

    data = resp.json()
    assert data["indicator"] == "macd_12_26_9_close@1.0"
    assert data["name"] == "MACD (12, 26, 9)"
    assert data["kind"] == "macd"
    assert data["pane"] == "separate"
    assert len(data["series"]) == 3
    assert [series["label"] for series in data["series"]] == [
        "MACD",
        "Signal",
        "Histogram",
    ]
    assert [series["seriesType"] for series in data["series"]] == [
        "line",
        "line",
        "histogram",
    ]
    assert all(len(series["data"]) == 3 for series in data["series"])


def test_get_indicator_returns_scalar_indicator(client):
    resp = client.get(
        "/api/indicator",
        params={"symbol": "TEST", "timeframe": "1d", "indicator": "sma_50@1.0"},
    )
    assert resp.status_code == 200

    data = resp.json()
    assert data["kind"] == "scalar"
    assert len(data["series"]) == 1
    assert data["series"][0]["key"] == "sma_50@1.0"


def test_get_indicator_returns_sma_osc_in_separate_pane(client):
    resp = client.get(
        "/api/indicator",
        params={"symbol": "TEST", "timeframe": "1d", "indicator": "sma_osc_20@1.0"},
    )
    assert resp.status_code == 200

    data = resp.json()
    assert data["indicator"] == "sma_osc_20@1.0"
    assert data["name"] == "SMA Osc (20)"
    assert data["kind"] == "sma_osc"
    assert data["pane"] == "separate"
    assert len(data["series"]) == 1
    assert data["series"][0]["label"] == "SMA Osc"
    assert data["series"][0]["seriesType"] == "line"
    assert data["series"][0]["valueFormat"] == "percent"
    assert len(data["series"][0]["data"]) == 3


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
