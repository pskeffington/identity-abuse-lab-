from datetime import UTC, datetime

from identity_abuse_lab.detectors.helpdesk_reset import HelpdeskResetDetector
from identity_abuse_lab.telemetry.event import IdentityEvent


def make_event(attributes: dict[str, object]) -> IdentityEvent:
    return IdentityEvent(
        user_id="user-001",
        timestamp=datetime(2026, 1, 1, tzinfo=UTC),
        source="idp",
        event_type="helpdesk_reset",
        ip_address="198.51.100.88",
        attributes=attributes,
    )


def test_helpdesk_reset_scores_high_risk_reset() -> None:
    detector = HelpdeskResetDetector()
    event = make_event(
        {
            "reset_channel": "helpdesk",
            "identity_verified": False,
            "urgent_request": True,
            "geo_change": True,
            "executive_claim": True,
        }
    )

    assert detector.score(event) == 1.0


def test_helpdesk_reset_scores_medium_risk_reset() -> None:
    detector = HelpdeskResetDetector()
    event = make_event(
        {
            "reset_channel": "helpdesk",
            "identity_verified": False,
        }
    )

    assert detector.score(event) == 0.65


def test_helpdesk_reset_ignores_non_reset_event() -> None:
    detector = HelpdeskResetDetector()
    event = IdentityEvent(
        user_id="user-001",
        timestamp=datetime(2026, 1, 1, tzinfo=UTC),
        source="idp",
        event_type="login",
        attributes={"reset_channel": "helpdesk"},
    )

    assert detector.score(event) == 0.0
