# Detector Thresholds and Scoring Notes

This table documents the current detector scoring logic used in the synthetic lab. Scores are transparent heuristics, not calibrated production probabilities.

| Detector | Event type | Key attributes | Score logic summary | Purpose |
|---|---|---|---|---|
| `AbnormalLoginDetector` | `login` | `geo_change`, `impossible_travel`, `unfamiliar_user_agent`, `anonymous_network` | 1 signal = 0.55; 2 signals = 0.80; 3+ signals = 1.00 | Detect abnormal access context early in the chain |
| `HelpdeskResetDetector` | `helpdesk_reset` | `reset_channel`, `identity_verified`, `urgent_request`, `geo_change`, `executive_claim` | 1 signal = 0.35; 2 signals = 0.65; 3 signals = 0.85; 4+ signals = 1.00 | Detect suspicious account-recovery workflows |
| `NewDeviceRiskDetector` | `new_device` | `device_trust`, `after_reset`, `geo_change` | unknown = 0.65; unknown + geo = 0.85; reset + geo = 0.95; blocked/malicious = 1.00 | Detect suspicious first-seen or enrolled device activity |
| `OAuthScopeRiskDetector` | `oauth_consent` | `scopes` | no scopes = 0.20; no high-risk overlap = 0.30; 1 high-risk scope = 0.60; 2 = 0.80; 3+ = 1.00 | Detect risky OAuth consent and broad SaaS permissions |
| `SaaSExportAnomalyDetector` | `saas_export` | `object_count` | 1+ objects = 0.20; >= 50 = 0.65; >= 500 = 1.00 | Detect high-volume SaaS collection/export behavior |

## Timeline threshold

The timeline correlation scorer currently uses:

| Parameter | Default | Description |
|---|---:|---|
| `detection_threshold` | 1.20 | Cumulative risk score required for scenario detection |
| `decay` | 0.90 | Prior cumulative score decay applied at each event |

## Interpretation boundary

These thresholds are useful for controlled comparison across synthetic scenarios. They are not production thresholds and should not be used directly in a live SIEM or identity platform without validation, tuning, and approved field mapping.
