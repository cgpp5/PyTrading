"""trading_ui.ingest — Ingestión perezosa de datos de mercado.

Hace que el backend sea **autosuficiente**: si un ``(symbol, timeframe)``
se pide y todavía no hay datos frescos en ``data_store``, se descargan
OHLCV del proveedor, se calculan las features y se persisten — todo dentro
del proceso del servidor, sin scripts externos.

Es la **única fuente de verdad** para:

  - la lista canónica de calculadoras de features (``build_feature_calculators``),
  - el flujo de descarga + persistencia (``fetch_and_store_symbol``),
  - la comprobación de frescura (``ensure_symbol_data``).

``trading_ui/seed.py`` y el servidor deleguen en este módulo para que las
listas de calculadoras nunca divergan entre rutas de ingesta.
"""

from __future__ import annotations

import math
import threading
from datetime import datetime, timedelta, timezone
from typing import Any

from data_store.core import DataStoreCore
from data_store.market_repo import (
    load_market_data,
    save_features,
    save_market_data,
    save_request_meta,
)
from market_feed.calendar import MarketCalendarResolver
from market_feed.market_feed import MarketFeed, ProviderTier
from market_feed.observability import InMemoryObservability
from market_feed.providers.yfinance import YFinanceProvider

from feature_engine.composition.adx import (
    AverageDirectionalIndex,
    MinusDirectionalIndex,
    PlusDirectionalIndex,
)
from feature_engine.composition.atr import AverageTrueRange
from feature_engine.composition.bollinger import (
    BollingerBandWidth,
    BollingerLowerBand,
    BollingerMiddleBand,
    BollingerUpperBand,
)
from feature_engine.composition.macd import MACDHistogram, MACDLine, MACDSignal
from feature_engine.composition.mogalef import (
    MogalefLowerBand,
    MogalefMiddleBand,
    MogalefUpperBand,
)
from feature_engine.composition.sma_osc import SMAOscillator
from feature_engine.errors import ComputationError
from feature_engine.primitives.external import (
    McClellanOscillator,
    McClellanSummation,
)
from feature_engine.primitives.returns import LogReturns, SimpleReturns
from feature_engine.primitives.rolling import RollingMean, RollingStd
from feature_engine.primitives.rsi import RSI
from feature_engine.primitives.volatility import TrueRange
from feature_engine.primitives.volume import VolumeZScore

# ---------------------------------------------------------------------------
# Configuración
# ---------------------------------------------------------------------------

DEFAULT_CALENDAR = "NYSE"

# Historia a descargar por timeframe.  yfinance limita el histórico
# intradía (~60 días); sólo ``1d`` permite ventanas largas.
_DAYS_BY_TIMEFRAME: dict[str, int] = {
    "1d": 365,
    "4h": 60,
    "1h": 60,
    "15m": 60,
}

# El acceso a yfinance/escritura a sqlite se serializa con un lock de módulo
# para evitar descargas duplicadas simultáneas y escrituras concurrentes.
_lock = threading.Lock()

# MarketFeed compartido, construido de forma perezosa (varias peticiones
# reutilizan el mismo resolver/feed).
_feed: MarketFeed | None = None


# ---------------------------------------------------------------------------
# Calculadoras de features — fuente de verdad canónica
# ---------------------------------------------------------------------------

def _feature_storage_key(feature: Any) -> str:
    """Devuelve la clave de almacenamiento de una calculadora."""
    storage_key = getattr(feature, "storage_key", None)
    if isinstance(storage_key, str):
        return storage_key
    spec = feature.spec
    return f"{spec.name}@{spec.version}"


def build_feature_calculators(timeframe: str) -> list[Any]:
    """Lista canónica de calculadoras de features para un timeframe.

    Unión de las primitivas y composiciones implementadas.  Mantener esta
    lista en un solo lugar evita que ``seed`` y el servidor persistan
    conjuntos distintos de features.
    """
    return [
        # --- primitivas ---
        SimpleReturns(timeframe=timeframe),
        LogReturns(timeframe=timeframe),
        RollingMean(window=20, timeframe=timeframe),
        RollingMean(window=50, timeframe=timeframe),
        RollingStd(window=20, timeframe=timeframe),
        TrueRange(timeframe=timeframe),
        VolumeZScore(window=20, timeframe=timeframe),
        RSI(period=14, timeframe=timeframe),
        # --- composiciones: bandas y osciladores ---
        BollingerMiddleBand(period=20, timeframe=timeframe),
        BollingerUpperBand(period=20, timeframe=timeframe),
        BollingerLowerBand(period=20, timeframe=timeframe),
        BollingerBandWidth(period=20, timeframe=timeframe),
        AverageTrueRange(period=14, timeframe=timeframe),
        PlusDirectionalIndex(period=14, timeframe=timeframe),
        MinusDirectionalIndex(period=14, timeframe=timeframe),
        AverageDirectionalIndex(period=14, timeframe=timeframe),
        MACDLine(timeframe=timeframe),
        MACDSignal(timeframe=timeframe),
        MACDHistogram(timeframe=timeframe),
        SMAOscillator(period=20, timeframe=timeframe),
        MogalefMiddleBand(timeframe=timeframe),
        MogalefUpperBand(timeframe=timeframe),
        MogalefLowerBand(timeframe=timeframe),
        # --- series externas ---
        McClellanOscillator(timeframe=timeframe),
        McClellanSummation(timeframe=timeframe),
    ]


def _compute_and_persist_features(
    conn,
    symbol: str,
    timeframe: str,
    df,
) -> int:
    """Calcula todas las features canónicas sobre ``df`` y las persiste.

    ``save_features`` sobrescribe el JSON ``features`` de cada fila, así que
    primero se acumulan todas las features por timestamp y después se hace
    una sola escritura por fila (igual que hacía ``seed.py``).
    """
    features_by_ts: dict[str, dict[str, dict[str, float | None | str]]] = {}
    saved = 0

    for feature in build_feature_calculators(timeframe):
        feature_key = _feature_storage_key(feature)
        try:
            series = feature.compute(df)
        except ComputationError:
            # Feature no aplicable a esta serie → se omite.
            continue

        for ts, value in series.items():
            is_nan = value is None or (
                isinstance(value, float) and math.isnan(value)
            )
            if is_nan:
                quality = "warmup" if "@" in feature_key else "missing"
                entry = {"value": None, "quality": quality}
            else:
                entry = {"value": float(value), "quality": "ready"}

            features_by_ts.setdefault(ts.isoformat(), {})[feature_key] = entry

    for ts_iso, feat_dict in features_by_ts.items():
        save_features(conn, symbol, timeframe, ts_iso, feat_dict)
        saved += len(feat_dict)

    return saved


# ---------------------------------------------------------------------------
# MarketFeed compartido
# ---------------------------------------------------------------------------

def _get_feed() -> MarketFeed:
    """Construye (una vez) y devuelve el MarketFeed compartido."""
    global _feed
    if _feed is None:
        obs = InMemoryObservability()
        cal = MarketCalendarResolver({}, obs)
        tiers = [ProviderTier(provider=YFinanceProvider(), quality="degraded")]
        _feed = MarketFeed(tiers=tiers, calendar_resolver=cal, observability=obs)
    return _feed


def _register_calendar(symbol: str) -> None:
    """Asegura que un símbolo arbitrario tenga calendario (por defecto NYSE).

    ``MarketCalendarResolver.resolve`` lanza ``ConfigurationError`` para
    símbolos desconocidos, así que hay que registrarlos antes de llamar a
    ``get_ohlcv``.  Asumimos acciones/ETFs estadounidenses (NYSE).
    """
    _get_feed()._cal._symbol_calendar_map.setdefault(symbol, DEFAULT_CALENDAR)


# ---------------------------------------------------------------------------
# Frescura
# ---------------------------------------------------------------------------

def _data_is_fresh(store: DataStoreCore, symbol: str, timeframe: str) -> bool:
    """True si hay datos y el último bar no está desactualizado."""
    conn = store.get_connection()
    try:
        df = load_market_data(conn, symbol, timeframe)
        if df.empty:
            return False
        latest = df.index.max()
    finally:
        conn.close()

    if latest.tzinfo is None:
        latest = latest.tz_localize("UTC")
    else:
        latest = latest.tz_convert("UTC")

    now = datetime.now(timezone.utc)
    age = now - latest

    # Margen para no re-descargar cada vez que se navega: diario permite
    # fin de semana; intradía se refresca antes.
    max_age = timedelta(days=4) if timeframe == "1d" else timedelta(days=2)
    return age <= max_age


# ---------------------------------------------------------------------------
# API pública
# ---------------------------------------------------------------------------

def fetch_and_store_symbol(
    store: DataStoreCore,
    symbol: str,
    timeframe: str,
    start: datetime,
    end: datetime,
) -> dict[str, Any]:
    """Descarga OHLCV, persiste datos + features y devuelve un resumen.

    Idempotente a nivel de fila (``INSERT OR REPLACE``): re-descargar el
    mismo rango no duplica filas.
    """
    _register_calendar(symbol)
    feed = _get_feed()

    md = feed.get_ohlcv(symbol, timeframe, start, end)

    if md.df.empty:
        return {
            "symbol": symbol,
            "timeframe": timeframe,
            "action": "no_data",
            "rows": 0,
            "features": 0,
        }

    conn = store.get_connection()
    try:
        rows = save_market_data(conn, symbol, timeframe, md.df)

        meta_dict = {
            "provider_used": md.meta.provider_used,
            "fallback_used": md.meta.fallback_used,
            "start": md.meta.start.isoformat(),
            "end": md.meta.end.isoformat(),
            "coverage_ratio": md.meta.coverage_ratio,
            "gap_count": md.meta.gap_count,
            "quality": md.meta.quality,
            "notes": md.meta.notes,
        }
        save_request_meta(conn, symbol, timeframe, meta_dict)

        features = _compute_and_persist_features(conn, symbol, timeframe, md.df)
    finally:
        conn.close()

    return {
        "symbol": symbol,
        "timeframe": timeframe,
        "action": "fetched",
        "rows": rows,
        "features": features,
    }


def ensure_symbol_data(
    store: DataStoreCore,
    symbol: str,
    timeframe: str,
    *,
    force: bool = False,
) -> dict[str, Any]:
    """Devuelve datos frescos para ``(symbol, timeframe)``, descargando si falta.

    Si ya hay datos frescos devuelve ``{"action": "cached"}`` sin tocar la
    red.  Si faltan (o están obsoletos), descarga y persiste.  Es el punto de
    entrada que el servidor llama ante cada lectura.
    """
    symbol = (symbol or "").strip().upper()
    timeframe = (timeframe or "").strip().lower()

    with _lock:
        if not force and _data_is_fresh(store, symbol, timeframe):
            return {
                "symbol": symbol,
                "timeframe": timeframe,
                "action": "cached",
            }

        end = datetime.now(timezone.utc)
        days = _DAYS_BY_TIMEFRAME.get(timeframe, _DAYS_BY_TIMEFRAME["1d"])
        start = end - timedelta(days=days)

        return fetch_and_store_symbol(store, symbol, timeframe, start, end)
