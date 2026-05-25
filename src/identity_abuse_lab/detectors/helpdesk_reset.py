from __future__ import annotations

from identity_abuse_lab.detectors.base import Detector
from identity_abuse_lab.telemetry.event import IdentityEvent


class HelpdeskResetDetector(Detector):
    """Scores help-desk reset and account recovery events."""

    name = "helpdesk_reset_risk"

    def score(self, event: IdentityEvent) -> float:
        if event.event_type != "helpdesk_reset":
            return 0.0

        reset_channel = str(event.attributes.get("reset_channel", "unknown")).lower()
        identity_verified = bool(event.attributes.get("identity_verified", True))
        urgent_request = bool(event.attributes.get("urgent_request", False))
        geo_change = bool(event.attributes.get("geo_change", False))
        executive_claim = bool(event.attributes.get("executive_claim", False))

        signal_count = sum(
            [
                reset_channel == "helpdesk",
                not identity_verified,
                urgent_request,
                geo_change,
                executive_claim,
            ]
        )

        if signal_count >= 4:
            return 1.0
        if signal_count == 3:
            return 0.85
        if signal_count == 2:
            return 0.65
        if signal_count == 1:
            return 0.35
        return 0.0
