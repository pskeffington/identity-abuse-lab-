# Release Checklist: v0.1-lab-baseline

## Release goal

Prepare the repository as a public baseline artifact for synthetic AI-assisted identity-abuse detection research.

## Required before tagging

### Code and tests

- [x] Python package scaffold exists
- [x] Synthetic scenario generator exists
- [x] Enriched scenario generator exists
- [x] Core detectors exist
- [x] Timeline scoring exists
- [x] Metrics reporting exists
- [x] Scored export pipeline exists
- [x] Figure generation exists
- [x] Unit tests exist
- [ ] CI passing on latest commit confirmed
- [ ] Local `make test` completed
- [ ] Local `make export` completed
- [ ] Local `make -f Makefile.paper figures` completed

### Documentation

- [x] Threat model complete
- [x] Ethics and safety statement complete
- [x] Data dictionary complete
- [x] Architecture overview complete
- [x] Project brief complete
- [x] Reviewer-facing README draft complete
- [x] Publication checklist complete
- [ ] Main `README.md` updated or replaced with `docs/readme_current.md`

### Paper artifacts

- [x] Manuscript sections drafted
- [x] Related work drafted
- [x] Working references added
- [x] Reproducibility appendix added
- [x] Figure captions added
- [x] Assembled manuscript draft added
- [ ] Final inline citation pass complete
- [ ] Figures generated and committed if desired
- [ ] Tables rechecked against regenerated outputs

### Detection artifacts

- [x] Abnormal login Sigma-style rule
- [x] New-device risk Sigma-style rule
- [x] OAuth scope-risk Sigma-style rule
- [x] SaaS export anomaly Sigma-style rule
- [ ] Helpdesk reset Sigma-style rule added
- [ ] Sigma syntax review completed

### Safety review

- [x] Synthetic-only policy documented
- [x] No real credential collection
- [x] No malware
- [x] No exploit development
- [x] No real production logs
- [x] No real target lists
- [ ] Secret scan completed
- [ ] Final dual-use wording review completed

## Suggested release tag

```text
v0.1-lab-baseline
```

## Suggested release title

```text
Identity Abuse Lab v0.1: Synthetic Baseline for AI-Assisted Identity-Abuse Detection
```

## Suggested release notes

This baseline release introduces a defensive synthetic lab for evaluating identity-abuse detection across baseline, manual-abuse, and AI-assisted-abuse scenarios. The release includes normalized telemetry models, synthetic scenario generators, detector interfaces, five detector families, timeline correlation scoring, scored CSV export, figure-generation utilities, Sigma-style rules, safety documentation, and a manuscript scaffold.

The primary bounded finding is that enriched synthetic detection identifies both abuse scenarios before simulated SaaS export, but the AI-assisted scenario leaves a shorter intervention window than the manual scenario.

## Known limitations

- Synthetic telemetry only
- Small scenario count
- Heuristic detector scores
- No production calibration
- No real-world detection-rate claims
- Limited false-positive modeling
- Citation pass still in progress

## Post-release priorities

1. Add benign false-positive scenarios
2. Add multi-user synthetic dataset generation
3. Add helpdesk reset Sigma-style rule
4. Add sensitivity analysis for timeline thresholds
5. Add generated figures to manuscript
6. Complete final citation formatting
7. Prepare technical blog version
