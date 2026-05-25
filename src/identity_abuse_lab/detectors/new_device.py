from __future__ import annotations

from identity_abuse_lab.detectors.base import Detector
from identity_abuse_lab.telemetry.event import IdentityEvent


class NewDeviceRiskDetector(Detector):
    """Scores new-device enrollment or first-seen device events."""

    name = "new_device_risk"

    def score(self, event: IdentityEvent) -> float:
        if event.event_type != "new_device":
            return 0.0

        device_trust = str(event.attributes.get("device_trust", "unknown")).lower()
        after_reset = bool(event.attributes.get("after_reset", False))
        geo_change = bool(event.attributes.get("geo_change", False))

        if device_trust in {"blocked", "malicious"}:
            return 1.0
        if after_reset and geo_change:
            return 0.95
        if device_trust == "unknown" and geo_change:
            return 0.85
        if device_trust == "unknown":
            return 0.65
        return 0.25
