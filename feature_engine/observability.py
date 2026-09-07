"""Fase 6 — Observabilidad de FeatureEngine.

Hace que FeatureEngine sea tan explicable como MarketFeed: saber *qué*
features se calcularon, *cuánto tardaron*, con *qué cobertura* y *cuál es la
tasa de degradación*.

Eventos (uno por feature, en orden de ejecución):
    - ``feature_computed``          → feature calculada correctamente.
    - ``feature_degraded``          → feature calculada con cobertura < 1.0 (NaN).
    - ``feature_missing_dependency``→ una dependencia no estaba disponible.
    - ``feature_skipped``           → feature omitida (modo degradado, sin error).

Métricas (agregadas en :meth:`FeatureObservability.summary`):
    - cobertura por feature,
    - latencia de cálculo por feature,
    - tasa de degradación global.

El módulo es *pull-free*: no accede a datos ni a estado; solo recibe eventos
emitidos por el DAG de ejecución.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class FeatureObservability(ABC):
    """Interfaz de observabilidad para el cálculo de features."""

    # ------------------------------------------------------------
    # Eventos por feature
    # ------------------------------------------------------------
    @abstractmethod
    def record_feature_computed(
        self, name: str, elapsed_ms: float, coverage: float
    ) -> None:
        """Una feature se calculó correctamente.

        :param name: nombre estable de la feature (``spec.name``).
        :param elapsed_ms: latencia de cálculo en milisegundos.
        :param coverage: fracción de valores no-NaN en el resultado (0..1).
        """

    @abstractmethod
    def record_feature_degraded(self, name: str, coverage: float) -> None:
        """Una feature se calculó pero con cobertura degradada (< 1.0)."""

    @abstractmethod
    def record_feature_missing_dependency(
        self, name: str, dependency: str
    ) -> None:
        """Una dependencia requerida por *name* no estaba disponible."""

    @abstractmethod
    def record_feature_skipped(self, name: str, reason: str) -> None:
        """Una feature se omitió sin lanzar error (modo degradado)."""


class InMemoryFeatureObservability(FeatureObservability):
    """Implementación en memoria para tests y uso headless."""

    def __init__(self) -> None:
        self.events: list[dict[str, Any]] = []
        self.coverage_by_feature: dict[str, float] = {}
        self.latencies: dict[str, list[float]] = {}
        self.degraded: list[str] = []
        self.missing_dependencies: list[dict[str, str]] = []
        self.skipped: list[dict[str, str]] = []

    # ------------------------------------------------------------
    # Eventos
    # ------------------------------------------------------------
    def record_feature_computed(
        self, name: str, elapsed_ms: float, coverage: float
    ) -> None:
        self.events.append({
            "type": "feature_computed",
            "name": name,
            "elapsed_ms": elapsed_ms,
            "coverage": coverage,
        })
        self.coverage_by_feature[name] = coverage
        self.latencies.setdefault(name, []).append(elapsed_ms)

    def record_feature_degraded(self, name: str, coverage: float) -> None:
        self.events.append({
            "type": "feature_degraded",
            "name": name,
            "coverage": coverage,
        })
        self.degraded.append(name)

    def record_feature_missing_dependency(
        self, name: str, dependency: str
    ) -> None:
        self.events.append({
            "type": "feature_missing_dependency",
            "name": name,
            "dependency": dependency,
        })
        self.missing_dependencies.append({"name": name, "dependency": dependency})

    def record_feature_skipped(self, name: str, reason: str) -> None:
        self.events.append({
            "type": "feature_skipped",
            "name": name,
            "reason": reason,
        })
        self.skipped.append({"name": name, "reason": reason})

    # ------------------------------------------------------------
    # Métricas agregadas
    # ------------------------------------------------------------
    def summary(self) -> dict[str, Any]:
        """Devuelve un resumen de métricas del último ciclo de cálculo."""
        computed = [e for e in self.events if e["type"] == "feature_computed"]
        computed_count = len(computed)
        degraded_count = len(self.degraded)

        degradation_rate = (
            degraded_count / computed_count if computed_count else 0.0
        )

        mean_latency = {
            name: sum(vals) / len(vals)
            for name, vals in self.latencies.items()
            if vals
        }

        return {
            "computed_count": computed_count,
            "degraded_count": degraded_count,
            "skipped_count": len(self.skipped),
            "missing_dependency_count": len(self.missing_dependencies),
            "degradation_rate": degradation_rate,
            "coverage_by_feature": dict(self.coverage_by_feature),
            "mean_latency_ms": mean_latency,
        }
