"""Training, evaluation, visualization, and artifact writing for NSL-KDD models."""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path
from typing import Any

_MPL_CONFIG_DIR = Path(tempfile.gettempdir()) / "ml-group-project-matplotlib"
_MPL_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(_MPL_CONFIG_DIR))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_recall_fscore_support,
    roc_auc_score,
    roc_curve,
)
from sklearn.pipeline import Pipeline

from src.core.features import (
    binary_target,
    build_preprocessor,
    get_feature_names,
    map_attack_category,
    split_features,
)
from src.core.models import build_models, build_multiclass_model, save_model


def _binary_target(series: pd.Series) -> pd.Series:
    return binary_target(series)


def _multiclass_target(series: pd.Series) -> pd.Series:
    return map_attack_category(series)


def _split_features(frame: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    return split_features(frame, target="binary")


def _split_features_multiclass(frame: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    return split_features(frame, target="multiclass")


def _get_feature_names(preprocessor: Any) -> list[str]:
    return get_feature_names(preprocessor)


def _evaluate_model(
    name: str,
    model: Pipeline,
    x_train: pd.DataFrame,
    y_train: pd.Series,
    x_test: pd.DataFrame,
    y_test: pd.Series,
) -> dict[str, Any]:
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    precision, recall, f1, _ = precision_recall_fscore_support(y_test, predictions, average="binary", zero_division=0)

    auc = None
    if hasattr(model, "predict_proba"):
        try:
            proba = model.predict_proba(x_test)[:, 1]
            auc = round(float(roc_auc_score(y_test, proba)), 4)
        except Exception:
            pass

    return {
        "model": name,
        "accuracy": round(float(accuracy_score(y_test, predictions)), 4),
        "precision": round(float(precision), 4),
        "recall": round(float(recall), 4),
        "f1": round(float(f1), 4),
        "auc": auc,
        "confusion_matrix": confusion_matrix(y_test, predictions).tolist(),
    }


def train_and_evaluate_models(
    train_df: pd.DataFrame, test_df: pd.DataFrame
) -> tuple[list[dict[str, Any]], dict[str, Pipeline], pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]:
    """Train all binary models and return results plus fitted pipelines and data splits."""
    x_train, y_train = _split_features(train_df)
    x_test, y_test = _split_features(test_df)
    preprocessor = build_preprocessor(x_train)
    models = build_models(preprocessor)

    results = []
    for name, model in models.items():
        result = _evaluate_model(name, model, x_train, y_train, x_test, y_test)
        results.append(result)

    return results, models, x_train, y_train, x_test, y_test


def select_best_model(results: list[dict[str, Any]], models: dict[str, Pipeline], metric: str = "f1") -> tuple[str, Pipeline]:
    best = max(results, key=lambda result: result.get(metric) or 0)
    return best["model"], models[best["model"]]


def train_multiclass_model(
    train_df: pd.DataFrame,
    test_df: pd.DataFrame,
    output_dir: str | Path = "outputs",
    return_model: bool = False,
) -> dict[str, Any] | tuple[dict[str, Any], Pipeline]:
    """Train a Random Forest on 5-class attack categories and write per-class report."""
    x_train, y_train = _split_features_multiclass(train_df)
    x_test, y_test = _split_features_multiclass(test_df)
    preprocessor = build_preprocessor(x_train)

    model = build_multiclass_model(preprocessor)
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)

    category_order = ["Normal", "DoS", "Probe", "R2L", "U2R"]
    report_str = classification_report(y_test, predictions, labels=category_order, zero_division=0)
    report_dict = classification_report(y_test, predictions, labels=category_order, zero_division=0, output_dict=True)

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    (output_path / "multiclass_report.txt").write_text(
        "Multiclass Attack-Category Classification Report\n"
        "================================================\n\n"
        f"{report_str}\n",
        encoding="utf-8",
    )

    cm = confusion_matrix(y_test, predictions, labels=category_order)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="YlOrRd", xticklabels=category_order, yticklabels=category_order)
    plt.title("Multiclass Confusion Matrix (5 Attack Categories)")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.savefig(output_path / "multiclass_confusion_matrix.png", dpi=150)
    plt.close()

    overall_acc = round(float(accuracy_score(y_test, predictions)), 4)
    print(f"  Multiclass accuracy: {overall_acc}")
    metrics = {"multiclass_accuracy": overall_acc, "per_class": report_dict}
    if return_model:
        return metrics, model
    return metrics


def render_model_visualizations(
    results: list[dict[str, Any]],
    models: dict[str, Pipeline],
    x_test: pd.DataFrame,
    y_test: pd.Series,
    output_dir: str | Path = "outputs",
) -> None:
    """Generate confusion matrix heatmaps, ROC curves, and feature importance plot."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid")

    n_models = len(results)

    fig, axes = plt.subplots(1, n_models, figsize=(6 * n_models, 5))
    if n_models == 1:
        axes = [axes]
    for idx, result in enumerate(results):
        cm = np.array(result["confusion_matrix"])
        sns.heatmap(
            cm,
            annot=True,
            fmt="d",
            cmap="Blues",
            ax=axes[idx],
            xticklabels=["Normal", "Attack"],
            yticklabels=["Normal", "Attack"],
        )
        axes[idx].set_title(result["model"].replace("_", " ").title())
        axes[idx].set_xlabel("Predicted")
        axes[idx].set_ylabel("Actual")
    plt.suptitle("Binary Confusion Matrices", fontsize=14)
    plt.tight_layout()
    plt.savefig(output_path / "confusion_matrices.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 6))
    for name, model in models.items():
        if hasattr(model, "predict_proba"):
            try:
                proba = model.predict_proba(x_test)[:, 1]
                fpr, tpr, _ = roc_curve(y_test, proba)
                auc_val = roc_auc_score(y_test, proba)
                label = f"{name.replace('_', ' ').title()} (AUC={auc_val:.3f})"
                plt.plot(fpr, tpr, label=label, linewidth=2)
            except Exception:
                pass
    plt.plot([0, 1], [0, 1], "k--", linewidth=1, label="Random (AUC=0.500)")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curves - Binary Classification")
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig(output_path / "roc_curves.png", dpi=150)
    plt.close()

    rf_model = models.get("random_forest")
    if rf_model is not None:
        clf = rf_model.named_steps["model"]
        preprocessor = rf_model.named_steps["preprocessor"]
        feature_names = _get_feature_names(preprocessor)
        importances = clf.feature_importances_

        if len(feature_names) == len(importances):
            imp_df = pd.DataFrame({"feature": feature_names, "importance": importances})
            imp_df = imp_df.sort_values("importance", ascending=False).head(20)

            plt.figure(figsize=(10, 8))
            sns.barplot(data=imp_df, x="importance", y="feature", hue="feature", legend=False, palette="viridis")
            plt.title("Top 20 Feature Importances (Random Forest)")
            plt.xlabel("Importance")
            plt.ylabel("Feature")
            plt.tight_layout()
            plt.savefig(output_path / "feature_importance.png", dpi=150)
            plt.close()

    metrics_df = pd.DataFrame(results)
    metrics_to_plot = ["accuracy", "precision", "recall", "f1"]
    if any(r.get("auc") is not None for r in results):
        metrics_to_plot.append("auc")

    melted = metrics_df.melt(id_vars=["model"], value_vars=metrics_to_plot, var_name="Metric", value_name="Score")
    melted = melted.dropna(subset=["Score"])

    plt.figure(figsize=(10, 5))
    sns.barplot(data=melted, x="Metric", y="Score", hue="model")
    plt.title("Model Comparison - Binary Classification Metrics")
    plt.ylim(0, 1)
    plt.legend(title="Model")
    plt.tight_layout()
    plt.savefig(output_path / "model_comparison.png", dpi=150)
    plt.close()

    print(f"  Rendered model visualizations to {output_path}")


def write_model_artifacts(results: list[dict[str, Any]], output_dir: str | Path = "outputs") -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    (output_path / "model_metrics.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Model Metrics",
        "",
        "| Model | Accuracy | Precision | Recall | F1 | AUC |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for result in results:
        auc_str = f"{result['auc']:.4f}" if result.get("auc") is not None else "N/A"
        lines.append(
            f"| {result['model']} | {result['accuracy']:.4f} | {result['precision']:.4f} "
            f"| {result['recall']:.4f} | {result['f1']:.4f} | {auc_str} |"
        )

    (output_path / "MODEL_METRICS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def save_detection_artifacts(
    binary_model: Pipeline,
    multiclass_model: Pipeline,
    model_dir: str | Path = "models",
    metadata: dict[str, Any] | None = None,
) -> dict[str, str]:
    model_path = Path(model_dir)
    model_path.mkdir(parents=True, exist_ok=True)

    binary_path = save_model(binary_model, model_path / "binary_model.joblib")
    multiclass_path = save_model(multiclass_model, model_path / "multiclass_model.joblib")
    metadata_path = model_path / "metadata.json"
    metadata_path.write_text(json.dumps(metadata or {}, indent=2) + "\n", encoding="utf-8")

    return {
        "binary_model": str(binary_path),
        "multiclass_model": str(multiclass_path),
        "metadata": str(metadata_path),
    }

