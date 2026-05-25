# Detecting AI-Assisted Identity Abuse in a Synthetic SaaS Enterprise Lab

## Abstract

This paper presents a controlled synthetic lab for studying identity-first abuse patterns in SaaS environments. The lab compares baseline user behavior, manually simulated identity abuse, and AI-assisted identity abuse using normalized identity and SaaS telemetry. The project implements transparent detectors for abnormal login context, help-desk reset risk, new-device risk, OAuth scope risk, and SaaS export anomalies. It then applies cumulative timeline scoring to measure whether abuse chains are detected before simulated data export.

Initial synthetic results suggest that AI-assisted identity abuse may not require fundamentally different telemetry to detect, but it compresses the response window available to defenders. In the enriched scenario set, manual abuse is detected 28 minutes before export, while AI-assisted abuse is detected 11 minutes before export. The repository contributes synthetic telemetry generation, executable Python scoring code, Sigma-style detection rules, and reproducible result outputs.

## 1. Introduction

Identity-first intrusions increasingly exploit authentication workflows, SaaS permissions, help-desk processes, OAuth consent, and cloud application access rather than relying only on malware or endpoint compromise. This shift creates a detection problem centered on weak identity signals that may appear benign in isolation but become meaningful when correlated across time.

This project asks whether controlled synthetic telemetry can be used to evaluate detection windows for identity-abuse chains, especially when AI assistance compresses the time between initial lure and attempted SaaS export.

## 2. Research Question

Which telemetry signals most reliably distinguish normal SaaS identity behavior from simulated AI-assisted identity-abuse chains in a controlled enterprise lab?

## 3. Threat Model

The simulated adversary is an identity-first abuse actor attempting to move from social-engineering contact to account access, persistence, collection, and SaaS export. The lab does not model real credential theft, real phishing campaigns, malware, exploit development, or unauthorized access.

## 4. Lab Design

The lab defines three synthetic scenario families: baseline activity, manual identity abuse, and AI-assisted identity abuse. Each scenario is represented as a sequence of normalized identity events containing a user identifier, timestamp, source, event type, IP address, user agent, and event-specific attributes.

## 5. Detection Method

The initial detector set includes abnormal-login scoring, help-desk reset scoring, new-device scoring, OAuth scope scoring, and SaaS export anomaly scoring. A cumulative timeline scorer applies detector outputs in event order and records when the detection threshold is crossed.

## 6. Results

The first scenario-level result set shows separation between baseline and abuse scenarios. Baseline activity remains low risk, while manual and AI-assisted scenarios produce high-risk events and elevated export volume.

The timeline result set shows that enriched detection can identify synthetic abuse before the export event. Manual abuse leaves a larger intervention window than AI-assisted abuse in the current scenario design.

## 7. Detection Rule Mapping

The repository maps detector logic to Sigma-style experimental rules for abnormal login context, suspicious new-device enrollment, high-risk OAuth consent, and high-volume SaaS export. These rules are written against the synthetic schema and require adaptation before production use.

## 8. Limitations

The lab uses synthetic telemetry and transparent heuristics. Results should not be interpreted as real-world detection rates. Scenario timing, thresholds, event fields, and detector weights are design parameters that require further validation.

## 9. Ethics and Safety

The project is defensive and synthetic-only. It does not include real phishing, credential collection, exploit code, malware, unauthorized access guidance, real user records, or production telemetry.

## 10. Future Work

Future work will add multi-user synthetic datasets, false-positive scenarios, help-desk workflow variants, MFA reset events, session reuse events, detector explainability, figures, and broader benchmark runs.

## 11. Conclusion

The lab demonstrates a reproducible way to study AI-assisted identity abuse using synthetic telemetry, transparent detection logic, and measurable intervention windows. The central early finding is that AI assistance may compress response time more than it changes the fundamental telemetry categories available to defenders.
