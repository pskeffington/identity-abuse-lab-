# Architecture Overview

Identity Abuse Lab is organized as a defensive research-engineering pipeline.

## Pipeline

```text
Synthetic scenario generator
        |
        v
Normalized IdentityEvent objects
        |
        v
Event-level detectors
        |
        v
RiskScoringEngine
        |
        v
TimelineCorrelationScorer
        |
        v
Scenario metrics, scored CSV outputs, figures, Sigma-style rules, manuscript tables
```

## Main components

| Component | Path | Purpose |
|---|---|---|
| Telemetry model | `src/identity_abuse_lab/telemetry/event.py` | Defines normalized `IdentityEvent` schema |
| Scenario generators | `src/identity_abuse_lab/telemetry/generators.py` and `enriched_generators.py` | Build baseline, manual abuse, and AI-assisted abuse event streams |
| Detectors | `src/identity_abuse_lab/detectors/` | Score event-level identity and SaaS risk |
| Event scoring | `src/identity_abuse_lab/scoring/risk_score.py` | Runs detector set over events |
| Timeline scoring | `src/identity_abuse_lab/scoring/timeline.py` | Computes cumulative chain risk and detection-before-export results |
| Metrics reporting | `src/identity_abuse_lab/reports/metrics.py` | Produces scenario-level result tables |
| CSV export | `src/identity_abuse_lab/reports/export.py` | Exports scored event rows for review |
| Figures | `src/identity_abuse_lab/reports/figures.py` | Generates publication figures |
| Rules | `rules/sigma/` | Maps detector logic to Sigma-style experimental rules |
| Paper | `paper/` | Stores manuscript sections, references, figures, and result notes |

## Object model

```text
IdentityEvent
  -> Detector.score(event)
  -> EventScore
  -> TimelinePoint
  -> TimelineDetectionSummary
  -> ScenarioMetrics
```

## Reproducibility commands

```bash
make install
make test
make generate
make export
make report
make -f Makefile.paper figures
make -f Makefile.paper manuscript
```

## Design principles

- Keep all data synthetic.
- Keep detector logic transparent.
- Preserve early simple scenarios while adding enriched variants separately.
- Treat production deployment as out of scope.
- Make every result reproducible through code and tests.
