"""Incident reporting endpoint."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException

from src.api.routes.predict import _load_service
from src.api.schemas import IncidentReportRequest, IncidentReportResponse
from src.services.reporting_service import ReportingService

router = APIRouter()


def _model_to_dict(model: object) -> dict:
    if hasattr(model, "model_dump"):
        return model.model_dump()
    return model.dict()


@router.post("/report/incidents", response_model=IncidentReportResponse)
def report_incidents(request: IncidentReportRequest) -> dict:
    if request.predictions is not None:
        predictions = [_model_to_dict(prediction) for prediction in request.predictions]
    elif request.records is not None:
        service = _load_service(request.model_dir)
        predictions = [prediction.to_dict() for prediction in service.predict_many(request.records)]
    else:
        raise HTTPException(status_code=400, detail="Provide either predictions or records.")

    return ReportingService().build_incident_report(predictions)
