"""Baseline model-training helpers for the NSL-KDD ML project scaffold."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_recall_fscore_support
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

TARGET_COLUMN = "label"
CATEGORICAL_COLUMNS = ["protocol_type", "service", "flag"]


def _binary_target(series: pd.Series) -> pd.Series:
    return (series.astype(str).str.lower() != "normal").astype(int)


def _split_features(frame: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    features = frame.drop(columns=[TARGET_COLUMN, "difficulty"], errors="ignore")
    target = _binary_target(frame[TARGET_COLUMN])
    return features, target


def build_preprocessor(features: pd.DataFrame) -> ColumnTransformer:
    categorical_columns = [column for column in CATEGORICAL_COLUMNS if column in features.columns]
    numeric_columns = [column for column in features.columns if column not in categorical_columns]

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


def build_models(preprocessor: ColumnTransformer) -> dict[str, Pipeline]:
    return {
        "logistic_regression": Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ("model", LogisticRegression(max_iter=1000)),
            ]
        ),
        "random_forest": Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ("model", RandomForestClassifier(n_estimators=300, random_state=42, n_jobs=-1)),
            ]
        ),
    }


def _evaluate_model(name: str, model: Pipeline, x_train: pd.DataFrame, y_train: pd.Series, x_test: pd.DataFrame, y_test: pd.Series) -> dict:
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    precision, recall, f1, _ = precision_recall_fscore_support(y_test, predictions, average="binary", zero_division=0)
    return {
        "model": name,
        "accuracy": round(float(accuracy_score(y_test, predictions)), 4),
        "precision": round(float(precision), 4),
        "recall": round(float(recall), 4),
        "f1": round(float(f1), 4),
        "confusion_matrix": confusion_matrix(y_test, predictions).tolist(),
    }


def train_and_evaluate_models(train_df: pd.DataFrame, test_df: pd.DataFrame) -> list[dict]:
    x_train, y_train = _split_features(train_df)
    x_test, y_test = _split_features(test_df)
    preprocessor = build_preprocessor(x_train)
    models = build_models(preprocessor)
    return [
        _evaluate_model(name, model, x_train, y_train, x_test, y_test)
        for name, model in models.items()
    ]


def write_model_artifacts(results: list[dict], output_dir: str | Path = "outputs") -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    (output_path / "model_metrics.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Model Metrics",
        "",
        "| Model | Accuracy | Precision | Recall | F1 |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for result in results:
        lines.append(
            f"| {result['model']} | {result['accuracy']:.4f} | {result['precision']:.4f} | {result['recall']:.4f} | {result['f1']:.4f} |"
        )

    (output_path / "MODEL_METRICS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
