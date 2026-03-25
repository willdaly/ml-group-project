---
marp: true
title: ML Group Project Presentation
paginate: true
---

# ML Group Project Presentation

## Slide 1: Title Slide

- **Project:** Machine Learning for Network Intrusion Detection with NSL-KDD
- **Course:** [Add course name and section]
- **Group members:** [Replace with student names]
- **Date:** [Add presentation date]

**Opening line:** Our project asks whether machine learning can detect malicious network traffic early enough to support a real security operations workflow.

---

## Slide 2: Business Problem

- Enterprise networks generate too many connections for manual review.
- Security teams need to catch attacks without overwhelming analysts with false alarms.
- **Business question:** Can we automatically flag suspicious connections while keeping the alert stream usable?
- **Why ML:** The data is high-volume, high-dimensional, and contains nonlinear relationships.

**Presenter note:** Emphasize that this is not only a classification exercise; it is an operations decision problem.

---

## Slide 3: Dataset And Why We Chose It

- **Dataset:** NSL-KDD
- **Files used:** `KDDTrain+.txt` and `KDDTest+.txt`
- **Rows:** 125,973 train + 22,544 test = 148,517 total
- **Columns:** 41 predictive features plus `label` and `difficulty_level`
- **Why we chose it:** established intrusion-detection benchmark, clear train/test split, strong fit for the course topic
- **Submission packaging:** local copy included in `data/nsl-kdd/` so the project runs offline

**Citation footer:** Tavallaee et al. (2009); Kaggle mirror: `hassan06/nslkdd`

---

## Slide 4: EDA And Data Quality

- Combined train/test summary showed **0 missing values** and **0 duplicate rows**
- Label distribution is imbalanced: normal traffic and a few high-volume attack types dominate
- Numeric features such as `duration` and `src_bytes` are heavily skewed
- Service, flag, and error-rate variables show strong signal for attack detection

**Visuals to include:**

- `outputs/label_distribution.png`
- `outputs/numeric_feature_boxplot.png`
- One screenshot or figure from `EDA.ipynb`

---

## Slide 5: Data Preparation

- **Target:** `normal = 0`, all attack labels = `1`
- **Dropped from features:** `label`, `difficulty_level`
- **Categorical fields:** `protocol_type`, `service`, `flag`
- **Categorical preprocessing:** most-frequent imputation + one-hot encoding
- **Numeric preprocessing:** median imputation + standard scaling

**Code snippet:**

```python
METADATA_COLUMNS = ("difficulty", "difficulty_level")
features = frame.drop(columns=[TARGET_COLUMN, *METADATA_COLUMNS], errors="ignore")
target = (frame[TARGET_COLUMN].astype(str).str.lower() != "normal").astype(int)
```

---

## Slide 6: ML Algorithms And Why

- **Logistic regression**
  - Fast baseline
  - Easy to explain
  - Useful for comparison
- **Random forest**
  - Captures nonlinear interactions
  - Handles mixed-feature patterns well after preprocessing
  - Often strong on tabular security data

**Metrics used:** accuracy, precision, recall, F1, confusion matrix

**Presenter note:** Explain that recall matters for missed attacks, while precision matters for analyst workload.

---

## Slide 7: Predictive Analytics Results

| Model | Accuracy | Precision | Recall | F1 |
| --- | ---: | ---: | ---: | ---: |
| Logistic regression | 0.7539 | 0.9176 | 0.6238 | 0.7427 |
| Random forest | **0.7772** | **0.9689** | **0.6288** | **0.7626** |

- Random forest had the best overall performance
- Biggest gain: fewer false positives on normal traffic
- Both models still missed a meaningful share of attacks

**Talking point:** This means the best model is useful, but not ready to replace human judgment.

---

## Slide 8: Prescriptive Analytics And Recommendations

- Use the **random forest** as the first-pass detection model
- Tune the threshold to increase recall when the cost of missed attacks is high
- Monitor **service**, **flag**, and **error-rate** features closely
- Test class weighting or resampling to improve rare-attack detection
- Expand later to multiclass attack-family prediction

**Key message:** The model should feed a ranked analyst queue, not operate as a fully autonomous blocker.

---

## Slide 9: Code Walk-Through

- `src/data_loader.py` — resolves the local dataset path and loads the train/test files
- `src/eda.py` — produces summary statistics and plots
- `src/train_models.py` — builds preprocessing and trains the baseline models
- `main.py` — runs the full pipeline end to end
- `EDA.ipynb` — interactive visual exploration for class discussion

**Demo command:**

```bash
python main.py --data-dir data/nsl-kdd --output-dir outputs
```

---

## Slide 10: Conclusion

- ML can support intrusion detection on NSL-KDD with useful baseline performance
- Random forest provided the strongest balance of precision and overall effectiveness
- The project produced both a data story and an operational recommendation
- The repository is submission-ready and reproducible offline

**Close:** Our final recommendation is to treat the random forest model as a decision-support tool and improve recall through threshold tuning and imbalance-aware training.
