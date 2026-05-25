# Enriched Detection Results

The enriched detector set adds abnormal-login and new-device risk scoring to the original OAuth and SaaS export detectors.

| Scenario | Detected before export | Intervention window | Additional early signals |
|---|---:|---:|---|
| manual_abuse | Yes | 28.0 minutes | abnormal login, unknown new device |
| ai_assisted_abuse | Yes | 11.0 minutes | abnormal login, reset-linked new device |

## Interpretation

Adding abnormal-login and new-device detectors shifts detection earlier in the synthetic chain. In the current enriched scenario design, manual abuse is detected 28 minutes before export, while AI-assisted abuse is detected 11 minutes before export.

This strengthens the project claim: identity telemetry can expose abuse before OAuth consent or data export, but AI-assisted compression still reduces the available response window.

## Methodological note

The enriched generator is intentionally separated from the first baseline generator. This keeps the original simple scenario stable while allowing additional telemetry realism to be added without rewriting earlier results.
