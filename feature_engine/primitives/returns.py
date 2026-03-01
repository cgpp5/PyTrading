"""Primitive features: simple and logarithmic returns."""

from __future__ import annotations

import numpy as np
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


class SimpleReturns(PrimitiveFeature):
    """Bar-over-bar percentage change of close price.

    Formula: (close[t] - close[t-1]) / close[t-1]
    First row is always NaN (no prior bar).
    """

    def __init__(self, timeframe: Timeframe = "1d") -> None:
        self._spec = FeatureSpec(
            name="returns",
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
        self._validate_columns(df, {"close"})
        return df["close"].pct_change(fill_method=None)


class LogReturns(PrimitiveFeature):
    """Bar-over-bar logarithmic return of close price.

    Formula: ln(close[t] / close[t-1])
    First row is always NaN.
    """

    def __init__(self, timeframe: Timeframe = "1d") -> None:
        self._spec = FeatureSpec(
            name="log_returns",
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
        self._validate_columns(df, {"close"})
        return np.log(df["close"] / df["close"].shift(1))
