"""Tests for Phase 4 — composed features."""

from __future__ import annotations

from datetime import datetime, timezone

import numpy as np
import pandas as pd
import pytest

from feature_engine.composition.adx import (
    AverageDirectionalIndex,
    MinusDirectionalIndex,
    PlusDirectionalIndex,
)
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
from feature_engine.composition.mogalef import (
    MogalefLowerBand,
    MogalefMiddleBand,
    MogalefUpperBand,
)
from feature_engine.composition.sma_osc import SMAOscillator


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


def _wilder_mean(values: pd.Series, period: int) -> pd.Series:
    values = values.astype("float64")
    result = pd.Series(np.nan, index=values.index, dtype="float64")
    seed = values.rolling(window=period, min_periods=period).mean()
    first_valid_pos = next((idx for idx, value in enumerate(seed.tolist()) if pd.notna(value)), None)
    if first_valid_pos is None:
        return result

    result.iloc[first_valid_pos] = float(seed.iloc[first_valid_pos])
    for pos in range(first_valid_pos + 1, len(values)):
        previous_value = result.iloc[pos - 1]
        current_value = values.iloc[pos]
        if pd.isna(previous_value) or pd.isna(current_value):
            continue
        result.iloc[pos] = ((previous_value * (period - 1)) + current_value) / period

    return result


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


class TestMogalef:
    """Tests for the Mogalef Bands (Eric Lefort) overlay features."""

    def _mogalef_df(self, vals: list[float]) -> pd.DataFrame:
        idx = pd.date_range(
            start=datetime(2026, 1, 5, 14, 30, tzinfo=timezone.utc),
            periods=len(vals),
            freq="1h",
        )
        # open=close, high/low offset by +/-1 so the weighted Mogalef price
        # (H + L + O + C + C)/5 reduces exactly to close.
        return pd.DataFrame(
            {
                "open": vals,
                "high": [v + 1.0 for v in vals],
                "low": [v - 1.0 for v in vals],
                "close": vals,
                "volume": [100.0] * len(vals),
            },
            index=idx,
        )

    def test_spec_contract(self):
        feature = MogalefMiddleBand(n=3, et=7, coef=2.0, timeframe="1d")
        assert feature.spec.name == "mogalef_middle_3_7_2"
        assert feature.spec.category == FeatureCategory.TECHNICAL
        assert feature.spec.depends_on == ()
        assert feature.spec.lookback_required == 9
        assert feature.spec.warmup_policy == WarmupPolicy.FIXED_LOOKBACK

    def test_band_siblings_have_distinct_names(self):
        lower = MogalefLowerBand(n=3, et=7, coef=2.0, timeframe="1d")
        upper = MogalefUpperBand(n=3, et=7, coef=2.0, timeframe="1d")
        assert lower.spec.name == "mogalef_lower_3_7_2"
        assert upper.spec.name == "mogalef_upper_3_7_2"
        assert lower.spec.lookback_required == 9
        assert upper.spec.lookback_required == 9

    def test_values_match_flat_breakout_construction(self):
        # Weighted prices 1..8 give a perfectly linear regression line, so the
        # band width (std dev of the regression line) is constant and the
        # flat/breakout scan drives the plateaued envelope.
        df = self._mogalef_df([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])

        middle = MogalefMiddleBand(n=3, et=3, coef=2.0, timeframe="1h").compute(df)
        upper = MogalefUpperBand(n=3, et=3, coef=2.0, timeframe="1h").compute(df)
        lower = MogalefLowerBand(n=3, et=3, coef=2.0, timeframe="1h").compute(df)

        # etyp = population std dev of the regression window [3,4,5] = sqrt(2/3).
        half = 2.0 * (2.0 / 3.0) ** 0.5
        expected = {
            "middle": [np.nan, np.nan, np.nan, np.nan, 6.0, 6.0, 8.0, 8.0],
            "upper": [
                np.nan, np.nan, np.nan, np.nan,
                6.0 + half, 6.0 + half, 8.0 + half, 8.0 + half,
            ],
            "lower": [
                np.nan, np.nan, np.nan, np.nan,
                6.0 - half, 6.0 - half, 8.0 - half, 8.0 - half,
            ],
        }

        for result, exp in [
            (middle, expected["middle"]),
            (upper, expected["upper"]),
            (lower, expected["lower"]),
        ]:
            assert result.index.equals(df.index)
            for got, want in zip(result.to_numpy(), exp):
                if pd.isna(want):
                    assert pd.isna(got)
                else:
                    assert got == pytest.approx(want)

    def test_final_bar_always_anchors_a_fresh_band(self):
        df = self._mogalef_df([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
        upper = MogalefUpperBand(n=3, et=3, coef=2.0, timeframe="1h").compute(df)

        reg_last = 8.0
        std_last = (2.0 / 3.0) ** 0.5
        assert upper.iloc[-1] == pytest.approx(reg_last + 2.0 * std_last)

    def test_gap_row_produces_nan(self):
        df = self._mogalef_df([100.0, float("nan"), 105.0, 110.0, 115.0])
        result = MogalefMiddleBand(n=3, et=3, coef=2.0, timeframe="1h").compute(df)
        assert pd.isna(result.iloc[1])

    def test_missing_columns_raise(self):
        df = pd.DataFrame({"open": [1.0, 2.0], "close": [1.0, 2.0]})
        with pytest.raises(ComputationError, match="high"):
            MogalefMiddleBand(n=3, et=3, coef=2.0).compute(df)

    def test_invalid_parameters_raise(self):
        with pytest.raises(ValueError, match="n must be >= 2"):
            MogalefMiddleBand(n=1, et=3, coef=2.0)
        with pytest.raises(ValueError, match="et must be >= 2"):
            MogalefUpperBand(n=3, et=1, coef=2.0)
        with pytest.raises(ValueError, match="coef must be > 0"):
            MogalefLowerBand(n=3, et=7, coef=0.0)


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

        expected = pd.Series([float("nan"), float("nan"), 2.0, 2.0, 2.0], index=df.index, dtype="float64")
        pd.testing.assert_series_equal(result, expected)

    def test_uses_precomputed_true_range_when_available(self):
        df = _ohlcv([10.0, 11.0, 12.0, 13.0])
        df["true_range"] = pd.Series([1.0, 2.0, 3.0, 4.0], index=df.index)
        result = AverageTrueRange(period=2, timeframe="1h").compute(df)
        expected = pd.Series([float("nan"), 1.5, 2.25, 3.125], index=df.index, dtype="float64")
        pd.testing.assert_series_equal(result, expected)

    def test_wilder_seed_differs_from_plain_ewm(self):
        df = _ohlcv([10.0, 12.0, 11.0, 15.0, 14.0])
        result = AverageTrueRange(period=3, timeframe="1h").compute(df)

        true_range = pd.concat([
            df["high"] - df["low"],
            (df["high"] - df["close"].shift(1)).abs(),
            (df["low"] - df["close"].shift(1)).abs(),
        ], axis=1).max(axis=1).astype("float64")
        ewm_result = true_range.ewm(alpha=1 / 3, adjust=False, min_periods=3).mean().astype("float64")

        assert result.iloc[2] != ewm_result.iloc[2]
        assert result.iloc[2] == pytest.approx(true_range.iloc[:3].mean())

    def test_period_zero_raises(self):
        with pytest.raises(ValueError):
            AverageTrueRange(period=0)


class TestADX:

    def test_spec_contract(self):
        plus = PlusDirectionalIndex(period=14, timeframe="1d")
        minus = MinusDirectionalIndex(period=14, timeframe="1d")
        adx = AverageDirectionalIndex(period=14, timeframe="1d")

        assert plus.spec.name == "plus_di_14"
        assert minus.spec.name == "minus_di_14"
        assert adx.spec.name == "adx_14"
        assert plus.spec.category == FeatureCategory.DERIVED
        assert minus.spec.depends_on == ("true_range", "minus_dm")
        assert plus.spec.depends_on == ("true_range", "plus_dm")
        assert adx.spec.depends_on == ("plus_di_14", "minus_di_14")
        assert plus.spec.lookback_required == 14
        assert adx.spec.lookback_required == 27
        assert adx.spec.warmup_policy == WarmupPolicy.FIXED_LOOKBACK

    def test_values_match_manual_wilder_formula(self):
        df = pd.DataFrame(
            {
                "open": [10.0, 11.0, 13.0, 12.0, 15.0, 14.0, 17.0],
                "high": [11.0, 13.0, 14.0, 13.0, 16.0, 15.0, 18.0],
                "low": [9.0, 10.0, 12.0, 10.0, 13.0, 12.0, 15.0],
                "close": [10.0, 12.0, 13.0, 11.0, 15.0, 13.0, 17.0],
                "volume": [100.0] * 7,
            },
            index=pd.date_range("2026-01-05", periods=7, freq="1D", tz="UTC"),
        )

        plus_di = PlusDirectionalIndex(period=3, timeframe="1d").compute(df)
        minus_di = MinusDirectionalIndex(period=3, timeframe="1d").compute(df)
        adx = AverageDirectionalIndex(period=3, timeframe="1d").compute(df)

        up_move = df["high"].diff()
        down_move = df["low"].shift(1) - df["low"]
        plus_dm = up_move.where((up_move > down_move) & (up_move > 0), 0.0).fillna(0.0).astype("float64")
        minus_dm = down_move.where((down_move > up_move) & (down_move > 0), 0.0).fillna(0.0).astype("float64")
        true_range = pd.concat([
            df["high"] - df["low"],
            (df["high"] - df["close"].shift(1)).abs(),
            (df["low"] - df["close"].shift(1)).abs(),
        ], axis=1).max(axis=1).astype("float64")

        smoothed_tr = _wilder_mean(true_range, 3)
        smoothed_plus_dm = _wilder_mean(plus_dm, 3)
        smoothed_minus_dm = _wilder_mean(minus_dm, 3)

        expected_plus_di = (100.0 * smoothed_plus_dm / smoothed_tr).where(smoothed_tr != 0.0).astype("float64")
        expected_minus_di = (100.0 * smoothed_minus_dm / smoothed_tr).where(smoothed_tr != 0.0).astype("float64")
        denominator = expected_plus_di + expected_minus_di
        dx = (100.0 * (expected_plus_di - expected_minus_di).abs() / denominator).where(denominator != 0.0, 0.0)
        expected_adx = _wilder_mean(dx.astype("float64"), 3)

        pd.testing.assert_series_equal(plus_di, expected_plus_di.rename(None))
        pd.testing.assert_series_equal(minus_di, expected_minus_di.rename(None))
        pd.testing.assert_series_equal(adx, expected_adx.rename(None))

    def test_adx_uses_precomputed_di_when_available(self):
        index = pd.date_range("2026-01-05", periods=6, freq="1D", tz="UTC")
        df = pd.DataFrame(
            {
                "plus_di_3": [np.nan, np.nan, 40.0, 35.0, 25.0, 30.0],
                "minus_di_3": [np.nan, np.nan, 20.0, 25.0, 35.0, 20.0],
            },
            index=index,
        )

        denominator = df["plus_di_3"] + df["minus_di_3"]
        dx = (100.0 * (df["plus_di_3"] - df["minus_di_3"]).abs() / denominator).where(denominator != 0.0, 0.0)
        expected = _wilder_mean(dx.astype("float64"), 3)

        result = AverageDirectionalIndex(period=3, timeframe="1d").compute(df)
        pd.testing.assert_series_equal(result, expected.rename(None))

    def test_invalid_period_raises(self):
        with pytest.raises(ValueError, match="period must be >= 2"):
            PlusDirectionalIndex(period=1)

    def test_missing_inputs_raise_when_dependencies_not_precomputed(self):
        df = pd.DataFrame({"open": [1.0, 2.0]})
        with pytest.raises(ComputationError, match="high"):
            PlusDirectionalIndex(period=3).compute(df)


class TestSMAOscillator:

    def test_spec_contract(self):
        feat = SMAOscillator(period=20, timeframe="1d")
        assert feat.spec.name == "sma_osc_20"
        assert feat.spec.category == FeatureCategory.DERIVED
        assert feat.spec.depends_on == ("sma_20",)
        assert feat.spec.lookback_required == 20
        assert feat.spec.warmup_policy == WarmupPolicy.FIXED_LOOKBACK

    def test_values_match_percentage_distance_to_sma(self):
        df = _ohlcv([10.0, 20.0, 30.0, 40.0])
        result = SMAOscillator(period=3, timeframe="1h").compute(df)

        sma = pd.Series([float("nan"), float("nan"), 20.0, 30.0], index=df.index, dtype="float64")
        expected = ((df["close"].astype("float64") - sma) / sma) * 100.0
        pd.testing.assert_series_equal(result, expected.rename(None))

    def test_uses_precomputed_sma_when_available(self):
        df = _ohlcv([10.0, 20.0, 30.0, 40.0])
        df["sma_3"] = pd.Series([float("nan"), float("nan"), 15.0, 25.0], index=df.index)
        result = SMAOscillator(period=3, timeframe="1h").compute(df)
        expected = (((df["close"].astype("float64") - df["sma_3"].astype("float64")) / df["sma_3"].astype("float64")) * 100.0).rename(None)
        pd.testing.assert_series_equal(result, expected)

    def test_returns_nan_when_sma_is_zero(self):
        df = _ohlcv([0.0, 0.0, 1.0])
        df["sma_2"] = pd.Series([float("nan"), 0.0, 0.0], index=df.index)
        result = SMAOscillator(period=2, timeframe="1h").compute(df)
        assert pd.isna(result.iloc[1])
        assert pd.isna(result.iloc[2])

    def test_period_zero_raises(self):
        with pytest.raises(ValueError):
            SMAOscillator(period=0)