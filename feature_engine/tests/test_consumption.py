from __future__ import annotations

"""Fase 7 — Interfaz de consumo de FeatureEngine.

Valida que :class:`FeatureConsumer` exponga features de forma no ambigua:
snapshot en una barra exacta (con calidad derivada del lookback) y ventana
temporal coherente para backtesting.
"""

from datetime import datetime, timezone

import pandas as pd
import pytest

from feature_engine.consumption import FeatureConsumer
from feature_engine.engine import FeatureEngine
from feature_engine.errors import AmbiguousSnapshotError, InvalidWindowError
from feature_engine.feature_spec.enums import AlignmentPolicy, FeatureCategory
from feature_engine.feature_spec.spec import FeatureSpec
from feature_engine.feature_spec.temporal import AvailabilityRule
from feature_engine.primitives.base import PrimitiveFeature
from feature_engine.registry import FeatureRegistry


def _ohlcv() -> pd.DataFrame:
    idx = pd.date_range(
        start=datetime(2026, 1, 5, 14, 30, tzinfo=timezone.utc),
        periods=4,
        freq="1h",
    )
    return pd.DataFrame(
        {
            "open": [10.0, 20.0, 30.0, 40.0],
            "high": [11.0, 21.0, 31.0, 41.0],
            "low": [9.0, 19.0, 29.0, 39.0],
            "close": [10.0, 20.0, 30.0, 40.0],
            "volume": [100.0, 100.0, 100.0, 100.0],
        },
        index=idx,
    )


class _CloseFeature(PrimitiveFeature):
    """Sin lookback → siempre 'ready' cuando hay valor."""

    @property
    def spec(self) -> FeatureSpec:
        return FeatureSpec(
            name="close_copy",
            version="1.0",
            category=FeatureCategory.TECHNICAL,
            timeframe="1h",
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
        )

    def compute(self, df: pd.DataFrame) -> pd.Series:
        self._validate_columns(df, {"close"})
        return df["close"]


class _WarmupFeature(PrimitiveFeature):
    """lookback_required=2 → las 2 primeras barras son 'warmup'."""

    @property
    def spec(self) -> FeatureSpec:
        from feature_engine.feature_spec.enums import WarmupPolicy

        return FeatureSpec(
            name="warmup_feat",
            version="1.0",
            category=FeatureCategory.TECHNICAL,
            timeframe="1h",
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            lookback_required=2,
            warmup_policy=WarmupPolicy.FIXED_LOOKBACK,
        )

    def compute(self, df: pd.DataFrame) -> pd.Series:
        self._validate_columns(df, {"close"})
        return df["close"] * 2.0


class _GapFeature(PrimitiveFeature):
    """Devuelve NaN en la última barra → 'missing' en el snapshot."""

    @property
    def spec(self) -> FeatureSpec:
        return FeatureSpec(
            name="gap_feat",
            version="1.0",
            category=FeatureCategory.TECHNICAL,
            timeframe="1h",
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
        )

    def compute(self, df: pd.DataFrame) -> pd.Series:
        self._validate_columns(df, {"close"})
        out = df["close"].copy()
        out.iloc[-1] = float("nan")
        return out


def _consumer(*features) -> FeatureConsumer:
    return FeatureConsumer(FeatureEngine(FeatureRegistry(features)))


BARS = [
    datetime(2026, 1, 5, 14, 30, tzinfo=timezone.utc),
    datetime(2026, 1, 5, 15, 30, tzinfo=timezone.utc),
    datetime(2026, 1, 5, 16, 30, tzinfo=timezone.utc),
    datetime(2026, 1, 5, 17, 30, tzinfo=timezone.utc),
]


# ----------------------------------------------------------------
# Snapshot: barra exacta + calidad
# ----------------------------------------------------------------

def test_snapshot_exact_bar_and_quality():
    consumer = _consumer(_CloseFeature())
    snap = consumer.snapshot(_ohlcv(), ["close_copy"], at=BARS[2])

    assert snap.timestamp == pd.Timestamp(BARS[2])
    assert snap.values["close_copy"] == 30.0
    assert snap.quality["close_copy"] == "ready"


def test_snapshot_warmup_quality_by_lookback():
    consumer = _consumer(_WarmupFeature())

    # Posición 0 y 1 → warmup (lookback_required=2)
    assert consumer.snapshot(_ohlcv(), ["warmup_feat"], at=BARS[0]).quality["warmup_feat"] == "warmup"
    assert consumer.snapshot(_ohlcv(), ["warmup_feat"], at=BARS[1]).quality["warmup_feat"] == "warmup"
    # Posición 2 → ready
    assert consumer.snapshot(_ohlcv(), ["warmup_feat"], at=BARS[2]).quality["warmup_feat"] == "ready"


def test_snapshot_missing_value_is_none():
    consumer = _consumer(_GapFeature())
    snap = consumer.snapshot(_ohlcv(), ["gap_feat"], at=BARS[3])

    assert snap.values["gap_feat"] is None
    assert snap.quality["gap_feat"] == "missing"


# ----------------------------------------------------------------
# Snapshot: ambigüedad → error
# ----------------------------------------------------------------

def test_snapshot_between_bars_raises():
    consumer = _consumer(_CloseFeature())
    between = datetime(2026, 1, 5, 15, 0, tzinfo=timezone.utc)  # entre 14:30 y 15:30

    with pytest.raises(AmbiguousSnapshotError):
        consumer.snapshot(_ohlcv(), ["close_copy"], at=between)


def test_snapshot_naive_timestamp_raises():
    consumer = _consumer(_CloseFeature())
    naive = datetime(2026, 1, 5, 14, 30)  # sin tz

    with pytest.raises(AmbiguousSnapshotError):
        consumer.snapshot(_ohlcv(), ["close_copy"], at=naive)


# ----------------------------------------------------------------
# Window: backtesting
# ----------------------------------------------------------------

def test_window_slices_inclusive_range():
    consumer = _consumer(_CloseFeature())
    win = consumer.window(_ohlcv(), ["close_copy"], start=BARS[1], end=BARS[2])

    assert win.start == pd.Timestamp(BARS[1])
    assert win.end == pd.Timestamp(BARS[2])
    assert list(win.df.index) == [pd.Timestamp(BARS[1]), pd.Timestamp(BARS[2])]
    assert win.df["close_copy"].tolist() == [20.0, 30.0]
    assert not win.empty


def test_window_empty_when_no_bars_in_range():
    consumer = _consumer(_CloseFeature())
    win = consumer.window(
        _ohlcv(), ["close_copy"],
        start=datetime(2026, 1, 6, tzinfo=timezone.utc),
        end=datetime(2026, 1, 7, tzinfo=timezone.utc),
    )
    assert win.empty


def test_window_start_after_end_raises():
    consumer = _consumer(_CloseFeature())
    with pytest.raises(InvalidWindowError):
        consumer.window(
            _ohlcv(), ["close_copy"],
            start=BARS[2], end=BARS[0],
        )
