from __future__ import annotations

from identity_abuse_lab.detectors.base import Detector
from identity_abuse_lab.telemetry.event import IdentityEvent


class AbnormalLoginDetector(Detector):
    """Scores login events with abnormal context signals."""

    name = "abnormal_login"

    def score(self, event: IdentityEvent) -> float:
        if event.event_type != "login":
            return 0.0

        geo_change = bool(event.attributes.get("geo_change", False))
        impossible_travel = bool(event.attributes.get("impossible_travel", False))
        unfamiliar_user_agent = bool(event.attributes.get("unfamiliar_user_agent", False))
        anonymous_network = bool(event.attributes.get("anonymous_network", False))

        signal_count = sum(
            [geo_change, impossible_travel, unfamiliar_user_agent, anonymous_network]
        )

        if signal_count >= 3:
            return 1.0
        if signal_count == 2:
            return 0.8
        if signal_count == 1:
            return 0.55
        return 0.0
