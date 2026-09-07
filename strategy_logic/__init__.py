"""StrategyLogic — motor declarativo de evaluación lógica.

Consume features alineadas (producidas por FeatureEngine) y parámetros ya
resueltos, y emite **intenciones abstractas** (:class:`SignalIntent`). No
ejecuta órdenes, no gestiona estado transversal ni accede a la base de datos.

Uso mínimo::

    from strategy_logic import (
        StrategyLogic, StrategyRegistry, Strategy, LogicalGraph,
        LogicalChain, LogicalCondition, IntentSpec, FeatureRef, ParamRef,
        Operator,
    )

    cond = LogicalCondition(
        id="rsi_oversold",
        left_operand=FeatureRef("rsi_14"),
        operator=Operator.LT,
        right_operand=ParamRef("oversold_threshold"),
    )
    strategy = Strategy(
        name="buy_oversold",
        version="1.0",
        entry_logic=LogicalGraph(root=LogicalChain(mode="AND", nodes=(cond,))),
        actions=(IntentSpec(action="BUY", funds_pct=ParamRef("funds_pct"), reason="RSI oversold"),),
    )
    logic = StrategyLogic(StrategyRegistry([strategy]))
    intents = logic.evaluate_bar(features, {"buy_oversold": {...}}, bar_index, ts)
"""

from __future__ import annotations

from .conditions import (
    EvaluationContext,
    LogicalChain,
    LogicalCondition,
    LogicalGraph,
)
from .engine import StrategyLogic, StrategyRegistry
from .intents import IntentSpec, SignalIntent, resolve_funds_pct
from .operands import FeatureRef, Operand, ParamRef
from .operators import Operator, compare, pct_change, slope
from .strategy import Strategy

__all__ = [
    "EvaluationContext",
    "LogicalChain",
    "LogicalCondition",
    "LogicalGraph",
    "StrategyLogic",
    "StrategyRegistry",
    "Strategy",
    "IntentSpec",
    "SignalIntent",
    "resolve_funds_pct",
    "FeatureRef",
    "Operand",
    "ParamRef",
    "Operator",
    "compare",
    "pct_change",
    "slope",
]
