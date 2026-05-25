from identity_abuse_lab.detectors.export_anomaly import SaaSExportAnomalyDetector
from identity_abuse_lab.detectors.oauth_scope_risk import OAuthScopeRiskDetector
from identity_abuse_lab.scoring.risk_score import RiskScoringEngine
from identity_abuse_lab.scoring.timeline import TimelineCorrelationScorer
from identity_abuse_lab.telemetry.generators import ScenarioGenerator


def build_scorer() -> TimelineCorrelationScorer:
    engine = RiskScoringEngine(
        detectors=[OAuthScopeRiskDetector(), SaaSExportAnomalyDetector()]
    )
    return TimelineCorrelationScorer(engine=engine, detection_threshold=1.2, decay=0.9)


def test_baseline_not_detected_by_timeline_correlation() -> None:
    generator = ScenarioGenerator()
    scorer = build_scorer()

    summary = scorer.summarize("baseline", generator.baseline())

    assert not summary.detected
    assert not summary.detected_before_export


def test_manual_abuse_detected_before_export() -> None:
    generator = ScenarioGenerator()
    scorer = build_scorer()

    summary = scorer.summarize("manual_abuse", generator.manual_abuse())

    assert summary.detected
    assert summary.detected_before_export
    assert summary.minutes_before_export == 15.0


def test_ai_assisted_abuse_detected_before_export_with_shorter_window() -> None:
    generator = ScenarioGenerator()
    scorer = build_scorer()

    summary = scorer.summarize("ai_assisted_abuse", generator.ai_assisted_abuse())

    assert summary.detected
    assert summary.detected_before_export
    assert summary.minutes_before_export == 6.0
