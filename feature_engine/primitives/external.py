"""CSV-backed external breadth features."""

from __future__ import annotations

from pathlib import Path
import os
import re

import pandas as pd

from market_feed.timeframes import Timeframe, validate_timeframe

from feature_engine.alignment.aligner import align
from feature_engine.errors import ComputationError
from feature_engine.feature_spec.enums import (
    AlignmentPolicy,
    FeatureCategory,
    InterpolationPolicy,
    WarmupPolicy,
)
from feature_engine.feature_spec.spec import FeatureSpec
from feature_engine.feature_spec.temporal import AvailabilityRule

from .base import PrimitiveFeature


EXTERNAL_CSV_DIR_ENV = "FEATURE_ENGINE_EXTERNAL_CSV_DIR"
DEFAULT_EXTERNAL_CSV_DIR = Path(__file__).resolve().parents[2] / "external_features"
_SIMPLE_DATE_RE = re.compile(r"^\d{4}\.\d{2}\.\d{2}$")


def get_external_csv_dir() -> Path:
    """Return the directory where CSV-backed external series are expected."""
    configured = os.environ.get(EXTERNAL_CSV_DIR_ENV)
    if configured:
        return Path(configured).expanduser().resolve()
    return DEFAULT_EXTERNAL_CSV_DIR


def _parse_dates(raw_dates: pd.Series, csv_path: Path) -> pd.DatetimeIndex:
    raw_dates = raw_dates.astype(str).str.strip()

    if raw_dates.map(lambda value: bool(_SIMPLE_DATE_RE.match(value))).all():
        parsed = pd.to_datetime(raw_dates, format="%Y.%m.%d", utc=True)
    else:
        parsed = pd.to_datetime(raw_dates, utc=True, errors="coerce")

    if parsed.isna().any():
        bad_rows = raw_dates[parsed.isna()].tolist()[:3]
        raise ComputationError(
            f"Invalid date values in {csv_path.name}: {bad_rows}"
        )

    return pd.DatetimeIndex(parsed, name="timestamp")


def load_external_csv_series(filename: str, *, csv_dir: Path | None = None) -> pd.Series:
    """Load a daily external series from a CSV file.

    Expected shape: two columns named Date, Value.
    Dates are typically stored as YYYY.MM.DD.
    """
    csv_path = (csv_dir or get_external_csv_dir()) / filename

    if not csv_path.exists():
        raise ComputationError(
            f"External feature CSV not found: {csv_path}"
        )

    try:
        df = pd.read_csv(csv_path, dtype=str)
    except Exception as exc:
        raise ComputationError(
            f"Failed to read external feature CSV {csv_path.name}: {exc}"
        ) from exc

    if len(df.columns) == 1:
        first_col = str(df.columns[0])
        if "," in first_col:
            split = df.iloc[:, 0].astype(str).str.split(",", n=1, expand=True)
            if split.shape[1] == 2:
                split.columns = [part.strip() for part in first_col.split(",", 1)]
                df = split

    columns = {str(col).strip().lower(): col for col in df.columns}
    if "date" in columns and "value" in columns:
        date_col = columns["date"]
        value_col = columns["value"]
    elif len(df.columns) == 2:
        date_col, value_col = df.columns
    else:
        raise ComputationError(
            f"{csv_path.name} must contain Date and Value columns"
        )

    dates = _parse_dates(df[date_col], csv_path)
    values = pd.to_numeric(df[value_col], errors="coerce")
    if values.isna().any():
        bad_rows = df.loc[values.isna(), value_col].astype(str).tolist()[:3]
        raise ComputationError(
            f"Invalid numeric values in {csv_path.name}: {bad_rows}"
        )

    series = pd.Series(values.astype("float64").to_numpy(), index=dates)
    series = series[~series.index.duplicated(keep="last")].sort_index()
    return series


class CsvExternalFeature(PrimitiveFeature):
    """External feature backed by a daily CSV file."""

    def __init__(
        self,
        *,
        name: str,
        filename: str,
        timeframe: Timeframe = "1d",
        csv_dir: Path | None = None,
    ) -> None:
        validate_timeframe(timeframe)
        self._target_timeframe = timeframe
        self._filename = filename
        self._csv_dir = csv_dir
        self._spec = FeatureSpec(
            name=name,
            version="1.0",
            category=FeatureCategory.EXTERNAL_SERIES,
            timeframe="1d",
            alignment=AlignmentPolicy.LINEAR_INTERPOLATION,
            availability=AvailabilityRule.NEXT_SESSION,
            external_sources=(filename,),
            interpolation=InterpolationPolicy.LINEAR,
            warmup_policy=WarmupPolicy.NONE,
            degrades_on_alignment=True,
        )

    @property
    def spec(self) -> FeatureSpec:
        return self._spec

    @property
    def storage_key(self) -> str:
        """Use a simple feature key for persisted external series."""
        return self.spec.name

    @property
    def csv_path(self) -> Path:
        return (self._csv_dir or get_external_csv_dir()) / self._filename

    def compute(self, df: pd.DataFrame) -> pd.Series:
        if not isinstance(df.index, pd.DatetimeIndex):
            raise ComputationError("External features require a DatetimeIndex")

        source_values = load_external_csv_series(self._filename, csv_dir=self._csv_dir)

        if self._target_timeframe == "1d":
            normalized_index = pd.DatetimeIndex(
                pd.to_datetime(df.index.normalize(), utc=True),
                name=df.index.name,
            )
            result = source_values.reindex(normalized_index)
            result.index = df.index
            return result.astype("float64")

        aligned = align(source_values, self.spec, df.index, self._target_timeframe)
        return aligned.values.astype("float64")


class McClellanOscillator(CsvExternalFeature):
    """McClellan Oscillator loaded from McClellanOsc.csv."""

    def __init__(self, timeframe: Timeframe = "1d", csv_dir: Path | None = None) -> None:
        super().__init__(
            name="mcclellan_oscillator",
            filename="McClellanOsc.csv",
            timeframe=timeframe,
            csv_dir=csv_dir,
        )


class McClellanSummation(CsvExternalFeature):
    """McClellan Summation loaded from McClellanSumOsc.csv."""

    def __init__(self, timeframe: Timeframe = "1d", csv_dir: Path | None = None) -> None:
        super().__init__(
            name="mcclellan_summation",
            filename="McClellanSumOsc.csv",
            timeframe=timeframe,
            csv_dir=csv_dir,
        )