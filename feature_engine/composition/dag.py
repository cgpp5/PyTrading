"""General execution DAG for FeatureEngine calculators."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from feature_engine.errors import ComputationError
from feature_engine.registry import FeatureRegistry, feature_storage_key

from .validators import build_dependency_graph, topological_sort


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

    def execute(self, market_data: pd.DataFrame, *, include_dependencies: bool = False) -> pd.DataFrame:
        """Execute the DAG in topological order against an aligned OHLCV DataFrame."""
        execution_context = market_data.copy()
        computed_by_name: dict[str, pd.Series] = {}

        for feature_name in self.execution_order:
            feature = self.registry.get(feature_name)
            series = feature.compute(execution_context)

            if not isinstance(series, pd.Series):
                raise ComputationError(f"{feature_name}: compute() must return a pandas Series")
            if not series.index.equals(market_data.index):
                raise ComputationError(f"{feature_name}: result index must match input market data index")

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

    def storage_keys(self) -> dict[str, str]:
        return {
            feature_name: feature_storage_key(self.registry.get(feature_name))
            for feature_name in self.execution_order
        }