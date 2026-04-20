# NSL-KDD Cybersecurity Detection Engine

**Live demo:** [machine-learning-project-94gj.onrender.com](https://machine-learning-project-94gj.onrender.com/)

## Overview

This repository packages a complete NSL-KDD intrusion-detection project for class submission and demo use. It preserves the original exploratory analysis and model-training pipeline, and adds a reusable detection engine with a lightweight FastAPI browser demo.

## Submission Contents

- `data/nsl-kdd/` — Local copy of `KDDTrain+.txt` and `KDDTest+.txt` for offline grading.
- `notebooks/EDA.ipynb` — Interactive exploration and visual analysis (styled, used for class presentation).
- `notebooks/01_eda_nsl_kdd.ipynb` — Full methodical EDA walkthrough on the complete training set with fine-grained attack-type breakdowns.
- `notebooks/ZahraDataset_Nslkdd.ipynb` — Additional exploratory notebook.
- `main.py` and `src/` — End-to-end pipeline, reusable ML core, service layer, and FastAPI app.
- `outputs/` — Generated charts and model metrics included with the submission.
- `models/` — Saved binary and multiclass inference models after training.
- `docs/` — Refactor plan, architecture notes, technical writeup, and presentation notes.
- `Report.pdf` — Final written report (submission copy).
- `PRESENTATION.pptx` — Slide deck with embedded charts (submission copy).
- `drafts/` — Markdown source files for the report and presentation.

## Architecture

```text
src/
  core/       reusable data loading, feature prep, model training, inference, and explanations
  services/   training, detection, and reporting workflows
  api/        FastAPI app, routes, and request/response schemas
```

The legacy imports in `src/data_loader.py`, `src/train_models.py`, and `src/eda.py` are kept so the original CLI and tests continue to work.

## Setup

```bash
pip install -r requirements.txt
```

## Run The Project

The repository is now self-contained and runs offline with the included dataset:

```bash
python main.py --data-dir data/nsl-kdd --output-dir outputs --model-dir models
```

Optional Kaggle fallback still works when internet access is available:

```bash
python main.py --dataset hassan06/nslkdd --output-dir outputs --model-dir models
```

Training writes:

- EDA charts and metrics to `outputs/`
- binary and multiclass model files to `models/`
- model metadata to `models/metadata.json`

## Run The FastAPI Demo

Train once so `models/` exists, then start the app:

```bash
uvicorn src.api.app:app --reload
```

Open:

```text
http://127.0.0.1:8000/demo
```

Useful endpoints:

- `GET /health`
- `POST /train`
- `POST /predict`
- `POST /predict/batch`
- `POST /report/incidents`
- `GET /demo`

Example single-record scoring:

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "record": {
      "duration": 0,
      "protocol_type": "tcp",
      "service": "http",
      "flag": "SF",
      "src_bytes": 181,
      "dst_bytes": 5450,
      "count": 8,
      "srv_count": 8,
      "serror_rate": 0,
      "srv_serror_rate": 0
    }
  }'
```

Example incident report from predictions:

```bash
curl -X POST http://127.0.0.1:8000/report/incidents \
  -H "Content-Type: application/json" \
  -d '{
    "predictions": [
      {
        "binary_class": "attack",
        "attack_category": "DoS",
        "confidence": 0.91,
        "explanation": "Traffic is classified as a DoS attack."
      }
    ]
  }'
```

## Quick Demo

```bash
# 1. Train models (one-time)
python main.py --data-dir data/nsl-kdd --output-dir outputs --model-dir models

# 2. Start the server
uvicorn src.api.app:app --reload

# 3. Open in browser
open http://127.0.0.1:8000/demo
```

On the `/demo` page, click **Load Benign Example** or **Load Attack Example**, then **Score Record** to see classification results with confidence scores and explanations.

See `docs/demo_runbook.md` for a full 60-second demo script.

## Run Tests

```bash
pytest
```

## Documentation

- `docs/technical_writeup.md` — project objective, dataset, modeling workflow, testing, limitations, and future work.
- `docs/architecture.md` — current module boundaries, request flow, and saved artifact layout.
- `docs/presentation_notes.md` — slide-ready content for a short project demo.

## Project Website

The FastAPI app doubles as a multi-page project website. After starting the server, visit:

| Page | Route | Description |
|------|-------|-------------|
| Home | `/` | Project overview and navigation |
| Demo | `/demo` | Live prediction with example inputs |
| How It Works | `/how-it-works` | Dataset, models, preprocessing |
| Results | `/results` | Charts, confusion matrices, ROC curves |
| Architecture | `/architecture` | Code organization and request flows |
| Presentation | `/presentation` | Slide-style project walkthrough |

A shared top navigation bar links all pages together, with an external link to the GitHub repository.
