"""Tests for Phase 4 — composed features."""

from __future__ import annotations

from datetime import datetime, timezone

import pandas as pd
import pytest

from feature_engine.errors import ComputationError
from feature_engine.feature_spec.enums import FeatureCategory, WarmupPolicy
from feature_engine.composition.atr import AverageTrueRange
from feature_engine.composition.bollinger import (
    BollingerBandWidth,
    BollingerLowerBand,
    BollingerMiddleBand,
    BollingerUpperBand,
)
from feature_engine.composition.macd import MACDHistogram, MACDLine, MACDSignal


def _ohlcv(closes: list[float]) -> pd.DataFrame:
    idx = pd.date_range(
        start=datetime(2026, 1, 5, 14, 30, tzinfo=timezone.utc),
        periods=len(closes),
        freq="1h",
    )
    return pd.DataFrame(
        {
            "open": closes,
            "high": [c + 1.0 for c in closes],
            "low": [c - 1.0 for c in closes],
            "close": closes,
            "volume": [100.0] * len(closes),
        },
        index=idx,
    )


class TestBollingerBands:

    def test_middle_spec_contract(self):
        feat = BollingerMiddleBand(period=20, timeframe="1d")
        assert feat.spec.name == "bollinger_middle_20"
        assert feat.spec.category == FeatureCategory.DERIVED
        assert feat.spec.depends_on == ("sma_20",)
        assert feat.spec.lookback_required == 20
        assert feat.spec.warmup_policy == WarmupPolicy.FIXED_LOOKBACK

    def test_upper_and_lower_specs_include_dependencies(self):
        upper = BollingerUpperBand(period=20, deviation=2.0, timeframe="1d")
        lower = BollingerLowerBand(period=20, deviation=2.0, timeframe="1d")

        assert upper.spec.name == "bollinger_upper_20_2"
        assert lower.spec.name == "bollinger_lower_20_2"
        assert upper.spec.depends_on == ("sma_20", "rolling_std_20")
        assert lower.spec.depends_on == ("sma_20", "rolling_std_20")

    def test_width_spec_tracks_band_dependencies(self):
        width = BollingerBandWidth(period=20, deviation=2.0, timeframe="1d")

        assert width.spec.name == "bollinger_width_20_2"
        assert width.spec.category == FeatureCategory.DERIVED
        assert width.spec.depends_on == (
            "bollinger_middle_20",
            "bollinger_upper_20_2",
            "bollinger_lower_20_2",
        )
        assert width.spec.lookback_required == 20
        assert width.spec.warmup_policy == WarmupPolicy.FIXED_LOOKBACK

    def test_values_match_manual_calculation(self):
        df = _ohlcv([10.0, 20.0, 30.0, 40.0, 50.0])

        middle = BollingerMiddleBand(period=3, timeframe="1h").compute(df)
        upper = BollingerUpperBand(period=3, deviation=2.0, timeframe="1h").compute(df)
        lower = BollingerLowerBand(period=3, deviation=2.0, timeframe="1h").compute(df)

        assert pd.isna(middle.iloc[0])
        assert pd.isna(middle.iloc[1])
        assert middle.iloc[2] == pytest.approx(20.0)
        assert middle.iloc[3] == pytest.approx(30.0)

        expected_std = pd.Series([10.0, 20.0, 30.0]).std(ddof=1)
        assert upper.iloc[2] == pytest.approx(20.0 + 2.0 * expected_std)
        assert lower.iloc[2] == pytest.approx(20.0 - 2.0 * expected_std)

    def test_deviation_parameter_changes_band_distance(self):
        df = _ohlcv([10.0, 20.0, 30.0, 40.0])

        upper = BollingerUpperBand(period=3, deviation=1.5, timeframe="1h").compute(df)
        lower = BollingerLowerBand(period=3, deviation=1.5, timeframe="1h").compute(df)

        expected_std = pd.Series([10.0, 20.0, 30.0]).std(ddof=1)
        assert upper.iloc[2] == pytest.approx(20.0 + 1.5 * expected_std)
        assert lower.iloc[2] == pytest.approx(20.0 - 1.5 * expected_std)

    def test_width_matches_percentage_formula(self):
        df = _ohlcv([10.0, 20.0, 30.0, 40.0, 50.0])

        width = BollingerBandWidth(period=3, deviation=2.0, timeframe="1h").compute(df)

        expected_std = pd.Series([10.0, 20.0, 30.0]).std(ddof=1)
        expected = ((20.0 + 2.0 * expected_std) - (20.0 - 2.0 * expected_std)) / 20.0 * 100.0
        assert width.iloc[2] == pytest.approx(expected)

    def test_width_returns_nan_when_middle_is_zero(self):
        df = _ohlcv([0.0, 0.0, 0.0, 0.0])
        width = BollingerBandWidth(period=2, deviation=2.0, timeframe="1h").compute(df)
        assert pd.isna(width.iloc[1])

    def test_missing_close_raises(self):
        df = pd.DataFrame({"open": [1.0, 2.0]})
        with pytest.raises(ComputationError, match="close"):
            BollingerUpperBand(period=3).compute(df)

    def test_gap_row_produces_nan(self):
        df = _ohlcv([100.0, float("nan"), 105.0, 110.0])
        result = BollingerMiddleBand(period=2, timeframe="1h").compute(df)
        assert pd.isna(result.iloc[1])

    def test_result_index_matches_input(self):
        df = _ohlcv([10.0, 20.0, 30.0, 40.0])
        for feat in [
            BollingerMiddleBand(period=2, timeframe="1h"),
            BollingerUpperBand(period=2, timeframe="1h"),
            BollingerLowerBand(period=2, timeframe="1h"),
            BollingerBandWidth(period=2, timeframe="1h"),
        ]:
            result = feat.compute(df)
            assert (result.index == df.index).all()


class TestMACD:

    def test_line_spec_contract(self):
        feat = MACDLine(fast=12, slow=26, signal=9, timeframe="1d")
        assert feat.spec.name == "macd_line_12_26_9_close"
        assert feat.spec.category == FeatureCategory.DERIVED
        assert feat.spec.depends_on == ("ema_12_close", "ema_26_close")
        assert feat.spec.lookback_required == 26

    def test_signal_and_histogram_specs_include_dependencies(self):
        signal = MACDSignal(fast=12, slow=26, signal=9, timeframe="1d")
        histogram = MACDHistogram(fast=12, slow=26, signal=9, timeframe="1d")

        assert signal.spec.depends_on == ("macd_line_12_26_9_close",)
        assert histogram.spec.depends_on == (
            "macd_line_12_26_9_close",
            "macd_signal_12_26_9_close",
        )
        assert signal.spec.lookback_required == 34
        assert histogram.spec.lookback_required == 34

    def test_values_match_pandas_ewm_formula(self):
        df = _ohlcv([10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0])
        line = MACDLine(fast=3, slow=5, signal=2, timeframe="1h").compute(df)
        signal = MACDSignal(fast=3, slow=5, signal=2, timeframe="1h").compute(df)
        histogram = MACDHistogram(fast=3, slow=5, signal=2, timeframe="1h").compute(df)

        fast_ema = df["close"].ewm(span=3, adjust=False, min_periods=3).mean()
        slow_ema = df["close"].ewm(span=5, adjust=False, min_periods=5).mean()
        expected_line = fast_ema - slow_ema
        expected_signal = expected_line.ewm(span=2, adjust=False, min_periods=2).mean()
        expected_histogram = expected_line - expected_signal

        pd.testing.assert_series_equal(line, expected_line.astype("float64"))
        pd.testing.assert_series_equal(signal, expected_signal.astype("float64"))
        pd.testing.assert_series_equal(histogram, expected_histogram.astype("float64"))

    def test_custom_column_name_flows_into_spec(self):
        feat = MACDLine(fast=8, slow=17, signal=5, column="open", timeframe="1h")
        assert feat.spec.name == "macd_line_8_17_5_open"
        assert feat.spec.depends_on == ("ema_8_open", "ema_17_open")

    def test_invalid_parameters_raise(self):
        with pytest.raises(ValueError, match="fast must be < slow"):
            MACDLine(fast=12, slow=12, signal=9)
        with pytest.raises(ValueError, match="signal must be >= 1"):
            MACDSignal(fast=12, slow=26, signal=0)

    def test_missing_close_raises(self):
        df = pd.DataFrame({"open": [1.0, 2.0]})
        with pytest.raises(ComputationError, match="close"):
            MACDLine().compute(df)


class TestAverageTrueRange:

    def test_spec_contract(self):
        feat = AverageTrueRange(period=14, timeframe="1d")
        assert feat.spec.name == "atr_14"
        assert feat.spec.category == FeatureCategory.DERIVED
        assert feat.spec.depends_on == ("true_range",)
        assert feat.spec.lookback_required == 14
        assert feat.spec.warmup_policy == WarmupPolicy.FIXED_LOOKBACK

    def test_values_match_wilder_smoothing(self):
        df = _ohlcv([10.0, 11.0, 12.0, 13.0, 14.0])
        result = AverageTrueRange(period=3, timeframe="1h").compute(df)

        true_range = pd.concat([
            df["high"] - df["low"],
            (df["high"] - df["close"].shift(1)).abs(),
            (df["low"] - df["close"].shift(1)).abs(),
        ], axis=1).max(axis=1)
        expected = true_range.ewm(alpha=1 / 3, adjust=False, min_periods=3).mean()
        pd.testing.assert_series_equal(result, expected.astype("float64"))

    def test_uses_precomputed_true_range_when_available(self):
        df = _ohlcv([10.0, 11.0, 12.0, 13.0])
        df["true_range"] = pd.Series([1.0, 2.0, 3.0, 4.0], index=df.index)
        result = AverageTrueRange(period=2, timeframe="1h").compute(df)
        expected = df["true_range"].ewm(alpha=1 / 2, adjust=False, min_periods=2).mean()
        pd.testing.assert_series_equal(result, expected.astype("float64"))

    def test_period_zero_raises(self):
        with pytest.raises(ValueError):
            AverageTrueRange(period=0)