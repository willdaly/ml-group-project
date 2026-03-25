"""Dataset-loading utilities for the NSL-KDD ML project scaffold."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Sequence

import kagglehub
import pandas as pd

DEFAULT_DATASET_HANDLE = os.getenv("KAGGLEHUB_DATASET", "hassan06/nslkdd")
LOCAL_DATASET_ENV = "NSL_KDD_DATA_DIR"
REPO_DATASET_ROOT = Path(__file__).resolve().parent.parent / "data" / "nsl-kdd"

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
    "difficulty_level",
]


def _find_matching_file(root: Path, candidates: Sequence[str]) -> Path:
    lowered = {candidate.lower() for candidate in candidates}
    for path in root.rglob("*"):
        if path.is_file() and path.name.lower() in lowered:
            return path
    raise FileNotFoundError(f"Could not find any of {sorted(lowered)} under {root}")


def _contains_nsl_kdd_files(root: Path) -> bool:
    try:
        _find_matching_file(root, ["KDDTrain+.txt", "KDDTrain+.csv"])
        _find_matching_file(root, ["KDDTest+.txt", "KDDTest+.csv"])
    except FileNotFoundError:
        return False
    return True


def _latest_cached_dataset_root(dataset_handle: str) -> Path | None:
    parts = [part.strip() for part in dataset_handle.split("/") if part.strip()]
    if len(parts) != 2:
        return None

    owner, dataset = parts
    versions_root = Path.home() / ".cache" / "kagglehub" / "datasets" / owner / dataset / "versions"
    if not versions_root.exists():
        return None

    version_paths = sorted(
        (path for path in versions_root.iterdir() if path.is_dir()),
        key=lambda path: (not path.name.isdigit(), int(path.name) if path.name.isdigit() else path.name),
    )
    for version_path in reversed(version_paths):
        if _contains_nsl_kdd_files(version_path):
            return version_path
    return None


def _resolve_local_dataset_root(data_dir: str | Path | None = None) -> Path | None:
    candidates = [
        data_dir,
        os.getenv(LOCAL_DATASET_ENV),
        REPO_DATASET_ROOT,
    ]
    for candidate in candidates:
        if not candidate:
            continue
        root = Path(candidate).expanduser()
        if root.exists() and _contains_nsl_kdd_files(root):
            return root
    return None


def download_dataset(dataset_handle: str | None = None, data_dir: str | Path | None = None) -> tuple[Path, str]:
    local_root = _resolve_local_dataset_root(data_dir)
    if local_root is not None:
        return local_root, "local_path"

    handle = (dataset_handle or DEFAULT_DATASET_HANDLE).strip()
    if not handle:
        raise ValueError("KAGGLEHUB_DATASET must be a non-empty KaggleHub dataset handle.")

    cached_root = _latest_cached_dataset_root(handle)
    if cached_root is not None:
        return cached_root, "kagglehub_cache"

    try:
        return Path(kagglehub.dataset_download(handle)), "kagglehub_download"
    except Exception as exc:  # pragma: no cover - network failures are environment-specific
        raise RuntimeError(
            "Unable to download the NSL-KDD dataset. Provide a local directory with "
            "KDDTrain+.txt and KDDTest+.txt via --data-dir or set NSL_KDD_DATA_DIR."
        ) from exc


def load_nsl_kdd_frames(
    dataset_handle: str | None = None,
    data_dir: str | Path | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, str]]:
    dataset_root, dataset_source = download_dataset(dataset_handle=dataset_handle, data_dir=data_dir)
    train_path = _find_matching_file(dataset_root, ["KDDTrain+.txt", "KDDTrain+.csv"])
    test_path = _find_matching_file(dataset_root, ["KDDTest+.txt", "KDDTest+.csv"])

    train_df = pd.read_csv(train_path, names=NSL_KDD_COLUMNS)
    test_df = pd.read_csv(test_path, names=NSL_KDD_COLUMNS)
    metadata = {
        "dataset_root": str(dataset_root),
        "dataset_source": dataset_source,
        "train_path": str(train_path),
        "test_path": str(test_path),
    }
    return train_df, test_df, metadata
