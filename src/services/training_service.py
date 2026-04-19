"""Application service for running the full NSL-KDD training workflow."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from src.core.data_loader import load_nsl_kdd_frames
from src.core.train import (
    render_model_visualizations,
    save_detection_artifacts,
    select_best_model,
    train_and_evaluate_models,
    train_multiclass_model,
    write_model_artifacts,
)
from src.eda import build_eda_summary, render_eda_artifacts


@dataclass(frozen=True)
class TrainingRunResult:
    dataset_metadata: dict[str, str]
    binary_metrics: list[dict[str, Any]]
    multiclass_metrics: dict[str, Any]
    best_binary_model: str
    output_dir: str
    model_paths: dict[str, str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class TrainingService:
    def run_training(
        self,
        data_dir: str | Path | None = None,
        dataset_handle: str | None = None,
        output_dir: str | Path = "outputs",
        model_dir: str | Path = "models",
    ) -> TrainingRunResult:
        train_df, test_df, metadata = load_nsl_kdd_frames(dataset_handle=dataset_handle, data_dir=data_dir)

        summary = build_eda_summary(train_df, test_df, metadata)
        render_eda_artifacts(train_df, summary, output_dir=output_dir)

        results, models, _x_train, _y_train, x_test, y_test = train_and_evaluate_models(train_df, test_df)
        write_model_artifacts(results, output_dir=output_dir)
        render_model_visualizations(results, models, x_test, y_test, output_dir=output_dir)

        multiclass_metrics, multiclass_model = train_multiclass_model(
            train_df,
            test_df,
            output_dir=output_dir,
            return_model=True,
        )
        best_name, best_model = select_best_model(results, models)
        model_paths = save_detection_artifacts(
            best_model,
            multiclass_model,
            model_dir=model_dir,
            metadata={
                "best_binary_model": best_name,
                "dataset": metadata,
                "output_dir": str(output_dir),
            },
        )

        return TrainingRunResult(
            dataset_metadata=metadata,
            binary_metrics=results,
            multiclass_metrics=multiclass_metrics,
            best_binary_model=best_name,
            output_dir=str(output_dir),
            model_paths=model_paths,
        )

