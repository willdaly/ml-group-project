"""Pydantic request and response schemas for the FastAPI demo."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class TrainRequest(BaseModel):
    data_dir: str | None = None
    dataset: str | None = None
    output_dir: str = "outputs"
    model_dir: str = "models"


class TrainResponse(BaseModel):
    dataset_metadata: dict[str, str]
    binary_metrics: list[dict[str, Any]]
    multiclass_metrics: dict[str, Any]
    best_binary_model: str
    output_dir: str
    model_paths: dict[str, str]


class PredictRequest(BaseModel):
    record: dict[str, Any] = Field(default_factory=dict)
    model_dir: str = "models"


class BatchPredictRequest(BaseModel):
    records: list[dict[str, Any]] = Field(default_factory=list)
    model_dir: str = "models"


class PredictionResponse(BaseModel):
    binary_class: str
    attack_category: str
    confidence: float | None = None
    explanation: str


class BatchPredictionResponse(BaseModel):
    predictions: list[PredictionResponse]


class IncidentReportRequest(BaseModel):
    predictions: list[PredictionResponse] | None = None
    records: list[dict[str, Any]] | None = None
    model_dir: str = "models"


class IncidentReportResponse(BaseModel):
    total_records: int
    attack_records: int
    normal_records: int
    attack_categories: dict[str, int]
    high_confidence_attack_records: int
    summary: str

