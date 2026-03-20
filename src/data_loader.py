"""Dataset-loading utilities for the NSL-KDD ML project scaffold."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Sequence

import kagglehub
import pandas as pd

DEFAULT_DATASET_HANDLE = os.getenv(
    "KAGGLEHUB_DATASET",
    "<set-your-nsl-kdd-kagglehub-handle>",
)

NSL_KDD_COLUMNS = [
    "duration",
    "protocol_type",
    "service",
    "flag",
    "src_bytes",
    "dst_bytes",
    "land",
    "wrong_fragment",
    "urgent",
    "hot",
    "num_failed_logins",
    "logged_in",
    "num_compromised",
    "root_shell",
    "su_attempted",
    "num_root",
    "num_file_creations",
    "num_shells",
    "num_access_files",
    "num_outbound_cmds",
    "is_host_login",
    "is_guest_login",
    "count",
    "srv_count",
    "serror_rate",
    "srv_serror_rate",
    "rerror_rate",
    "srv_rerror_rate",
    "same_srv_rate",
    "diff_srv_rate",
    "srv_diff_host_rate",
    "dst_host_count",
    "dst_host_srv_count",
    "dst_host_same_srv_rate",
    "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate",
    "dst_host_serror_rate",
    "dst_host_srv_serror_rate",
    "dst_host_rerror_rate",
    "dst_host_srv_rerror_rate",
    "label",
    "difficulty",
]


def _find_matching_file(root: Path, candidates: Sequence[str]) -> Path:
    lowered = {candidate.lower() for candidate in candidates}
    for path in root.rglob("*"):
        if path.is_file() and path.name.lower() in lowered:
            return path
    raise FileNotFoundError(f"Could not find any of {sorted(lowered)} under {root}")


def download_dataset(dataset_handle: str | None = None) -> Path:
    handle = (dataset_handle or DEFAULT_DATASET_HANDLE).strip()
    if not handle or handle.startswith("<"):
        raise ValueError(
            "Set KAGGLEHUB_DATASET to the KaggleHub handle for your NSL-KDD dataset before running this scaffold."
        )
    return Path(kagglehub.dataset_download(handle))


def load_nsl_kdd_frames(dataset_handle: str | None = None) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, str]]:
    dataset_root = download_dataset(dataset_handle)
    train_path = _find_matching_file(dataset_root, ["KDDTrain+.txt", "KDDTrain+.csv"])
    test_path = _find_matching_file(dataset_root, ["KDDTest+.txt", "KDDTest+.csv"])

    train_df = pd.read_csv(train_path, names=NSL_KDD_COLUMNS)
    test_df = pd.read_csv(test_path, names=NSL_KDD_COLUMNS)
    metadata = {
        "dataset_root": str(dataset_root),
        "train_path": str(train_path),
        "test_path": str(test_path),
    }
    return train_df, test_df, metadata
