"""FastAPI application factory for the NSL-KDD detection demo."""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.api.routes import health, predict, report, train

PROJECT_ROOT = Path(__file__).resolve().parents[2]
TEMPLATES = Jinja2Templates(directory=str(PROJECT_ROOT / "templates"))


def create_app() -> FastAPI:
    app = FastAPI(
        title="NSL-KDD Cybersecurity Detection Engine",
        description="Reusable ML core with a lightweight FastAPI demo layer.",
        version="0.1.0",
    )
    static_dir = PROJECT_ROOT / "static"
    static_dir.mkdir(exist_ok=True)
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

    app.include_router(health.router)
    app.include_router(train.router)
    app.include_router(predict.router)
    app.include_router(report.router)

    @app.get("/demo", response_class=HTMLResponse)
    def demo(request: Request) -> HTMLResponse:
        return TEMPLATES.TemplateResponse(request, "index.html")

    return app


app = create_app()
