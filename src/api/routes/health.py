"""Health endpoint."""

from __future__ import annotations

from fastapi import APIRouter

from src.services.detection_service import DetectionService

router = APIRouter()


@router.get("/health")
def health() -> dict[str, object]:
    service = DetectionService()
    return {
        "status": "ok",
        "model_ready": service.is_ready(),
        "service": "nsl-kdd-detection-engine",
    }

