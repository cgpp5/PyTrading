from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from feature_engine.errors import ComputationError
from feature_engine.feature_spec.enums import AlignmentPolicy, FeatureCategory
from feature_engine.feature_spec.temporal import AvailabilityRule
from feature_engine.primitives.external import (
    McClellanOscillator,
    McClellanSummation,
    load_external_csv_series,
)


@pytest.fixture()
def csv_dir(tmp_path: Path) -> Path:
    (tmp_path / "McClellanOsc.csv").write_text(
        "Date,Value\n2007.09.28,37.70000000\n2007.09.29,63.46500000\n",
        encoding="utf-8",
    )
    (tmp_path / "McClellanSumOsc.csv").write_text(
        "Date,Value\n2007.09.28,1000.0\n2007.09.29,1015.5\n",
        encoding="utf-8",
    )
    return tmp_path


def test_load_external_csv_series_parses_expected_shape(csv_dir: Path):
    series = load_external_csv_series("McClellanOsc.csv", csv_dir=csv_dir)

    assert len(series) == 2
    assert series.index[0] == pd.Timestamp("2007-09-28T00:00:00Z")
    assert series.iloc[0] == pytest.approx(37.7)
    assert series.iloc[1] == pytest.approx(63.465)


def test_load_external_csv_series_keeps_last_duplicate(csv_dir: Path):
    (csv_dir / "McClellanOsc.csv").write_text(
        "Date,Value\n2007.09.28,37.7\n2007.09.28,40.0\n",
        encoding="utf-8",
    )

    series = load_external_csv_series("McClellanOsc.csv", csv_dir=csv_dir)

    assert len(series) == 1
    assert series.iloc[0] == pytest.approx(40.0)


def test_load_external_csv_series_missing_file_raises(tmp_path: Path):
    with pytest.raises(ComputationError, match="not found"):
        load_external_csv_series("McClellanOsc.csv", csv_dir=tmp_path)


def test_mcclellan_oscillator_daily_reindex(csv_dir: Path):
    idx = pd.date_range("2007-09-28", periods=3, freq="D", tz="UTC", name="timestamp")
    df = pd.DataFrame(index=idx)

    result = McClellanOscillator(csv_dir=csv_dir).compute(df)

    assert result.iloc[0] == pytest.approx(37.7)
    assert result.iloc[1] == pytest.approx(63.465)
    assert pd.isna(result.iloc[2])
    assert (result.index == df.index).all()


def test_mcclellan_summation_hourly_alignment(csv_dir: Path):
    idx = pd.date_range("2007-09-30 09:30", periods=4, freq="1h", tz="UTC", name="timestamp")
    df = pd.DataFrame(index=idx)

    result = McClellanSummation(timeframe="1h", csv_dir=csv_dir).compute(df)

    assert len(result) == 4
    assert result.notna().all()
    assert result.iloc[0] > 1000.0
    assert result.iloc[-1] == pytest.approx(1015.5)


def test_external_feature_storage_key_is_simple(csv_dir: Path):
    feat = McClellanOscillator(csv_dir=csv_dir)

    assert feat.storage_key == "mcclellan_oscillator"
    assert feat.spec.category == FeatureCategory.EXTERNAL_SERIES
    assert feat.spec.alignment == AlignmentPolicy.LINEAR_INTERPOLATION
    assert feat.spec.availability == AvailabilityRule.NEXT_SESSION