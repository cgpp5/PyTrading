"""Derived ATR feature."""

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
from feature_engine.primitives.volatility import TrueRange

from .base import DerivedFeature


class AverageTrueRange(DerivedFeature):
    """Average True Range using Wilder smoothing."""

    def __init__(self, period: int = 14, timeframe: Timeframe = "1d") -> None:
        if period < 1:
            raise ValueError("period must be >= 1")
        self._period = period
        self._timeframe = timeframe
        self._spec = FeatureSpec(
            name=f"atr_{period}",
            version="1.0",
            category=FeatureCategory.DERIVED,
            timeframe=timeframe,
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            depends_on=("true_range",),
            lookback_required=period,
            warmup_policy=WarmupPolicy.FIXED_LOOKBACK,
        )

    @property
    def spec(self) -> FeatureSpec:
        return self._spec

    def compute(self, df: pd.DataFrame) -> pd.Series:
        self._validate_columns(df, {"high", "low", "close"})
        true_range = df["true_range"] if "true_range" in df.columns else TrueRange(self._timeframe).compute(df)
        return true_range.ewm(alpha=1 / self._period, adjust=False, min_periods=self._period).mean().astype("float64")