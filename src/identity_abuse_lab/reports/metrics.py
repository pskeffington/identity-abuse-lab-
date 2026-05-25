from __future__ import annotations

from dataclasses import dataclass

from identity_abuse_lab.detectors.export_anomaly import SaaSExportAnomalyDetector
from identity_abuse_lab.detectors.oauth_scope_risk import OAuthScopeRiskDetector
from identity_abuse_lab.scoring.risk_score import RiskScoringEngine
from identity_abuse_lab.telemetry.event import IdentityEvent


@dataclass(frozen=True)
class ScenarioMetrics:
    """Summary metrics for one synthetic telemetry scenario."""

    scenario: str
    event_count: int
    duration_minutes: float
    max_detector_score: float
    high_risk_event_count: int
    export_volume: int
    oauth_consent_count: int

    def as_row(self) -> dict[str, str | int | float]:
        return {
            "scenario": self.scenario,
            "event_count": self.event_count,
            "duration_minutes": self.duration_minutes,
            "max_detector_score": self.max_detector_score,
            "high_risk_event_count": self.high_risk_event_count,
            "export_volume": self.export_volume,
            "oauth_consent_count": self.oauth_consent_count,
        }


class ScenarioMetricsReporter:
    """Builds reproducible summary metrics for identity-abuse scenarios."""

    def __init__(self, high_risk_threshold: float = 0.7) -> None:
        self.high_risk_threshold = high_risk_threshold
        self.engine = RiskScoringEngine(
            detectors=[OAuthScopeRiskDetector(), SaaSExportAnomalyDetector()]
        )

    def summarize(self, scenario: str, events: list[IdentityEvent]) -> ScenarioMetrics:
        if not events:
            return ScenarioMetrics(
                scenario=scenario,
                event_count=0,
                duration_minutes=0.0,
                max_detector_score=0.0,
                high_risk_event_count=0,
                export_volume=0,
                oauth_consent_count=0,
            )

        sorted_events = sorted(events, key=lambda event: event.timestamp)
        duration = sorted_events[-1].timestamp - sorted_events[0].timestamp
        scored_events = self.engine.score_events(sorted_events)
        max_score = max(score.max_score for score in scored_events)
        high_risk_count = sum(
            1 for score in scored_events if score.max_score >= self.high_risk_threshold
        )
        export_volume = sum(
            int(event.attributes.get("object_count", 0))
            for event in sorted_events
            if event.event_type == "saas_export"
        )
        oauth_consent_count = sum(
            1 for event in sorted_events if event.event_type == "oauth_consent"
        )

        return ScenarioMetrics(
            scenario=scenario,
            event_count=len(sorted_events),
            duration_minutes=duration.total_seconds() / 60,
            max_detector_score=max_score,
            high_risk_event_count=high_risk_count,
            export_volume=export_volume,
            oauth_consent_count=oauth_consent_count,
        )

    def summarize_many(
        self, scenarios: dict[str, list[IdentityEvent]]
    ) -> list[ScenarioMetrics]:
        return [self.summarize(name, events) for name, events in scenarios.items()]


def to_markdown_table(metrics: list[ScenarioMetrics]) -> str:
    """Render scenario metrics as a compact markdown table."""
    header = (
        "| Scenario | Events | Duration min | Max score | High-risk events | "
        "Export volume | OAuth consents |"
    )
    separator = "|---|---:|---:|---:|---:|---:|---:|"
    rows = [header, separator]
    for row in metrics:
        rows.append(
            "| "
            f"{row.scenario} | "
            f"{row.event_count} | "
            f"{row.duration_minutes:.1f} | "
            f"{row.max_detector_score:.2f} | "
            f"{row.high_risk_event_count} | "
            f"{row.export_volume} | "
            f"{row.oauth_consent_count} |"
        )
    return "\n".join(rows)
