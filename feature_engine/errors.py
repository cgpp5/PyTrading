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


class CircularDependency(FeatureEngineError):
    """Raised when the feature dependency graph contains a cycle."""


class InvalidAlignment(FeatureEngineError):
    """Raised when a temporal alignment operation is invalid."""


class InsufficientLookback(FeatureEngineError):
    """Raised when there are not enough observations for a feature's lookback."""


class ComputationError(FeatureEngineError):
    """Raised when a feature computation fails due to invalid or missing input data."""


class AmbiguousSnapshotError(FeatureEngineError):
    """Raised when a snapshot cannot be resolved to exactly one bar.

    A snapshot is *ambiguous* when the requested timestamp does not match a
    bar in the feature index (e.g. a naive timestamp against a UTC index, or a
    timestamp that falls between bars). The consumer must request an exact bar.
    """


class InvalidWindowError(FeatureEngineError):
    """Raised when a temporal window is inconsistent (e.g. start after end)."""
