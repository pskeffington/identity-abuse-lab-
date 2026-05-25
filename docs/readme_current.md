# Identity Abuse Lab

Identity Abuse Lab is a defensive synthetic research environment for studying AI-assisted identity-abuse patterns across SaaS and identity-provider telemetry.

The project compares baseline user behavior, manually simulated identity abuse, and AI-assisted identity abuse using normalized telemetry, transparent Python detectors, cumulative timeline scoring, Sigma-style detection rules, and publication-ready manuscript sections.

## Core research question

Which telemetry signals most reliably distinguish normal SaaS identity behavior from simulated AI-assisted identity-abuse chains in a controlled enterprise lab?

## Current working finding

The current synthetic result set suggests that AI-assisted identity abuse may not require fundamentally different telemetry categories to detect, but it can compress the defender response window enough that slow manual review and late-stage exfiltration alerts become less reliable.

In the enriched scenario set:

| Scenario | Detected before export | Intervention window | Early signals |
|---|---:|---:|---|
| Manual abuse | Yes | 28.0 minutes | abnormal login, unknown new device |
| AI-assisted abuse | Yes | 11.0 minutes | abnormal login, reset-linked new device |

These results are bounded to synthetic lab scenarios. They are not production detection rates.

## What the lab includes

- Synthetic identity and SaaS telemetry generation
- Normalized `IdentityEvent` model
- Baseline, manual-abuse, and AI-assisted-abuse scenarios
- Enriched scenarios with additional identity-risk fields
- Abnormal login detector
- Help-desk reset detector
- New-device risk detector
- OAuth scope-risk detector
- SaaS export anomaly detector
- Cumulative timeline scoring
- Scenario metrics reporting
- Scored event CSV export
- Figure generation utilities
- Sigma-style experimental detection rules
- Unit tests and CI
- Threat model, safety statement, data dictionary, and architecture documentation
- Manuscript sections, references, figure captions, and reproducibility appendix

## Safety boundary

This repository is defensive and synthetic-only. It does not include:

- real phishing or vishing campaigns;
- credential collection;
- malware;
- exploit development;
- unauthorized access guidance;
- production logs;
- real user records; or
- real customer data.

## Repository map

| Path | Purpose |
|---|---|
| `src/identity_abuse_lab/telemetry/` | Event schema and synthetic scenario generators |
| `src/identity_abuse_lab/detectors/` | Event-level detector implementations |
| `src/identity_abuse_lab/scoring/` | Event scoring and timeline correlation |
| `src/identity_abuse_lab/reports/` | Metrics, CSV export, and figure generation |
| `tests/` | Unit tests for models, detectors, scoring, reports, and figures |
| `rules/sigma/` | Sigma-style experimental rules |
| `docs/` | Threat model, safety, architecture, data dictionary, project brief |
| `paper/` | Manuscript sections, references, figures, captions, and checklists |
| `scripts/` | Reproducible command scripts |

## Quick start

Install development dependencies:

```bash
make install
```

Run tests:

```bash
make test
```

Generate synthetic telemetry:

```bash
make generate
```

Export scored events:

```bash
make export
```

Print scenario report:

```bash
make report
```

Generate paper figures:

```bash
make -f Makefile.paper figures
```

Assemble manuscript:

```bash
make -f Makefile.paper manuscript
```

## Key outputs

| Output | Command | Path |
|---|---|---|
| Synthetic JSONL telemetry | `make generate` | `data/synthetic/` |
| Scored event CSV | `make export` | `data/processed/scored_events.csv` |
| Timeline and intervention figures | `make -f Makefile.paper figures` | `paper/figures/` |
| Assembled manuscript | `make -f Makefile.paper manuscript` | `paper/manuscript_assembled.md` |

## Detection rules

The current Sigma-style rules map to the synthetic event schema:

| Rule | Signal |
|---|---|
| `rules/sigma/abnormal_login_context.yml` | Abnormal login context |
| `rules/sigma/new_device_after_risk_signal.yml` | Suspicious new-device enrollment |
| `rules/sigma/suspicious_oauth_consent.yml` | High-risk OAuth consent |
| `rules/sigma/abnormal_saas_export.yml` | High-volume SaaS export |

## Manuscript status

The manuscript currently includes:

- abstract;
- introduction;
- citation-ready related work;
- methods;
- detection model;
- results;
- discussion;
- limitations and ethics;
- conclusion;
- reproducibility appendix; and
- working references.

## Reviewer links

- Project brief: `docs/project_brief.md`
- Architecture: `docs/architecture.md`
- Threat model: `docs/threat_model.md`
- Ethics and safety: `docs/ethics_and_safety.md`
- Data dictionary: `docs/data_dictionary.md`
- Detector thresholds: `paper/detector_thresholds.md`
- Publication checklist: `paper/publication_checklist.md`
- Figure captions: `paper/figure_captions.md`
- Working references: `paper/references.md`

## Interpretation boundary

This lab is a controlled synthetic research artifact. It should not be treated as a production detection benchmark, a validated incident-response playbook, or a replacement for environment-specific security engineering. Production use would require authorized telemetry, field mapping, privacy review, legal review, security review, and threshold calibration.

## License

See `LICENSE`.
