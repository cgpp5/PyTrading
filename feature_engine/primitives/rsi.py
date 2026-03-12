"""Primitive feature: RSI (Relative Strength Index) — Wilder smoothing."""

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


class RSI(PrimitiveFeature):
    """Relative Strength Index (Wilder smoothing).

    Oscillator bounded [0, 100] measuring relative magnitude of recent
    gains vs losses using Wilder's exponential smoothing (alpha = 1/period).

    RSI = 100 - 100 / (1 + RS)
    RS  = avg_gain / avg_loss
    """

    def __init__(
        self,
        period: int = 14,
        column: str = "close",
        timeframe: Timeframe = "1d",
    ) -> None:
        if period < 1:
            raise ValueError("period must be >= 1")
        self._period = period
        self._column = column
        self._spec = FeatureSpec(
            name=f"rsi_{period}",
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

        delta = df[self._column].diff()
        gain = delta.where(delta > 0, 0.0)
        loss = (-delta).where(delta < 0, 0.0)

        # Preserve NaN where delta is NaN (first bar + gap rows)
        nan_mask = delta.isna()
        gain = gain.where(~nan_mask)
        loss = loss.where(~nan_mask)

        avg_gain = gain.ewm(alpha=1 / self._period, min_periods=self._period, adjust=False).mean()
        avg_loss = loss.ewm(alpha=1 / self._period, min_periods=self._period, adjust=False).mean()

        rs = avg_gain / avg_loss
        rsi = 100.0 - (100.0 / (1.0 + rs))
        return rsi
