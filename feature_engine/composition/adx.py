"""Derived ADX feature family using Wilder smoothing."""

from __future__ import annotations

import pandas as pd

from market_feed.timeframes import Timeframe

from feature_engine.feature_spec.enums import (
    AlignmentPolicy,
    FeatureCategory,
    WarmupPolicy,
)
from feature_engine.feature_spec.spec import FeatureSpec
from feature_engine.feature_spec.temporal import AvailabilityRule
from feature_engine.primitives.rolling import WilderMovingAverage
from feature_engine.primitives.volatility import (
    NegativeDirectionalMovement,
    PositiveDirectionalMovement,
    TrueRange,
)

from .base import DerivedFeature


def _adx_name(period: int) -> str:
    return f"adx_{period}"


def _plus_di_name(period: int) -> str:
    return f"plus_di_{period}"


def _minus_di_name(period: int) -> str:
    return f"minus_di_{period}"


def _validate_period(period: int) -> None:
    if period < 2:
        raise ValueError("period must be >= 2")


def _resolve_series(df: pd.DataFrame, feature_name: str, fallback: pd.Series) -> pd.Series:
    if feature_name in df.columns:
        return df[feature_name].astype("float64")
    return fallback.astype("float64")


def _wilder_smooth(
    df: pd.DataFrame,
    series: pd.Series,
    period: int,
    timeframe: Timeframe,
    source_name: str,
) -> pd.Series:
    if source_name in df.columns:
        source_df = df
        column = source_name
    else:
        column = f"__adx_{source_name}"
        source_df = df.assign(**{column: series.astype("float64")})
    return WilderMovingAverage(period=period, column=column, timeframe=timeframe).compute(source_df).astype("float64")


class PlusDirectionalIndex(DerivedFeature):
    """Positive Directional Indicator (+DI) using Wilder smoothing."""

    def __init__(self, period: int = 14, timeframe: Timeframe = "1d") -> None:
        _validate_period(period)
        self._period = period
        self._timeframe: Timeframe = timeframe
        self._spec = FeatureSpec(
            name=_plus_di_name(period),
            version="1.0",
            category=FeatureCategory.DERIVED,
            timeframe=timeframe,
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            depends_on=("true_range", "plus_dm"),
            lookback_required=period,
            warmup_policy=WarmupPolicy.FIXED_LOOKBACK,
        )

    @property
    def spec(self) -> FeatureSpec:
        return self._spec

    def compute(self, df: pd.DataFrame) -> pd.Series:
        true_range = df["true_range"].astype("float64") if "true_range" in df.columns else TrueRange(self._timeframe).compute(df).astype("float64")
        plus_dm = df["plus_dm"].astype("float64") if "plus_dm" in df.columns else PositiveDirectionalMovement(self._timeframe).compute(df).astype("float64")

        smoothed_tr = _wilder_smooth(df, true_range, self._period, self._timeframe, "true_range")
        smoothed_plus_dm = _wilder_smooth(df, plus_dm, self._period, self._timeframe, "plus_dm")
        plus_di = (100.0 * smoothed_plus_dm / smoothed_tr).where(smoothed_tr != 0.0)
        return plus_di.astype("float64").rename(None)


class MinusDirectionalIndex(DerivedFeature):
    """Negative Directional Indicator (-DI) using Wilder smoothing."""

    def __init__(self, period: int = 14, timeframe: Timeframe = "1d") -> None:
        _validate_period(period)
        self._period = period
        self._timeframe: Timeframe = timeframe
        self._spec = FeatureSpec(
            name=_minus_di_name(period),
            version="1.0",
            category=FeatureCategory.DERIVED,
            timeframe=timeframe,
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            depends_on=("true_range", "minus_dm"),
            lookback_required=period,
            warmup_policy=WarmupPolicy.FIXED_LOOKBACK,
        )

    @property
    def spec(self) -> FeatureSpec:
        return self._spec

    def compute(self, df: pd.DataFrame) -> pd.Series:
        true_range = df["true_range"].astype("float64") if "true_range" in df.columns else TrueRange(self._timeframe).compute(df).astype("float64")
        minus_dm = df["minus_dm"].astype("float64") if "minus_dm" in df.columns else NegativeDirectionalMovement(self._timeframe).compute(df).astype("float64")

        smoothed_tr = _wilder_smooth(df, true_range, self._period, self._timeframe, "true_range")
        smoothed_minus_dm = _wilder_smooth(df, minus_dm, self._period, self._timeframe, "minus_dm")
        minus_di = (100.0 * smoothed_minus_dm / smoothed_tr).where(smoothed_tr != 0.0)
        return minus_di.astype("float64").rename(None)


class AverageDirectionalIndex(DerivedFeature):
    """Average Directional Index (ADX) using Wilder smoothing."""

    def __init__(self, period: int = 14, timeframe: Timeframe = "1d") -> None:
        _validate_period(period)
        self._period = period
        self._timeframe: Timeframe = timeframe
        self._spec = FeatureSpec(
            name=_adx_name(period),
            version="1.0",
            category=FeatureCategory.DERIVED,
            timeframe=timeframe,
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            depends_on=(_plus_di_name(period), _minus_di_name(period)),
            lookback_required=(2 * period) - 1,
            warmup_policy=WarmupPolicy.FIXED_LOOKBACK,
        )

    @property
    def spec(self) -> FeatureSpec:
        return self._spec

    def compute(self, df: pd.DataFrame) -> pd.Series:
        plus_di_name = _plus_di_name(self._period)
        minus_di_name = _minus_di_name(self._period)
        plus_di = df[plus_di_name].astype("float64") if plus_di_name in df.columns else PlusDirectionalIndex(self._period, self._timeframe).compute(df).astype("float64")
        minus_di = df[minus_di_name].astype("float64") if minus_di_name in df.columns else MinusDirectionalIndex(self._period, self._timeframe).compute(df).astype("float64")

        denominator = plus_di + minus_di
        dx = (100.0 * (plus_di - minus_di).abs() / denominator).where(denominator != 0.0, 0.0)
        dx = dx.astype("float64").rename(None)
        return _wilder_smooth(df, dx, self._period, self._timeframe, "dx").rename(None)