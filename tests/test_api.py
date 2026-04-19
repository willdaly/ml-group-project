from __future__ import annotations

from pathlib import Path

import asyncio
import joblib
import httpx
import numpy as np

from src.api.app import create_app


class DummyBinaryModel:
    classes_ = np.array([0, 1])

    def predict(self, frame):
        return np.array([1 for _ in range(len(frame))])

    def predict_proba(self, frame):
        return np.array([[0.15, 0.85] for _ in range(len(frame))])


class DummyMulticlassModel:
    def predict(self, frame):
        return np.array(["Probe" for _ in range(len(frame))])


def _write_dummy_models(model_dir: Path) -> None:
    model_dir.mkdir()
    joblib.dump(DummyBinaryModel(), model_dir / "binary_model.joblib")
    joblib.dump(DummyMulticlassModel(), model_dir / "multiclass_model.joblib")


def test_health_and_demo_routes() -> None:
    async def run_requests():
        transport = httpx.ASGITransport(app=create_app())
        async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
            health = await client.get("/health")
            demo = await client.get("/demo")
        return health, demo

    health, demo = asyncio.run(run_requests())

    assert health.status_code == 200
    assert health.json()["status"] == "ok"
    assert demo.status_code == 200
    assert "NSL-KDD Detection Demo" in demo.text


def test_predict_and_report_routes_with_saved_models(tmp_path: Path) -> None:
    model_dir = tmp_path / "models"
    _write_dummy_models(model_dir)

    async def run_requests():
        transport = httpx.ASGITransport(app=create_app())
        async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
            predict_response = await client.post(
                "/predict",
                json={
                    "model_dir": str(model_dir),
                    "record": {"protocol_type": "tcp", "service": "http", "flag": "SF"},
                },
            )
            prediction = predict_response.json()
            report_response = await client.post("/report/incidents", json={"predictions": [prediction]})
        return predict_response, prediction, report_response

    predict_response, prediction, report_response = asyncio.run(run_requests())
    assert predict_response.status_code == 200
    assert prediction["binary_class"] == "attack"
    assert prediction["attack_category"] == "Probe"

    assert report_response.status_code == 200
    assert report_response.json()["attack_records"] == 1
