"""Primitive features: rolling statistics (mean, std)."""

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


class ExponentialMovingAverage(PrimitiveFeature):
    """Exponential moving average over a source column."""

    def __init__(
        self,
        period: int,
        column: str = "close",
        timeframe: Timeframe = "1d",
    ) -> None:
        if period < 1:
            raise ValueError("period must be >= 1")
        self._period = period
        self._column = column
        self._spec = FeatureSpec(
            name=f"ema_{period}_{column}",
            version="1.0",
            category=FeatureCategory.TECHNICAL,
            timeframe=timeframe,
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            lookback_required=period,
            warmup_policy=WarmupPolicy.FIXED_LOOKBACK,
        )

    @property
    def spec(self) -> FeatureSpec:
        return self._spec

    def compute(self, df: pd.DataFrame) -> pd.Series:
        self._validate_columns(df, {self._column})
        return df[self._column].ewm(span=self._period, adjust=False, min_periods=self._period).mean()


class WilderMovingAverage(PrimitiveFeature):
    """Wilder-style moving average seeded by the first simple average."""

    def __init__(
        self,
        period: int,
        column: str = "close",
        timeframe: Timeframe = "1d",
    ) -> None:
        if period < 1:
            raise ValueError("period must be >= 1")
        self._period = period
        self._column = column
        self._spec = FeatureSpec(
            name=f"wilder_ma_{period}_{column}",
            version="1.0",
            category=FeatureCategory.TECHNICAL,
            timeframe=timeframe,
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            lookback_required=period,
            warmup_policy=WarmupPolicy.FIXED_LOOKBACK,
        )

    @property
    def spec(self) -> FeatureSpec:
        return self._spec

    def compute(self, df: pd.DataFrame) -> pd.Series:
        self._validate_columns(df, {self._column})

        values = df[self._column].astype("float64")
        result = pd.Series(np.nan, index=values.index, dtype="float64")
        seed = values.rolling(window=self._period, min_periods=self._period).mean()

        valid_positions = np.flatnonzero(seed.notna().to_numpy())
        if len(valid_positions) == 0:
            return result

        first_valid_pos = int(valid_positions[0])
        first_valid_label = seed.index[first_valid_pos]
        result.iloc[first_valid_pos] = float(seed.loc[first_valid_label])

        for pos in range(first_valid_pos + 1, len(values)):
            previous_value = result.iloc[pos - 1]
            current_value = values.iloc[pos]
            if pd.isna(previous_value) or pd.isna(current_value):
                continue
            result.iloc[pos] = ((previous_value * (self._period - 1)) + current_value) / self._period

        return result
