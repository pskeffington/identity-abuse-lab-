from identity_abuse_lab.detectors.abnormal_login import AbnormalLoginDetector
from identity_abuse_lab.detectors.export_anomaly import SaaSExportAnomalyDetector
from identity_abuse_lab.detectors.new_device import NewDeviceRiskDetector
from identity_abuse_lab.detectors.oauth_scope_risk import OAuthScopeRiskDetector
from identity_abuse_lab.scoring.risk_score import RiskScoringEngine
from identity_abuse_lab.scoring.timeline import TimelineCorrelationScorer
from identity_abuse_lab.telemetry.enriched_generators import EnrichedScenarioGenerator


def build_enriched_scorer() -> TimelineCorrelationScorer:
    engine = RiskScoringEngine(
        detectors=[
            AbnormalLoginDetector(),
            NewDeviceRiskDetector(),
            OAuthScopeRiskDetector(),
            SaaSExportAnomalyDetector(),
        ]
    )
    return TimelineCorrelationScorer(engine=engine, detection_threshold=1.2, decay=0.9)


def test_enriched_manual_abuse_detects_before_oauth_consent() -> None:
    generator = EnrichedScenarioGenerator()
    scorer = build_enriched_scorer()

    summary = scorer.summarize("manual_abuse", generator.manual_abuse())

    assert summary.detected
    assert summary.detected_before_export
    assert summary.minutes_before_export == 28.0


def test_enriched_ai_assisted_abuse_detects_with_compressed_window() -> None:
    generator = EnrichedScenarioGenerator()
    scorer = build_enriched_scorer()

    summary = scorer.summarize("ai_assisted_abuse", generator.ai_assisted_abuse())

    assert summary.detected
    assert summary.detected_before_export
    assert summary.minutes_before_export == 11.0
