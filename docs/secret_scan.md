# Secret Scan Guidance

Before any public release tag, run a local secret scan and review the repository for accidental sensitive material.

## Recommended checks

```bash
git status
python -m pip install detect-secrets
detect-secrets scan > .secrets.baseline
detect-secrets audit .secrets.baseline
```

Alternative tools include GitHub secret scanning, Gitleaks, TruffleHog, and repository-hosted security scanning.

## What must not be committed

- API keys
- Access tokens
- OAuth refresh tokens
- Passwords
- SSH private keys
- Production logs
- Customer data
- Real user records
- Real email addresses from investigations
- Real phishing targets
- Private incident details

## Current project policy

Identity Abuse Lab should contain synthetic telemetry only. Example IP addresses should use documentation-safe ranges, and all identities should be synthetic or generic.

## Release gate

Do not create a release tag until secret scanning and manual review are complete.
