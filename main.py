"""NSL-KDD ML group project: load data, EDA artifacts, train baseline models."""

from __future__ import annotations

import argparse
import sys

from src.data_loader import load_nsl_kdd_frames
from src.eda import build_eda_summary, render_eda_artifacts
from src.train_models import train_and_evaluate_models, write_model_artifacts


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run NSL-KDD EDA and baseline model training.")
    parser.add_argument(
        "--output-dir",
        default="outputs",
        help="Directory for EDA plots, eda_summary.json, and model metrics (default: outputs).",
    )
    parser.add_argument(
        "--dataset",
        default=None,
        help="KaggleHub dataset handle (default: KAGGLEHUB_DATASET env or hassan06/nslkdd).",
    )
    args = parser.parse_args(argv)

    train_df, test_df, metadata = load_nsl_kdd_frames(dataset_handle=args.dataset)
    summary = build_eda_summary(train_df, test_df, metadata)
    render_eda_artifacts(train_df, summary, output_dir=args.output_dir)

    results = train_and_evaluate_models(train_df, test_df)
    write_model_artifacts(results, output_dir=args.output_dir)

    print("Wrote EDA summary and plots to", args.output_dir)
    print("Wrote model_metrics.json and MODEL_METRICS.md to", args.output_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
