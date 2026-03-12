"""Derived MACD feature family."""

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
from feature_engine.primitives.rolling import ExponentialMovingAverage

from .base import DerivedFeature


def _macd_apply_to(column: str) -> str:
    return column.replace(".", "_")


def _ema_name(period: int, column: str) -> str:
    return f"ema_{period}_{_macd_apply_to(column)}"


def _macd_line_name(fast: int, slow: int, signal: int, column: str) -> str:
    return f"macd_line_{fast}_{slow}_{signal}_{_macd_apply_to(column)}"


def _macd_signal_name(fast: int, slow: int, signal: int, column: str) -> str:
    return f"macd_signal_{fast}_{slow}_{signal}_{_macd_apply_to(column)}"


def _macd_histogram_name(fast: int, slow: int, signal: int, column: str) -> str:
    return f"macd_histogram_{fast}_{slow}_{signal}_{_macd_apply_to(column)}"


def _validate_macd_params(fast: int, slow: int, signal: int) -> None:
    if fast < 1:
        raise ValueError("fast must be >= 1")
    if slow < 2:
        raise ValueError("slow must be >= 2")
    if signal < 1:
        raise ValueError("signal must be >= 1")
    if fast >= slow:
        raise ValueError("fast must be < slow")


def _resolve_series(df: pd.DataFrame, feature_name: str, fallback: pd.Series) -> pd.Series:
    if feature_name in df.columns:
        return df[feature_name].astype("float64")
    return fallback.astype("float64")


class MACDLine(DerivedFeature):
    """MACD line: fast EMA minus slow EMA."""

    def __init__(
        self,
        fast: int = 12,
        slow: int = 26,
        signal: int = 9,
        column: str = "close",
        timeframe: Timeframe = "1d",
    ) -> None:
        _validate_macd_params(fast, slow, signal)
        self._fast = fast
        self._slow = slow
        self._signal = signal
        self._column = column
        self._timeframe = timeframe
        self._spec = FeatureSpec(
            name=_macd_line_name(fast, slow, signal, column),
            version="1.0",
            category=FeatureCategory.DERIVED,
            timeframe=timeframe,
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            depends_on=(
                _ema_name(fast, column),
                _ema_name(slow, column),
            ),
            lookback_required=slow,
            warmup_policy=WarmupPolicy.FIXED_LOOKBACK,
        )

    @property
    def spec(self) -> FeatureSpec:
        return self._spec

    def compute(self, df: pd.DataFrame) -> pd.Series:
        self._validate_columns(df, {self._column})
        fast_name = _ema_name(self._fast, self._column)
        slow_name = _ema_name(self._slow, self._column)
        fast_ema = _resolve_series(
            df,
            fast_name,
            ExponentialMovingAverage(self._fast, self._column, self._timeframe).compute(df),
        )
        slow_ema = _resolve_series(
            df,
            slow_name,
            ExponentialMovingAverage(self._slow, self._column, self._timeframe).compute(df),
        )
        return (fast_ema - slow_ema).astype("float64")


class MACDSignal(DerivedFeature):
    """MACD signal line: EMA over MACD line."""

    def __init__(
        self,
        fast: int = 12,
        slow: int = 26,
        signal: int = 9,
        column: str = "close",
        timeframe: Timeframe = "1d",
    ) -> None:
        _validate_macd_params(fast, slow, signal)
        self._fast = fast
        self._slow = slow
        self._signal = signal
        self._column = column
        self._timeframe = timeframe
        self._spec = FeatureSpec(
            name=_macd_signal_name(fast, slow, signal, column),
            version="1.0",
            category=FeatureCategory.DERIVED,
            timeframe=timeframe,
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            depends_on=(_macd_line_name(fast, slow, signal, column),),
            lookback_required=slow + signal - 1,
            warmup_policy=WarmupPolicy.FIXED_LOOKBACK,
        )

    @property
    def spec(self) -> FeatureSpec:
        return self._spec

    def compute(self, df: pd.DataFrame) -> pd.Series:
        self._validate_columns(df, {self._column})
        line_name = _macd_line_name(self._fast, self._slow, self._signal, self._column)
        line = _resolve_series(
            df,
            line_name,
            MACDLine(self._fast, self._slow, self._signal, self._column, self._timeframe).compute(df),
        )
        return line.ewm(span=self._signal, adjust=False, min_periods=self._signal).mean().astype("float64")


class MACDHistogram(DerivedFeature):
    """MACD histogram: MACD line minus signal line."""

    def __init__(
        self,
        fast: int = 12,
        slow: int = 26,
        signal: int = 9,
        column: str = "close",
        timeframe: Timeframe = "1d",
    ) -> None:
        _validate_macd_params(fast, slow, signal)
        self._fast = fast
        self._slow = slow
        self._signal = signal
        self._column = column
        self._timeframe = timeframe
        self._spec = FeatureSpec(
            name=_macd_histogram_name(fast, slow, signal, column),
            version="1.0",
            category=FeatureCategory.DERIVED,
            timeframe=timeframe,
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            depends_on=(
                _macd_line_name(fast, slow, signal, column),
                _macd_signal_name(fast, slow, signal, column),
            ),
            lookback_required=slow + signal - 1,
            warmup_policy=WarmupPolicy.FIXED_LOOKBACK,
        )

    @property
    def spec(self) -> FeatureSpec:
        return self._spec

    def compute(self, df: pd.DataFrame) -> pd.Series:
        self._validate_columns(df, {self._column})
        line_name = _macd_line_name(self._fast, self._slow, self._signal, self._column)
        signal_name = _macd_signal_name(self._fast, self._slow, self._signal, self._column)
        line = _resolve_series(
            df,
            line_name,
            MACDLine(self._fast, self._slow, self._signal, self._column, self._timeframe).compute(df),
        )
        signal = _resolve_series(
            df,
            signal_name,
            MACDSignal(self._fast, self._slow, self._signal, self._column, self._timeframe).compute(df),
        )
        return (line - signal).astype("float64")