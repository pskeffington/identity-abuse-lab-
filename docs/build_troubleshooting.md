# Build Troubleshooting

This document records likely build issues and fixes for the artifact workflows.

## Known CI-sensitive areas

### Ruff import ordering

The project originally enabled Ruff import sorting through the `I` rule. In CI, this can fail builds even when code is functionally correct. A `.ruff.toml` override now keeps linting focused on core correctness checks:

```toml
line-length = 100
src = ["src", "tests"]

[lint]
select = ["E", "F", "B", "UP"]
```

### Package initialization

The detector package now includes:

```text
src/identity_abuse_lab/detectors/__init__.py
```

This makes detector imports more reliable in tests, scripts, and CI environments.

### Workflow artifacts

The `artifact-build` workflow expects the following generated files:

```text
data/synthetic/*.jsonl
data/processed/scored_events.csv
paper/figures/*.png
paper/manuscript_assembled.md
```

If artifact upload fails, check whether the generation step before it completed successfully.

## Local debug order

Run these commands in order:

```bash
python -m pip install -e .[dev]
pytest
ruff check src tests
python -m identity_abuse_lab generate
PYTHONPATH=src python scripts/export_scored_events.py
PYTHONPATH=src:. python scripts/verify_expected_results.py
PYTHONPATH=src python scripts/generate_figures.py
PYTHONPATH=src python scripts/assemble_manuscript.py
```

## Most likely failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Ruff fails on import order | Import sorting rule too strict for current artifact stage | `.ruff.toml` override added |
| ImportError for detector modules | Missing package init or PYTHONPATH issue | `detectors/__init__.py` added; use `PYTHONPATH=src:.` for scripts |
| Upload artifact fails | Expected generated file missing | Check generation step above the upload |
| Figure generation fails | Matplotlib/backend issue | Confirm matplotlib install from `pyproject.toml` and run locally |
| Expected results fail | Scenario or detector changed without updating expected values | Update `scripts/verify_expected_results.py` and affected manuscript tables |
