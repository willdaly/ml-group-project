# Architecture Notes

## Goal

The repository is organized as a reusable detection engine with a small demo layer. The structure keeps the class-project pipeline intact while making inference, reporting, and HTTP access easier to test and reuse.

## Module Layout

```text
src/
  core/
    data_loader.py   dataset resolution and NSL-KDD frame loading
    features.py      target mapping, preprocessing, feature-frame normalization
    models.py        scikit-learn model factories and joblib persistence
    train.py         training, evaluation, visualization, saved model artifacts
    infer.py         single and batch inference helpers
    explain.py       concise analyst-style explanation text
  services/
    training_service.py    full training workflow
    detection_service.py   model loading plus predict/predict_many
    reporting_service.py   incident summary aggregation
  api/
    app.py           FastAPI factory and `/demo`
    schemas.py       request and response models
    routes/          health, train, predict, and report routes
```

## Compatibility Layer

The original top-level modules remain available:

- `src/data_loader.py`
- `src/train_models.py`
- `src/eda.py`

They preserve existing import paths while delegating reusable logic into `src/core/`.

## Training Flow

```text
main.py or POST /train
  -> TrainingService.run_training
  -> load_nsl_kdd_frames
  -> build EDA summary and charts
  -> train/evaluate binary models
  -> train multiclass attack-category model
  -> save selected binary model and multiclass model
  -> return metrics and artifact paths
```

## Prediction Flow

```text
POST /predict
  -> DetectionService(model_dir)
  -> load binary_model.joblib and multiclass_model.joblib
  -> ensure incoming record has NSL-KDD feature columns
  -> score binary model
  -> score multiclass model for attack category when needed
  -> return confidence and analyst explanation
```

## Reporting Flow

```text
POST /report/incidents
  -> accept predictions or raw records
  -> generate predictions when records are supplied
  -> count normal vs attack records
  -> count attack categories
  -> summarize high-confidence attacks
```

## Saved Artifacts

```text
outputs/
  eda_summary.json
  MODEL_METRICS.md
  model_metrics.json
  plots and confusion matrices

models/
  binary_model.joblib
  multiclass_model.joblib
  metadata.json
```

## Design Boundaries

- Core modules do not import FastAPI.
- Services coordinate workflows but do not define HTTP schemas.
- API routes validate requests, call services, and return response models.
- Compatibility shims keep old imports stable for tests, notebooks, and class-submission scripts.

