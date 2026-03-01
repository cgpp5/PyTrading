"""Primitive features: volatility measures."""

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

from .base import PrimitiveFeature


class TrueRange(PrimitiveFeature):
    """True Range: max(high-low, |high-prev_close|, |low-prev_close|).

    First row is NaN (no previous close available).
    """

    def __init__(self, timeframe: Timeframe = "1d") -> None:
        self._spec = FeatureSpec(
            name="true_range",
            version="1.0",
            category=FeatureCategory.TECHNICAL,
            timeframe=timeframe,
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            lookback_required=1,
            warmup_policy=WarmupPolicy.FIXED_LOOKBACK,
        )

    @property
    def spec(self) -> FeatureSpec:
        return self._spec

    def compute(self, df: pd.DataFrame) -> pd.Series:
        self._validate_columns(df, {"high", "low", "close"})
        prev_close = df["close"].shift(1)
        high_low = df["high"] - df["low"]
        high_prev = (df["high"] - prev_close).abs()
        low_prev = (df["low"] - prev_close).abs()
        return pd.concat([high_low, high_prev, low_prev], axis=1).max(axis=1)
