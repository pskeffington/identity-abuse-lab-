# Release Status: v0.1-lab-baseline

## Current status

The repository is close to a v0.1 baseline release. The core research-engineering artifact is implemented: synthetic telemetry, detectors, scoring, tests, detection rules, documentation, and manuscript scaffolding are all present.

## Completed release items

- Python package scaffold
- Synthetic scenario generation
- Enriched scenario generation
- IdentityEvent schema
- Detector interface
- Abnormal login detector
- Helpdesk reset detector
- New-device detector
- OAuth scope-risk detector
- SaaS export anomaly detector
- Timeline correlation scoring
- Scenario metrics reporter
- Scored event export pipeline
- Figure generation utilities
- Unit tests
- CI workflow
- Sigma-style rules for all current detector families
- Threat model
- Ethics and safety statement
- Data dictionary
- Architecture overview
- Project brief
- Reviewer-facing README draft
- Manuscript sections
- Related work draft
- Working references
- Reproducibility appendix
- Publication checklist
- Release checklist
- Secret scan guidance

## Still required before tagging

1. Confirm latest CI run passes.
2. Run local `make test`.
3. Run local `make export`.
4. Run local `make -f Makefile.paper figures`.
5. Replace or update main `README.md` using `docs/readme_current.md`.
6. Complete secret scan and manual review.
7. Confirm generated tables match manuscript tables.
8. Complete final inline-citation pass or mark citations as working draft.
9. Create release tag `v0.1-lab-baseline`.

## Release readiness judgment

The repository is suitable for internal review and portfolio preview now. It should wait for test confirmation, secret scan, README update, and final table verification before being tagged as a public v0.1 release.
