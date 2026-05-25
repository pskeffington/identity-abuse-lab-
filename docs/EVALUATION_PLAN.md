# Defensive Evaluation Plan

## Purpose

Define a non-operational evaluation plan for identity-abuse and misuse-risk research.

## Required before implementation

1. Public-safe threat model completed.
2. Synthetic or toy data plan approved.
3. Evaluation task scoped to defensive detection, audit, or governance.
4. Exclusion rules documented.
5. Manual public-safety review completed.

## Candidate evaluation categories

| Category | Status | Notes |
|---|---|---|
| Policy or governance checklist | Pending | Lowest risk starting point |
| Synthetic detection benchmark | Pending | Must not use real identities |
| Audit-log schema | Pending | Defensive only |
| Red-team taxonomy | Pending | High-level only, no operational detail |

## Output targets

- `docs/SAFE_THREAT_MODEL.md`
- `docs/EVALUATION_PLAN.md`
- `examples/synthetic/README.md`
- `results/audit_schema_example.json`

## Boundary

Do not build or publish functionality that enables identity misuse, impersonation, fraud, credential misuse, or evasion.
