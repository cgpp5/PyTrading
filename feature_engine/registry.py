"""Formal registry for FeatureEngine calculators."""

from __future__ import annotations

from typing import Iterable, Iterator, Protocol

import pandas as pd

from feature_engine.errors import FeatureNotRegistered
from feature_engine.feature_spec.spec import FeatureSpec


class FeatureCalculator(Protocol):
    @property
    def spec(self) -> FeatureSpec:
        ...

    def compute(self, df: pd.DataFrame) -> pd.Series:
        ...


def feature_storage_key(feature: FeatureCalculator) -> str:
    storage_key = getattr(feature, "storage_key", None)
    if isinstance(storage_key, str):
        return storage_key
    return f"{feature.spec.name}@{feature.spec.version}"


class FeatureRegistry:
    """Explicit registry of available feature calculators keyed by spec.name."""

    def __init__(self, features: Iterable[FeatureCalculator] | None = None) -> None:
        self._features: dict[str, FeatureCalculator] = {}
        if features is not None:
            self.register_many(features)

    def register(self, feature: FeatureCalculator) -> None:
        spec = getattr(feature, "spec", None)
        compute = getattr(feature, "compute", None)
        if not isinstance(spec, FeatureSpec) or not callable(compute):
            raise TypeError("Registered objects must expose FeatureSpec 'spec' and callable 'compute'")

        existing = self._features.get(spec.name)
        if existing is not None:
            raise ValueError(f"Feature {spec.name!r} is already registered")

        self._features[spec.name] = feature

    def register_many(self, features: Iterable[FeatureCalculator]) -> None:
        for feature in features:
            self.register(feature)

    def get(self, name: str) -> FeatureCalculator:
        try:
            return self._features[name]
        except KeyError as exc:
            raise FeatureNotRegistered(f"Feature {name!r} is not registered") from exc

    def __contains__(self, name: object) -> bool:
        return isinstance(name, str) and name in self._features

    def __len__(self) -> int:
        return len(self._features)

    def __iter__(self) -> Iterator[FeatureCalculator]:
        return iter(self._features.values())

    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._features))

    def items(self) -> tuple[tuple[str, FeatureCalculator], ...]:
        return tuple((name, self._features[name]) for name in sorted(self._features))