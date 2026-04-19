"""NSL-KDD ML group project: load data, EDA artifacts, train and evaluate models."""

from __future__ import annotations

import argparse
import sys

from src.data_loader import load_nsl_kdd_frames
from src.eda import build_eda_summary, render_eda_artifacts
from src.train_models import (
    render_model_visualizations,
    save_detection_artifacts,
    select_best_model,
    train_and_evaluate_models,
    train_multiclass_model,
    write_model_artifacts,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run NSL-KDD EDA and model training.")
    parser.add_argument(
        "--data-dir",
        default=None,
        help="Optional local directory containing KDDTrain+ and KDDTest+ files.",
    )
    parser.add_argument(
        "--output-dir",
        default="outputs",
        help="Directory for EDA plots, model metrics, and visualizations (default: outputs).",
    )
    parser.add_argument(
        "--dataset",
        default=None,
        help="KaggleHub dataset handle (default: KAGGLEHUB_DATASET env or hassan06/nslkdd).",
    )
    parser.add_argument(
        "--model-dir",
        default="models",
        help="Directory for saved inference models (default: models).",
    )
    args = parser.parse_args(argv)

    # --- Load data ---
    train_df, test_df, metadata = load_nsl_kdd_frames(dataset_handle=args.dataset, data_dir=args.data_dir)
    dataset_root = metadata.get("dataset_root", "unknown")
    dataset_source = metadata.get("dataset_source", "unspecified_source")
    print(f"Loaded dataset from {dataset_root} ({dataset_source})")

    # --- EDA ---
    print("\n[1/4] Building EDA summary and artifacts...")
    summary = build_eda_summary(train_df, test_df, metadata)
    render_eda_artifacts(train_df, summary, output_dir=args.output_dir)

    # --- Binary classification (3 models) ---
    print("\n[2/4] Training binary classifiers (LogReg, RF, GBM)...")
    results, models, x_train, y_train, x_test, y_test = train_and_evaluate_models(train_df, test_df)
    write_model_artifacts(results, output_dir=args.output_dir)

    for r in results:
        auc_str = f", AUC={r['auc']}" if r.get("auc") else ""
        print(f"  {r['model']}: Acc={r['accuracy']}, F1={r['f1']}{auc_str}")

    # --- Model visualizations (confusion matrices, ROC, feature importance) ---
    print("\n[3/4] Generating model visualizations...")
    render_model_visualizations(results, models, x_test, y_test, output_dir=args.output_dir)

    # --- Multiclass classification ---
    print("\n[4/4] Training multiclass attack-category classifier...")
    multiclass_metrics, multiclass_model = train_multiclass_model(
        train_df,
        test_df,
        output_dir=args.output_dir,
        return_model=True,
    )
    best_model_name, best_model = select_best_model(results, models)
    model_paths = save_detection_artifacts(
        best_model,
        multiclass_model,
        model_dir=args.model_dir,
        metadata={
            "best_binary_model": best_model_name,
            "dataset": metadata,
            "multiclass_accuracy": multiclass_metrics["multiclass_accuracy"],
        },
    )

    print(f"\nAll outputs written to {args.output_dir}/")
    print(f"Saved inference models to {args.model_dir}/")
    for model_name, model_path in model_paths.items():
        print(f"  {model_name}: {model_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
