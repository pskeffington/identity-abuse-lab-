from datetime import UTC, datetime

from identity_abuse_lab.detectors.export_anomaly import SaaSExportAnomalyDetector
from identity_abuse_lab.detectors.oauth_scope_risk import OAuthScopeRiskDetector
from identity_abuse_lab.scoring.risk_score import RiskScoringEngine
from identity_abuse_lab.telemetry.event import IdentityEvent


def test_risk_scoring_engine_returns_detector_scores() -> None:
    event = IdentityEvent(
        user_id="user-001",
        timestamp=datetime(2026, 1, 1, tzinfo=UTC),
        source="lab",
        event_type="oauth_consent",
        attributes={"scopes": ["mail.read", "offline_access"]},
    )
    engine = RiskScoringEngine(
        detectors=[OAuthScopeRiskDetector(), SaaSExportAnomalyDetector()]
    )

    score = engine.score_event(event)

    assert score.detector_scores["oauth_scope_risk"] == 0.8
    assert score.detector_scores["saas_export_anomaly"] == 0.0
    assert score.max_score == 0.8
