from __future__ import annotations

from enum import Enum
from typing import Optional

from .enums import AlignmentPolicy


class AvailabilityRule(Enum):
    """Defines when a feature value becomes available (point-in-time)."""
    AT_CLOSE = "at_close"
    NEXT_SESSION = "next_session"
    IMMEDIATE = "immediate"


def validate_availability(
    availability: Optional[AvailabilityRule],
    alignment: AlignmentPolicy,
) -> None:
    """Validate that availability is set when alignment requires it.

    Raises:
        ValueError: If alignment != NONE but availability is None.
    """
    if alignment != AlignmentPolicy.NONE and availability is None:
        raise ValueError(
            "AlignmentPolicy requires an explicit AvailabilityRule"
        )


def is_point_in_time_safe(rule: AvailabilityRule) -> bool:
    """Return True if the rule guarantees no look-ahead bias.

    AT_CLOSE and NEXT_SESSION are safe; IMMEDIATE must be verified
    externally (e.g. for real-time external feeds).
    """
    return rule in (AvailabilityRule.AT_CLOSE, AvailabilityRule.NEXT_SESSION)
