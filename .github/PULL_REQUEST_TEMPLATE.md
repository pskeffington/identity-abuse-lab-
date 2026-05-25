# Pull Request

## Summary

Describe the change.

## Type of change

- [ ] Bug fix
- [ ] Feature
- [ ] Documentation
- [ ] Test
- [ ] Release/workflow
- [ ] Manuscript/paper

## Affected area

- [ ] telemetry generation
- [ ] detectors
- [ ] scoring
- [ ] reports/exports
- [ ] figures
- [ ] Sigma-style rules
- [ ] docs/manuscript
- [ ] CI/release

## Validation

- [ ] `make test`
- [ ] `make lint`
- [ ] `PYTHONPATH=src:. python scripts/verify_expected_results.py`
- [ ] Generated tables reviewed if outputs changed
- [ ] Manuscript/docs updated if claims changed

## Safety review

- [ ] Synthetic-only data
- [ ] No credentials or secrets
- [ ] No production logs
- [ ] No real user records
- [ ] No exploit or malware content
- [ ] No live phishing or unauthorized access guidance

## Result impact

Does this change expected metrics, intervention windows, or manuscript tables?

- [ ] No
- [ ] Yes, and expected-results checks/docs have been updated
