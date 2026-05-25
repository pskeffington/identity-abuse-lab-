from datetime import UTC, datetime

from identity_abuse_lab.telemetry.event import IdentityEvent


def test_identity_event_defaults_to_low_risk() -> None:
    event = IdentityEvent(
        user_id="user-001",
        timestamp=datetime(2026, 1, 1, tzinfo=UTC),
        source="idp",
        event_type="login",
    )

    assert event.risk_score == 0.0
    assert event.attributes == {}
    assert not event.is_high_risk()


def test_identity_event_high_risk_threshold() -> None:
    event = IdentityEvent(
        user_id="user-001",
        timestamp=datetime(2026, 1, 1, tzinfo=UTC),
        source="idp",
        event_type="oauth_consent",
        risk_score=0.8,
    )

    assert event.is_high_risk()
