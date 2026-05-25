# 3. Detection Model

## 3.1 Abnormal login context

The abnormal-login detector scores login events with contextual risk attributes. The current model considers geographic change, impossible travel, unfamiliar user agent, and anonymous network indicators. These fields represent common identity-risk categories without binding the lab to any specific production identity provider.

The detector is intended to identify early account-access anomalies before later persistence or collection behavior appears.

## 3.2 Help-desk reset risk

The help-desk reset detector scores account recovery events. It considers reset channel, whether identity verification was completed, urgency pressure, geographic context, and executive-impersonation claims. The purpose is to model a high-risk account-recovery path often associated with identity-first social engineering.

This detector gives the lab a way to evaluate account recovery as an early abuse signal rather than treating compromise as beginning only at login.

## 3.3 New-device risk

The new-device detector scores first-seen device or device-enrollment events. Unknown device state, reset-linked enrollment, geographic change, and blocked or malicious trust state increase risk. This captures a common persistence or account-takeover indicator: the addition of a device that can maintain access or bypass normal user expectations.

## 3.4 OAuth scope risk

The OAuth detector scores consent events based on requested scope sensitivity. High-risk scopes include mail access, file access, offline access, directory access, and broad user-read scopes. The detector is designed to model consent-abuse risk without implementing any real OAuth abuse flow.

## 3.5 SaaS export anomaly

The SaaS export detector scores export events by object volume. Low-volume exports are treated as low risk, while high-volume exports represent collection or exfiltration-like behavior in the synthetic scenario.

## 3.6 Correlated timeline scoring

The timeline scorer combines event-level signals into a cumulative chain score. This is intentionally simple and transparent. It supports the research objective by allowing the lab to compare when detection occurs relative to export. A richer future model may introduce user baselines, probabilistic calibration, graph features, or supervised learning, but the current design prioritizes interpretability and reproducibility.

## 3.7 Rule translation

The lab maps detector concepts to Sigma-style experimental rules. These rules are written against the synthetic event schema and are not intended for direct production deployment. Their purpose is to translate research logic into security-operations artifacts that a reviewer can inspect and adapt.
