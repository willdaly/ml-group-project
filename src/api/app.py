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

    outputs_dir = PROJECT_ROOT / "outputs"
    if outputs_dir.is_dir():
        app.mount("/static/outputs", StaticFiles(directory=str(outputs_dir)), name="outputs")

    app.include_router(health.router)
    app.include_router(train.router)
    app.include_router(predict.router)
    app.include_router(report.router)

    @app.get("/", response_class=HTMLResponse)
    def home(request: Request) -> HTMLResponse:
        return TEMPLATES.TemplateResponse(request, "home.html", {"active_page": "home"})

    @app.get("/demo", response_class=HTMLResponse)
    def demo(request: Request) -> HTMLResponse:
        return TEMPLATES.TemplateResponse(request, "index.html", {"active_page": "demo"})

    @app.get("/how-it-works", response_class=HTMLResponse)
    def how_it_works(request: Request) -> HTMLResponse:
        return TEMPLATES.TemplateResponse(request, "how_it_works.html", {"active_page": "how-it-works"})

    @app.get("/results", response_class=HTMLResponse)
    def results(request: Request) -> HTMLResponse:
        return TEMPLATES.TemplateResponse(request, "results.html", {"active_page": "results"})

    @app.get("/architecture", response_class=HTMLResponse)
    def architecture(request: Request) -> HTMLResponse:
        return TEMPLATES.TemplateResponse(request, "architecture.html", {"active_page": "architecture"})

    @app.get("/presentation", response_class=HTMLResponse)
    def presentation(request: Request) -> HTMLResponse:
        return TEMPLATES.TemplateResponse(request, "presentation.html", {"active_page": "presentation"})

    return app


app = create_app()
