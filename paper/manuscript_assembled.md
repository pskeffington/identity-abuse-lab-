# Abstract

Identity-first abuse increasingly targets authentication workflows, SaaS permissions, help-desk recovery processes, and OAuth consent rather than relying only on endpoint malware or software exploitation. This paper presents Identity Abuse Lab, a controlled synthetic research environment for evaluating how correlated identity telemetry can detect simulated SaaS account-abuse chains before data export. The lab compares baseline user activity, manually simulated identity abuse, and AI-assisted identity abuse using a normalized event schema, transparent Python detectors, cumulative timeline scoring, and Sigma-style detection rules.

The current implementation models abnormal login context, help-desk reset risk, new-device enrollment, OAuth scope risk, and SaaS export anomaly signals. Initial synthetic results show that enriched correlation detects both manual and AI-assisted abuse before simulated export. In the current scenario design, manual abuse is detected 28 minutes before export, while AI-assisted abuse is detected 11 minutes before export. These findings are intentionally bounded to synthetic scenarios, but they support a defensible working thesis: AI assistance may not require fundamentally different telemetry categories to detect identity abuse, but it can compress the defender response window enough that slow manual review and late-stage exfiltration alerts become less reliable.

The project contributes a reproducible defensive lab, synthetic telemetry generation, event-level and timeline-level scoring, test-backed result claims, detection-rule mappings, and a publication-ready research scaffold. All data are synthetic, and the repository excludes real phishing, credential collection, malware, exploit development, production logs, or instructions for unauthorized access.

# 1. Introduction

Enterprise intrusion patterns increasingly reflect an identity-first operating environment. In many modern incidents, the decisive security boundary is not a vulnerable endpoint or an exposed network service, but the integrity of authentication, account recovery, OAuth consent, device enrollment, and SaaS access workflows. These workflows create a detection challenge because the relevant signals often appear as ordinary business telemetry: a login, a reset, a new device, an application consent, or a document export. Individually, these events may not be sufficient to justify a major response. Correlated in sequence, they may represent an account-abuse chain.

AI assistance may intensify this problem by compressing the time required to prepare social-engineering content, tailor lures, iterate messages, simulate personas, or move from access to collection. The defensive question is therefore not only whether identity-abuse telemetry can be detected, but whether defenders can detect it early enough to act before SaaS data is exported.

This paper introduces Identity Abuse Lab, a synthetic research environment designed to test that question in a controlled and reproducible way. The lab generates synthetic event sequences for baseline user behavior, manually simulated identity abuse, and AI-assisted identity abuse. It then applies transparent detector logic and cumulative timeline scoring to measure whether detection occurs before simulated export and how much intervention time remains.

The project is deliberately narrow. It does not simulate real phishing campaigns, collect credentials, target real users, exploit real systems, or publish offensive procedures. Instead, it focuses on defensive telemetry modeling: which synthetic signals appear, when they appear, how they can be scored, and how response windows differ between manual and AI-assisted scenarios.

The central research question is: which telemetry signals most reliably distinguish normal SaaS identity behavior from simulated AI-assisted identity-abuse chains in a controlled enterprise lab?

The initial contribution is threefold. First, the project provides a reproducible synthetic dataset design and normalized event schema. Second, it implements Python-based detectors for abnormal login context, help-desk reset risk, new-device risk, OAuth scope risk, and SaaS export anomalies. Third, it translates those detectors into Sigma-style rule artifacts and uses timeline scoring to quantify detection-before-export windows.

# 2. Related Work and Literature Review

Identity-first compromise, OAuth abuse, help-desk social engineering, synthetic CTI research, and AI-assisted cyber operations all motivate this lab. The modular related-work section is maintained in `paper/sections/02_related_work_cited.md` and should be treated as the canonical citation-ready literature review source until final manuscript assembly.

# 3. Methods

Identity Abuse Lab uses a controlled synthetic scenario design. The lab compares normal baseline activity, manually simulated identity abuse, and AI-assisted identity abuse. Each scenario is represented as a chronological event sequence using a shared normalized schema.

The design goal is not to estimate real-world incident rates. Instead, the lab measures how detector scores evolve over time in controlled scenarios and whether detection occurs before a simulated SaaS export event.

# 4. Detection Model

The lab implements modular detectors through a shared detector interface. Each detector receives a normalized event and returns a transparent normalized score. Current detectors include abnormal login context, help-desk reset risk, new-device risk, OAuth scope risk, and SaaS export anomaly scoring.

Detector scores are heuristic and interpretable. They are not calibrated probabilities. Their purpose is to support reproducible scenario comparison and defensible discussion of detection windows.

# 5. Results

The initial synthetic result set separates baseline behavior from abuse scenarios. Baseline activity contains five events over forty minutes, produces a maximum detector score of 0.20, and includes only a low-volume export of four objects. Manual abuse and AI-assisted abuse each contain five events and produce maximum detector scores of 1.00. Manual abuse includes a simulated export volume of 650 objects, while AI-assisted abuse includes a simulated export volume of 900 objects.

| Scenario | Events | Duration min | Max score | High-risk events | Export volume | OAuth consents |
|---|---:|---:|---:|---:|---:|---:|
| baseline | 5 | 40.0 | 0.20 | 0 | 4 | 0 |
| manual_abuse | 5 | 77.0 | 1.00 | 2 | 650 | 1 |
| ai_assisted_abuse | 5 | 24.0 | 1.00 | 2 | 900 | 1 |

The enriched result shows earlier detection:

| Scenario | Detected before export | Intervention window | Additional early signals |
|---|---:|---:|---|
| manual_abuse | Yes | 28.0 minutes | abnormal login, unknown new device |
| ai_assisted_abuse | Yes | 11.0 minutes | abnormal login, reset-linked new device |

# 6. Discussion

The current lab results suggest that AI-assisted identity abuse should be analyzed not only as a problem of new indicators, but as a problem of compressed operational tempo. In the synthetic scenarios, the same broad telemetry families remain informative: abnormal login context, device enrollment, OAuth consent, and SaaS export behavior. The differentiating factor is the reduced time between the initial lure marker and the simulated export event.

This distinction matters for defensive operations. Many organizations rely on alert triage, manual review, ticket routing, escalation queues, and human approval processes. If AI assistance compresses an abuse chain from more than an hour to less than half an hour, a detector may technically fire before exfiltration while still failing operationally because the response process is too slow.

# 7. Limitations and Ethics

The lab uses synthetic telemetry. The results should not be interpreted as estimates of real-world detection rates, attacker success rates, or enterprise false-positive rates. The event timings, attribute values, detector thresholds, and export volumes are scenario-design choices.

The project is defensive and synthetic-only. It excludes real phishing, credential collection, exploit code, malware, unauthorized access guidance, and production logs. Detection rules are written against a synthetic schema and require adaptation before production use.

# 8. Conclusion

Identity Abuse Lab demonstrates a reproducible method for studying AI-assisted identity abuse using synthetic SaaS and identity-provider telemetry. The lab generates controlled scenarios, scores event-level risk, correlates risk across timelines, exports scored event data, and maps detector concepts to Sigma-style rules.

The current synthetic findings support a bounded but useful conclusion: AI-assisted abuse may not require fundamentally new telemetry categories to detect, but it can compress the response window enough that late-stage alerts and slow manual review become less reliable.

# References

See `paper/references.md` for the working bibliography.
