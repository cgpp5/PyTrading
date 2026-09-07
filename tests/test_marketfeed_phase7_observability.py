from __future__ import annotations

"""Fase 7 — Observability real de MarketFeed.

Valida que el orquestador emita eventos estructurados, contadores y métricas
de latencia/calidad sobre `InMemoryObservability` en los tres flujos posibles:
éxito directo, fallback y fallo total de la cadena.
"""

from datetime import datetime, timezone

import pandas as pd

from market_feed.market_feed import MarketFeed, ProviderTier
from market_feed.calendar import MarketCalendarResolver
from market_feed.observability import InMemoryObservability
from market_feed.providers.base import MarketDataProvider
from market_feed.errors import ProviderError


# ----------------------------------------------------------------
# Proveedores dummy
# ----------------------------------------------------------------

class FullSessionProvider(MarketDataProvider):
    """Sesión NYSE completa de 6 barras 1h (2026-03-02, EST)."""

    @property
    def name(self) -> str:
        return "full_provider"

    def fetch_ohlcv(self, symbol, timeframe, start, end):
        idx = pd.date_range(
            start=datetime(2026, 3, 2, 14, 30, tzinfo=timezone.utc),
            periods=6,
            freq="1h",
        )
        return pd.DataFrame(
            {
                "timestamp": idx,
                "open": [100.0, 101.0, 102.0, 103.0, 104.0, 105.0],
                "high": [101.0, 102.0, 103.0, 104.0, 105.0, 106.0],
                "low": [99.0, 100.0, 101.0, 102.0, 103.0, 104.0],
                "close": [101.0, 102.0, 103.0, 104.0, 105.0, 106.0],
                "volume": [1000.0] * 6,
            }
        )


class FailingProvider(MarketDataProvider):
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def fetch_ohlcv(self, *args, **kwargs):
        raise ProviderError(f"{self._name} down")


# ----------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------

def _make_feed(tiers, obs=None):
    obs = obs or InMemoryObservability()
    cal = MarketCalendarResolver(
        symbol_calendar_map={"AAPL": "NYSE"},
        observability=obs,
    )
    feed = MarketFeed(
        tiers=tiers,
        calendar_resolver=cal,
        observability=obs,
    )
    return feed, obs


def _events_of_type(obs, etype):
    return [e for e in obs.events if e["type"] == etype]


# Ventana de un solo día (2026-03-02, NYSE) para que la cobertura sea completa.
START = datetime(2026, 3, 2, tzinfo=timezone.utc)
END = datetime(2026, 3, 2, tzinfo=timezone.utc)


# ----------------------------------------------------------------
# Éxito directo (tier 1 resuelve)
# ----------------------------------------------------------------

def test_success_records_attempt_and_success():
    feed, obs = _make_feed(
        [ProviderTier(provider=FullSessionProvider(), quality="normal")]
    )
    md = feed.get_ohlcv("AAPL", "1h", START, END)

    assert not md.df.empty
    assert md.meta.provider_used == "full_provider"
    assert md.meta.fallback_used is False

    attempts = _events_of_type(obs, "provider_attempt")
    successes = _events_of_type(obs, "provider_success")
    failures = _events_of_type(obs, "provider_failure")

    assert len(attempts) == 1
    assert attempts[0]["provider"] == "full_provider"
    assert attempts[0]["tier"] == 0
    assert len(successes) == 1
    assert successes[0]["provider"] == "full_provider"
    assert len(failures) == 0
    # Sin fallback en el flujo de éxito directo
    assert _events_of_type(obs, "fallback_used") == []
    assert obs.counters.get("fallback", 0) == 0


def test_success_records_latency_and_quality():
    feed, obs = _make_feed(
        [ProviderTier(provider=FullSessionProvider(), quality="normal")]
    )
    md = feed.get_ohlcv("AAPL", "1h", START, END)

    # Latencia por proveedor y total
    assert "provider:full_provider" in obs.latencies
    assert len(obs.latencies["provider:full_provider"]) == 1
    assert obs.latencies["provider:full_provider"][0] >= 0.0
    assert "total" in obs.latencies
    assert len(obs.latencies["total"]) == 1
    assert obs.latencies["total"][0] >= 0.0

    # Calidad registrada con cobertura completa
    assert len(obs.data_quality) == 1
    dq = obs.data_quality[0]
    assert dq["symbol"] == "AAPL"
    assert dq["timeframe"] == "1h"
    assert dq["quality"] == "normal"
    assert dq["coverage_ratio"] == 1.0
    assert dq["gap_count"] == 0


# ----------------------------------------------------------------
# Fallback (tier 1 y 2 fallan, tier 3 resuelve)
# ----------------------------------------------------------------

def test_fallback_records_failures_and_counter():
    feed, obs = _make_feed(
        [
            ProviderTier(provider=FailingProvider("alpaca"), quality="normal"),
            ProviderTier(provider=FailingProvider("tiingo"), quality="normal"),
            ProviderTier(provider=FullSessionProvider(), quality="degraded"),
        ]
    )
    md = feed.get_ohlcv("AAPL", "1h", START, END)

    assert md.meta.provider_used == "full_provider"
    assert md.meta.fallback_used is True
    assert md.meta.extra["attempted_providers"] == [
        "alpaca", "tiingo", "full_provider",
    ]

    attempts = _events_of_type(obs, "provider_attempt")
    failures = _events_of_type(obs, "provider_failure")
    assert len(attempts) == 3
    assert len(failures) == 2
    assert {f["provider"] for f in failures} == {"alpaca", "tiingo"}

    # Contador de fallos de proveedor
    assert obs.counters.get("provider_failure", 0) == 2

    # Evento de fallback + contador
    fallbacks = _events_of_type(obs, "fallback_used")
    assert len(fallbacks) == 1
    assert fallbacks[0]["attempted_providers"] == [
        "alpaca", "tiingo", "full_provider",
    ]
    assert obs.counters.get("fallback", 0) == 1


# ----------------------------------------------------------------
# Fallo total de la cadena
# ----------------------------------------------------------------

def test_all_failed_records_error_and_latency():
    feed, obs = _make_feed(
        [
            ProviderTier(provider=FailingProvider("alpaca"), quality="normal"),
            ProviderTier(provider=FailingProvider("tiingo"), quality="normal"),
        ]
    )
    md = feed.get_ohlcv("AAPL", "1h", START, END)

    assert md.df.empty
    assert md.meta.provider_used == "none"
    assert md.meta.quality == "degraded"
    assert md.meta.notes == "All providers failed"

    # Error estructurado registrado
    assert len(obs.errors) == 1
    event, ctx = obs.errors[0]
    assert event == "all_providers_failed"
    assert ctx["attempted_providers"] == ["alpaca", "tiingo"]
    assert ctx["last_error"] is not None

    # Latencia total registrada aun en el fallo
    assert "total" in obs.latencies
    assert len(obs.latencies["total"]) == 1

    # Sin calidad registrada (no hubo datos)
    assert obs.data_quality == []
    assert obs.counters.get("provider_failure", 0) == 2
