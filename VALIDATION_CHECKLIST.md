# Local Validation Checklist

Use this checklist before tagging `v0.1-lab-baseline`.

## 1. Clean working tree

```bash
git status
```

Expected result: no unexpected modified or untracked files, except generated artifacts intentionally being reviewed.

## 2. Install dependencies

```bash
make install
```

Expected result: package installs in editable mode with development dependencies.

## 3. Run tests

```bash
make test
```

Expected result: all tests pass.

Current test coverage should include:

- event model tests;
- detector tests;
- helpdesk reset tests;
- generator tests;
- metrics tests;
- timeline tests;
- enriched timeline tests;
- export pipeline tests; and
- figure generation tests.

## 4. Run lint

```bash
make lint
```

Expected result: no Ruff lint failures.

## 5. Generate synthetic telemetry

```bash
make generate
```

Expected outputs:

```text
data/synthetic/baseline_events.jsonl
data/synthetic/manual_abuse_events.jsonl
data/synthetic/ai_assisted_abuse_events.jsonl
```

## 6. Export scored events

```bash
make export
```

Expected output:

```text
data/processed/scored_events.csv
```

Confirm the CSV contains columns:

```text
scenario,timestamp,user_id,source,event_type,ip_address,event_score,cumulative_score,detected
```

## 7. Print scenario report

```bash
make report
```

Confirm the printed table still matches the manuscript tables or update the manuscript if values changed.

## 8. Generate figures

```bash
make -f Makefile.paper figures
```

Expected outputs:

```text
paper/figures/timeline_risk.png
paper/figures/intervention_window.png
```

Open both figures and confirm they render correctly.

## 9. Assemble manuscript

```bash
make -f Makefile.paper manuscript
```

Expected output:

```text
paper/manuscript_assembled.md
```

Confirm the assembled manuscript includes:

- abstract;
- introduction;
- related work;
- methods;
- detection model;
- results;
- discussion;
- limitations and ethics;
- conclusion;
- reproducibility appendix; and
- references.

## 10. Update root README

Before release, update the root README from the reviewer-facing draft:

```bash
cp docs/readme_current.md README.md
git add README.md
git commit -m "docs: update README for v0.1 baseline review"
```

## 11. Secret scan

Follow `docs/secret_scan.md`.

Minimum recommended command:

```bash
python -m pip install detect-secrets
detect-secrets scan > .secrets.baseline
detect-secrets audit .secrets.baseline
```

Do not release if unexpected secrets, tokens, credentials, production logs, or real user data are found.

## 12. Table verification

Cross-check generated outputs against:

- `paper/results_table.md`
- `paper/timeline_detection_results.md`
- `paper/enriched_detection_results.md`
- `paper/sections/05_results.md`
- `docs/project_brief.md`
- `docs/readme_current.md`
- `RELEASE_NOTES_v0.1.md`

If generated values differ, update all affected files before tagging.

## 13. Final safety review

Confirm the repository does not include:

- real phishing workflows;
- credential collection;
- malware;
- exploit code;
- production logs;
- real victim information;
- unauthorized access guidance; or
- real incident-sensitive data.

## 14. Suggested tag

After validation passes:

```bash
git tag v0.1-lab-baseline
git push origin v0.1-lab-baseline
```

Use `RELEASE_NOTES_v0.1.md` as the release-note draft.
