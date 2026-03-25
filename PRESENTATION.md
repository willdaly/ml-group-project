# ML Group Project — Presentation

## Slide 1: Business problem

- Networks see huge connection volume; manual review does not scale.
- **Goal:** Flag **intrusions** early using connection-level features, balancing **catching attacks** (recall) with **analyst workload** (precision / false alarms).
- **Why ML:** High dimensionality, nonlinear patterns, labeled historical traffic (e.g. NSL-KDD).

---

## Slide 2: Dataset — NSL-KDD

- **Source:** NSL-KDD (`hassan06/nslkdd` via KaggleHub) — train and test files **KDDTrain+** / **KDDTest+**.
- **Size:** **125,973** train + **22,544** test rows; **41** features + label + `difficulty_level` (metadata only).
- **Why this dataset:** Standard IDS benchmark; honest train/test split; multiple attack families.
- **Caveat:** Dated traffic; **class imbalance** (rare attack types).

---

## Slide 3: EDA highlights

- **Quality:** **0** missing values, **0** duplicate rows (combined summary).
- **Labels:** Dominated by `normal` and high-volume attacks (e.g. DoS); rare classes exist.
- **Plots (see `EDA.ipynb`):** Attack **category** mix; top **services** and **flags**; **duration** / **src_bytes** normal vs attack; **error-rate heatmap** by category.
- **Takeaway:** Categorical and error-rate features carry signal; imbalance motivates careful metrics (**precision/recall/F1**), not accuracy alone.

---

## Slide 4: Preprocessing and target

- **Target:** `normal` → 0, any attack label → 1.
- **Drop:** `label`, **`difficulty_level`** (not a traffic feature).
- **Categorical** (`protocol_type`, `service`, `flag`): impute → **one-hot**.
- **Numeric:** median impute → **standardize**.

**Snippet — feature/target split:**

```python
METADATA_COLUMNS = ("difficulty", "difficulty_level")
features = frame.drop(columns=[TARGET_COLUMN, *METADATA_COLUMNS], errors="ignore")
target = (frame[TARGET_COLUMN].astype(str).str.lower() != "normal").astype(int)
```

---

## Slide 5: Models and metrics

- **Models:** **Logistic regression** (interpretable linear boundary) vs **Random forest** (300 trees, nonlinear).
- **Metrics:** Accuracy, precision, recall, F1, confusion matrix on **held-out KDDTest+**.
- **Why these metrics:** Security teams care about **missed attacks** (recall) and **false alerts** (precision).

---

## Slide 6: Results (test set)

| Model | Accuracy | Precision | Recall | F1 |
| --- | ---: | ---: | ---: | ---: |
| Logistic regression | 0.754 | 0.918 | 0.624 | 0.743 |
| Random forest | **0.777** | **0.969** | 0.629 | **0.763** |

- Random forest: **fewer false positives on normal traffic** (better precision).
- Both models: **moderate attack recall** — room for threshold tuning / class weights.

**Snippet — end-to-end entry point:**

```python
# main.py
train_df, test_df, metadata = load_nsl_kdd_frames(dataset_handle=args.dataset)
summary = build_eda_summary(train_df, test_df, metadata)
render_eda_artifacts(train_df, summary, output_dir=args.output_dir)
results = train_and_evaluate_models(train_df, test_df)
write_model_artifacts(results, output_dir=args.output_dir)
```

---

## Slide 7: Recommendations and code walkthrough roles

- **Recommendations:** Use RF scores as a **first filter**; **tune thresholds** for operational recall targets; monitor **service/flag/error-rate** features; consider **class weights** for rare attacks.
- **Group walkthrough:**  
  - Member A: `EDA.ipynb` — categories and heatmap.  
  - Member B: `src/data_loader.py` + `main.py`.  
  - Member C: `src/train_models.py` — `ColumnTransformer` and metrics.
