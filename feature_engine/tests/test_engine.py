from __future__ import annotations

from datetime import datetime, timezone

import pandas as pd
import pytest

from feature_engine.composition.base import DerivedFeature
from feature_engine.composition.dag import FeatureExecutionDAG
from feature_engine.composition.validators import build_dependency_graph, topological_sort
from feature_engine.engine import FeatureEngine
from feature_engine.errors import CircularDependency, InvalidAlignment, MissingDependency
from feature_engine.feature_spec.enums import AlignmentPolicy, FeatureCategory
from feature_engine.feature_spec.spec import FeatureSpec
from feature_engine.feature_spec.temporal import AvailabilityRule
from feature_engine.primitives.base import PrimitiveFeature
from feature_engine.registry import FeatureRegistry, feature_storage_key


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


class _AddOneFeature(DerivedFeature):
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


class _DoubleFeature(DerivedFeature):
    @property
    def spec(self) -> FeatureSpec:
        return FeatureSpec(
            name="close_plus_one_times_two",
            version="1.0",
            category=FeatureCategory.DERIVED,
            timeframe="1h",
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            depends_on=("close_plus_one",),
        )

    def compute(self, df: pd.DataFrame) -> pd.Series:
        self._validate_columns(df, {"close_plus_one"})
        return df["close_plus_one"] * 2.0


class _MissingDependencyFeature(DerivedFeature):
    @property
    def spec(self) -> FeatureSpec:
        return FeatureSpec(
            name="missing_dep",
            version="1.0",
            category=FeatureCategory.DERIVED,
            timeframe="1h",
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            depends_on=("not_registered",),
        )

    def compute(self, df: pd.DataFrame) -> pd.Series:
        return df["close"]


class _CycleA(DerivedFeature):
    @property
    def spec(self) -> FeatureSpec:
        return FeatureSpec(
            name="cycle_a",
            version="1.0",
            category=FeatureCategory.DERIVED,
            timeframe="1h",
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            depends_on=("cycle_b",),
        )

    def compute(self, df: pd.DataFrame) -> pd.Series:
        return df["close"]


class _CycleB(DerivedFeature):
    @property
    def spec(self) -> FeatureSpec:
        return FeatureSpec(
            name="cycle_b",
            version="1.0",
            category=FeatureCategory.DERIVED,
            timeframe="1h",
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            depends_on=("cycle_a",),
        )

    def compute(self, df: pd.DataFrame) -> pd.Series:
        return df["close"]


class _DailyBase(PrimitiveFeature):
    @property
    def spec(self) -> FeatureSpec:
        return FeatureSpec(
            name="daily_close_copy",
            version="1.0",
            category=FeatureCategory.TECHNICAL,
            timeframe="1d",
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
        )

    def compute(self, df: pd.DataFrame) -> pd.Series:
        return df["close"]


class _IntradayDerived(DerivedFeature):
    @property
    def spec(self) -> FeatureSpec:
        return FeatureSpec(
            name="intraday_from_daily",
            version="1.0",
            category=FeatureCategory.DERIVED,
            timeframe="1h",
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            depends_on=("daily_close_copy",),
        )

    def compute(self, df: pd.DataFrame) -> pd.Series:
        return df["close"]


def test_registry_registers_and_looks_up_features():
    registry = FeatureRegistry([_CloseFeature(), _AddOneFeature()])
    assert registry.names() == ("close_copy", "close_plus_one")
    assert registry.get("close_copy").spec.version == "1.0"


def test_registry_rejects_duplicate_feature_names():
    registry = FeatureRegistry([_CloseFeature()])
    with pytest.raises(ValueError, match="already registered"):
        registry.register(_CloseFeature())


def test_storage_key_uses_version_by_default():
    assert feature_storage_key(_CloseFeature()) == "close_copy@1.0"


def test_graph_builder_returns_dependencies_and_topological_order():
    registry = FeatureRegistry([_CloseFeature(), _AddOneFeature(), _DoubleFeature()])
    graph = build_dependency_graph(registry, ["close_plus_one_times_two"])
    assert graph == {
        "close_copy": (),
        "close_plus_one": ("close_copy",),
        "close_plus_one_times_two": ("close_plus_one",),
    }
    assert topological_sort(graph) == (
        "close_copy",
        "close_plus_one",
        "close_plus_one_times_two",
    )


def test_graph_builder_rejects_missing_dependencies():
    registry = FeatureRegistry([_MissingDependencyFeature()])
    with pytest.raises(MissingDependency, match="not_registered"):
        build_dependency_graph(registry, ["missing_dep"])


def test_graph_builder_rejects_cycles():
    registry = FeatureRegistry([_CycleA(), _CycleB()])
    with pytest.raises(CircularDependency, match="cycle_a -> cycle_b -> cycle_a"):
        build_dependency_graph(registry, ["cycle_a"])


def test_graph_builder_rejects_timeframe_mismatches():
    registry = FeatureRegistry([_DailyBase(), _IntradayDerived()])
    with pytest.raises(InvalidAlignment, match="mismatched timeframe"):
        build_dependency_graph(registry, ["intraday_from_daily"])


def test_execution_dag_computes_requested_features_only_by_default():
    registry = FeatureRegistry([_CloseFeature(), _AddOneFeature(), _DoubleFeature()])
    dag = FeatureExecutionDAG.build(registry, ["close_plus_one_times_two"])

    result = dag.execute(_ohlcv())

    assert list(result.columns) == ["close_plus_one_times_two"]
    assert result.iloc[0, 0] == pytest.approx(22.0)


def test_execution_dag_can_include_dependencies():
    registry = FeatureRegistry([_CloseFeature(), _AddOneFeature(), _DoubleFeature()])
    dag = FeatureExecutionDAG.build(registry, ["close_plus_one_times_two"])

    result = dag.execute(_ohlcv(), include_dependencies=True)

    assert list(result.columns) == ["close_copy", "close_plus_one", "close_plus_one_times_two"]
    assert result.iloc[0].tolist() == pytest.approx([10.0, 11.0, 22.0])


def test_feature_engine_wraps_registry_and_dag_execution():
    registry = FeatureRegistry([_CloseFeature(), _AddOneFeature(), _DoubleFeature()])
    engine = FeatureEngine(registry)

    result = engine.compute(_ohlcv(), ["close_plus_one"], include_dependencies=True)

    assert list(result.columns) == ["close_copy", "close_plus_one"]
    assert result.iloc[-1].tolist() == pytest.approx([40.0, 41.0])