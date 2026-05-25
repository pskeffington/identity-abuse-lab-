# Detection Rules

This directory contains Sigma-style experimental rules derived from the synthetic identity-abuse lab scenarios.

These rules are research artifacts. They are written against the normalized synthetic event schema used in this repository and must be adapted before use in production SIEM or identity-platform environments.

## Rule index

| Rule | Signal | Scenario relevance |
|---|---|---|
| `sigma/abnormal_login_context.yml` | Abnormal login context | Early identity compromise signal |
| `sigma/new_device_after_risk_signal.yml` | Suspicious new-device enrollment | Persistence or account takeover signal |
| `sigma/suspicious_oauth_consent.yml` | High-risk OAuth scope request | Consent abuse and persistence signal |
| `sigma/abnormal_saas_export.yml` | High-volume SaaS export | Collection or exfiltration signal |

## Lab finding supported

The enriched synthetic scenarios show that abnormal-login and new-device rules can produce earlier detection than OAuth or export-only detection. In the current model, enriched manual abuse is detected 28 minutes before export, while enriched AI-assisted abuse is detected 11 minutes before export.
