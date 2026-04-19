# Technical Writeup

## Objective

This project refactors an NSL-KDD intrusion-detection class submission into a reusable cybersecurity detection engine with a small FastAPI demo layer. The original training and evaluation flow remains available through `main.py`, while the new structure separates ML logic, service workflows, and HTTP routes.

## Dataset And Task

The project uses the NSL-KDD dataset, a refined benchmark derived from KDD Cup 1999 network intrusion data. Each row describes a network connection with protocol, service, flag, byte counts, error rates, host-level statistics, an attack label, and a difficulty score.

The system supports two supervised learning tasks:

- Binary classification: `normal` vs `attack`.
- Multiclass classification: `Normal`, `DoS`, `Probe`, `R2L`, and `U2R`.

The repository includes `KDDTrain+.txt` and `KDDTest+.txt` under `data/nsl-kdd/` so the project can run offline.

## Original Architecture

The original project behaved like a compact class-submission pipeline:

- `src/data_loader.py` resolved the local or KaggleHub dataset.
- `src/eda.py` generated summary statistics and charts.
- `src/train_models.py` trained binary and multiclass models and wrote metrics.
- `main.py` orchestrated the complete run.

That design was good for reproducible grading, but less convenient for browser demos, reusable inference, saved models, or future integration with an agent runtime.

## Refactor Rationale

The refactor keeps the original behavior while introducing cleaner boundaries:

- `src/core/` owns pure data, feature, model, training, inference, and explanation logic.
- `src/services/` owns application workflows such as full training runs, model-backed detection, and incident reporting.
- `src/api/` owns FastAPI schemas and routes.

Legacy modules remain as compatibility shims so existing tests and imports continue to work.

## Model Workflow

The training flow loads the NSL-KDD train/test splits, generates EDA artifacts, trains three binary classifiers, evaluates them, selects the best binary model by F1 score, trains a multiclass Random Forest attack-category model, and saves both fitted pipelines.

Binary models:

- Logistic Regression
- Random Forest
- Gradient Boosting

Multiclass model:

- Random Forest over the five standard NSL-KDD categories

Saved inference artifacts:

- `models/binary_model.joblib`
- `models/multiclass_model.joblib`
- `models/metadata.json`

## Inference Workflow

Single-record and batch inference accept dictionaries shaped like NSL-KDD feature records. Missing NSL-KDD feature columns are filled with safe defaults before scoring so the demo can work with compact examples.

Each prediction returns:

- binary classification
- attack category
- confidence score when `predict_proba` is available
- analyst-style explanation

## FastAPI Demo Flow

The FastAPI app exposes:

- `GET /health`
- `POST /train`
- `POST /predict`
- `POST /predict/batch`
- `POST /report/incidents`
- `GET /demo`

The `/demo` page provides a simple browser form for submitting one network record and viewing the JSON prediction response.

## Testing Approach

The test suite covers:

- existing target mapping, preprocessing, data loading, and CLI smoke behavior
- detection service model loading and scoring
- incident report summaries
- FastAPI health, demo, prediction, and report routes

API tests use tiny deterministic saved models so they stay fast and do not require full NSL-KDD training.

## Limitations

- NSL-KDD is a benchmark dataset and does not represent modern production traffic by itself.
- The analyst explanations are concise heuristics layered around model output, not full feature-attribution explanations.
- The default model choices are intentionally simple and scikit-learn based for class-demo clarity.
- `/train` is synchronous, so a large training run blocks the API worker during the request.

## Future Work

- Add richer explanation methods such as permutation importance or SHAP-style summaries.
- Add asynchronous training jobs and persisted run history.
- Add uploaded CSV batch scoring.
- Add model cards with dataset, metrics, and known caveats.
- Wrap the detection and reporting services in a later autonomous agent integration without changing the pure ML core.

