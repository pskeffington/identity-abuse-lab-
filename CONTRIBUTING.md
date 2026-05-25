# Contributing

Identity Abuse Lab is a defensive, synthetic-only research project. Contributions should preserve the project's safety boundaries, reproducibility, and transparent methodology.

## Contribution principles

- Keep all data synthetic.
- Do not add real credentials, tokens, production logs, customer data, or real user records.
- Do not add exploit code, malware, credential collection, live phishing workflows, or unauthorized access guidance.
- Prefer transparent, inspectable detector logic over opaque complexity.
- Add or update tests when changing detector behavior, scenario generation, scoring, or reporting.
- Update documentation when changing assumptions, schemas, thresholds, or outputs.

## Development workflow

Recommended local validation:

```bash
make install
make test
make lint
make generate
make export
make report
make -f Makefile.paper figures
make -f Makefile.paper manuscript
PYTHONPATH=src:. python scripts/verify_expected_results.py
```

## Pull request expectations

A pull request should describe:

- what changed;
- why it changed;
- how it was tested;
- whether result tables or manuscript claims changed;
- whether any safety boundary changed; and
- whether documentation needs updating.

## Detector changes

Detector changes must include:

- unit tests;
- threshold documentation updates if scores change;
- expected-results updates if scenario outputs change; and
- manuscript or README updates if published claims change.

## Scenario changes

Scenario changes must preserve synthetic-only data and should include:

- updated tests;
- updated metrics expectations;
- updated data dictionary fields if new attributes are added; and
- a clear note if intervention-window values change.

## Release discipline

Before release, follow:

- `VALIDATION_CHECKLIST.md`
- `RELEASE_CHECKLIST.md`
- `docs/release_gates.md`
- `docs/secret_scan.md`
