from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from identity_abuse_lab.scoring.risk_score import RiskScoringEngine
from identity_abuse_lab.telemetry.event import IdentityEvent


@dataclass(frozen=True)
class TimelinePoint:
    """Cumulative risk state at one point in a scenario timeline."""

    timestamp: datetime
    event_type: str
    event_score: float
    cumulative_score: float
    detected: bool


@dataclass(frozen=True)
class TimelineDetectionSummary:
    """Chain-level detection summary for a synthetic scenario."""

    scenario: str
    detected: bool
    first_detection_time: datetime | None
    export_time: datetime | None
    detected_before_export: bool
    minutes_before_export: float | None
    final_cumulative_score: float


class TimelineCorrelationScorer:
    """Scores scenario timelines using cumulative event risk.

    The scorer intentionally uses a simple transparent cumulative model. This makes the
    research artifact easy to inspect, critique, and replace with richer models later.
    """

    def __init__(
        self,
        engine: RiskScoringEngine,
        detection_threshold: float = 1.2,
        decay: float = 0.9,
    ) -> None:
        self.engine = engine
        self.detection_threshold = detection_threshold
        self.decay = decay

    def score_timeline(self, events: list[IdentityEvent]) -> list[TimelinePoint]:
        sorted_events = sorted(events, key=lambda event: event.timestamp)
        cumulative = 0.0
        points: list[TimelinePoint] = []

        for event in sorted_events:
            event_score = self.engine.score_event(event).max_score
            cumulative = (cumulative * self.decay) + event_score
            points.append(
                TimelinePoint(
                    timestamp=event.timestamp,
                    event_type=event.event_type,
                    event_score=event_score,
                    cumulative_score=cumulative,
                    detected=cumulative >= self.detection_threshold,
                )
            )

        return points

    def summarize(self, scenario: str, events: list[IdentityEvent]) -> TimelineDetectionSummary:
        points = self.score_timeline(events)
        first_detection = next((point for point in points if point.detected), None)
        export_events = sorted(
            (event for event in events if event.event_type == "saas_export"),
            key=lambda event: event.timestamp,
        )
        export_time = export_events[0].timestamp if export_events else None
        detected_before_export = False
        minutes_before_export: float | None = None

        if first_detection is not None and export_time is not None:
            detected_before_export = first_detection.timestamp < export_time
            if detected_before_export:
                delta = export_time - first_detection.timestamp
                minutes_before_export = delta.total_seconds() / 60

        return TimelineDetectionSummary(
            scenario=scenario,
            detected=first_detection is not None,
            first_detection_time=first_detection.timestamp if first_detection else None,
            export_time=export_time,
            detected_before_export=detected_before_export,
            minutes_before_export=minutes_before_export,
            final_cumulative_score=points[-1].cumulative_score if points else 0.0,
        )
