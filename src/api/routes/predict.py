"""Prediction endpoints."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException

from src.api.schemas import BatchPredictionResponse, BatchPredictRequest, PredictRequest, PredictionResponse
from src.services.detection_service import DetectionService

router = APIRouter()


def _load_service(model_dir: str) -> DetectionService:
    service = DetectionService(model_dir=model_dir)
    if not service.is_ready():
        raise HTTPException(status_code=503, detail="No trained model found. Run POST /train first.")
    return service.load()


@router.post("/predict", response_model=PredictionResponse)
def predict(request: PredictRequest) -> dict:
    service = _load_service(request.model_dir)
    return service.predict(request.record).to_dict()


@router.post("/predict/batch", response_model=BatchPredictionResponse)
def predict_batch(request: BatchPredictRequest) -> dict[str, list[dict]]:
    service = _load_service(request.model_dir)
    predictions = [prediction.to_dict() for prediction in service.predict_many(request.records)]
    return {"predictions": predictions}

