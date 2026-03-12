"""Base class for composed (derived) feature calculators."""

from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd

from feature_engine.errors import ComputationError
from feature_engine.feature_spec.spec import FeatureSpec


class DerivedFeature(ABC):
    """Abstract base class for derived features built from other signals."""

    @property
    @abstractmethod
    def spec(self) -> FeatureSpec:
        """The FeatureSpec that declares this feature's contract."""
        ...

    @abstractmethod
    def compute(self, df: pd.DataFrame) -> pd.Series:
        """Compute the feature from an aligned market DataFrame."""
        ...

    def _validate_columns(self, df: pd.DataFrame, required: set[str]) -> None:
        """Raise ComputationError if *df* is missing any required columns."""
        missing = required - set(df.columns)
        if missing:
            raise ComputationError(
                f"{self.spec.name}: missing columns {sorted(missing)}"
            )