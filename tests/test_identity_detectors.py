from datetime import UTC, datetime

from identity_abuse_lab.detectors.abnormal_login import AbnormalLoginDetector
from identity_abuse_lab.detectors.new_device import NewDeviceRiskDetector
from identity_abuse_lab.telemetry.event import IdentityEvent


def make_event(event_type: str, attributes: dict[str, object]) -> IdentityEvent:
    return IdentityEvent(
        user_id="user-001",
        timestamp=datetime(2026, 1, 1, tzinfo=UTC),
        source="idp",
        event_type=event_type,
        ip_address="198.51.100.88",
        attributes=attributes,
    )


def test_abnormal_login_scores_multiple_context_signals() -> None:
    detector = AbnormalLoginDetector()
    event = make_event(
        "login",
        {
            "geo_change": True,
            "unfamiliar_user_agent": True,
            "anonymous_network": True,
        },
    )

    assert detector.score(event) == 1.0


def test_abnormal_login_ignores_normal_login() -> None:
    detector = AbnormalLoginDetector()
    event = make_event("login", {})

    assert detector.score(event) == 0.0


def test_new_device_scores_reset_and_geo_change() -> None:
    detector = NewDeviceRiskDetector()
    event = make_event(
        "new_device",
        {"device_trust": "unknown", "geo_change": True, "after_reset": True},
    )

    assert detector.score(event) == 0.95


def test_new_device_scores_unknown_device() -> None:
    detector = NewDeviceRiskDetector()
    event = make_event("new_device", {"device_trust": "unknown"})

    assert detector.score(event) == 0.65
