from __future__ import annotations

import csv
from collections.abc import Iterable
from pathlib import Path

from identity_abuse_lab.detectors.abnormal_login import AbnormalLoginDetector
from identity_abuse_lab.detectors.export_anomaly import SaaSExportAnomalyDetector
from identity_abuse_lab.detectors.helpdesk_reset import HelpdeskResetDetector
from identity_abuse_lab.detectors.new_device import NewDeviceRiskDetector
from identity_abuse_lab.detectors.oauth_scope_risk import OAuthScopeRiskDetector
from identity_abuse_lab.scoring.risk_score import RiskScoringEngine
from identity_abuse_lab.scoring.timeline import TimelineCorrelationScorer
from identity_abuse_lab.telemetry.event import IdentityEvent
from identity_abuse_lab.telemetry.enriched_generators import EnrichedScenarioGenerator


DEFAULT_FIELDNAMES = [
    "scenario",
    "timestamp",
    "user_id",
    "source",
    "event_type",
    "ip_address",
    "event_score",
    "cumulative_score",
    "detected",
]


def build_default_engine() -> RiskScoringEngine:
    return RiskScoringEngine(
        detectors=[
            AbnormalLoginDetector(),
            HelpdeskResetDetector(),
            NewDeviceRiskDetector(),
            OAuthScopeRiskDetector(),
            SaaSExportAnomalyDetector(),
        ]
    )


class ScoredEventExporter:
    """Exports scenario event scores to CSV for reproducible analysis."""

    def __init__(self, engine: RiskScoringEngine | None = None) -> None:
        self.engine = engine or build_default_engine()
        self.timeline_scorer = TimelineCorrelationScorer(engine=self.engine)

    def rows_for_scenario(
        self, scenario: str, events: list[IdentityEvent]
    ) -> list[dict[str, str | float | bool]]:
        points = self.timeline_scorer.score_timeline(events)
        sorted_events = sorted(events, key=lambda event: event.timestamp)
        rows: list[dict[str, str | float | bool]] = []

        for event, point in zip(sorted_events, points, strict=True):
            rows.append(
                {
                    "scenario": scenario,
                    "timestamp": event.timestamp.isoformat(),
                    "user_id": event.user_id,
                    "source": event.source,
                    "event_type": event.event_type,
                    "ip_address": event.ip_address or "",
                    "event_score": round(point.event_score, 4),
                    "cumulative_score": round(point.cumulative_score, 4),
                    "detected": point.detected,
                }
            )
        return rows

    def rows_for_scenarios(
        self, scenarios: dict[str, list[IdentityEvent]]
    ) -> list[dict[str, str | float | bool]]:
        rows: list[dict[str, str | float | bool]] = []
        for scenario, events in scenarios.items():
            rows.extend(self.rows_for_scenario(scenario, events))
        return rows

    def write_csv(
        self,
        rows: Iterable[dict[str, str | float | bool]],
        output_path: Path,
    ) -> None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=DEFAULT_FIELDNAMES)
            writer.writeheader()
            writer.writerows(rows)


def export_default_scored_events(output_path: Path) -> None:
    generator = EnrichedScenarioGenerator()
    exporter = ScoredEventExporter()
    rows = exporter.rows_for_scenarios(generator.all_scenarios())
    exporter.write_csv(rows, output_path)
