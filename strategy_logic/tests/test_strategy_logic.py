"""Tests para el motor declarativo de StrategyLogic."""

from __future__ import annotations

from datetime import datetime, timezone

import pandas as pd
import pytest

from strategy_logic import (
    EvaluationContext,
    FeatureRef,
    IntentSpec,
    LogicalChain,
    LogicalCondition,
    LogicalGraph,
    Operator,
    ParamRef,
    SignalIntent,
    Strategy,
    StrategyLogic,
    StrategyRegistry,
)


def _ctx(features: pd.DataFrame, params: dict, bar_index: int) -> EvaluationContext:
    return EvaluationContext(
        features=features,
        params=params,
        bar_index=bar_index,
        timestamp=features.index[bar_index],
    )


def _features() -> pd.DataFrame:
    idx = pd.date_range(
        start=datetime(2026, 1, 5, 14, 30, tzinfo=timezone.utc),
        periods=6,
        freq="1h",
    )
    return pd.DataFrame(
        {
            "rsi_14": [30.0, 25.0, 20.0, 45.0, 60.0, 70.0],
            "close": [100.0, 98.0, 95.0, 97.0, 101.0, 105.0],
            "adx_14": [20.0, 22.0, 25.0, 30.0, 35.0, 40.0],
        },
        index=idx,
    )


# ----------------------------------------------------------------------
# Operadores de comparación
# ----------------------------------------------------------------------

def test_comparison_condition_true():
    cond = LogicalCondition(
        id="c1",
        left_operand=FeatureRef("rsi_14"),
        operator=Operator.LT,
        right_operand=ParamRef("threshold"),
    )
    # rsi en barra 0 = 30 < 35 → True
    assert cond.evaluate(_ctx(_features(), {"threshold": 35.0}, 0)) is True
    # rsi en barra 5 = 70 < 35 → False
    assert cond.evaluate(_ctx(_features(), {"threshold": 35.0}, 5)) is False


def test_comparison_with_literal():
    cond = LogicalCondition(
        id="c1",
        left_operand=FeatureRef("rsi_14"),
        operator=Operator.GE,
        right_operand=30.0,
    )
    assert cond.evaluate(_ctx(_features(), {}, 0)) is True   # 30 >= 30
    assert cond.evaluate(_ctx(_features(), {}, 1)) is False  # 25 >= 30


def test_comparison_nan_returns_false():
    df = _features()
    df.iloc[0, df.columns.get_loc("rsi_14")] = float("nan")
    cond = LogicalCondition(
        id="c1",
        left_operand=FeatureRef("rsi_14"),
        operator=Operator.LT,
        right_operand=35.0,
    )
    assert cond.evaluate(_ctx(df, {}, 0)) is False


# ----------------------------------------------------------------------
# Operadores de serie
# ----------------------------------------------------------------------

def test_pct_change_operator():
    # close: 100 → 95 entre barra 0 y 2 → -5%
    cond = LogicalCondition(
        id="c1",
        left_operand=FeatureRef("close"),
        operator=Operator.PCT_CHANGE,
        right_operand=ParamRef("down_pct"),
        params={"lookback": 2, "compare": Operator.LE},
    )
    # pct_change(close, 2, at=2) = ((95-100)/100)*100 = -5.0 <= -4 → True
    assert cond.evaluate(_ctx(_features(), {"down_pct": -4.0}, 2)) is True
    # Umbral más estricto: -5 <= -6 → False
    assert cond.evaluate(_ctx(_features(), {"down_pct": -6.0}, 2)) is False


def test_slope_operator():
    # close sube de 95→97→101→105 (barras 2..5): pendiente positiva
    cond = LogicalCondition(
        id="c1",
        left_operand=FeatureRef("close"),
        operator=Operator.SLOPE,
        right_operand=ParamRef("min_slope"),
        params={"window": 4, "compare": Operator.GT},
    )
    # En barra 5, ventana 4 (barras 2..5): pendiente > 0 → True
    assert cond.evaluate(_ctx(_features(), {"min_slope": 0.0}, 5)) is True
    # Pendiente > 100 → False
    assert cond.evaluate(_ctx(_features(), {"min_slope": 100.0}, 5)) is False


def test_series_operator_insufficient_history_returns_false():
    cond = LogicalCondition(
        id="c1",
        left_operand=FeatureRef("close"),
        operator=Operator.PCT_CHANGE,
        right_operand=-100.0,
        params={"lookback": 5, "compare": Operator.LE},
    )
    # En barra 2 no hay 5 barras de histórico → False (no error)
    assert cond.evaluate(_ctx(_features(), {}, 2)) is False


# ----------------------------------------------------------------------
# LogicalChain AND / OR
# ----------------------------------------------------------------------

def test_chain_and():
    chain = LogicalChain(
        mode="AND",
        nodes=(
            LogicalCondition("a", FeatureRef("rsi_14"), Operator.LT, 30.0),
            LogicalCondition("b", FeatureRef("adx_14"), Operator.GE, 20.0),
        ),
    )
    # Barra 1: rsi=25 < 30 (True) y adx=22 >= 20 (True) → True
    assert chain.evaluate(_ctx(_features(), {}, 1)) is True
    # Barra 4: rsi=60 < 30 (False) → False
    assert chain.evaluate(_ctx(_features(), {}, 4)) is False


def test_chain_or():
    chain = LogicalChain(
        mode="OR",
        nodes=(
            LogicalCondition("a", FeatureRef("rsi_14"), Operator.LT, 30.0),
            LogicalCondition("b", FeatureRef("rsi_14"), Operator.GT, 65.0),
        ),
    )
    # Barra 0: rsi=30 → ni <30 ni >65 → False
    assert chain.evaluate(_ctx(_features(), {}, 0)) is False
    # Barra 5: rsi=70 > 65 → True
    assert chain.evaluate(_ctx(_features(), {}, 5)) is True


def test_nested_chain():
    inner = LogicalChain(
        mode="OR",
        nodes=(
            LogicalCondition("a", FeatureRef("rsi_14"), Operator.LT, 25.0),
            LogicalCondition("b", FeatureRef("rsi_14"), Operator.GT, 65.0),
        ),
    )
    outer = LogicalChain(
        mode="AND",
        nodes=(inner, LogicalCondition("c", FeatureRef("adx_14"), Operator.GE, 30.0)),
    )
    # Barra 5: rsi=70>65 (True) y adx=40>=30 (True) → True
    assert outer.evaluate(_ctx(_features(), {}, 5)) is True
    # Barra 1: rsi=25 no <25 (False) → False
    assert outer.evaluate(_ctx(_features(), {}, 1)) is False


def test_chain_invalid_mode_raises():
    with pytest.raises(ValueError):
        LogicalChain(mode="XOR", nodes=(LogicalCondition("a", 1, Operator.LT, 2),))


def test_chain_empty_raises():
    with pytest.raises(ValueError):
        LogicalChain(mode="AND", nodes=())


# ----------------------------------------------------------------------
# Strategy + intenciones
# ----------------------------------------------------------------------

def _buy_oversold_strategy() -> Strategy:
    cond = LogicalCondition(
        id="rsi_oversold",
        left_operand=FeatureRef("rsi_14"),
        operator=Operator.LT,
        right_operand=ParamRef("oversold_threshold"),
    )
    return Strategy(
        name="buy_oversold",
        version="1.0",
        entry_logic=LogicalGraph(root=LogicalChain(mode="AND", nodes=(cond,))),
        actions=(
            IntentSpec(
                action="BUY",
                funds_pct=ParamRef("funds_pct"),
                reason="RSI below oversold threshold",
                metadata={"indicator": "rsi_14"},
            ),
        ),
    )


def test_strategy_emits_intent_when_active():
    strategy = _buy_oversold_strategy()
    params = {"oversold_threshold": 30.0, "funds_pct": 5.0}

    # Barra 1: rsi=25 < 30 → emite BUY
    intents = strategy.evaluate(_features(), params, bar_index=1, timestamp="t1")
    assert len(intents) == 1
    intent = intents[0]
    assert isinstance(intent, SignalIntent)
    assert intent.strategy == "buy_oversold"
    assert intent.action == "BUY"
    assert intent.funds_pct == 5.0
    assert intent.reason == "RSI below oversold threshold"
    assert intent.metadata == {"indicator": "rsi_14"}


def test_strategy_no_intent_when_inactive():
    strategy = _buy_oversold_strategy()
    params = {"oversold_threshold": 30.0, "funds_pct": 5.0}

    # Barra 4: rsi=60 → no activa → lista vacía
    assert strategy.evaluate(_features(), params, bar_index=4, timestamp="t4") == []


def test_funds_pct_literal():
    cond = LogicalCondition("c", FeatureRef("rsi_14"), Operator.LT, 30.0)
    strategy = Strategy(
        name="s",
        version="1.0",
        entry_logic=LogicalGraph(root=cond),
        actions=(IntentSpec(action="BUY", funds_pct=2.5, reason="r"),),
    )
    intents = strategy.evaluate(_features(), {}, bar_index=1, timestamp="t")
    assert intents[0].funds_pct == 2.5


# ----------------------------------------------------------------------
# Registry + StrategyLogic
# ----------------------------------------------------------------------

def test_registry_register_and_get():
    reg = StrategyRegistry([_buy_oversold_strategy()])
    assert "buy_oversold" in reg
    assert len(reg) == 1
    assert reg.get("buy_oversold").name == "buy_oversold"
    with pytest.raises(KeyError):
        reg.get("nope")


def test_registry_duplicate_raises():
    reg = StrategyRegistry()
    reg.register(_buy_oversold_strategy())
    with pytest.raises(ValueError):
        reg.register(_buy_oversold_strategy())


def test_logic_evaluate_bar_active_filter():
    logic = StrategyLogic(StrategyRegistry([_buy_oversold_strategy()]))
    params = {"buy_oversold": {"oversold_threshold": 30.0, "funds_pct": 5.0}}

    # Barra 1 activa → 1 intención
    intents = logic.evaluate_bar(_features(), params, bar_index=1, timestamp="t1")
    assert len(intents) == 1

    # Estrategia desactivada → 0 intenciones
    intents_off = logic.evaluate_bar(
        _features(), params, bar_index=1, timestamp="t1", active=[]
    )
    assert intents_off == []


def test_logic_evaluate_series_backtest():
    logic = StrategyLogic(StrategyRegistry([_buy_oversold_strategy()]))
    params = {"buy_oversold": {"oversold_threshold": 30.0, "funds_pct": 5.0}}

    intents = logic.evaluate_series(_features(), params)

    # Barras con rsi < 30: índice 1 (25) y 2 (20) → 2 intenciones
    assert len(intents) == 2
    assert all(i.action == "BUY" for i in intents)
    # Orden temporal preservado
    assert [i.timestamp for i in intents] == list(_features().index[1:3])


def test_logic_missing_params_defaults_empty():
    logic = StrategyLogic(StrategyRegistry([_buy_oversold_strategy()]))
    # Sin params para la estrategia → {} → threshold ausente → KeyError en resolve
    # Pero como la condición usa ParamRef, falta el parámetro. Verificamos que
    # al no haber parámetro la evaluación no active (KeyError se propaga).
    with pytest.raises(KeyError):
        logic.evaluate_bar(_features(), {}, bar_index=1, timestamp="t1")
