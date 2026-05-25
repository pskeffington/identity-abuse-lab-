# Portfolio One-Pager

## Project

**Identity Abuse Lab**

## Role demonstrated

Senior technical threat investigator / cyber threat analyst / AI abuse research engineer.

## Summary

Identity Abuse Lab is a defensive synthetic research environment for evaluating AI-assisted identity-abuse detection in SaaS settings. It models baseline user activity, manually simulated abuse, and AI-assisted abuse using normalized telemetry and transparent Python detectors. The lab measures whether correlated identity signals detect abuse before simulated SaaS export and how much intervention time remains.

## Core result

| Scenario | Detected before export | Intervention window |
|---|---:|---:|
| Manual abuse | Yes | 28.0 minutes |
| AI-assisted abuse | Yes | 11.0 minutes |

## Interpretation

The current synthetic result suggests that AI-assisted abuse may not require fundamentally different telemetry categories to detect, but it can compress the response window enough that slow manual review becomes less reliable.

## Technical stack

- Python
- Pydantic
- Pytest
- Ruff
- Matplotlib
- GitHub Actions
- Sigma-style detection rules
- Markdown manuscript workflow

## Implemented components

- Synthetic event schema
- Scenario generators
- Abnormal login detector
- Help-desk reset detector
- New-device detector
- OAuth scope-risk detector
- SaaS export anomaly detector
- Timeline correlation scorer
- Metrics reporter
- Scored CSV exporter
- Figure generator
- Expected-results verifier
- CI workflows
- Manuscript draft
- Safety and release documentation

## Why it matters

The project demonstrates practical overlap among AI abuse investigation, cyber threat intelligence, identity security, detection engineering, and research communication. It converts an abstract AI-risk claim into a measurable detection variable: minutes of response time before simulated data export.

## Safety boundary

All telemetry is synthetic. The project excludes real phishing, credential collection, malware, exploit development, unauthorized access guidance, production logs, and real user data.

## Reviewer starting point

Start with:

1. `ARTIFACT.md`
2. `docs/reviewer_index.md`
3. `docs/project_brief.md`
4. `paper/manuscript_assembled.md`
5. `VALIDATION_CHECKLIST.md`
