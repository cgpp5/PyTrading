from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Sequence

from .errors import ConfigurationError
from .observability import Observability


@dataclass(frozen=True)
class MarketCalendar:
    name: str

    def expected_bars(self, timeframe: str, start: datetime, end: datetime) -> Sequence[datetime]:
        # Fase 0: stub. En Fase 5 se integra calendario real y generación de barras.
        return []


class MarketCalendarResolver:
    def __init__(self, symbol_calendar_map: dict[str, str], observability: Observability):
        self._map = dict(symbol_calendar_map)
        self._obs = observability

    def resolve(self, symbol: str) -> MarketCalendar:
        cal = self._map.get(symbol)
        if not cal:
            self._obs.alert_critical("calendar_not_configured", symbol=symbol)
            raise ConfigurationError(f"No calendar configured for symbol={symbol}")
        return MarketCalendar(name=cal)
