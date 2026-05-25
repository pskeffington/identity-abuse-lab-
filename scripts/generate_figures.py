from pathlib import Path

from identity_abuse_lab.reports.figures import (
    save_intervention_window_figure,
    save_timeline_risk_figure,
)


if __name__ == "__main__":
    save_timeline_risk_figure(Path("paper/figures/timeline_risk.png"))
    save_intervention_window_figure(Path("paper/figures/intervention_window.png"))
