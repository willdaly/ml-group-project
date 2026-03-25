"""Tests for main entry point."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pandas as pd

from main import main
from src.data_loader import NSL_KDD_COLUMNS


def _minimal_frames():
    rows = []
    for index in range(12):
        label = "normal" if index % 2 == 0 else "neptune"
        row = {column: 0 for column in NSL_KDD_COLUMNS}
        row.update(
            {
                "protocol_type": "tcp",
                "service": "http",
                "flag": "SF",
                "src_bytes": index * 5,
                "dst_bytes": index + 1,
                "label": label,
                "difficulty_level": 1,
            }
        )
        rows.append(row)
    train_df = pd.DataFrame(rows[:8])
    test_df = pd.DataFrame(rows[8:])
    meta = {"dataset_root": "/tmp/mock"}
    return train_df, test_df, meta


@patch("main.load_nsl_kdd_frames")
def test_main_runs_without_kaggle_download(mock_load, tmp_path: Path) -> None:
    mock_load.return_value = _minimal_frames()
    out = tmp_path / "out"
    code = main(["--output-dir", str(out)])
    assert code == 0
    assert (out / "eda_summary.json").is_file()
    assert (out / "model_metrics.json").is_file()
    assert (out / "MODEL_METRICS.md").is_file()
