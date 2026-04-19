"""Backward-compatible imports for dataset-loading utilities."""

from src.core import data_loader as _core_data_loader
from src.core.data_loader import *  # noqa: F401,F403

kagglehub = _core_data_loader.kagglehub

