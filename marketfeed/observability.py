from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


class Observability(Protocol):
    def log_warning(self, event: str, **fields: Any) -> None: ...
    def log_error(self, event: str, **fields: Any) -> None: ...
    def alert_critical(self, event: str, **fields: Any) -> None: ...


@dataclass
class InMemoryObservability:
    warnings: list[tuple[str, dict[str, Any]]]
    errors: list[tuple[str, dict[str, Any]]]
    criticals: list[tuple[str, dict[str, Any]]]

    def __init__(self) -> None:
        self.warnings = []
        self.errors = []
        self.criticals = []

    def log_warning(self, event: str, **fields: Any) -> None:
        self.warnings.append((event, fields))

    def log_error(self, event: str, **fields: Any) -> None:
        self.errors.append((event, fields))

    def alert_critical(self, event: str, **fields: Any) -> None:
        self.criticals.append((event, fields))
