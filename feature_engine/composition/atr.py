"""Derived ATR feature."""

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
from feature_engine.primitives.volatility import TrueRange

from .base import DerivedFeature


class AverageTrueRange(DerivedFeature):
    """Average True Range using Wilder smoothing."""

    def __init__(self, period: int = 14, timeframe: Timeframe = "1d") -> None:
        if period < 1:
            raise ValueError("period must be >= 1")
        self._period = period
        self._timeframe: Timeframe = timeframe
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
        true_range = true_range.astype("float64")

        atr = pd.Series(np.nan, index=true_range.index, dtype="float64")
        seed = true_range.rolling(window=self._period, min_periods=self._period).mean()
        first_valid = seed.first_valid_index()
        if first_valid is None:
            return atr

        valid_positions = np.flatnonzero(seed.notna().to_numpy())
        if len(valid_positions) == 0:
            return atr

        first_valid_pos = int(valid_positions[0])
        atr.iloc[first_valid_pos] = float(seed.loc[first_valid])

        for pos in range(first_valid_pos + 1, len(true_range)):
            previous_atr = atr.iloc[pos - 1]
            current_true_range = true_range.iloc[pos]
            if pd.isna(previous_atr) or pd.isna(current_true_range):
                continue
            atr.iloc[pos] = ((previous_atr * (self._period - 1)) + current_true_range) / self._period

        return atr