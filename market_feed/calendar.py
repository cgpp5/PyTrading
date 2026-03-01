from dataclasses import dataclass
from datetime import datetime
from typing import List

import pandas_market_calendars as mcal

from .errors import ConfigurationError


# ---------------------------------------------------------------------
# Modelo de datos de sesión (Fase 5.2)
# ---------------------------------------------------------------------
@dataclass(frozen=True)
class SessionInfo:
    market_open: datetime
    market_close: datetime
    expected_bars: int
    is_special_session: bool


# ---------------------------------------------------------------------
# Resolver de calendario de mercado
# ---------------------------------------------------------------------
class MarketCalendarResolver:
    def __init__(
        self,
        symbol_calendar_map: dict[str, str],
        observability=None,
    ):
        if symbol_calendar_map is None:
            raise ValueError("symbol_calendar_map must be provided")

        self._symbol_calendar_map = symbol_calendar_map
        self._observability = observability
        self._calendar_cache: dict[str, mcal.MarketCalendar] = {}
        self._standard_duration_cache: dict[str, float] = {}

    # -----------------------------------------------------------------
    # Resolución de calendario por símbolo
    # -----------------------------------------------------------------
    def resolve(self, symbol: str) -> mcal.MarketCalendar:
        if symbol not in self._symbol_calendar_map:
            self._observability.alert_critical(
                "calendar_not_configured",
                symbol=symbol,
            )
            raise ConfigurationError(
                f"No calendar configured for symbol {symbol}"
            )

        cal_name = self._symbol_calendar_map[symbol]

        if cal_name not in self._calendar_cache:
            self._calendar_cache[cal_name] = mcal.get_calendar(cal_name)

        return self._calendar_cache[cal_name]

    # -----------------------------------------------------------------
    # API explícita de sesiones oficiales (Fase 5.2)
    # -----------------------------------------------------------------
    def get_session_info(
        self,
        symbol: str,
        start: datetime,
        end: datetime,
        timeframe: str = "1h",
    ) -> List[SessionInfo]:
        if timeframe != "1h":
            raise ValueError(
                "SessionInfo only supports 1h timeframe"
            )

        calendar = self.resolve(symbol)

        schedule = calendar.schedule(
            start_date=start,
            end_date=end,
        )

        if schedule.empty:
            return []

        cal_name = self._symbol_calendar_map[symbol]

        if cal_name not in self._standard_duration_cache:
            full_schedule = calendar.schedule(
                start_date="2000-01-01",
                end_date="2000-12-31",
            )

            durations = (
                full_schedule["market_close"] - full_schedule["market_open"]
            ).dt.total_seconds()

            self._standard_duration_cache[cal_name] = durations.median()

        standard_duration = self._standard_duration_cache[cal_name]

        sessions: list[SessionInfo] = []

        for _, row in schedule.iterrows():
            market_open = row["market_open"].to_pydatetime()
            market_close = row["market_close"].to_pydatetime()

            duration_seconds = (
                market_close - market_open
            ).total_seconds()

            # Número entero exacto de barras de 1h
            expected_bars = int(duration_seconds // 3600)

            is_special = bool(duration_seconds != standard_duration)

            sessions.append(
                SessionInfo(
                    market_open=market_open,
                    market_close=market_close,
                    expected_bars=expected_bars,
                    is_special_session=is_special,
                )
            )

        return sessions
