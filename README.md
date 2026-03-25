# ML Group Project

## Overview

This repository implements the NSL-KDD intrusion-detection workflow: exploratory analysis (`EDA.ipynb`), reproducible EDA artifacts and baseline models (`main.py`), and written deliverables (`Report.md`, `PRESENTATION.md`).

## Full Assignment

See `ASSIGNMENT.md` for the complete assignment brief.

## Due Date

2026-04-04T03:59:59Z

## Setup

```bash
pip install -r requirements.txt
```

[KaggleHub](https://github.com/Kaggle/kagglehub) downloads the dataset on first run. The default handle is `hassan06/nslkdd`. Override with the environment variable `KAGGLEHUB_DATASET` or `python main.py --dataset your/handle`.

## Run the pipeline

```bash
python main.py
```

Optional:

```bash
python main.py --output-dir outputs --dataset hassan06/nslkdd
```

This loads `KDDTrain+.txt` and `KDDTest+.txt`, writes `eda_summary.json`, EDA plots, `model_metrics.json`, and `MODEL_METRICS.md` under `outputs/` (ignored by git).

## Notebook vs script

- **`EDA.ipynb`** — Interactive exploration, plots, and Phase I narrative (attack categories, services, distributions).
- **`main.py`** — Same dataset definitions as the notebook; regenerates summary statistics and trains/evaluates baseline models for the report.

## Running tests

```bash
pytest
```

## Course context

See `COURSE_CONTEXT.md` for relevant excerpts from course materials.

## Deliverables in repo

- `Report.md` — Written report (Phase I and II).
- `PRESENTATION.md` — Slide outline and talking points.
- `src/` — Shared loaders, EDA helpers, and sklearn pipelines.
