from __future__ import annotations

from enum import Enum


class FeatureQuality(Enum):
    """Quality state of a feature value at a given point in time."""
    READY = "ready"
    WARMUP = "warmup"
    DEGRADED = "degraded"
    MISSING = "missing"


# Allowed state transitions: from_state -> {valid next states}
VALID_TRANSITIONS: dict[FeatureQuality, frozenset[FeatureQuality]] = {
    FeatureQuality.MISSING: frozenset({
        FeatureQuality.WARMUP,
        FeatureQuality.DEGRADED,
    }),
    FeatureQuality.WARMUP: frozenset({
        FeatureQuality.READY,
        FeatureQuality.DEGRADED,
        FeatureQuality.MISSING,
    }),
    FeatureQuality.READY: frozenset({
        FeatureQuality.DEGRADED,
        FeatureQuality.MISSING,
    }),
    FeatureQuality.DEGRADED: frozenset({
        FeatureQuality.READY,
        FeatureQuality.MISSING,
    }),
}


def can_transition(
    from_state: FeatureQuality,
    to_state: FeatureQuality,
) -> bool:
    """Check whether a quality transition is valid."""
    if from_state == to_state:
        return True
    return to_state in VALID_TRANSITIONS.get(from_state, frozenset())
