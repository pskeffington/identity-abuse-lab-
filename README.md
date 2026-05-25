# Identity Abuse Lab

A controlled, synthetic research lab for studying AI-assisted identity abuse patterns across enterprise SaaS environments.

## Purpose

This project builds a reproducible internal lab for generating, scoring, and analyzing synthetic identity-abuse telemetry. The goal is to compare baseline user activity, manual abuse chains, and AI-assisted abuse chains using observable identity and SaaS signals.

## Research question

Which telemetry signals most reliably distinguish normal SaaS identity behavior from simulated AI-assisted identity-abuse chains in a controlled enterprise lab?

## Scope

This repository is defensive and research-oriented. It does not include real phishing campaigns, real credential collection, victim targeting, or instructions for unauthorized access. All data is synthetic and all scenarios are designed for controlled lab use.

## Planned outputs

- Synthetic telemetry datasets
- Detection logic for identity-abuse signals
- Correlated risk scoring
- Reproducible notebooks
- Metrics tables and figures
- Sigma-style detection rules
- Publication-ready white paper

## Repository layout

```text
identity-abuse-lab-/
  docs/                 Lab design, threat model, methodology, safety notes
  src/                  Python package source
  tests/                Unit tests
  data/                 Synthetic and processed data
  notebooks/            Reproducible analysis notebooks
  rules/                Detection rules
  paper/                Manuscript and publication assets
```

## Quick start

```bash
python -m pip install -e .[dev]
pytest
```

## License

See `LICENSE`.
