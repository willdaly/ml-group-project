"""Backward-compatible imports for model training utilities."""

from src.core.features import build_preprocessor
from src.core.models import build_models
from src.core.train import (  # noqa: F401
    _binary_target,
    _evaluate_model,
    _get_feature_names,
    _multiclass_target,
    _split_features,
    _split_features_multiclass,
)
from src.core.train import *  # noqa: F401,F403
