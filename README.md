# ML Group Project

## Overview

This repository packages a complete NSL-KDD intrusion-detection project for class submission. It includes the dataset, exploratory analysis, reproducible model-training code, generated artifacts, a written report, and a slide-ready presentation outline.

## Submission Contents

- `data/nsl-kdd/` — Local copy of `KDDTrain+.txt` and `KDDTest+.txt` for offline grading.
- `EDA.ipynb` — Interactive exploration and visual analysis (styled, used for class presentation).
- `01_eda_nsl_kdd.ipynb` — Full methodical EDA walkthrough on the complete training set with fine-grained attack-type breakdowns.
- `main.py` and `src/` — End-to-end pipeline for EDA artifacts and baseline ML models.
- `outputs/` — Generated charts and model metrics included with the submission.
- `Report.pdf` — Final written report (submission copy).
- `PRESENTATION.pptx` — Slide deck with embedded charts (submission copy).
- `drafts/` — Markdown source files for the report and presentation.
- `SUBMISSION_CHECKLIST.md` — Quick turn-in checklist mapped to the assignment.

## Setup

```bash
pip install -r requirements.txt
```

## Run The Project

The repository is now self-contained and runs offline with the included dataset:

```bash
python main.py --data-dir data/nsl-kdd --output-dir outputs
```

Optional Kaggle fallback still works when internet access is available:

```bash
python main.py --dataset hassan06/nslkdd --output-dir outputs
```

## Run Tests

```bash
pytest
```
