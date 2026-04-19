# Presentation Notes

## 1. Title / Overview

NSL-KDD Cybersecurity Detection Engine

One-sentence story: a class ML pipeline was refactored into a reusable intrusion-detection engine with saved models, inference services, incident reports, and a browser demo.

## 2. Problem

Network defenders need fast ways to separate normal traffic from suspicious activity. The project uses supervised learning to classify connection records and summarize likely incidents for an analyst.

## 3. Dataset

Dataset: NSL-KDD

Key points:

- tabular network connection records
- protocol, service, byte counts, error rates, and host-level traffic statistics
- labels for normal traffic and multiple attack types
- standard attack categories: DoS, Probe, R2L, U2R, and Normal

## 4. Modeling Approach

Binary task:

- normal vs attack
- Logistic Regression, Random Forest, Gradient Boosting
- best model selected by F1 score

Multiclass task:

- attack-category classification
- Random Forest over five NSL-KDD categories

Preprocessing:

- one-hot encoding for categorical fields
- median imputation and scaling for numeric fields

## 5. Refactor

Before:

- compact class-submission pipeline
- training and artifact generation centered around `main.py`

After:

- reusable ML core
- service layer for training, detection, and reporting
- FastAPI routes for demo workflows
- saved model artifacts for repeatable inference

## 6. Architecture

Core:

- data loading
- feature engineering
- model training
- inference
- explanations

Services:

- full training workflow
- detection service
- incident reporting

API:

- health check
- train endpoint
- single and batch prediction
- incident report
- browser demo

## 7. Demo

Demo sequence:

1. Run training or show saved `models/` artifacts.
2. Start FastAPI with `uvicorn src.api.app:app --reload`.
3. Open `/demo`.
4. Submit one network record.
5. Show binary class, attack category, confidence, and explanation.
6. Call `/report/incidents` to summarize one or more predictions.

## 8. Results

Show generated artifacts:

- `outputs/MODEL_METRICS.md`
- binary confusion matrices
- ROC curves
- multiclass confusion matrix
- feature importance plot

Explain that the exact scores depend on the train/test split included with NSL-KDD and the selected model.

## 9. Limitations

- NSL-KDD is useful for learning but not a modern production traffic corpus.
- Explanations are concise analyst summaries, not full causal explanations.
- Training endpoint is synchronous and intended for demos.
- Models are classical scikit-learn baselines, kept readable for the class project.

## 10. Future Work

- richer explanations
- uploaded CSV batch scoring
- asynchronous training jobs
- model cards and run history
- later autonomous agent wrapper around the service layer

