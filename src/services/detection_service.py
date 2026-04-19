"""Application service for model loading and detection inference."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from src.core.infer import DetectionResult, predict_batch, predict_record
from src.core.models import load_model


class DetectionService:
    def __init__(
        self,
        model_dir: str | Path = "models",
        binary_model: Any | None = None,
        multiclass_model: Any | None = None,
    ) -> None:
        self.model_dir = Path(model_dir)
        self.binary_model = binary_model
        self.multiclass_model = multiclass_model

    @property
    def binary_model_path(self) -> Path:
        return self.model_dir / "binary_model.joblib"

    @property
    def multiclass_model_path(self) -> Path:
        return self.model_dir / "multiclass_model.joblib"

    def is_ready(self) -> bool:
        return self.binary_model is not None or self.binary_model_path.is_file()

    def load(self) -> "DetectionService":
        if self.binary_model is None:
            self.binary_model = load_model(self.binary_model_path)
        if self.multiclass_model is None and self.multiclass_model_path.is_file():
            self.multiclass_model = load_model(self.multiclass_model_path)
        return self

    def predict(self, record: dict[str, Any]) -> DetectionResult:
        if self.binary_model is None:
            self.load()
        return predict_record(self.binary_model, record, multiclass_model=self.multiclass_model)

    def predict_many(self, records: list[dict[str, Any]]) -> list[DetectionResult]:
        if self.binary_model is None:
            self.load()
        return predict_batch(self.binary_model, records, multiclass_model=self.multiclass_model)

