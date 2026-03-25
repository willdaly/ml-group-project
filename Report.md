# ML Group Project Report

## Project Title

**Machine Learning for Network Intrusion Detection with NSL-KDD**

## Real-World Problem

Enterprise networks generate far more traffic than a human analyst can review manually. Security teams need a way to identify suspicious connections quickly enough to stop denial-of-service attacks, probes, and unauthorized access before the damage spreads. This is a strong machine-learning problem because the traffic is high-volume, the feature space mixes categorical and numeric signals, and the relationships between variables are not always obvious from simple rules alone.

This project studies whether machine-learning models can distinguish normal network traffic from malicious traffic in a way that is useful for a security operations team. The practical business question is straightforward: can the organization catch more attacks while keeping false alarms low enough that analysts can still trust and use the system?

## Dataset Selection And Rationale

The group selected the **NSL-KDD** benchmark dataset, using the local submission copy in `data/nsl-kdd/` and the Kaggle mirror maintained at [Kaggle](https://www.kaggle.com/datasets/hassan06/nslkdd). NSL-KDD is a cleaned and improved version of the original KDD Cup 1999 intrusion-detection dataset and remains a common baseline for network intrusion research (Tavallaee et al., 2009).

We chose this dataset for four reasons:

1. It directly matches the course theme of malware and network intrusion detection.
2. It provides labeled train and test files, which supports an honest held-out evaluation.
3. It contains 41 traffic features plus labels, giving enough signal for both EDA and supervised learning.
4. It is widely cited, which makes it a credible benchmark for a classroom project.

The combined dataset contains **148,517** rows: **125,973** in `KDDTrain+` and **22,544** in `KDDTest+`. Each record represents a network connection and includes protocol, service, TCP flag, byte counts, login indicators, error rates, and host-level aggregate statistics.

## EDA Workflow And Findings

### What We Did In Exploration

The project loads the training and test files with explicit NSL-KDD column names, combines them for summary statistics, and then explores label frequencies, service distribution, connection flags, and representative numeric features. The notebook `EDA.ipynb` handles the more visual exploration, while `main.py` reproduces the key EDA artifacts into `outputs/` for submission.

### Data Volume And Structure

- Rows: **148,517**
- Predictive features: **41**
- Additional fields: `label` and `difficulty_level`
- Splits used: the dataset's original train/test files

### Missing Data, Duplicates, And Cleanliness

The combined summary shows **0 missing values** and **0 duplicate rows**. That allowed the project to focus more on feature encoding and class balance than on record repair.

### Outliers And Suspicious Values

Several numeric variables, especially `duration` and `src_bytes`, are strongly right-skewed. These values were not automatically removed as outliers because in intrusion detection they can be meaningful indicators of attack behavior rather than bad data.

### Cleaning And Preparation Decisions

- Assigned explicit schema names to the raw text files
- Excluded `difficulty_level` from modeling because it is benchmark metadata rather than a real traffic feature
- Converted the multiclass attack labels into a binary target: `normal = 0`, `attack = 1`
- One-hot encoded the categorical fields `protocol_type`, `service`, and `flag`
- Median-imputed and standardized the numeric columns

### What We Found

EDA surfaced a clear class-imbalance pattern: normal traffic and a few high-volume attacks dominate the dataset, while rare attack types such as U2R appear only a handful of times. Service, flag, and error-rate variables also show visible separation between benign and malicious traffic. Those patterns mattered because they justified the chosen preprocessing pipeline and explained why accuracy alone would not be enough to evaluate success.

### Proposed Next Steps From EDA

The exploration suggested three modeling priorities:

1. Start with a binary classifier before attempting fine-grained attack-type prediction.
2. Compare an interpretable linear model with a nonlinear ensemble.
3. Report precision, recall, F1, and confusion matrices so the class imbalance does not hide weak attack detection.

## Machine Learning Methodology

### Algorithms Used And Why

The final pipeline compares two supervised models:

1. **Logistic regression**: a strong baseline that is easy to explain and fast to train.
2. **Random forest**: an ensemble model that can capture nonlinear interactions across encoded categorical and numeric variables.

These models were selected because together they offer a useful tradeoff between interpretability and predictive flexibility.

### Metrics Used

The project evaluates each model on the held-out `KDDTest+` file using:

- Accuracy
- Precision
- Recall
- F1 score
- Confusion matrix

These metrics align with the business problem. Security teams care about **recall** because missed attacks are costly, but they also care about **precision** because too many false positives create alert fatigue.

### Code Walk-Through

The code is organized so each stage of the workflow is easy to explain in class:

- `src/data_loader.py` resolves the dataset path, supports offline local data, and loads `KDDTrain+` and `KDDTest+`
- `src/eda.py` computes dataset-level summary statistics and exports chart artifacts
- `src/train_models.py` builds the preprocessing pipeline with `ColumnTransformer`, fits the baseline models, and writes evaluation metrics
- `main.py` ties the full workflow together so a single command reproduces the project outputs

## Results And Analysis

The models were evaluated on **22,544** held-out network connections.

| Model | Accuracy | Precision | Recall | F1 |
| --- | ---: | ---: | ---: | ---: |
| Logistic regression | 0.7539 | 0.9176 | 0.6238 | 0.7427 |
| Random forest | **0.7772** | **0.9689** | **0.6288** | **0.7626** |

### Confusion Matrices

- Logistic regression: normal `[8992, 719]`; attack `[4828, 8005]`
- Random forest: normal `[9452, 259]`; attack `[4764, 8069]`

### Interpretation

The random forest performed best overall. Its largest advantage is precision: it produced far fewer false alarms on normal traffic than logistic regression. That makes it more practical as an analyst-facing first-stage filter. Both models still missed a meaningful number of attacks, which shows that NSL-KDD remains a challenging classification problem even for a reasonably strong baseline.

The result matches the EDA story. Because the dataset contains mixed feature types and nonlinear relationships, the tree-based model was better able to capture the useful interactions. At the same time, the moderate recall values confirm that class imbalance and attack overlap remain important limitations.

## Predictive And Prescriptive Analytics

### Predictive Analytics

The predictive portion of the project answers the question: **can the model forecast whether a connection is malicious?** The answer is yes. Both models separated attack traffic from normal traffic better than chance, and the random forest produced the strongest overall balance of accuracy, precision, and F1.

### Prescriptive Analytics

The prescriptive part of the project focuses on what the data owner should do next based on those results:

1. Use the random forest as the initial detection model for analyst review queues.
2. Tune the decision threshold to target a higher operational recall when attack coverage matters more than alert volume.
3. Monitor service, flag, and error-rate features because they appear to carry the strongest signal.
4. Test class-weighted or resampled models to improve performance on rare attack behaviors.
5. Extend the workflow to multiclass attack-family prediction after the binary baseline is stable.

## Conclusion

This project shows that machine learning can support intrusion detection in a practical and defensible way. On the NSL-KDD benchmark, both baseline models detected malicious traffic patterns, and the random forest offered the better operating tradeoff for a real-world security team. The analysis also showed why the problem is difficult: the dataset is imbalanced, some attacks are rare, and not every malicious connection is easy to distinguish from normal behavior.

From a stakeholder perspective, the most useful takeaway is not simply that one model scored higher than another. The more important result is that the project identifies a reproducible workflow for loading security data, exploring class structure, encoding mixed features, evaluating baseline models, and turning those outputs into recommendations for analyst operations. That makes the work suitable both as a classroom presentation and as a foundation for a more advanced intrusion-detection system.

## References

Tavallaee, M., Bagheri, E., Lu, W., & Ghorbani, A. A. (2009). *A detailed analysis of the KDD CUP 99 data set*. 2009 IEEE Symposium on Computational Intelligence for Security and Defense Applications. https://doi.org/10.1109/CISDA.2009.5356528

hassan06. (n.d.). *NSL-KDD* [Data set]. Kaggle. https://www.kaggle.com/datasets/hassan06/nslkdd

## Appendix

- Reproducible pipeline entry point: `python main.py --data-dir data/nsl-kdd --output-dir outputs`
- EDA notebook: `EDA.ipynb`
- Generated artifacts: `outputs/eda_summary.json`, `outputs/model_metrics.json`, `outputs/MODEL_METRICS.md`, `outputs/label_distribution.png`, `outputs/numeric_feature_boxplot.png`
