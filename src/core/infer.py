"""Reusable inference helpers for fitted NSL-KDD detection models."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

import numpy as np

from src.core.explain import explain_prediction
from src.core.features import ensure_feature_frame


@dataclass(frozen=True)
class DetectionResult:
    binary_class: str
    attack_category: str
    confidence: float | None
    explanation: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _class_confidence(model: Any, frame: Any, predicted: Any) -> float | None:
    if not hasattr(model, "predict_proba"):
        return None

    try:
        probabilities = model.predict_proba(frame)
        classes = list(getattr(model, "classes_", []))
        if not classes and hasattr(model, "named_steps"):
            classes = list(getattr(model.named_steps.get("model"), "classes_", []))
        class_index = classes.index(predicted)
        return round(float(probabilities[0][class_index]), 4)
    except Exception:
        return None


def _binary_label(prediction: Any) -> str:
    if isinstance(prediction, (np.integer, int)):
        return "attack" if int(prediction) == 1 else "normal"
    normalized = str(prediction).strip().lower()
    return "normal" if normalized in {"0", "normal"} else "attack"


def predict_record(
    binary_model: Any,
    record: dict[str, Any],
    multiclass_model: Any | None = None,
) -> DetectionResult:
    frame = ensure_feature_frame(record)
    raw_binary = binary_model.predict(frame)[0]
    binary_label = _binary_label(raw_binary)
    confidence = _class_confidence(binary_model, frame, raw_binary)

    if binary_label == "normal":
        attack_category = "Normal"
    elif multiclass_model is not None:
        attack_category = str(multiclass_model.predict(frame)[0])
    else:
        attack_category = "Attack"

    explanation = explain_prediction(record, binary_label, attack_category, confidence)
    return DetectionResult(
        binary_class=binary_label,
        attack_category=attack_category,
        confidence=confidence,
        explanation=explanation,
    )


def predict_batch(
    binary_model: Any,
    records: list[dict[str, Any]],
    multiclass_model: Any | None = None,
) -> list[DetectionResult]:
    return [predict_record(binary_model, record, multiclass_model=multiclass_model) for record in records]

