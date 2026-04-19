"""Lightweight analyst-style explanations for model predictions."""

from __future__ import annotations

from typing import Any


def explain_prediction(record: dict[str, Any], binary_label: str, attack_category: str, confidence: float | None) -> str:
    confidence_text = f" with {confidence:.1%} model confidence" if confidence is not None else ""
    if binary_label == "normal":
        return f"Traffic is classified as normal{confidence_text}; no immediate incident escalation is suggested."

    signals = []
    if float(record.get("serror_rate") or 0) > 0.5 or float(record.get("srv_serror_rate") or 0) > 0.5:
        signals.append("high connection error rates")
    if int(float(record.get("count") or 0)) > 100 or int(float(record.get("srv_count") or 0)) > 100:
        signals.append("elevated connection counts")
    if float(record.get("dst_host_serror_rate") or 0) > 0.5:
        signals.append("destination-host error concentration")
    if float(record.get("num_failed_logins") or 0) > 0:
        signals.append("failed login activity")

    if not signals:
        signals.append("feature patterns learned from NSL-KDD attacks")

    signal_text = ", ".join(signals)
    return (
        f"Traffic is classified as an {attack_category} attack{confidence_text}. "
        f"Primary contributing signals: {signal_text}."
    )

