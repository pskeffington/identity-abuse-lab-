from __future__ import annotations

from identity_abuse_lab.detectors.base import Detector
from identity_abuse_lab.telemetry.event import IdentityEvent


class SaaSExportAnomalyDetector(Detector):
    """Scores SaaS export events based on exported object volume."""

    name = "saas_export_anomaly"

    def __init__(self, medium_threshold: int = 50, high_threshold: int = 500) -> None:
        self.medium_threshold = medium_threshold
        self.high_threshold = high_threshold

    def score(self, event: IdentityEvent) -> float:
        if event.event_type != "saas_export":
            return 0.0

        object_count = int(event.attributes.get("object_count", 0))
        if object_count >= self.high_threshold:
            return 1.0
        if object_count >= self.medium_threshold:
            return 0.65
        if object_count > 0:
            return 0.2
        return 0.0
