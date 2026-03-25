"""EDA helpers for the NSL-KDD ML project scaffold."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def build_eda_summary(train_df: pd.DataFrame, test_df: pd.DataFrame, metadata: dict[str, str]) -> dict:
    combined_df = pd.concat([train_df.assign(split="train"), test_df.assign(split="test")], ignore_index=True)
    numeric_columns = combined_df.select_dtypes(include=["number"]).columns.tolist()
    return {
        "dataset_root": metadata.get("dataset_root", ""),
        "train_rows": int(len(train_df)),
        "test_rows": int(len(test_df)),
        "combined_rows": int(len(combined_df)),
        "feature_count": int(train_df.shape[1] - 2),
        "missing_values": int(combined_df.isna().sum().sum()),
        "duplicate_rows": int(combined_df.duplicated().sum()),
        "label_distribution": combined_df["label"].value_counts().to_dict(),
        "numeric_columns": numeric_columns,
    }


def render_eda_artifacts(train_df: pd.DataFrame, summary: dict, output_dir: str | Path = "outputs") -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    (output_path / "eda_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    plt.figure(figsize=(10, 5))
    train_df["label"].value_counts().head(10).plot(kind="bar")
    plt.title("Top NSL-KDD Class Labels")
    plt.tight_layout()
    plt.savefig(output_path / "label_distribution.png")
    plt.close()

    numeric_columns = train_df.select_dtypes(include=["number"]).columns.tolist()[:6]
    if numeric_columns:
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=train_df[numeric_columns])
        plt.xticks(rotation=30, ha="right")
        plt.title("Sample Numeric Feature Distribution")
        plt.tight_layout()
        plt.savefig(output_path / "numeric_feature_boxplot.png")
        plt.close()
