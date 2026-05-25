# Reviewer Navigation Index

This page is the recommended starting point for reviewers evaluating Identity Abuse Lab.

## Fast path

| Goal | Start here |
|---|---|
| Understand the project quickly | `docs/project_brief.md` |
| Review architecture | `docs/architecture.md` |
| Review safety boundaries | `docs/ethics_and_safety.md` |
| Review threat model | `docs/threat_model.md` |
| Review data fields | `docs/data_dictionary.md` |
| Review detector scoring | `paper/detector_thresholds.md` |
| Review detection rules | `rules/README.md` |
| Review manuscript | `paper/manuscript_assembled.md` |
| Review release status | `RELEASE_STATUS.md` |

## Core claim

The current synthetic lab supports a bounded working finding: AI-assisted identity abuse may not require fundamentally different telemetry categories to detect, but it can compress the defender response window enough that slow manual review and late-stage exfiltration alerts become less reliable.

## Current enriched result

| Scenario | Detected before export | Intervention window |
|---|---:|---:|
| Manual abuse | Yes | 28.0 minutes |
| AI-assisted abuse | Yes | 11.0 minutes |

## What to inspect first

1. `docs/project_brief.md`
2. `docs/architecture.md`
3. `paper/sections/05_results.md`
4. `paper/detector_thresholds.md`
5. `rules/README.md`
6. `VALIDATION_CHECKLIST.md`

## What is deliberately out of scope

The project does not include real phishing, credential collection, malware, exploit development, unauthorized access guidance, production logs, real user records, real customer data, or real incident-sensitive details.

## How to reproduce

```bash
make install
make test
make generate
make export
make report
make -f Makefile.paper figures
make -f Makefile.paper manuscript
PYTHONPATH=src:. python scripts/verify_expected_results.py
```

## Release status

The repository is suitable for internal review and portfolio preview. Before public release tagging, complete the gates in `docs/release_gates.md` and `VALIDATION_CHECKLIST.md`.
