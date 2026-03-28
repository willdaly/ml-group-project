import pandas as pd

from src.data_loader import NSL_KDD_COLUMNS
from src.train_models import _binary_target, _split_features, build_preprocessor, train_and_evaluate_models


def test_binary_target_marks_attacks_as_one():
    result = _binary_target(pd.Series(["normal", "neptune", "smurf"]))
    assert result.tolist() == [0, 1, 1]


def test_build_preprocessor_handles_known_nsl_kdd_columns():
    frame = pd.DataFrame(
        {
            "protocol_type": ["tcp", "udp"],
            "service": ["http", "domain_u"],
            "flag": ["SF", "S0"],
            "src_bytes": [181, 239],
            "dst_bytes": [5450, 486],
        }
    )
    preprocessor = build_preprocessor(frame)
    assert preprocessor is not None


def test_split_features_drops_label_and_difficulty_metadata():
    row = {column: 0 for column in NSL_KDD_COLUMNS}
    row.update(
        {
            "protocol_type": "tcp",
            "service": "http",
            "flag": "SF",
            "src_bytes": 100,
            "label": "normal",
            "difficulty_level": 20,
        }
    )
    frame = pd.DataFrame([row])
    features, target = _split_features(frame)
    assert "label" not in features.columns
    assert "difficulty_level" not in features.columns
    assert "difficulty" not in features.columns
    assert target.iloc[0] == 0


def test_train_and_evaluate_models_smoke():
    rows = []
    for index in range(24):
        label = "normal" if index % 2 == 0 else "neptune"
        row = {column: 0 for column in NSL_KDD_COLUMNS}
        row.update(
            {
                "protocol_type": "tcp",
                "service": "http",
                "flag": "SF",
                "src_bytes": index * 10,
                "dst_bytes": index + 1,
                "label": label,
                "difficulty_level": 1,
            }
        )
        rows.append(row)
    train_df = pd.DataFrame(rows[:16])
    test_df = pd.DataFrame(rows[16:])
    results, *_ = train_and_evaluate_models(train_df, test_df)
    assert len(results) == 3
    assert {result["model"] for result in results} == {
        "logistic_regression",
        "random_forest",
        "gradient_boosting",
    }
    assert all(0 <= result["accuracy"] <= 1 for result in results)
