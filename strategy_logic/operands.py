"""Operandos de las condiciones lógicas de StrategyLogic.

Un operando es lo que una :class:`LogicalCondition` compara. Puede ser:

- :class:`FeatureRef` → referencia a una feature (por nombre) del DataFrame
  de features alineadas.
- :class:`ParamRef` → referencia a un parámetro de estrategia ya resuelto.
- Un literal numérico (``int`` / ``float``).

La distinción explícita evita ambigüedades: un nombre de feature nunca se
confunde con un parámetro ni con un literal.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True)
class FeatureRef:
    """Referencia a una feature por su nombre estable."""

    name: str


@dataclass(frozen=True)
class ParamRef:
    """Referencia a un parámetro de estrategia (clave del dict resuelto)."""

    name: str


# Un operando es una referencia a feature, una referencia a parámetro o un literal.
Operand = Union[FeatureRef, ParamRef, int, float]
