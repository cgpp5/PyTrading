"""Condiciones lógicas declarativas de StrategyLogic.

Formaliza el contrato ``Strategy = LogicalGraph + ActionMapping``:

- :class:`LogicalCondition` → átomo lógico puro (una relación booleana).
- :class:`LogicalChain` → composición ``AND`` / ``OR`` (anidable).
- :class:`LogicalGraph` → estructura completa de activación de una estrategia.

La evaluación es **determinista** y **sin estado**: recibe un
:class:`EvaluationContext` (features alineadas + parámetros resueltos + barra
actual) y devuelve ``True`` / ``False``.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Union

import pandas as pd

from .operands import FeatureRef, Operand, ParamRef
from .operators import (
    Operator,
    compare,
    is_finite,
    pct_change,
    slope,
)


# ----------------------------------------------------------------------
# Contexto de evaluación
# ----------------------------------------------------------------------

@dataclass(frozen=True)
class EvaluationContext:
    """Todo lo que una condición necesita para evaluarse en una barra.

    - ``features``: DataFrame de features alineadas (índice = timestamps).
    - ``params``: parámetros de estrategia ya resueltos (dict plano).
    - ``bar_index``: posición de la barra actual dentro de ``features``.
    - ``timestamp``: timestamp de la barra actual.
    """

    features: pd.DataFrame
    params: dict
    bar_index: int
    timestamp: object


# ----------------------------------------------------------------------
# Resolución de operandos
# ----------------------------------------------------------------------

def _resolve_scalar(operand: Operand, ctx: EvaluationContext) -> float:
    """Resuelve un operando a un escalar en la barra actual."""
    if isinstance(operand, FeatureRef):
        return ctx.features[operand.name].iloc[ctx.bar_index]
    if isinstance(operand, ParamRef):
        return ctx.params[operand.name]
    return operand  # literal


def _resolve_series(operand: Operand, ctx: EvaluationContext) -> pd.Series:
    """Resuelve un operando a una serie completa (solo FeatureRef)."""
    if isinstance(operand, FeatureRef):
        return ctx.features[operand.name]
    raise ValueError(
        "Series operators require a FeatureRef left operand, "
        f"got {type(operand).__name__}"
    )


def _parse_compare(value: Union[Operator, str]) -> Operator:
    if isinstance(value, Operator):
        return value
    try:
        return Operator(value)
    except ValueError as exc:
        raise ValueError(f"Unknown comparison operator {value!r}") from exc


# ----------------------------------------------------------------------
# LogicalCondition
# ----------------------------------------------------------------------

@dataclass(frozen=True)
class LogicalCondition:
    """Átomo lógico reutilizable: una relación booleana pura.

    Para operadores de **comparación** (``<``, ``>``, ...):
        - ``left_operand`` / ``right_operand`` se resuelven a escalares en la
          barra actual y se comparan.

    Para operadores de **serie** (``pct_change``, ``slope``):
        - ``left_operand`` debe ser un :class:`FeatureRef` (la serie).
        - ``params`` incluye la ventana (``lookback`` / ``window``) y la
          dirección de comparación (``compare``).
        - ``right_operand`` es el umbral contra el que se compara el valor
          derivado.
    """

    id: str
    left_operand: Operand
    operator: Operator
    right_operand: Operand
    params: dict = field(default_factory=dict)

    def evaluate(self, ctx: EvaluationContext) -> bool:
        if self.operator.is_comparison:
            return self._eval_comparison(ctx)
        return self._eval_series(ctx)

    # -- comparación -------------------------------------------------
    def _eval_comparison(self, ctx: EvaluationContext) -> bool:
        left = _resolve_scalar(self.left_operand, ctx)
        right = _resolve_scalar(self.right_operand, ctx)
        if pd.isna(left) or pd.isna(right):
            return False
        return compare(self.operator, float(left), float(right))

    # -- serie -------------------------------------------------------
    def _eval_series(self, ctx: EvaluationContext) -> bool:
        series = _resolve_series(self.left_operand, ctx)
        threshold = _resolve_scalar(self.right_operand, ctx)
        if pd.isna(threshold):
            return False

        if self.operator is Operator.PCT_CHANGE:
            lookback = int(self.params.get("lookback", 1))
            value = pct_change(series, lookback, ctx.bar_index)
        elif self.operator is Operator.SLOPE:
            window = int(self.params.get("window", 2))
            value = slope(series, window, ctx.bar_index)
        else:  # pragma: no cover
            raise ValueError(f"Unsupported series operator {self.operator.value!r}")

        if not is_finite(value):
            return False

        compare_op = _parse_compare(self.params.get("compare", Operator.LE))
        return compare(compare_op, float(value), float(threshold))


# ----------------------------------------------------------------------
# LogicalChain
# ----------------------------------------------------------------------

@dataclass(frozen=True)
class LogicalChain:
    """Composición lógica ``AND`` / ``OR`` de condiciones o cadenas anidadas."""

    mode: str  # "AND" | "OR"
    nodes: tuple[Union["LogicalCondition", "LogicalChain"], ...]

    def __post_init__(self) -> None:
        if self.mode not in ("AND", "OR"):
            raise ValueError(f"LogicalChain.mode must be 'AND' or 'OR', got {self.mode!r}")
        if not self.nodes:
            raise ValueError("LogicalChain requires at least one node")

    def evaluate(self, ctx: EvaluationContext) -> bool:
        results = (node.evaluate(ctx) for node in self.nodes)
        if self.mode == "AND":
            return all(results)
        return any(results)


# ----------------------------------------------------------------------
# LogicalGraph
# ----------------------------------------------------------------------

@dataclass(frozen=True)
class LogicalGraph:
    """Estructura completa de activación de una estrategia.

    Envuelve un nodo raíz (condición o cadena). Es serializable, editable
    desde UI y reutilizable.
    """

    root: Union[LogicalCondition, LogicalChain]

    def evaluate(self, ctx: EvaluationContext) -> bool:
        return self.root.evaluate(ctx)
