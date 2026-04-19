"""Incident-report summaries built from detection results."""

from __future__ import annotations

from collections import Counter
from typing import Any


class ReportingService:
    def build_incident_report(self, predictions: list[dict[str, Any]]) -> dict[str, Any]:
        total = len(predictions)
        attacks = [item for item in predictions if item.get("binary_class") == "attack"]
        categories = Counter(item.get("attack_category", "Unknown") for item in attacks)
        high_confidence = [
            item
            for item in attacks
            if item.get("confidence") is not None and float(item.get("confidence")) >= 0.8
        ]

        if not attacks:
            summary = "No attack traffic detected in the submitted records."
        else:
            top_category, top_count = categories.most_common(1)[0]
            summary = f"Detected {len(attacks)} attack records out of {total}; most common category is {top_category} ({top_count})."

        return {
            "total_records": total,
            "attack_records": len(attacks),
            "normal_records": total - len(attacks),
            "attack_categories": dict(categories),
            "high_confidence_attack_records": len(high_confidence),
            "summary": summary,
        }

