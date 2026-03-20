import pandas as pd

from src.train_models import _binary_target, build_preprocessor


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
