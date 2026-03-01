"""Primitive features: rolling statistics (mean, std)."""

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


class RollingMean(PrimitiveFeature):
    """Simple moving average over a rolling window.

    Parametric: *window* sets the number of bars, *column* the source series.
    """

    def __init__(
        self,
        window: int,
        column: str = "close",
        timeframe: Timeframe = "1d",
    ) -> None:
        if window < 1:
            raise ValueError("window must be >= 1")
        self._window = window
        self._column = column
        self._spec = FeatureSpec(
            name=f"sma_{window}",
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
        self._validate_columns(df, {self._column})
        return df[self._column].rolling(self._window).mean()


class RollingStd(PrimitiveFeature):
    """Rolling standard deviation over a window.

    Uses ddof=1 (sample std) by default.
    """

    def __init__(
        self,
        window: int,
        column: str = "close",
        timeframe: Timeframe = "1d",
    ) -> None:
        if window < 2:
            raise ValueError("window must be >= 2 for std")
        self._window = window
        self._column = column
        self._spec = FeatureSpec(
            name=f"rolling_std_{window}",
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
        self._validate_columns(df, {self._column})
        return df[self._column].rolling(self._window).std(ddof=1)
