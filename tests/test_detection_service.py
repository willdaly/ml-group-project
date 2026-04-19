from __future__ import annotations

from pathlib import Path

import joblib
import numpy as np

from src.services.detection_service import DetectionService
from src.services.reporting_service import ReportingService


class DummyBinaryModel:
    classes_ = np.array([0, 1])

    def predict(self, frame):
        return np.array([1 for _ in range(len(frame))])

    def predict_proba(self, frame):
        return np.array([[0.2, 0.8] for _ in range(len(frame))])


class DummyMulticlassModel:
    def predict(self, frame):
        return np.array(["DoS" for _ in range(len(frame))])


def _write_dummy_models(model_dir: Path) -> None:
    model_dir.mkdir()
    joblib.dump(DummyBinaryModel(), model_dir / "binary_model.joblib")
    joblib.dump(DummyMulticlassModel(), model_dir / "multiclass_model.joblib")


def test_detection_service_loads_models_and_scores_record(tmp_path: Path) -> None:
    model_dir = tmp_path / "models"
    _write_dummy_models(model_dir)

    result = DetectionService(model_dir=model_dir).predict({"protocol_type": "tcp", "service": "http", "flag": "SF"})

    assert result.binary_class == "attack"
    assert result.attack_category == "DoS"
    assert result.confidence == 0.8
    assert "DoS attack" in result.explanation


def test_reporting_service_summarizes_predictions() -> None:
    report = ReportingService().build_incident_report(
        [
            {"binary_class": "attack", "attack_category": "DoS", "confidence": 0.9},
            {"binary_class": "normal", "attack_category": "Normal", "confidence": 0.7},
        ]
    )

    assert report["total_records"] == 2
    assert report["attack_records"] == 1
    assert report["attack_categories"] == {"DoS": 1}
    assert report["high_confidence_attack_records"] == 1

