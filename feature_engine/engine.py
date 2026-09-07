"""FeatureEngine orchestration over a formal registry and validated DAG."""

from __future__ import annotations

import pandas as pd

from feature_engine.composition.dag import FeatureExecutionDAG
from feature_engine.observability import FeatureObservability
from feature_engine.registry import FeatureRegistry


class FeatureEngine:
    """Compute registered features with validated dependency ordering."""

    def __init__(self, registry: FeatureRegistry) -> None:
        self._registry = registry

    @property
    def registry(self) -> FeatureRegistry:
        return self._registry

    def build_dag(self, requested_features: tuple[str, ...] | list[str]) -> FeatureExecutionDAG:
        return FeatureExecutionDAG.build(self._registry, requested_features)

    def compute(
        self,
        market_data: pd.DataFrame,
        requested_features: tuple[str, ...] | list[str],
        *,
        include_dependencies: bool = False,
        observability: FeatureObservability | None = None,
    ) -> pd.DataFrame:
        dag = self.build_dag(requested_features)
        return dag.execute(
            market_data,
            include_dependencies=include_dependencies,
            observability=observability,
        )