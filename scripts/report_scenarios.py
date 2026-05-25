from identity_abuse_lab.reports.metrics import ScenarioMetricsReporter, to_markdown_table
from identity_abuse_lab.telemetry.generators import ScenarioGenerator


def main() -> None:
    generator = ScenarioGenerator()
    reporter = ScenarioMetricsReporter()
    metrics = reporter.summarize_many(generator.all_scenarios())
    print(to_markdown_table(metrics))


if __name__ == "__main__":
    main()
