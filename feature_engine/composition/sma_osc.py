"""Derived SMA oscillator feature."""

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
from feature_engine.primitives.rolling import RollingMean

from .base import DerivedFeature


def _sma_osc_name(period: int) -> str:
    return f"sma_osc_{period}"


class SMAOscillator(DerivedFeature):
    """Percentage distance of close from its simple moving average."""

    def __init__(self, period: int = 20, timeframe: Timeframe = "1d") -> None:
        if period < 1:
            raise ValueError("period must be >= 1")
        self._period = period
        self._timeframe: Timeframe = timeframe
        self._spec = FeatureSpec(
            name=_sma_osc_name(period),
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
        sma_name = f"sma_{self._period}"
        sma = df[sma_name].astype("float64") if sma_name in df.columns else RollingMean(window=self._period, timeframe=self._timeframe).compute(df).astype("float64")
        oscillator = ((df["close"].astype("float64") - sma) / sma) * 100.0
        return oscillator.where(sma != 0.0).astype("float64").rename(None)