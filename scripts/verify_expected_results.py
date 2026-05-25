from __future__ import annotations

from identity_abuse_lab.detectors.abnormal_login import AbnormalLoginDetector
from identity_abuse_lab.detectors.export_anomaly import SaaSExportAnomalyDetector
from identity_abuse_lab.detectors.helpdesk_reset import HelpdeskResetDetector
from identity_abuse_lab.detectors.new_device import NewDeviceRiskDetector
from identity_abuse_lab.detectors.oauth_scope_risk import OAuthScopeRiskDetector
from identity_abuse_lab.reports.metrics import ScenarioMetricsReporter
from identity_abuse_lab.scoring.risk_score import RiskScoringEngine
from identity_abuse_lab.scoring.timeline import TimelineCorrelationScorer
from identity_abuse_lab.telemetry.enriched_generators import EnrichedScenarioGenerator
from identity_abuse_lab.telemetry.generators import ScenarioGenerator


EXPECTED_SCENARIO_METRICS = {
    "baseline": {
        "event_count": 5,
        "duration_minutes": 40.0,
        "max_detector_score": 0.20,
        "high_risk_event_count": 0,
        "export_volume": 4,
        "oauth_consent_count": 0,
    },
    "manual_abuse": {
        "event_count": 5,
        "duration_minutes": 77.0,
        "max_detector_score": 1.00,
        "high_risk_event_count": 2,
        "export_volume": 650,
        "oauth_consent_count": 1,
    },
    "ai_assisted_abuse": {
        "event_count": 5,
        "duration_minutes": 24.0,
        "max_detector_score": 1.00,
        "high_risk_event_count": 2,
        "export_volume": 900,
        "oauth_consent_count": 1,
    },
}

EXPECTED_ENRICHED_WINDOWS = {
    "manual_abuse": 28.0,
    "ai_assisted_abuse": 11.0,
}


def assert_close(actual: float, expected: float, label: str) -> None:
    if abs(actual - expected) > 0.001:
        raise AssertionError(f"{label}: expected {expected}, got {actual}")


def verify_scenario_metrics() -> None:
    generator = ScenarioGenerator()
    reporter = ScenarioMetricsReporter()
    metrics = {row.scenario: row for row in reporter.summarize_many(generator.all_scenarios())}

    for scenario, expected in EXPECTED_SCENARIO_METRICS.items():
        actual = metrics[scenario]
        if actual.event_count != expected["event_count"]:
            raise AssertionError(f"{scenario} event_count mismatch")
        assert_close(actual.duration_minutes, expected["duration_minutes"], f"{scenario} duration")
        assert_close(actual.max_detector_score, expected["max_detector_score"], f"{scenario} max score")
        if actual.high_risk_event_count != expected["high_risk_event_count"]:
            raise AssertionError(f"{scenario} high_risk_event_count mismatch")
        if actual.export_volume != expected["export_volume"]:
            raise AssertionError(f"{scenario} export_volume mismatch")
        if actual.oauth_consent_count != expected["oauth_consent_count"]:
            raise AssertionError(f"{scenario} oauth_consent_count mismatch")


def verify_enriched_windows() -> None:
    generator = EnrichedScenarioGenerator()
    engine = RiskScoringEngine(
        detectors=[
            AbnormalLoginDetector(),
            HelpdeskResetDetector(),
            NewDeviceRiskDetector(),
            OAuthScopeRiskDetector(),
            SaaSExportAnomalyDetector(),
        ]
    )
    scorer = TimelineCorrelationScorer(engine=engine)

    for scenario, expected_window in EXPECTED_ENRICHED_WINDOWS.items():
        summary = scorer.summarize(scenario, generator.all_scenarios()[scenario])
        if not summary.detected_before_export:
            raise AssertionError(f"{scenario} was not detected before export")
        assert_close(
            summary.minutes_before_export or 0.0,
            expected_window,
            f"{scenario} enriched intervention window",
        )


def main() -> None:
    verify_scenario_metrics()
    verify_enriched_windows()
    print("Expected result verification passed.")


if __name__ == "__main__":
    main()
