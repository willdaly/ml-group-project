"""EDA helpers for the NSL-KDD ML project."""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

_MPL_CONFIG_DIR = Path(tempfile.gettempdir()) / "ml-group-project-matplotlib"
_MPL_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(_MPL_CONFIG_DIR))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from src.core.features import ATTACK_CATEGORY_MAP, map_attack_category


def build_eda_summary(train_df: pd.DataFrame, test_df: pd.DataFrame, metadata: dict[str, str]) -> dict:
    combined_df = pd.concat([train_df.assign(split="train"), test_df.assign(split="test")], ignore_index=True)
    numeric_columns = combined_df.select_dtypes(include=["number"]).columns.tolist()

    combined_df["attack_category"] = map_attack_category(combined_df["label"])
    category_dist = combined_df["attack_category"].value_counts().to_dict()

    return {
        "dataset_root": metadata.get("dataset_root", ""),
        "train_rows": int(len(train_df)),
        "test_rows": int(len(test_df)),
        "combined_rows": int(len(combined_df)),
        "feature_count": int(train_df.shape[1] - 2),
        "missing_values": int(combined_df.isna().sum().sum()),
        "duplicate_rows": int(combined_df.duplicated().sum()),
        "label_distribution": combined_df["label"].value_counts().to_dict(),
        "attack_category_distribution": category_dist,
        "numeric_columns": numeric_columns,
    }


def render_eda_artifacts(train_df: pd.DataFrame, summary: dict, output_dir: str | Path = "outputs") -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    sns.set_theme(style="whitegrid", palette="muted")

    (output_path / "eda_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    train_df = train_df.copy()
    train_df["attack_category"] = map_attack_category(train_df["label"])
    category_order = ["Normal", "DoS", "Probe", "R2L", "U2R"]
    cat_counts = train_df["attack_category"].value_counts().reindex(category_order, fill_value=0)
    colors = ["#4CAF50", "#F44336", "#FF9800", "#2196F3", "#9C27B0"]

    # --- 1. Top 10 fine-grained labels ---
    plt.figure(figsize=(12, 5))
    label_counts = train_df["label"].value_counts().head(10)
    ax = sns.barplot(x=label_counts.index, y=label_counts.values, hue=label_counts.index, legend=False)
    ax.bar_label(ax.containers[0], fmt="%d", fontsize=8)
    plt.title("Top 10 NSL-KDD Attack Labels (Training Set)")
    plt.xlabel("Attack Label")
    plt.ylabel("Count")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    plt.savefig(output_path / "label_distribution.png", dpi=150)
    plt.close()

    # --- 2. Attack category bar + pie ---
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    bars = axes[0].bar(cat_counts.index, cat_counts.values, color=colors)
    axes[0].bar_label(bars, fmt="%d", fontsize=9)
    axes[0].set_title("Attack Category Distribution")
    axes[0].set_ylabel("Count")
    axes[1].pie(cat_counts.values, labels=cat_counts.index, autopct="%1.1f%%", colors=colors, startangle=90)
    axes[1].set_title("Attack Category Proportions")
    plt.tight_layout()
    plt.savefig(output_path / "attack_category_distribution.png", dpi=150)
    plt.close()

    # --- 3. Binary class distribution ---
    binary_counts = train_df["attack_category"].apply(lambda x: "Normal" if x == "Normal" else "Attack").value_counts()
    plt.figure(figsize=(6, 4))
    ax = sns.barplot(x=binary_counts.index, y=binary_counts.values, hue=binary_counts.index,
                     palette=["#F44336", "#4CAF50"], legend=False)
    ax.bar_label(ax.containers[0], fmt="%d")
    plt.title("Binary Class Distribution (Training Set)")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(output_path / "binary_class_distribution.png", dpi=150)
    plt.close()

    # --- 4. Correlation heatmap ---
    numeric_cols = train_df.select_dtypes(include=["number"]).columns.tolist()
    numeric_cols = [c for c in numeric_cols if c not in ("difficulty_level",)]
    if len(numeric_cols) > 2:
        corr_matrix = train_df[numeric_cols].corr()
        plt.figure(figsize=(14, 12))
        mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
        sns.heatmap(corr_matrix, mask=mask, cmap="RdBu_r", center=0,
                    square=True, linewidths=0.5, cbar_kws={"shrink": 0.7},
                    vmin=-1, vmax=1)
        plt.title("Feature Correlation Heatmap")
        plt.tight_layout()
        plt.savefig(output_path / "correlation_heatmap.png", dpi=150)
        plt.close()

    # --- 5. Key feature boxplots by attack category ---
    key_features = ["duration", "src_bytes", "dst_bytes", "count", "srv_count", "serror_rate"]
    key_features = [f for f in key_features if f in train_df.columns]
    if key_features:
        fig, axes = plt.subplots(2, 3, figsize=(16, 9))
        for idx, feature in enumerate(key_features):
            ax = axes[idx // 3][idx % 3]
            data_for_plot = []
            labels_for_plot = []
            for cat in category_order:
                subset = train_df.loc[train_df["attack_category"] == cat, feature].dropna()
                data_for_plot.append(subset.values)
                labels_for_plot.append(cat)
            ax.boxplot(data_for_plot, tick_labels=labels_for_plot, showfliers=False)
            ax.set_title(feature, fontsize=10)
            ax.tick_params(axis="x", rotation=30, labelsize=8)
        plt.suptitle("Key Feature Distributions by Attack Category (outliers hidden)", fontsize=13)
        plt.tight_layout()
        plt.savefig(output_path / "numeric_feature_boxplot.png", dpi=150)
        plt.close()

    # --- 6. Categorical features by attack category ---
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    for idx, col in enumerate(["protocol_type", "service", "flag"]):
        if col not in train_df.columns:
            continue
        ct = pd.crosstab(train_df[col], train_df["attack_category"])
        ct = ct.reindex(columns=category_order, fill_value=0)
        if col == "service":
            ct = ct.loc[ct.sum(axis=1).nlargest(10).index]
        ct.plot(kind="bar", stacked=True, ax=axes[idx], color=colors[:ct.shape[1]])
        axes[idx].set_title(f"{col} by Attack Category")
        axes[idx].tick_params(axis="x", rotation=35)
        axes[idx].legend(fontsize=7)
    plt.tight_layout()
    plt.savefig(output_path / "categorical_features_by_attack.png", dpi=150)
    plt.close()

    print(f"  Rendered 6 EDA chart sets to {output_path}")
