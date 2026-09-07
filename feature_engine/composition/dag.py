"""General execution DAG for FeatureEngine calculators."""

from __future__ import annotations

import re
import time
from dataclasses import dataclass

import pandas as pd

from feature_engine.errors import ComputationError
from feature_engine.observability import FeatureObservability
from feature_engine.registry import FeatureRegistry, feature_storage_key

from .validators import build_dependency_graph, topological_sort

_MISSING_COLUMNS_RE = re.compile(r"missing columns \[(?P<cols>[^\]]*)\]")


@dataclass(frozen=True)
class FeatureExecutionDAG:
    registry: FeatureRegistry
    requested_features: tuple[str, ...]
    graph: dict[str, tuple[str, ...]]
    execution_order: tuple[str, ...]

    @classmethod
    def build(
        cls,
        registry: FeatureRegistry,
        requested_features: tuple[str, ...] | list[str],
    ) -> "FeatureExecutionDAG":
        requested = tuple(requested_features)
        graph = build_dependency_graph(registry, requested)
        execution_order = topological_sort(graph)
        return cls(
            registry=registry,
            requested_features=requested,
            graph=graph,
            execution_order=execution_order,
        )

    def execute(
        self,
        market_data: pd.DataFrame,
        *,
        include_dependencies: bool = False,
        observability: FeatureObservability | None = None,
    ) -> pd.DataFrame:
        """Execute the DAG in topological order against an aligned OHLCV DataFrame.

        When *observability* is provided, per-feature events and metrics are
        emitted (Fase 6). Behavior is unchanged when it is ``None``.
        """
        execution_context = market_data.copy()
        computed_by_name: dict[str, pd.Series] = {}

        for feature_name in self.execution_order:
            feature = self.registry.get(feature_name)

            start = time.perf_counter()
            try:
                series = feature.compute(execution_context)
            except ComputationError as exc:
                if observability is not None:
                    dependency = self._extract_missing_dependency(str(exc))
                    if dependency is not None:
                        observability.record_feature_missing_dependency(
                            feature_name, dependency
                        )
                raise
            elapsed_ms = (time.perf_counter() - start) * 1000

            if not isinstance(series, pd.Series):
                raise ComputationError(f"{feature_name}: compute() must return a pandas Series")
            if not series.index.equals(market_data.index):
                raise ComputationError(f"{feature_name}: result index must match input market data index")

            if observability is not None:
                coverage = float(series.notna().mean()) if len(series) else 0.0
                observability.record_feature_computed(
                    feature_name, elapsed_ms, coverage
                )
                if coverage < 1.0:
                    observability.record_feature_degraded(feature_name, coverage)

            computed_by_name[feature_name] = series
            execution_context[feature_name] = series

        if include_dependencies:
            selected_names = self.execution_order
        else:
            selected_names = self.requested_features

        result = pd.DataFrame(index=market_data.index)
        for feature_name in selected_names:
            result[feature_name] = computed_by_name[feature_name]
        return result

    @staticmethod
    def _extract_missing_dependency(error_message: str) -> str | None:
        """Extrae el nombre de la primera columna/feature faltante de un error.

        Devuelve ``None`` si el mensaje no corresponde a una dependencia
        ausente (p. ej. un error de índice o de tipo).
        """
        match = _MISSING_COLUMNS_RE.search(error_message)
        if not match:
            return None
        cols = [c.strip().strip("'\"") for c in match.group("cols").split(",")]
        cols = [c for c in cols if c]
        return cols[0] if cols else None

    def storage_keys(self) -> dict[str, str]:
        return {
            feature_name: feature_storage_key(self.registry.get(feature_name))
            for feature_name in self.execution_order
        }