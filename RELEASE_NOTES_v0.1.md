# Release Notes: v0.1-lab-baseline

## Identity Abuse Lab v0.1: Synthetic Baseline for AI-Assisted Identity-Abuse Detection

This baseline release introduces a defensive synthetic lab for evaluating identity-abuse detection across baseline, manual-abuse, and AI-assisted-abuse scenarios.

## Core contribution

Identity Abuse Lab links synthetic identity/SaaS telemetry, transparent Python detectors, cumulative timeline scoring, scored CSV outputs, Sigma-style rules, and manuscript-ready documentation into one reproducible research artifact.

## Current bounded finding

In the enriched synthetic scenario set, correlated identity telemetry detects both abuse chains before simulated SaaS export:

| Scenario | Detected before export | Intervention window |
|---|---:|---:|
| Manual abuse | Yes | 28.0 minutes |
| AI-assisted abuse | Yes | 11.0 minutes |

The working interpretation is that AI-assisted identity abuse may not require fundamentally different telemetry categories to detect, but it can compress the defender response window enough that slow manual review becomes less reliable.

## Included in this release

- Normalized `IdentityEvent` telemetry model
- Baseline, manual-abuse, and AI-assisted-abuse scenario generators
- Enriched scenario generator
- Abnormal-login detector
- Help-desk reset detector
- New-device risk detector
- OAuth scope-risk detector
- SaaS export anomaly detector
- Risk scoring engine
- Timeline correlation scorer
- Scenario metrics reporter
- Scored event CSV exporter
- Figure generation utilities
- Sigma-style experimental rules
- Unit tests and CI workflow
- Threat model
- Ethics and safety statement
- Data dictionary
- Architecture overview
- Project brief
- Manuscript sections and assembled draft
- Working references
- Reproducibility appendix

## Safety boundary

This release is synthetic-only and defensive. It does not include real phishing, credential collection, malware, exploit development, unauthorized access guidance, production logs, real user records, or real customer data.

## Known limitations

- Synthetic telemetry only
- Small scenario count
- Heuristic detector scoring
- No production calibration
- No real-world detection-rate claims
- Limited false-positive modeling
- Final citation pass still in progress
- Root README should be updated from `docs/readme_current.md` before final public release tagging

## Recommended reviewer starting points

- `docs/readme_current.md`
- `docs/project_brief.md`
- `docs/architecture.md`
- `docs/threat_model.md`
- `docs/ethics_and_safety.md`
- `paper/manuscript_assembled.md`
- `paper/publication_checklist.md`
- `RELEASE_STATUS.md`

## Suggested tag

```text
v0.1-lab-baseline
```
