# 6. Limitations and Ethics

## 6.1 Synthetic evidence boundary

The lab uses synthetic telemetry. The results should not be interpreted as estimates of real-world detection rates, attacker success rates, or enterprise false-positive rates. The event timings, attribute values, detector thresholds, and export volumes are scenario-design choices.

The purpose of the lab is to create a reproducible framework for reasoning about identity-abuse telemetry and response-window compression. Production validation would require authorized enterprise telemetry, legal review, privacy review, security review, and environment-specific tuning.

## 6.2 Detector calibration

The detector scores are transparent heuristics. They are useful for reproducible comparison, but they are not calibrated probabilities. A score of 1.00 should be read as maximum detector concern within the lab model, not as a quantified probability of compromise.

Future work should test threshold sensitivity, false-positive conditions, user-baseline deviation, and detector contribution analysis.

## 6.3 Scenario realism

The current scenarios are intentionally compact. They contain enough structure to demonstrate the method, but they do not capture the full complexity of enterprise identity systems, device management, SaaS audit logging, identity governance, legal hold workflows, or incident-response processes.

## 6.4 Dual-use controls

The project is defensive and synthetic-only. It excludes real phishing, credential collection, exploit code, malware, unauthorized access guidance, and production logs. Detection rules are written against a synthetic schema and require adaptation before production use.

## 6.5 Human-subjects considerations

The current project does not involve human subjects. It does not collect user behavior, conduct interviews, run surveys, or test real employees. If future work incorporates real incident data, interviews, or user studies, additional ethics review may be required.
