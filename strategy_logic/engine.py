"""Motor de StrategyLogic: registry de estrategias + evaluación.

``StrategyLogic`` actúa como **registry**, no como clase monolítica:

- Las estrategias se registran explícitamente.
- El motor itera sobre las estrategias *activas*.
- Cada estrategia se evalúa de forma aislada y determinista.

El motor **no accede a DataStore**: recibe features alineadas y parámetros ya
resueltos (``params_by_strategy``) inyectados por el orquestador superior.
"""

from __future__ import annotations

from typing import Iterable

import pandas as pd

from .intents import SignalIntent
from .strategy import Strategy


class StrategyRegistry:
    """Registry explícito de estrategias claveadas por ``name``."""

    def __init__(self, strategies: Iterable[Strategy] | None = None) -> None:
        self._strategies: dict[str, Strategy] = {}
        if strategies is not None:
            self.register_many(strategies)

    def register(self, strategy: Strategy) -> None:
        if not isinstance(strategy, Strategy):
            raise TypeError("Only Strategy instances can be registered")
        if strategy.name in self._strategies:
            raise ValueError(f"Strategy {strategy.name!r} is already registered")
        self._strategies[strategy.name] = strategy

    def register_many(self, strategies: Iterable[Strategy]) -> None:
        for strategy in strategies:
            self.register(strategy)

    def get(self, name: str) -> Strategy:
        try:
            return self._strategies[name]
        except KeyError as exc:
            raise KeyError(f"Strategy {name!r} is not registered") from exc

    def __contains__(self, name: object) -> bool:
        return isinstance(name, str) and name in self._strategies

    def __len__(self) -> int:
        return len(self._strategies)

    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._strategies))

    def active(self, active_names: Iterable[str] | None = None) -> list[Strategy]:
        """Devuelve las estrategias activas en orden determinista.

        Si *active_names* es ``None``, todas las registradas están activas.
        """
        if active_names is None:
            return [self._strategies[name] for name in self.names()]
        wanted = set(active_names)
        return [self._strategies[name] for name in self.names() if name in wanted]


class StrategyLogic:
    """Orquestador de evaluación de estrategias registradas."""

    def __init__(self, registry: StrategyRegistry) -> None:
        self._registry = registry

    @property
    def registry(self) -> StrategyRegistry:
        return self._registry

    def evaluate_bar(
        self,
        features: pd.DataFrame,
        params_by_strategy: dict[str, dict],
        bar_index: int,
        timestamp: object,
        active: Iterable[str] | None = None,
    ) -> list[SignalIntent]:
        """Evalúa todas las estrategias activas en una barra.

        :param features: DataFrame de features alineadas (índice = timestamps).
        :param params_by_strategy: parámetros resueltos por estrategia
            (``{name: {...}}``). Las estrategias sin entrada usan ``{}``.
        :param bar_index: posición de la barra actual.
        :param timestamp: timestamp de la barra actual.
        :param active: nombres de estrategias activas (``None`` = todas).
        :returns: lista de intenciones emitidas (puede ser vacía).
        """
        intents: list[SignalIntent] = []
        for strategy in self._registry.active(active):
            params = params_by_strategy.get(strategy.name, {})
            intents.extend(
                strategy.evaluate(features, params, bar_index, timestamp)
            )
        return intents

    def evaluate_series(
        self,
        features: pd.DataFrame,
        params_by_strategy: dict[str, dict],
        active: Iterable[str] | None = None,
    ) -> list[SignalIntent]:
        """Evalúa las estrategias activas sobre todas las barras.

        Útil para backtesting: recorre el índice de *features* y recoge todas
        las intenciones emitidas, en orden temporal.
        """
        intents: list[SignalIntent] = []
        for bar_index in range(len(features)):
            timestamp = features.index[bar_index]
            intents.extend(
                self.evaluate_bar(
                    features, params_by_strategy, bar_index, timestamp, active
                )
            )
        return intents
