from pathlib import Path

from identity_abuse_lab.telemetry.generators import ScenarioGenerator, load_jsonl


def test_generator_builds_all_expected_scenarios() -> None:
    generator = ScenarioGenerator()
    scenarios = generator.all_scenarios()

    assert set(scenarios) == {"baseline", "manual_abuse", "ai_assisted_abuse"}
    assert len(scenarios["baseline"]) == 5
    assert len(scenarios["manual_abuse"]) == 5
    assert len(scenarios["ai_assisted_abuse"]) == 5


def test_ai_assisted_scenario_progresses_faster_than_manual() -> None:
    generator = ScenarioGenerator()
    manual = generator.manual_abuse()
    ai_assisted = generator.ai_assisted_abuse()

    manual_duration = manual[-1].timestamp - manual[0].timestamp
    ai_duration = ai_assisted[-1].timestamp - ai_assisted[0].timestamp

    assert ai_duration < manual_duration


def test_write_and_load_jsonl_round_trip(tmp_path: Path) -> None:
    generator = ScenarioGenerator()
    output_path = tmp_path / "baseline_events.jsonl"

    generator.write_jsonl(generator.baseline(), output_path)
    loaded = load_jsonl(output_path)

    assert len(loaded) == 5
    assert loaded[0].event_type == "login"
    assert loaded[-1].event_type == "logout"
