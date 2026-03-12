"""Derived Bollinger Band features."""

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
from feature_engine.primitives.rolling import RollingMean, RollingStd

from .base import DerivedFeature


def _format_param(value: float) -> str:
    return f"{value:g}".replace(".", "_")


def _middle_name(period: int) -> str:
    return f"bollinger_middle_{period}"


def _upper_name(period: int, deviation: float) -> str:
    return f"bollinger_upper_{period}_{_format_param(deviation)}"


def _lower_name(period: int, deviation: float) -> str:
    return f"bollinger_lower_{period}_{_format_param(deviation)}"


class BollingerMiddleBand(DerivedFeature):
    """Middle Bollinger Band: rolling mean of close."""

    def __init__(self, period: int = 20, timeframe: Timeframe = "1d") -> None:
        if period < 1:
            raise ValueError("period must be >= 1")
        self._period = period
        self._timeframe = timeframe
        self._spec = FeatureSpec(
            name=_middle_name(period),
            version="1.0",
            category=FeatureCategory.DERIVED,
            timeframe=timeframe,
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            depends_on=(f"sma_{period}",),
            lookback_required=period,
            warmup_policy=WarmupPolicy.FIXED_LOOKBACK,
        )

    @property
    def spec(self) -> FeatureSpec:
        return self._spec

    def compute(self, df: pd.DataFrame) -> pd.Series:
        self._validate_columns(df, {"close"})
        return RollingMean(window=self._period, timeframe=self._timeframe).compute(df)


class BollingerUpperBand(DerivedFeature):
    """Upper Bollinger Band: SMA + deviation * rolling std."""

    def __init__(
        self,
        period: int = 20,
        deviation: float = 2.0,
        timeframe: Timeframe = "1d",
    ) -> None:
        if period < 2:
            raise ValueError("period must be >= 2")
        if deviation <= 0:
            raise ValueError("deviation must be > 0")
        self._period = period
        self._deviation = deviation
        self._timeframe = timeframe
        self._spec = FeatureSpec(
            name=_upper_name(period, deviation),
            version="1.0",
            category=FeatureCategory.DERIVED,
            timeframe=timeframe,
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            depends_on=(f"sma_{period}", f"rolling_std_{period}"),
            lookback_required=period,
            warmup_policy=WarmupPolicy.FIXED_LOOKBACK,
        )

    @property
    def spec(self) -> FeatureSpec:
        return self._spec

    def compute(self, df: pd.DataFrame) -> pd.Series:
        self._validate_columns(df, {"close"})
        mean = RollingMean(window=self._period, timeframe=self._timeframe).compute(df)
        std = RollingStd(window=self._period, timeframe=self._timeframe).compute(df)
        return mean + (self._deviation * std)


class BollingerLowerBand(DerivedFeature):
    """Lower Bollinger Band: SMA - deviation * rolling std."""

    def __init__(
        self,
        period: int = 20,
        deviation: float = 2.0,
        timeframe: Timeframe = "1d",
    ) -> None:
        if period < 2:
            raise ValueError("period must be >= 2")
        if deviation <= 0:
            raise ValueError("deviation must be > 0")
        self._period = period
        self._deviation = deviation
        self._timeframe = timeframe
        self._spec = FeatureSpec(
            name=_lower_name(period, deviation),
            version="1.0",
            category=FeatureCategory.DERIVED,
            timeframe=timeframe,
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            depends_on=(f"sma_{period}", f"rolling_std_{period}"),
            lookback_required=period,
            warmup_policy=WarmupPolicy.FIXED_LOOKBACK,
        )

    @property
    def spec(self) -> FeatureSpec:
        return self._spec

    def compute(self, df: pd.DataFrame) -> pd.Series:
        self._validate_columns(df, {"close"})
        mean = RollingMean(window=self._period, timeframe=self._timeframe).compute(df)
        std = RollingStd(window=self._period, timeframe=self._timeframe).compute(df)
        return mean - (self._deviation * std)


class BollingerBandWidth(DerivedFeature):
    """Bollinger Band Width as percentage of the middle band."""

    def __init__(
        self,
        period: int = 20,
        deviation: float = 2.0,
        timeframe: Timeframe = "1d",
    ) -> None:
        if period < 2:
            raise ValueError("period must be >= 2")
        if deviation <= 0:
            raise ValueError("deviation must be > 0")
        self._period = period
        self._deviation = deviation
        self._timeframe = timeframe
        self._spec = FeatureSpec(
            name=f"bollinger_width_{period}_{_format_param(deviation)}",
            version="1.0",
            category=FeatureCategory.DERIVED,
            timeframe=timeframe,
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            depends_on=(
                _middle_name(period),
                _upper_name(period, deviation),
                _lower_name(period, deviation),
            ),
            lookback_required=period,
            warmup_policy=WarmupPolicy.FIXED_LOOKBACK,
        )

    @property
    def spec(self) -> FeatureSpec:
        return self._spec

    def compute(self, df: pd.DataFrame) -> pd.Series:
        self._validate_columns(df, {"close"})
        middle = BollingerMiddleBand(period=self._period, timeframe=self._timeframe).compute(df)
        upper = BollingerUpperBand(
            period=self._period,
            deviation=self._deviation,
            timeframe=self._timeframe,
        ).compute(df)
        lower = BollingerLowerBand(
            period=self._period,
            deviation=self._deviation,
            timeframe=self._timeframe,
        ).compute(df)

        width = ((upper - lower) / middle) * 100.0
        return width.where(middle != 0.0)