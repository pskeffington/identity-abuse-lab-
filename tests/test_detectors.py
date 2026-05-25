from datetime import UTC, datetime

from identity_abuse_lab.detectors.export_anomaly import SaaSExportAnomalyDetector
from identity_abuse_lab.detectors.oauth_scope_risk import OAuthScopeRiskDetector
from identity_abuse_lab.telemetry.event import IdentityEvent


def make_event(event_type: str, attributes: dict[str, object]) -> IdentityEvent:
    return IdentityEvent(
        user_id="user-001",
        timestamp=datetime(2026, 1, 1, tzinfo=UTC),
        source="lab",
        event_type=event_type,
        attributes=attributes,
    )


def test_oauth_scope_risk_scores_high_risk_scopes() -> None:
    detector = OAuthScopeRiskDetector()
    event = make_event(
        "oauth_consent",
        {"scopes": ["Mail.Read", "Files.Read.All", "offline_access"]},
    )

    assert detector.score(event) == 1.0


def test_oauth_scope_risk_ignores_non_oauth_events() -> None:
    detector = OAuthScopeRiskDetector()
    event = make_event("login", {"scopes": ["mail.read"]})

    assert detector.score(event) == 0.0


def test_export_anomaly_scores_high_volume_exports() -> None:
    detector = SaaSExportAnomalyDetector(medium_threshold=50, high_threshold=500)
    event = make_event("saas_export", {"object_count": 900})

    assert detector.score(event) == 1.0


def test_export_anomaly_scores_medium_volume_exports() -> None:
    detector = SaaSExportAnomalyDetector(medium_threshold=50, high_threshold=500)
    event = make_event("saas_export", {"object_count": 75})

    assert detector.score(event) == 0.65
