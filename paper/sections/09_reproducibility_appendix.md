# Appendix A. Reproducibility

## A.1 Repository structure

Identity Abuse Lab is organized as a reproducible research-engineering repository. The source package contains telemetry models, generators, detectors, scoring logic, and reporting utilities. The `tests/` directory validates model behavior, detector scoring, timeline detection, and export logic. The `paper/` directory contains manuscript sections, result tables, and publication notes. The `rules/` directory contains Sigma-style experimental detection rules.

## A.2 Environment setup

A reviewer can install the package in editable mode with development dependencies:

```bash
make install
```

This installs the local Python package and development tools declared in `pyproject.toml`.

## A.3 Test execution

The test suite can be run with:

```bash
make test
```

The current tests verify:

- event-model defaults and risk thresholds;
- detector scoring for OAuth, SaaS export, abnormal login, new device, and help-desk reset events;
- scenario generation and JSONL round-trip loading;
- scenario metrics reporting;
- timeline correlation scoring;
- enriched timeline detection; and
- scored-event CSV export.

## A.4 Synthetic telemetry generation

Synthetic scenario telemetry can be generated with:

```bash
make generate
```

This writes JSONL scenario files under `data/synthetic/` using the package CLI.

## A.5 Scored event export

Event-level detector and timeline scores can be exported with:

```bash
make export
```

The export script writes `data/processed/scored_events.csv`. The CSV includes scenario name, timestamp, user identifier, source, event type, IP address, event score, cumulative score, and detection state.

## A.6 Scenario report generation

A markdown scenario report can be printed with:

```bash
make report
```

This report summarizes event count, duration, maximum detector score, high-risk event count, export volume, and OAuth consent count for each scenario.

## A.7 Full reproduction command

The full local reproduction workflow is:

```bash
make all
```

This generates synthetic telemetry, exports scored events, prints the report, and runs the test suite.

## A.8 Reproducibility boundary

The results are reproducible within the synthetic scenario definitions currently committed to the repository. They are not production detection benchmarks. Any production use would require authorized telemetry, legal review, security review, privacy review, SIEM field mapping, and environment-specific validation.
