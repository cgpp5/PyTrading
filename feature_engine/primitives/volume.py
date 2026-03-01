"""Primitive features: volume-based measures."""

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


class VolumeZScore(PrimitiveFeature):
    """Z-score of volume relative to its rolling mean/std.

    Formula: (volume - rolling_mean) / rolling_std
    Requires at least *window* bars to produce a non-NaN value.
    """

    def __init__(
        self,
        window: int = 20,
        timeframe: Timeframe = "1d",
    ) -> None:
        if window < 2:
            raise ValueError("window must be >= 2 for z-score")
        self._window = window
        self._spec = FeatureSpec(
            name=f"volume_zscore_{window}",
            version="1.0",
            category=FeatureCategory.TECHNICAL,
            timeframe=timeframe,
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            lookback_required=window,
            warmup_policy=WarmupPolicy.FIXED_LOOKBACK,
        )

    @property
    def spec(self) -> FeatureSpec:
        return self._spec

    def compute(self, df: pd.DataFrame) -> pd.Series:
        self._validate_columns(df, {"volume"})
        vol = df["volume"]
        mean = vol.rolling(self._window).mean()
        std = vol.rolling(self._window).std(ddof=1)
        return (vol - mean) / std
