# Detection Rule Mapping

The lab produces four Sigma-style experimental rules aligned to the synthetic identity-abuse chain.

| Chain phase | Synthetic event | Detector | Rule file | Purpose |
|---|---|---|---|---|
| Initial access | `login` | AbnormalLoginDetector | `rules/sigma/abnormal_login_context.yml` | Detect abnormal login context before later abuse steps |
| Persistence / account takeover | `new_device` | NewDeviceRiskDetector | `rules/sigma/new_device_after_risk_signal.yml` | Detect suspicious device enrollment or first-seen device behavior |
| Persistence / collection | `oauth_consent` | OAuthScopeRiskDetector | `rules/sigma/suspicious_oauth_consent.yml` | Detect high-risk OAuth scope consent |
| Collection / exfiltration | `saas_export` | SaaSExportAnomalyDetector | `rules/sigma/abnormal_saas_export.yml` | Detect high-volume SaaS object export |

## Interpretation

The detection rules translate the Python scoring model into portable security logic. The early-chain rules are especially important because they detect abnormal access and device-state changes before simulated OAuth consent or SaaS export.

## Research contribution

This bridges three artifacts in one reproducible workflow: synthetic telemetry, executable scoring code, and human-readable detection rules. That structure supports both technical replication and operational review.
