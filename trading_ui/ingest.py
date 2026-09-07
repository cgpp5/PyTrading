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

# Historia por defecto y máxima a descargar por timeframe.
#
#   - Diario (``1d``): yfinance permite décadas de histórico.
#   - ``4h``/``1h``: se derivan/descarga de ``1h`` (límite ~2 años).
#   - ``15m``: yfinance limita ~60 días para datos de 1 minuto/15m.
_DAYS_BY_TIMEFRAME: dict[str, int] = {
    "1d": 365,
    "4h": 60,
    "1h": 60,
    "15m": 60,
}
_MAX_DAYS_BY_TIMEFRAME: dict[str, int] = {
    "1d": 3650,   # hasta 10 años de velas diarias
    "4h": 730,
    "1h": 730,
    "15m": 60,
}

# Si una descarga no devuelve datos (ticker no válido / índice con prefijo
# como ^SPX), no reintentamos contra yfinance hasta pasado este tiempo, para
# no martillear el proveedor ante cada lectura.
_EMPTY_COOLDOWN_SEC = 30.0
_last_empty_fetch: dict[tuple[str, str], float] = {}

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
# Cobertura y frescura
# ---------------------------------------------------------------------------

def _as_utc(ts) -> datetime:
    """Normaliza un timestamp de pandas a UTC con tzinfo."""
    if ts.tzinfo is None:
        return ts.tz_localize("UTC")
    return ts.tz_convert("UTC")


def _cached_extent(store: DataStoreCore, symbol: str, timeframe: str):
    """Devuelve ``(oldest, latest)`` de los datos cacheados o ``None``."""
    conn = store.get_connection()
    try:
        df = load_market_data(conn, symbol, timeframe)
        if df.empty:
            return None
        return df.index.min(), df.index.max()
    finally:
        conn.close()


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
    days: int | None = None,
    force: bool = False,
) -> dict[str, Any]:
    """Asegura ``days`` días de historia para ``(symbol, timeframe)``.

    - ``days=None`` → usa la historia por defecto del timeframe.
    - Descarga si no hay datos, si están obsoletos, o si la cobertura
      cacheada es menor que la pedida (para ampliar el histórico).
    - Los tickers que no devuelven datos se marcan en ``_last_empty_fetch``
      para no martillear al proveedor ante cada lectura.
    """
    symbol = (symbol or "").strip().upper()
    timeframe = (timeframe or "").strip().lower()

    default_days = _DAYS_BY_TIMEFRAME.get(timeframe, 365)
    max_days = _MAX_DAYS_BY_TIMEFRAME.get(timeframe, default_days)
    if days is None:
        days = default_days
    days = max(1, min(int(days), max_days))

    with _lock:
        now = datetime.now(timezone.utc)
        window_start = now - timedelta(days=days)
        key = (symbol, timeframe)

        # Cooldown anti-martilleo: si el último intento de este ticker no dio
        # datos y fue hace poco, servimos lo que haya (normalmente vacío).
        last_empty = _last_empty_fetch.get(key)
        if not force and last_empty is not None and (
            now - last_empty
        ).total_seconds() < _EMPTY_COOLDOWN_SEC:
            return {
                "symbol": symbol,
                "timeframe": timeframe,
                "action": "cooldown",
                "rows": 0,
                "features": 0,
            }

        extent = None if force else _cached_extent(store, symbol, timeframe)

        if extent is not None:
            oldest, latest = _as_utc(extent[0]), _as_utc(extent[1])
            # Cobertura suficiente => tenemos al menos `days` de historia.
            coverage_ok = oldest <= window_start
            # Margen de frescura: diario tolera fin de semana; intradía menos.
            max_age = timedelta(days=4) if timeframe == "1d" else timedelta(days=2)
            fresh = (now - latest) <= max_age
            if coverage_ok and fresh:
                return {
                    "symbol": symbol,
                    "timeframe": timeframe,
                    "action": "cached",
                }

        result = fetch_and_store_symbol(
            store, symbol, timeframe, window_start, now
        )
        if result.get("action") == "no_data":
            _last_empty_fetch[key] = now
        else:
            _last_empty_fetch.pop(key, None)
        return result


def ensure_history_back_to(
    store: DataStoreCore,
    symbol: str,
    timeframe: str,
    start: datetime,
) -> dict[str, Any]:
    """Asegura que el histórico cacheado llegue al menos hasta ``start``.

    Si ya hay datos más antiguos que ``start``, no hace nada.  En caso
    contrario descarga únicamente el tramo más antiguo que falta (desde
    ``start`` hasta el dato más antiguo ya cacheado), calcula y persiste sus
    features, y deja intacto el resto.  Es la pieza que permite cargar más
    historia "hacia la izquierda" según el usuario hace scroll/pan.
    """
    symbol = (symbol or "").strip().upper()
    timeframe = (timeframe or "").strip().lower()

    with _lock:
        now = datetime.now(timezone.utc)
        key = (symbol, timeframe)

        # Cooldown anti-martilleo (símbolos que no devuelven datos).
        last_empty = _last_empty_fetch.get(key)
        if last_empty is not None and (
            now - last_empty
        ).total_seconds() < _EMPTY_COOLDOWN_SEC:
            return {
                "symbol": symbol,
                "timeframe": timeframe,
                "action": "cooldown",
                "rows": 0,
                "features": 0,
            }

        extent = _cached_extent(store, symbol, timeframe)
        target = start.astimezone(timezone.utc)

        if extent is None:
            # Nada cacheado: descarga [start, now].
            result = fetch_and_store_symbol(
                store, symbol, timeframe, target, now
            )
        else:
            oldest = _as_utc(extent[0])
            if oldest <= target:
                return {
                    "symbol": symbol,
                    "timeframe": timeframe,
                    "action": "cached",
                }
            # Falta el tramo [target, oldest): descargar sólo ese trozo.
            result = fetch_and_store_symbol(
                store, symbol, timeframe, target, oldest
            )

        if result.get("action") == "no_data":
            _last_empty_fetch[key] = now
        else:
            _last_empty_fetch.pop(key, None)
        return result
