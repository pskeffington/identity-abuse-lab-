from pathlib import Path

from identity_abuse_lab.reports.export import ScoredEventExporter
from identity_abuse_lab.telemetry.enriched_generators import EnrichedScenarioGenerator


def test_exporter_builds_rows_for_all_scenarios() -> None:
    generator = EnrichedScenarioGenerator()
    exporter = ScoredEventExporter()

    rows = exporter.rows_for_scenarios(generator.all_scenarios())

    assert len(rows) == 15
    assert {row["scenario"] for row in rows} == {
        "baseline",
        "manual_abuse",
        "ai_assisted_abuse",
    }
    assert "cumulative_score" in rows[0]


def test_exporter_writes_csv(tmp_path: Path) -> None:
    generator = EnrichedScenarioGenerator()
    exporter = ScoredEventExporter()
    output_path = tmp_path / "scored_events.csv"

    rows = exporter.rows_for_scenarios(generator.all_scenarios())
    exporter.write_csv(rows, output_path)

    content = output_path.read_text(encoding="utf-8")
    assert "scenario,timestamp,user_id,source,event_type" in content
    assert "ai_assisted_abuse" in content
