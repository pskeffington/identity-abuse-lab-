from pathlib import Path

from identity_abuse_lab.reports.export import export_default_scored_events


if __name__ == "__main__":
    export_default_scored_events(Path("data/processed/scored_events.csv"))
