"""Domain errors for FeatureEngine.

Every error has a clear semantic meaning — no generic exceptions are raised.
"""

from __future__ import annotations


class FeatureEngineError(Exception):
    """Base class for all FeatureEngine errors."""


class FeatureNotRegistered(FeatureEngineError):
    """Raised when a feature name is not found in the registry."""


class MissingDependency(FeatureEngineError):
    """Raised when a required dependency (feature or external source) is unavailable."""


class InvalidAlignment(FeatureEngineError):
    """Raised when a temporal alignment operation is invalid."""


class InsufficientLookback(FeatureEngineError):
    """Raised when there are not enough observations for a feature's lookback."""


class ComputationError(FeatureEngineError):
    """Raised when a feature computation fails due to invalid or missing input data."""
