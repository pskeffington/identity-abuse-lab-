from scripts.verify_expected_results import verify_enriched_windows, verify_scenario_metrics


def test_expected_scenario_metrics_match_current_outputs() -> None:
    verify_scenario_metrics()


def test_expected_enriched_windows_match_current_outputs() -> None:
    verify_enriched_windows()
