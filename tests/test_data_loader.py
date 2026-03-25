from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pandas as pd

from src.data_loader import NSL_KDD_COLUMNS, load_nsl_kdd_frames


def _write_frame(path: Path, labels: list[str]) -> None:
    rows = []
    for index, label in enumerate(labels):
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

    pd.DataFrame(rows, columns=NSL_KDD_COLUMNS).to_csv(path, index=False, header=False)


@patch("src.data_loader.kagglehub.dataset_download", side_effect=AssertionError("download should not be called"))
def test_load_nsl_kdd_frames_prefers_local_data_dir(_mock_download, tmp_path: Path) -> None:
    dataset_root = tmp_path / "nsl-kdd"
    dataset_root.mkdir()
    _write_frame(dataset_root / "KDDTrain+.txt", ["normal", "neptune"])
    _write_frame(dataset_root / "KDDTest+.txt", ["normal"])

    train_df, test_df, metadata = load_nsl_kdd_frames(data_dir=dataset_root)

    assert len(train_df) == 2
    assert len(test_df) == 1
    assert metadata["dataset_source"] == "local_path"
    assert metadata["dataset_root"] == str(dataset_root)
