# Release Gates

This document defines the gates that should pass before tagging `v0.1-lab-baseline`.

## Automated gates

The following workflows should pass on `main` before release:

| Workflow | Purpose |
|---|---|
| `.github/workflows/tests.yml` | Runs test suite and Ruff linting |
| `.github/workflows/validate-results.yml` | Verifies expected scenario metrics and enriched intervention windows |
| `.github/workflows/release-validation.yml` | Full release validation workflow for tags and manual dispatch |

## Release validation workflow

The release validation workflow runs:

```text
pytest
ruff check src tests
python -m identity_abuse_lab generate
PYTHONPATH=src python scripts/export_scored_events.py
PYTHONPATH=src:. python scripts/verify_expected_results.py
PYTHONPATH=src python scripts/generate_figures.py
PYTHONPATH=src python scripts/assemble_manuscript.py
```

## Manual gates

Before release, manually confirm:

- root `README.md` has been updated from `docs/readme_current.md`;
- generated figures render correctly;
- generated tables match manuscript claims;
- release notes accurately describe known limitations;
- `docs/secret_scan.md` has been followed;
- no secrets, production logs, real user records, or real incident-sensitive data are present;
- dual-use wording remains defensive and synthetic-only.

## Tag gate

Only tag after automated and manual gates pass:

```bash
git tag v0.1-lab-baseline
git push origin v0.1-lab-baseline
```

Use `RELEASE_NOTES_v0.1.md` as the release-note draft.
