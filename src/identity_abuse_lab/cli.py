from __future__ import annotations

import argparse
from pathlib import Path

from identity_abuse_lab.telemetry.generators import ScenarioGenerator


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Identity Abuse Lab CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    generate = subparsers.add_parser("generate", help="Generate synthetic telemetry JSONL files")
    generate.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/synthetic"),
        help="Directory for generated JSONL files.",
    )
    return parser


def generate(output_dir: Path) -> None:
    generator = ScenarioGenerator()
    for scenario_name, events in generator.all_scenarios().items():
        generator.write_jsonl(events, output_dir / f"{scenario_name}_events.jsonl")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "generate":
        generate(args.output_dir)


if __name__ == "__main__":
    main()
