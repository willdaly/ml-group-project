"""Training endpoint."""

from __future__ import annotations

from fastapi import APIRouter

from src.api.schemas import TrainRequest, TrainResponse
from src.services.training_service import TrainingService

router = APIRouter()


@router.post("/train", response_model=TrainResponse)
def train(request: TrainRequest) -> dict:
    result = TrainingService().run_training(
        data_dir=request.data_dir,
        dataset_handle=request.dataset,
        output_dir=request.output_dir,
        model_dir=request.model_dir,
    )
    return result.to_dict()

