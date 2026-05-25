from identity_abuse_lab.reports.metrics import ScenarioMetricsReporter, to_markdown_table
from identity_abuse_lab.telemetry.generators import ScenarioGenerator


def test_metrics_capture_expected_scenario_differences() -> None:
    generator = ScenarioGenerator()
    reporter = ScenarioMetricsReporter()
    metrics = {row.scenario: row for row in reporter.summarize_many(generator.all_scenarios())}

    assert metrics["baseline"].max_detector_score < metrics["manual_abuse"].max_detector_score
    assert metrics["baseline"].max_detector_score < metrics["ai_assisted_abuse"].max_detector_score
    assert metrics["ai_assisted_abuse"].duration_minutes < metrics["manual_abuse"].duration_minutes
    assert metrics["ai_assisted_abuse"].export_volume > metrics["manual_abuse"].export_volume


def test_markdown_table_contains_all_scenarios() -> None:
    generator = ScenarioGenerator()
    reporter = ScenarioMetricsReporter()
    table = to_markdown_table(reporter.summarize_many(generator.all_scenarios()))

    assert "baseline" in table
    assert "manual_abuse" in table
    assert "ai_assisted_abuse" in table
    assert "High-risk events" in table
