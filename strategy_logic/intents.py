"""Intenciones de señal de StrategyLogic.

El output exclusivo del módulo es :class:`SignalIntent`: una **intención
abstracta**, no una orden. La traducción a órdenes reales es responsabilidad
de capas posteriores (``SignalEngine``, ``ExecutionController``).

:class:`IntentSpec` define *qué* intención emite una estrategia cuando su
grafo lógico evalúa a verdadero (el mapeo ``LogicalGraph → intenciones``).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .operands import FeatureRef, Operand, ParamRef


@dataclass(frozen=True)
class IntentSpec:
    """Definición de una intención a emitir (parte del ActionMapping).

    - ``action``: tipo de intención (``BUY``, ``SELL``, ...).
    - ``funds_pct``: tamaño relativo; literal o :class:`ParamRef` resuelto en
      tiempo de evaluación.
    - ``reason``: explicación semántica.
    - ``metadata``: información adicional no operativa.
    """

    action: str
    funds_pct: Operand
    reason: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class SignalIntent:
    """Intención abstracta emitida por una estrategia.

    Invariantes: no implica ejecución, no tiene prioridad, no conoce otras
    señales.
    """

    strategy: str
    action: str
    funds_pct: float
    timestamp: object
    reason: str
    metadata: dict[str, Any] = field(default_factory=dict)


def resolve_funds_pct(spec: IntentSpec, params: dict) -> float:
    """Resuelve el tamaño de una intención contra los parámetros resueltos."""
    value = spec.funds_pct
    if isinstance(value, ParamRef):
        value = params[value.name]
    if isinstance(value, FeatureRef):
        raise ValueError("funds_pct cannot reference a feature; use a literal or ParamRef")
    return float(value)
