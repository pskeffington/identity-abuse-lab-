from __future__ import annotations

from dataclasses import dataclass

from identity_abuse_lab.detectors.base import Detector
from identity_abuse_lab.telemetry.event import IdentityEvent


@dataclass(frozen=True)
class EventScore:
    """Detector scores for a single event."""

    event: IdentityEvent
    detector_scores: dict[str, float]

    @property
    def max_score(self) -> float:
        if not self.detector_scores:
            return 0.0
        return max(self.detector_scores.values())


class RiskScoringEngine:
    """Runs multiple detectors and produces event-level risk scores."""

    def __init__(self, detectors: list[Detector]) -> None:
        self.detectors = detectors

    def score_event(self, event: IdentityEvent) -> EventScore:
        scores = {detector.name: detector.score(event) for detector in self.detectors}
        return EventScore(event=event, detector_scores=scores)

    def score_events(self, events: list[IdentityEvent]) -> list[EventScore]:
        return [self.score_event(event) for event in events]
