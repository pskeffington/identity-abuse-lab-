from __future__ import annotations

from datetime import UTC, datetime

from identity_abuse_lab.telemetry.event import IdentityEvent
from identity_abuse_lab.telemetry.generators import ScenarioGenerator


class EnrichedScenarioGenerator(ScenarioGenerator):
    """Scenario generator with additional login and device-risk signals."""

    def __init__(self, base_time: datetime | None = None) -> None:
        super().__init__(base_time or datetime(2026, 1, 1, 9, 0, tzinfo=UTC))

    def manual_abuse(self) -> list[IdentityEvent]:
        abnormal_ip = "198.51.100.77"
        return [
            self._event(0, "email", "lure_received", self.user.normal_ip, {"variant": "manual"}),
            self._event(
                42,
                "idp",
                "login",
                abnormal_ip,
                {"geo_change": True, "unfamiliar_user_agent": True},
            ),
            self._event(
                49,
                "idp",
                "new_device",
                abnormal_ip,
                {"device_trust": "unknown", "geo_change": True},
            ),
            self._event(
                62,
                "idp",
                "oauth_consent",
                abnormal_ip,
                {"scopes": ["mail.read", "files.read.all"]},
            ),
            self._event(77, "saas", "saas_export", abnormal_ip, {"object_count": 650}),
        ]

    def ai_assisted_abuse(self) -> list[IdentityEvent]:
        abnormal_ip = "198.51.100.88"
        return [
            self._event(0, "email", "lure_received", self.user.normal_ip, {"variant": "ai_assisted"}),
            self._event(
                11,
                "idp",
                "login",
                abnormal_ip,
                {
                    "geo_change": True,
                    "unfamiliar_user_agent": True,
                    "anonymous_network": True,
                },
            ),
            self._event(
                13,
                "idp",
                "new_device",
                abnormal_ip,
                {"device_trust": "unknown", "geo_change": True, "after_reset": True},
            ),
            self._event(
                18,
                "idp",
                "oauth_consent",
                abnormal_ip,
                {"scopes": ["mail.read", "files.read.all", "offline_access"]},
            ),
            self._event(24, "saas", "saas_export", abnormal_ip, {"object_count": 900}),
        ]
