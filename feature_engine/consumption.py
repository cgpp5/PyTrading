"""Fase 7 — Interfaz de consumo de FeatureEngine.

Expone features de forma **segura y no ambigua**. El consumidor no puede pedir
algo temporalmente inconsistente:

- :meth:`FeatureConsumer.snapshot` resuelve un único timestamp exacto a una
  única barra (sin interpolación ni aproximación). Si el timestamp no coincide
  con una barra del índice, se lanza :class:`AmbiguousSnapshotError`.
- :meth:`FeatureConsumer.window` devuelve una ventana temporal coherente
  (``start <= end``) para backtesting.

Garantías:
    - Timestamps siempre tz-aware UTC.
    - Valores ``NaN`` se exponen como ``None`` (nunca un float ambiguo).
    - Cada valor lleva una calidad explícita (``ready`` / ``warmup`` /
      ``missing``) derivada del lookback declarado en el :class:`FeatureSpec`.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

import pandas as pd

from feature_engine.engine import FeatureEngine
from feature_engine.errors import AmbiguousSnapshotError, InvalidWindowError
from feature_engine.feature_spec.spec import FeatureSpec


def _to_utc(ts: datetime) -> pd.Timestamp:
    """Convierte un datetime a ``pd.Timestamp`` UTC (exige tz-aware)."""
    if ts.tzinfo is None:
        raise AmbiguousSnapshotError(
            "Timestamps must be timezone-aware; got a naive timestamp."
        )
    return pd.Timestamp(ts).tz_convert("UTC")


def _derive_quality(
    value: float | None,
    position: int,
    spec: FeatureSpec | None,
) -> str:
    """Deriva la calidad de un valor en una posición dada.

    - ``None`` (NaN) → ``missing``.
    - Posición dentro del lookback requerido → ``warmup``.
    - En otro caso → ``ready``.
    """
    if value is None:
        return "missing"
    if spec is not None and spec.lookback_required > 0:
        if position < spec.lookback_required:
            return "warmup"
    return "ready"


@dataclass(frozen=True)
class FeatureSnapshot:
    """Snapshot de features en un único timestamp (una barra exacta)."""

    timestamp: pd.Timestamp
    values: dict[str, Any]
    quality: dict[str, str]

    def get(self, name: str) -> Any:
        return self.values.get(name)


@dataclass(frozen=True)
class FeatureWindow:
    """Ventana temporal de features para backtesting."""

    start: pd.Timestamp
    end: pd.Timestamp
    df: pd.DataFrame

    @property
    def empty(self) -> bool:
        return self.df.empty


class FeatureConsumer:
    """Interfaz de consumo no ambigua sobre un :class:`FeatureEngine`."""

    def __init__(self, engine: FeatureEngine) -> None:
        self._engine = engine

    # ------------------------------------------------------------------
    # Snapshot
    # ------------------------------------------------------------------
    def snapshot(
        self,
        market_data: pd.DataFrame,
        features: tuple[str, ...] | list[str],
        at: datetime,
    ) -> FeatureSnapshot:
        """Devuelve el valor de *features* en la barra exacta de *at*.

        :raises AmbiguousSnapshotError: si *at* no coincide con una barra del
            índice (timestamp naive o entre barras).
        """
        target = _to_utc(at)
        result = self._engine.compute(market_data, list(features))

        index = result.index
        if target not in index:
            raise AmbiguousSnapshotError(
                f"Timestamp {target.isoformat()} does not match any bar in the "
                f"feature index; a snapshot must resolve to exactly one bar."
            )

        position = int(index.get_loc(target))
        row = result.loc[target]

        values: dict[str, Any] = {}
        quality: dict[str, str] = {}
        for name in features:
            raw = row[name]
            value = None if pd.isna(raw) else float(raw)
            spec = self._spec_for(name)
            values[name] = value
            quality[name] = _derive_quality(value, position, spec)

        return FeatureSnapshot(timestamp=target, values=values, quality=quality)

    # ------------------------------------------------------------------
    # Window
    # ------------------------------------------------------------------
    def window(
        self,
        market_data: pd.DataFrame,
        features: tuple[str, ...] | list[str],
        start: datetime,
        end: datetime,
    ) -> FeatureWindow:
        """Devuelve las *features* en la ventana ``[start, end]`` (inclusive).

        :raises InvalidWindowError: si ``start > end`` o los timestamps son naive.
        """
        start_ts = _to_utc(start)
        end_ts = _to_utc(end)
        if start_ts > end_ts:
            raise InvalidWindowError(
                f"Window start {start_ts.isoformat()} is after end "
                f"{end_ts.isoformat()}."
            )

        result = self._engine.compute(market_data, list(features))
        sliced = result.loc[(result.index >= start_ts) & (result.index <= end_ts)]

        return FeatureWindow(start=start_ts, end=end_ts, df=sliced)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _spec_for(self, name: str) -> FeatureSpec | None:
        try:
            feature = self._engine.registry.get(name)
        except Exception:
            return None
        spec = getattr(feature, "spec", None)
        return spec if isinstance(spec, FeatureSpec) else None
