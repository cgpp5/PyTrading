from __future__ import annotations

"""Fase 6 — Observabilidad de FeatureEngine.

Valida que el DAG de ejecución emita eventos y métricas sobre
``InMemoryFeatureObservability``: cobertura, latencia, degradación y
dependencias ausentes, sin alterar el resultado del cálculo.
"""

from datetime import datetime, timezone

import pandas as pd
import pytest

from feature_engine.composition.base import DerivedFeature
from feature_engine.engine import FeatureEngine
from feature_engine.errors import ComputationError
from feature_engine.feature_spec.enums import AlignmentPolicy, FeatureCategory
from feature_engine.feature_spec.spec import FeatureSpec
from feature_engine.feature_spec.temporal import AvailabilityRule
from feature_engine.observability import InMemoryFeatureObservability
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


class _HalfCloseFeature(PrimitiveFeature):
    """Devuelve NaN en la mitad de las barras → cobertura 0.5."""

    @property
    def spec(self) -> FeatureSpec:
        return FeatureSpec(
            name="half_close",
            version="1.0",
            category=FeatureCategory.TECHNICAL,
            timeframe="1h",
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
        )

    def compute(self, df: pd.DataFrame) -> pd.Series:
        self._validate_columns(df, {"close"})
        out = df["close"].copy()
        out.iloc[: len(out) // 2] = float("nan")
        return out


class _DependentFeature(DerivedFeature):
    @property
    def spec(self) -> FeatureSpec:
        return FeatureSpec(
            name="close_plus_one",
            version="1.0",
            category=FeatureCategory.DERIVED,
            timeframe="1h",
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            depends_on=("close_copy",),
        )

    def compute(self, df: pd.DataFrame) -> pd.Series:
        self._validate_columns(df, {"close_copy"})
        return df["close_copy"] + 1.0


class _BrokenFeature(DerivedFeature):
    """Falla en compute() por columna ausente → dependencia faltante."""

    @property
    def spec(self) -> FeatureSpec:
        return FeatureSpec(
            name="broken",
            version="1.0",
            category=FeatureCategory.DERIVED,
            timeframe="1h",
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            depends_on=("close_copy",),
        )

    def compute(self, df: pd.DataFrame) -> pd.Series:
        # 'close_copy' existe, pero pedimos una columna que no está.
        self._validate_columns(df, {"nonexistent_column"})
        return df["close_copy"]


def _registry(*features) -> FeatureRegistry:
    return FeatureRegistry(features)


# ----------------------------------------------------------------
# Eventos de cálculo correcto
# ----------------------------------------------------------------

def test_computed_event_records_coverage_and_latency():
    obs = InMemoryFeatureObservability()
    engine = FeatureEngine(_registry(_CloseFeature()))

    result = engine.compute(_ohlcv(), ["close_copy"], observability=obs)

    assert list(result.columns) == ["close_copy"]
    assert result["close_copy"].notna().all()

    computed = [e for e in obs.events if e["type"] == "feature_computed"]
    assert len(computed) == 1
    assert computed[0]["name"] == "close_copy"
    assert computed[0]["coverage"] == 1.0
    assert computed[0]["elapsed_ms"] >= 0.0

    # Sin degradación
    assert obs.degraded == []
    summary = obs.summary()
    assert summary["computed_count"] == 1
    assert summary["degradation_rate"] == 0.0
    assert summary["coverage_by_feature"]["close_copy"] == 1.0
    assert "close_copy" in summary["mean_latency_ms"]


# ----------------------------------------------------------------
# Degradación (cobertura < 1.0)
# ----------------------------------------------------------------

def test_degraded_event_on_partial_coverage():
    obs = InMemoryFeatureObservability()
    engine = FeatureEngine(_registry(_HalfCloseFeature()))

    result = engine.compute(_ohlcv(), ["half_close"], observability=obs)

    # 2 de 4 barras son NaN → cobertura 0.5
    assert result["half_close"].notna().sum() == 2

    degraded = [e for e in obs.events if e["type"] == "feature_degraded"]
    assert len(degraded) == 1
    assert degraded[0]["name"] == "half_close"
    assert degraded[0]["coverage"] == pytest.approx(0.5)
    assert "half_close" in obs.degraded

    summary = obs.summary()
    assert summary["degraded_count"] == 1
    assert summary["degradation_rate"] == pytest.approx(1.0)


# ----------------------------------------------------------------
# Dependencia ausente en compute()
# ----------------------------------------------------------------

def test_missing_dependency_event_and_error_propagates():
    obs = InMemoryFeatureObservability()
    engine = FeatureEngine(_registry(_CloseFeature(), _BrokenFeature()))

    with pytest.raises(ComputationError):
        engine.compute(_ohlcv(), ["broken"], observability=obs)

    missing = [e for e in obs.events if e["type"] == "feature_missing_dependency"]
    assert len(missing) == 1
    assert missing[0]["name"] == "broken"
    assert missing[0]["dependency"] == "nonexistent_column"
    assert obs.missing_dependencies == [
        {"name": "broken", "dependency": "nonexistent_column"}
    ]

    summary = obs.summary()
    assert summary["missing_dependency_count"] == 1


# ----------------------------------------------------------------
# Sin observability → comportamiento inalterado
# ----------------------------------------------------------------

def test_no_observability_keeps_behavior():
    engine = FeatureEngine(_registry(_CloseFeature(), _DependentFeature()))

    result = engine.compute(_ohlcv(), ["close_plus_one"])

    assert list(result.columns) == ["close_plus_one"]
    assert result["close_plus_one"].tolist() == [11.0, 21.0, 31.0, 41.0]


# ----------------------------------------------------------------
# Múltiples features: orden y cobertura por feature
# ----------------------------------------------------------------

def test_multiple_features_summary():
    obs = InMemoryFeatureObservability()
    engine = FeatureEngine(_registry(_CloseFeature(), _HalfCloseFeature()))

    engine.compute(
        _ohlcv(), ["close_copy", "half_close"], observability=obs
    )

    summary = obs.summary()
    assert summary["computed_count"] == 2
    assert summary["degraded_count"] == 1
    assert summary["coverage_by_feature"]["close_copy"] == 1.0
    assert summary["coverage_by_feature"]["half_close"] == pytest.approx(0.5)
    # Tasa de degradación = 1 degradada / 2 calculadas
    assert summary["degradation_rate"] == pytest.approx(0.5)
