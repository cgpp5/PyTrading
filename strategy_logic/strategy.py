"""Entidad Strategy: composición declarativa de condiciones + mapeo a intenciones.

``Strategy = LogicalGraph + ActionMapping``.

Una estrategia **no es código imperativo**: es una declaración de *cuándo* se
activa (``entry_logic``) y *qué* intención emite (``actions``). No mantiene
estado, no accede a la base de datos ni conoce la UI.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import pandas as pd

from .conditions import EvaluationContext, LogicalGraph
from .intents import IntentSpec, SignalIntent, resolve_funds_pct


@dataclass(frozen=True)
class Strategy:
    """Estrategia declarativa.

    - ``name``: identificador estable (``"dca"``, ``"circuit_breaker"``...).
    - ``version``: versión semántica de la lógica.
    - ``entry_logic``: grafo lógico de activación.
    - ``actions``: intenciones a emitir cuando el grafo evalúa a verdadero.
    """

    name: str
    version: str
    entry_logic: LogicalGraph
    actions: tuple[IntentSpec, ...] = field(default_factory=tuple)

    def evaluate(
        self,
        features: pd.DataFrame,
        params: dict,
        bar_index: int,
        timestamp: object,
    ) -> list[SignalIntent]:
        """Evalúa la estrategia en una barra y devuelve las intenciones emitidas.

        Si el grafo lógico no se activa, devuelve una lista vacía.
        """
        ctx = EvaluationContext(
            features=features,
            params=params,
            bar_index=bar_index,
            timestamp=timestamp,
        )
        if not self.entry_logic.evaluate(ctx):
            return []

        return [
            SignalIntent(
                strategy=self.name,
                action=spec.action,
                funds_pct=resolve_funds_pct(spec, params),
                timestamp=timestamp,
                reason=spec.reason,
                metadata=dict(spec.metadata),
            )
            for spec in self.actions
        ]
