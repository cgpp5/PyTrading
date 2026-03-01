"""Base class for primitive (atomic) feature calculators.

A primitive feature:
  - Derives directly from OHLCV market data (one source).
  - Operates over a single window.
  - Has no inter-feature dependencies.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd

from feature_engine.errors import ComputationError
from feature_engine.feature_spec.spec import FeatureSpec

# Canonical OHLCV columns expected in the input DataFrame.
REQUIRED_COLUMNS = {"open", "high", "low", "close", "volume"}


class PrimitiveFeature(ABC):
    """Abstract base class for atomic feature calculators."""

    @property
    @abstractmethod
    def spec(self) -> FeatureSpec:
        """The FeatureSpec that declares this feature's contract."""
        ...

    @abstractmethod
    def compute(self, df: pd.DataFrame) -> pd.Series:
        """Compute the feature from an OHLCV DataFrame.

        Args:
            df: DataFrame with canonical OHLCV columns and DatetimeIndex[UTC].

        Returns:
            Series with same index as *df*, containing the computed values.
            NaN inputs (gap rows) naturally produce NaN outputs.

        Raises:
            ComputationError: If required columns are missing.
        """
        ...

    # ------------------------------------------------------------------
    # Shared helpers
    # ------------------------------------------------------------------

    def _validate_columns(self, df: pd.DataFrame, required: set[str]) -> None:
        """Raise ComputationError if *df* is missing any required columns."""
        missing = required - set(df.columns)
        if missing:
            raise ComputationError(
                f"{self.spec.name}: missing columns {sorted(missing)}"
            )
