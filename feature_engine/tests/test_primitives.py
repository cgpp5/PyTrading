"""Tests for Phase 2 — Primitive (atomic) features.

Each test verifies:
  - Correct FeatureSpec contract.
  - Correct numerical output on controlled data.
  - NaN propagation (gap rows / warmup period).
  - ComputationError on missing columns.
"""

from __future__ import annotations

from datetime import datetime, timezone

import numpy as np
import pandas as pd
import pytest

from feature_engine.errors import ComputationError
from feature_engine.feature_spec.enums import FeatureCategory, WarmupPolicy
from feature_engine.primitives.returns import LogReturns, SimpleReturns
from feature_engine.primitives.rolling import RollingMean, RollingStd
from feature_engine.primitives.volatility import TrueRange
from feature_engine.primitives.volume import VolumeZScore


# ------------------------------------------------------------------
# Helper: build a minimal OHLCV DataFrame
# ------------------------------------------------------------------

def _ohlcv(
    closes: list[float],
    *,
    highs: list[float] | None = None,
    lows: list[float] | None = None,
    volumes: list[float] | None = None,
) -> pd.DataFrame:
    n = len(closes)
    idx = pd.date_range(
        start=datetime(2026, 1, 5, 14, 30, tzinfo=timezone.utc),
        periods=n,
        freq="1h",
    )
    return pd.DataFrame(
        {
            "open": closes,  # simplified: open == close for tests
            "high": highs if highs is not None else [c + 1.0 for c in closes],
            "low": lows if lows is not None else [c - 1.0 for c in closes],
            "close": closes,
            "volume": volumes if volumes is not None else [100.0] * n,
        },
        index=idx,
    )


# ==================================================================
# SimpleReturns
# ==================================================================

class TestSimpleReturns:

    def test_spec_contract(self):
        feat = SimpleReturns(timeframe="1h")
        assert feat.spec.name == "returns"
        assert feat.spec.category == FeatureCategory.TECHNICAL
        assert feat.spec.timeframe == "1h"
        assert feat.spec.lookback_required == 1
        assert feat.spec.warmup_policy == WarmupPolicy.FIXED_LOOKBACK

    def test_values(self):
        df = _ohlcv([100.0, 110.0, 104.5])
        result = SimpleReturns("1h").compute(df)

        assert pd.isna(result.iloc[0])
        assert result.iloc[1] == pytest.approx(0.10)
        assert result.iloc[2] == pytest.approx((104.5 - 110.0) / 110.0)

    def test_nan_close_propagates(self):
        df = _ohlcv([100.0, float("nan"), 105.0])
        result = SimpleReturns("1h").compute(df)
        assert pd.isna(result.iloc[1])
        assert pd.isna(result.iloc[2])  # NaN / number → NaN

    def test_missing_column_raises(self):
        df = pd.DataFrame({"open": [1.0]})
        with pytest.raises(ComputationError, match="close"):
            SimpleReturns().compute(df)


# ==================================================================
# LogReturns
# ==================================================================

class TestLogReturns:

    def test_spec_contract(self):
        feat = LogReturns(timeframe="1d")
        assert feat.spec.name == "log_returns"

    def test_values(self):
        df = _ohlcv([100.0, 110.0, 104.5])
        result = LogReturns("1h").compute(df)

        assert pd.isna(result.iloc[0])
        assert result.iloc[1] == pytest.approx(np.log(110.0 / 100.0))
        assert result.iloc[2] == pytest.approx(np.log(104.5 / 110.0))


# ==================================================================
# RollingMean (SMA)
# ==================================================================

class TestRollingMean:

    def test_spec_contract(self):
        feat = RollingMean(window=20, timeframe="1d")
        assert feat.spec.name == "sma_20"
        assert feat.spec.lookback_required == 20

    def test_values(self):
        df = _ohlcv([10.0, 20.0, 30.0, 40.0, 50.0])
        result = RollingMean(window=3, timeframe="1h").compute(df)

        assert pd.isna(result.iloc[0])
        assert pd.isna(result.iloc[1])
        assert result.iloc[2] == pytest.approx(20.0)  # (10+20+30)/3
        assert result.iloc[3] == pytest.approx(30.0)  # (20+30+40)/3
        assert result.iloc[4] == pytest.approx(40.0)  # (30+40+50)/3

    def test_custom_column(self):
        df = _ohlcv([1.0, 2.0, 3.0], volumes=[100.0, 200.0, 300.0])
        result = RollingMean(window=2, column="volume", timeframe="1h").compute(df)
        assert result.iloc[2] == pytest.approx(250.0)

    def test_window_zero_raises(self):
        with pytest.raises(ValueError):
            RollingMean(window=0)

    def test_missing_column_raises(self):
        df = pd.DataFrame({"open": [1.0, 2.0]})
        with pytest.raises(ComputationError, match="close"):
            RollingMean(window=2).compute(df)


# ==================================================================
# RollingStd
# ==================================================================

class TestRollingStd:

    def test_spec_contract(self):
        feat = RollingStd(window=10, timeframe="1h")
        assert feat.spec.name == "rolling_std_10"
        assert feat.spec.lookback_required == 10

    def test_values(self):
        df = _ohlcv([10.0, 20.0, 30.0, 40.0])
        result = RollingStd(window=3, timeframe="1h").compute(df)

        assert pd.isna(result.iloc[0])
        assert pd.isna(result.iloc[1])
        expected_std = pd.Series([10.0, 20.0, 30.0]).std(ddof=1)
        assert result.iloc[2] == pytest.approx(expected_std)

    def test_window_one_raises(self):
        with pytest.raises(ValueError):
            RollingStd(window=1)


# ==================================================================
# TrueRange
# ==================================================================

class TestTrueRange:

    def test_spec_contract(self):
        feat = TrueRange(timeframe="1h")
        assert feat.spec.name == "true_range"
        assert feat.spec.lookback_required == 1

    def test_values(self):
        #                  O     H     L     C     V
        df = pd.DataFrame(
            {
                "open":   [100, 110, 105],
                "high":   [105, 115, 110],
                "low":    [ 95, 100, 100],
                "close":  [102, 108, 106],
                "volume": [100, 100, 100],
            },
            index=pd.date_range("2026-01-05", periods=3, freq="1D", tz="UTC"),
            dtype=float,
        )
        result = TrueRange("1d").compute(df)

        # Bar 0: no prev close → high_prev and low_prev are NaN,
        # but high-low = 10 is valid → true_range = 10
        assert result.iloc[0] == pytest.approx(10.0)

        # Bar 1: prev_close=102
        # high-low=15, |high-prev_close|=13, |low-prev_close|=2 → 15
        assert result.iloc[1] == pytest.approx(15.0)

        # Bar 2: prev_close=108
        # high-low=10, |high-prev_close|=2, |low-prev_close|=8 → 10
        assert result.iloc[2] == pytest.approx(10.0)

    def test_missing_columns_raises(self):
        df = pd.DataFrame({"close": [1.0]})
        with pytest.raises(ComputationError, match="high"):
            TrueRange().compute(df)


# ==================================================================
# VolumeZScore
# ==================================================================

class TestVolumeZScore:

    def test_spec_contract(self):
        feat = VolumeZScore(window=20, timeframe="1d")
        assert feat.spec.name == "volume_zscore_20"
        assert feat.spec.lookback_required == 20

    def test_values(self):
        vols = [100.0, 200.0, 300.0, 400.0, 500.0]
        df = _ohlcv([10.0] * 5, volumes=vols)
        result = VolumeZScore(window=3, timeframe="1h").compute(df)

        # First 2 values are NaN (window=3, not enough data)
        assert pd.isna(result.iloc[0])
        assert pd.isna(result.iloc[1])

        # Bar 2: window=[100,200,300], mean=200, std≈100
        # z = (300-200)/100 = 1.0
        assert result.iloc[2] == pytest.approx(1.0)

    def test_window_one_raises(self):
        with pytest.raises(ValueError):
            VolumeZScore(window=1)

    def test_missing_column_raises(self):
        df = pd.DataFrame({"close": [1.0, 2.0, 3.0]})
        with pytest.raises(ComputationError, match="volume"):
            VolumeZScore(window=2).compute(df)


# ==================================================================
# Cross-cutting: PrimitiveFeature contract
# ==================================================================

class TestPrimitiveContract:

    def test_result_index_matches_input(self):
        """Output Series must share the same DatetimeIndex as the input."""
        df = _ohlcv([10.0, 20.0, 30.0, 40.0, 50.0])
        for feat in [
            SimpleReturns("1h"),
            LogReturns("1h"),
            RollingMean(window=3, timeframe="1h"),
            RollingStd(window=3, timeframe="1h"),
            TrueRange("1h"),
            VolumeZScore(window=3, timeframe="1h"),
        ]:
            result = feat.compute(df)
            assert (result.index == df.index).all(), f"{feat.spec.name} index mismatch"

    def test_result_length_matches_input(self):
        """Output length == input length (NaN padding, never truncation)."""
        df = _ohlcv([10.0, 20.0, 30.0])
        for feat in [SimpleReturns("1h"), TrueRange("1h")]:
            assert len(feat.compute(df)) == len(df)

    def test_gap_row_nan_propagation(self):
        """NaN OHLCV rows (gap rows) must produce NaN output — never crash."""
        df = _ohlcv(
            [100.0, float("nan"), 105.0, 110.0, 115.0],
            highs=[101.0, float("nan"), 106.0, 111.0, 116.0],
            lows=[99.0, float("nan"), 104.0, 109.0, 114.0],
            volumes=[100.0, float("nan"), 100.0, 100.0, 100.0],
        )
        for feat in [
            SimpleReturns("1h"),
            LogReturns("1h"),
            RollingMean(window=2, timeframe="1h"),
            TrueRange("1h"),
            VolumeZScore(window=2, timeframe="1h"),
        ]:
            result = feat.compute(df)
            assert len(result) == len(df), f"{feat.spec.name} length mismatch"
            # Row 1 (NaN input) should produce NaN output
            assert pd.isna(result.iloc[1]), f"{feat.spec.name} should be NaN at gap"
