# ML Group Project Report

## Real-World Problem

Enterprise networks face constant intrusion attempts: denial-of-service floods, probing scans, unauthorized access (R2L), and privilege escalation (U2R). Security teams cannot inspect every connection manually. **Network intrusion detection** uses connection-level features (protocol, service, byte volumes, error rates, host statistics) to flag suspicious traffic before damage spreads. Big-data ML fits because traffic volume is huge, labels are noisy, and nonlinear interactions among features matter. This project uses supervised learning on **NSL-KDD** to learn **normal vs attack** patterns and to quantify tradeoffs between catching attacks and burdening analysts with false alarms.

## Dataset Selection: NSL-KDD

We use **NSL-KDD** ([Kaggle `hassan06/nslkdd`](https://www.kaggle.com/datasets/hassan06/nslkdd)), an improved version of the KDD Cup 1999 data. It includes **KDDTrain+** and **KDDTest+** with **41 traffic features**, a **label** (e.g. `normal`, `neptune`, `satan`), and a **`difficulty_level`** field used in benchmark studies—not as an input feature.

We chose NSL-KDD because it is a **standard benchmark** for intrusion detection, includes both normal and many attack types, and separates training and test sets so we can report **honest generalization**. Limitations include age (traffic patterns have evolved) and a **class imbalance** (some attack types are rare).

## EDA Workflow

**What we did.** We loaded training data with explicit column names, counted rows and labels, mapped the 23 attack labels into high-level categories (**Normal, DoS, Probing, R2L, U2R**) for visualization, and plotted top services, TCP connection flags, numeric distributions (e.g. `duration`, `src_bytes`), and mean **serror / rerror** rates by category.

**Dataset size (combined train+test).** **148,517** rows (**125,973** train, **22,544** test), **41** predictive features plus `label` and `difficulty_level`.

**Quality.** **No missing values** and **no duplicate rows** in the combined frame used for summary statistics.

**Outliers.** Features such as **duration** and **src_bytes** are **heavy-tailed**; large values often correspond to attacks rather than erroneous measurements, so we did not winsorize for EDA.

**Cleaning.** We assigned column names to raw CSV rows, and we **exclude `difficulty_level` from modeling** because it is a benchmark metadata column, not a network measurement.

**Findings.** The label distribution is **imbalanced**: `normal` and high-volume attacks (e.g. **neptune**) dominate; rare classes (e.g. **U2R**) have few examples. **Error-rate** features (`serror_rate`, `rerror_rate`, etc.) show different **fingerprints** by attack category in the heatmap in `EDA.ipynb`. **Service** and **flag** distributions differ between normal and attack traffic.

**Proposed next steps.** Train **binary classifiers** (normal vs attack) with interpretable and tree-based models; report **precision, recall, F1, and confusion matrices**; optionally extend to multiclass or cost-sensitive learning given imbalance.

**Business questions for ML.** (1) Can we **automatically flag** likely intrusions with acceptable **false alarm** rates? (2) Which features drive alerts so analysts can **prioritize** investigations?

## Data Preparation

- **Target:** binary indicator **1 = attack**, **0 = normal** (all labels other than `normal`).
- **Features:** all columns except `label` and **`difficulty_level`** (and `difficulty` if present in other exports).
- **Categorical:** `protocol_type`, `service`, `flag` — missing values imputed with **most frequent**, then **one-hot** encoded (unknown categories ignored at test time).
- **Numeric:** remaining columns — **median** imputation, **standard scaling**.
- **Split:** use the dataset’s **native train/test files** (no random split on train).

## ML Methodology and Algorithms

**Algorithms.**

1. **Logistic regression** — linear baseline, fast to train, coefficients support qualitative interpretation of feature directions after preprocessing.
2. **Random forest (300 trees)** — captures **nonlinear** interactions and feature importance without manual feature crosses; strong baseline on mixed categorical/numeric data after encoding.

**Metrics.** **Accuracy**, **precision**, **recall**, **F1** (binary average), and **confusion matrix** on **KDDTest+**. For security, **recall** matters for catching attacks; **precision** matters to limit alert fatigue.

**Code walk-through (`src/train_models.py`).** `build_preprocessor` builds a **ColumnTransformer**: one branch for categoricals (impute → one-hot), one for numerics (impute → scale). `build_models` wraps the same preprocessor with each estimator. `train_and_evaluate_models` fits on **KDDTrain+** and evaluates on **KDDTest+**. `main.py` loads data via `load_nsl_kdd_frames`, writes EDA artifacts via `render_eda_artifacts`, then trains and writes `model_metrics.json` and `MODEL_METRICS.md`.

## Results and Metrics

On **22,544** test connections, **held-out** from training:

| Model | Accuracy | Precision | Recall | F1 |
| --- | ---: | ---: | ---: | ---: |
| Logistic regression | 0.7539 | 0.9176 | 0.6238 | 0.7427 |
| Random forest | **0.7772** | **0.9689** | 0.6288 | **0.7626** |

**Confusion matrices** (rows: true normal / attack; columns: predicted normal / attack):

- **Logistic regression:** normal: [8992, 719]; attack: [4828, 8005].
- **Random forest:** normal: [9452, 259]; attack: [4764, 8069].

**Analysis.** Random forest achieves **higher accuracy and precision** and **fewer false positives on normal traffic** (259 vs 719 false alarms in the “predicted attack” column for true normals). Both models show **moderate recall on attacks** (~0.62–0.63), so a non-trivial fraction of attacks are missed—consistent with a difficult test set and overlapping feature distributions. EDA showed **class imbalance and rare attack types**; improving recall may require **threshold tuning**, **class weights**, or **resampling**, at the cost of precision.

**Figures.** See `EDA.ipynb` for category, service, flag, and error-rate plots. Running `python main.py` generates `outputs/label_distribution.png`, `outputs/numeric_feature_boxplot.png`, and metric files (see Appendix).

## Interpretation and Recommendations

**For the data owner (security operations):** The tree-based model offers a **better precision–accuracy tradeoff** on this split, meaning **fewer false alerts per true positive** than logistic regression. Neither model should replace human judgment; both should feed a **ranked queue** for analysts.

**Recommendations.**

1. **Deploy review:** Use **random forest** scores as a first-stage filter; **audit** false negatives on business-critical subnets.
2. **Thresholding:** Tune the decision threshold on a **validation** slice to target a required **recall** or **max false positive rate**.
3. **Features to monitor:** Prioritize **protocol**, **service**, **flag**, and **error-rate** features—they appear in EDA and are included in the pipeline; use **permutation importance** from the forest for a data-driven ranking.
4. **Next modeling steps:** **Class weights** or **focal loss** analogs for imbalance; **multiclass** models per attack category; or **newer** tabular data and streaming features beyond NSL-KDD.

## Weekly Code Walkthrough Notes

- **Loader:** `src/data_loader.py` — KaggleHub download, `KDDTrain+` / `KDDTest+` paths.
- **EDA:** `src/eda.py` — `build_eda_summary`, `render_eda_artifacts`.
- **Training:** `src/train_models.py` — preprocessor, pipelines, metrics.
- **Entry point:** `main.py` — end-to-end run.

## Appendix

**Generated artifacts (after `python main.py`):** `outputs/eda_summary.json`, `outputs/model_metrics.json`, `outputs/MODEL_METRICS.md`, `outputs/label_distribution.png`, `outputs/numeric_feature_boxplot.png`.

**Key code — binary target and feature drop:**

```python
# src/train_models.py (conceptual)
METADATA_COLUMNS = ("difficulty", "difficulty_level")
features = frame.drop(columns=[TARGET_COLUMN, *METADATA_COLUMNS], errors="ignore")
target = (frame[TARGET_COLUMN].astype(str).str.lower() != "normal").astype(int)
```

**Preprocessor (sklearn ColumnTransformer):** categorical → `SimpleImputer(most_frequent)` → `OneHotEncoder(handle_unknown="ignore")`; numeric → `SimpleImputer(median)` → `StandardScaler()`.
