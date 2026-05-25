# Identity Abuse Lab Artifact

## Artifact title

**Identity Abuse Lab: A Synthetic Research Environment for AI-Assisted Identity-Abuse Detection**

## Artifact type

Defensive cyber threat analysis and research-engineering artifact.

## One-sentence description

Identity Abuse Lab is a synthetic, reproducible research environment that measures whether correlated identity and SaaS telemetry can detect simulated manual and AI-assisted account-abuse chains before data export.

## Core contribution

The artifact links five components into one inspectable workflow:

1. synthetic identity and SaaS telemetry;
2. transparent Python detector logic;
3. cumulative timeline scoring;
4. Sigma-style experimental detection rules; and
5. manuscript-ready documentation and reproducibility controls.

## Current bounded finding

In the enriched synthetic scenario set, correlated identity telemetry detects both manual and AI-assisted abuse before simulated SaaS export. The manual-abuse scenario leaves a 28-minute intervention window, while the AI-assisted scenario leaves an 11-minute intervention window.

This supports a bounded working finding: AI-assisted identity abuse may not require fundamentally different telemetry categories to detect, but it can compress the defender response window enough that slow manual review and late-stage exfiltration alerts become less reliable.

## Artifact components

| Component | Location | Purpose |
|---|---|---|
| Telemetry model | `src/identity_abuse_lab/telemetry/event.py` | Defines normalized event structure |
| Scenario generators | `src/identity_abuse_lab/telemetry/` | Generate baseline, manual-abuse, and AI-assisted-abuse timelines |
| Detectors | `src/identity_abuse_lab/detectors/` | Score identity and SaaS risk signals |
| Timeline scoring | `src/identity_abuse_lab/scoring/timeline.py` | Measures detection-before-export and intervention windows |
| Reports and export | `src/identity_abuse_lab/reports/` | Produces metrics, CSV outputs, and figures |
| Detection rules | `rules/sigma/` | Translates detector logic into Sigma-style rule artifacts |
| Manuscript | `paper/` | Stores paper sections, results, captions, references, and appendix |
| Safety docs | `docs/ethics_and_safety.md`, `SECURITY.md` | Define defensive boundaries |
| Release docs | `RELEASE_STATUS.md`, `VALIDATION_CHECKLIST.md` | Define validation and release gates |

## What the artifact demonstrates

- Cyber threat analysis framing
- Identity-security telemetry modeling
- AI-abuse risk reasoning
- Object-oriented Python implementation
- Detector design and testing
- Timeline-based risk correlation
- Reproducible result validation
- Detection-rule translation
- Publication discipline
- Safety-aware dual-use handling

## Reproduction path

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

## Safety boundary

This artifact is synthetic-only and defensive. It does not include real phishing, credential collection, malware, exploit development, unauthorized access guidance, production logs, real user data, customer data, or real incident-sensitive material.

## Intended audiences

- AI abuse investigation teams
- Trust and safety teams
- Cyber threat intelligence teams
- Identity-security teams
- Detection engineers
- Security research reviewers
- Technical hiring reviewers

## Status

The artifact is suitable for internal review and portfolio preview. Public baseline release should wait for successful local validation, CI confirmation, secret scan, README replacement, final table verification, and citation cleanup.
