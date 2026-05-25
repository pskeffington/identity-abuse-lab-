from pathlib import Path

from identity_abuse_lab.reports.figures import (
    save_intervention_window_figure,
    save_timeline_risk_figure,
)


def test_timeline_risk_figure_is_created(tmp_path: Path) -> None:
    output_path = tmp_path / "timeline_risk.png"

    save_timeline_risk_figure(output_path)

    assert output_path.exists()
    assert output_path.stat().st_size > 0


def test_intervention_window_figure_is_created(tmp_path: Path) -> None:
    output_path = tmp_path / "intervention_window.png"

    save_intervention_window_figure(output_path)

    assert output_path.exists()
    assert output_path.stat().st_size > 0
