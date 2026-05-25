from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from identity_abuse_lab.detectors.abnormal_login import AbnormalLoginDetector
from identity_abuse_lab.detectors.export_anomaly import SaaSExportAnomalyDetector
from identity_abuse_lab.detectors.helpdesk_reset import HelpdeskResetDetector
from identity_abuse_lab.detectors.new_device import NewDeviceRiskDetector
from identity_abuse_lab.detectors.oauth_scope_risk import OAuthScopeRiskDetector
from identity_abuse_lab.scoring.risk_score import RiskScoringEngine
from identity_abuse_lab.scoring.timeline import TimelineCorrelationScorer
from identity_abuse_lab.telemetry.enriched_generators import EnrichedScenarioGenerator


def build_figure_engine() -> RiskScoringEngine:
    return RiskScoringEngine(
        detectors=[
            AbnormalLoginDetector(),
            HelpdeskResetDetector(),
            NewDeviceRiskDetector(),
            OAuthScopeRiskDetector(),
            SaaSExportAnomalyDetector(),
        ]
    )


def save_timeline_risk_figure(output_path: Path) -> None:
    """Save a cumulative-risk timeline figure for enriched abuse scenarios."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    generator = EnrichedScenarioGenerator()
    scorer = TimelineCorrelationScorer(engine=build_figure_engine())

    fig, ax = plt.subplots()
    for scenario_name in ["manual_abuse", "ai_assisted_abuse"]:
        events = generator.all_scenarios()[scenario_name]
        points = scorer.score_timeline(events)
        start = points[0].timestamp
        minutes = [(point.timestamp - start).total_seconds() / 60 for point in points]
        scores = [point.cumulative_score for point in points]
        ax.plot(minutes, scores, marker="o", label=scenario_name)

    ax.axhline(scorer.detection_threshold, linestyle="--", label="detection threshold")
    ax.set_title("Cumulative identity-abuse risk over scenario timeline")
    ax.set_xlabel("Minutes since initial lure marker")
    ax.set_ylabel("Cumulative risk score")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)


def save_intervention_window_figure(output_path: Path) -> None:
    """Save a bar chart comparing enriched intervention windows."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    generator = EnrichedScenarioGenerator()
    scorer = TimelineCorrelationScorer(engine=build_figure_engine())

    scenarios = ["manual_abuse", "ai_assisted_abuse"]
    windows = []
    for scenario in scenarios:
        summary = scorer.summarize(scenario, generator.all_scenarios()[scenario])
        windows.append(summary.minutes_before_export or 0.0)

    fig, ax = plt.subplots()
    ax.bar(scenarios, windows)
    ax.set_title("Intervention window before simulated SaaS export")
    ax.set_xlabel("Scenario")
    ax.set_ylabel("Minutes before export")
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)
