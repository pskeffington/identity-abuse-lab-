from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path
import json

from identity_abuse_lab.telemetry.event import IdentityEvent


@dataclass(frozen=True)
class SyntheticUser:
    """Synthetic lab user profile."""

    user_id: str
    normal_ip: str
    normal_user_agent: str


class ScenarioGenerator:
    """Generates controlled synthetic telemetry scenarios for identity-abuse research."""

    def __init__(self, base_time: datetime | None = None) -> None:
        self.base_time = base_time or datetime(2026, 1, 1, 9, 0, tzinfo=UTC)
        self.user = SyntheticUser(
            user_id="user-001",
            normal_ip="203.0.113.10",
            normal_user_agent="Mozilla/5.0 LabBrowser/1.0",
        )

    def baseline(self) -> list[IdentityEvent]:
        """Generate normal SaaS identity activity."""
        return [
            self._event(0, "idp", "login", self.user.normal_ip),
            self._event(8, "saas", "document_read", self.user.normal_ip, {"object_count": 3}),
            self._event(16, "saas", "document_read", self.user.normal_ip, {"object_count": 2}),
            self._event(28, "saas", "saas_export", self.user.normal_ip, {"object_count": 4}),
            self._event(40, "idp", "logout", self.user.normal_ip),
        ]

    def manual_abuse(self) -> list[IdentityEvent]:
        """Generate a slower manually simulated identity-abuse chain."""
        abnormal_ip = "198.51.100.77"
        return [
            self._event(0, "email", "lure_received", self.user.normal_ip, {"variant": "manual"}),
            self._event(42, "idp", "login", abnormal_ip, {"geo_change": True}),
            self._event(49, "idp", "new_device", abnormal_ip, {"device_trust": "unknown"}),
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
        """Generate a faster simulated AI-assisted identity-abuse chain."""
        abnormal_ip = "198.51.100.88"
        return [
            self._event(0, "email", "lure_received", self.user.normal_ip, {"variant": "ai_assisted"}),
            self._event(11, "idp", "login", abnormal_ip, {"geo_change": True}),
            self._event(13, "idp", "new_device", abnormal_ip, {"device_trust": "unknown"}),
            self._event(
                18,
                "idp",
                "oauth_consent",
                abnormal_ip,
                {"scopes": ["mail.read", "files.read.all", "offline_access"]},
            ),
            self._event(24, "saas", "saas_export", abnormal_ip, {"object_count": 900}),
        ]

    def all_scenarios(self) -> dict[str, list[IdentityEvent]]:
        return {
            "baseline": self.baseline(),
            "manual_abuse": self.manual_abuse(),
            "ai_assisted_abuse": self.ai_assisted_abuse(),
        }

    def write_jsonl(self, events: list[IdentityEvent], output_path: Path) -> None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", encoding="utf-8") as handle:
            for event in events:
                handle.write(event.model_dump_json() + "\n")

    def _event(
        self,
        minute_offset: int,
        source: str,
        event_type: str,
        ip_address: str,
        attributes: dict[str, object] | None = None,
    ) -> IdentityEvent:
        return IdentityEvent(
            user_id=self.user.user_id,
            timestamp=self.base_time + timedelta(minutes=minute_offset),
            source=source,
            event_type=event_type,
            ip_address=ip_address,
            user_agent=self.user.normal_user_agent,
            attributes=attributes or {},
        )


def load_jsonl(input_path: Path) -> list[IdentityEvent]:
    """Load IdentityEvent objects from a JSONL file."""
    events: list[IdentityEvent] = []
    with input_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            row = json.loads(line)
            events.append(IdentityEvent.model_validate(row))
    return events
