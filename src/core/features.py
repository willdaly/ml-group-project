"""Feature preparation and target helpers for NSL-KDD models."""

from __future__ import annotations

from typing import Any

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.core.data_loader import FEATURE_COLUMNS

TARGET_COLUMN = "label"
METADATA_COLUMNS = ("difficulty", "difficulty_level")
CATEGORICAL_COLUMNS = ["protocol_type", "service", "flag"]

ATTACK_CATEGORY_MAP = {
    "normal": "Normal",
    "back": "DoS",
    "land": "DoS",
    "neptune": "DoS",
    "pod": "DoS",
    "smurf": "DoS",
    "teardrop": "DoS",
    "apache2": "DoS",
    "mailbomb": "DoS",
    "processtable": "DoS",
    "udpstorm": "DoS",
    "ipsweep": "Probe",
    "nmap": "Probe",
    "portsweep": "Probe",
    "satan": "Probe",
    "mscan": "Probe",
    "saint": "Probe",
    "ftp_write": "R2L",
    "guess_passwd": "R2L",
    "imap": "R2L",
    "multihop": "R2L",
    "phf": "R2L",
    "spy": "R2L",
    "warezclient": "R2L",
    "warezmaster": "R2L",
    "httptunnel": "R2L",
    "named": "R2L",
    "sendmail": "R2L",
    "snmpgetattack": "R2L",
    "snmpguess": "R2L",
    "worm": "R2L",
    "xlock": "R2L",
    "xsnoop": "R2L",
    "buffer_overflow": "U2R",
    "loadmodule": "U2R",
    "perl": "U2R",
    "rootkit": "U2R",
    "ps": "U2R",
    "sqlattack": "U2R",
    "xterm": "U2R",
}

DEFAULT_RECORD_VALUES: dict[str, Any] = {
    "protocol_type": "tcp",
    "service": "http",
    "flag": "SF",
}


def map_attack_category(label_series: pd.Series) -> pd.Series:
    """Map fine-grained attack labels to the five standard NSL-KDD categories."""
    return label_series.astype(str).str.lower().str.strip().map(ATTACK_CATEGORY_MAP).fillna("Unknown")


def binary_target(series: pd.Series) -> pd.Series:
    return (series.astype(str).str.lower().str.strip() != "normal").astype(int)


def multiclass_target(series: pd.Series) -> pd.Series:
    return map_attack_category(series)


def split_features(frame: pd.DataFrame, target: str = "binary") -> tuple[pd.DataFrame, pd.Series]:
    drop_cols = [TARGET_COLUMN, *METADATA_COLUMNS]
    features = frame.drop(columns=drop_cols, errors="ignore")
    if target == "binary":
        y = binary_target(frame[TARGET_COLUMN])
    elif target == "multiclass":
        y = multiclass_target(frame[TARGET_COLUMN])
    else:
        raise ValueError("target must be either 'binary' or 'multiclass'")
    return features, y


def build_preprocessor(features: pd.DataFrame) -> ColumnTransformer:
    categorical_columns = [c for c in CATEGORICAL_COLUMNS if c in features.columns]
    numeric_columns = [c for c in features.columns if c not in categorical_columns]

    return ColumnTransformer(
        transformers=[
            (
                "categorical",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="most_frequent")),
                        ("encoder", OneHotEncoder(handle_unknown="ignore")),
                    ]
                ),
                categorical_columns,
            ),
            (
                "numeric",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="median")),
                        ("scaler", StandardScaler()),
                    ]
                ),
                numeric_columns,
            ),
        ],
        remainder="drop",
    )


def get_feature_names(preprocessor: ColumnTransformer) -> list[str]:
    """Extract feature names after preprocessing."""
    names = []
    for name, transformer, columns in preprocessor.transformers_:
        if name == "remainder":
            continue
        if name == "categorical":
            encoder = transformer.named_steps["encoder"]
            if hasattr(encoder, "get_feature_names_out"):
                names.extend(encoder.get_feature_names_out(columns).tolist())
            else:
                names.extend([f"{col}_enc" for col in columns])
        else:
            names.extend(columns)
    return names


def ensure_feature_frame(records: dict[str, Any] | list[dict[str, Any]]) -> pd.DataFrame:
    rows = records if isinstance(records, list) else [records]
    normalized_rows: list[dict[str, Any]] = []
    for record in rows:
        normalized = {column: DEFAULT_RECORD_VALUES.get(column, 0) for column in FEATURE_COLUMNS}
        normalized.update(record)
        for metadata_column in (TARGET_COLUMN, *METADATA_COLUMNS):
            normalized.pop(metadata_column, None)
        normalized_rows.append(normalized)
    return pd.DataFrame(normalized_rows)

