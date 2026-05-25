# 2. Methods

## 2.1 Study design

Identity Abuse Lab uses a controlled synthetic scenario design. The lab compares three categories of identity and SaaS telemetry: normal baseline activity, manually simulated identity abuse, and AI-assisted identity abuse. Each scenario is represented as a chronological event sequence using a shared normalized schema.

The design goal is not to estimate real-world incident rates. Instead, the lab measures how detector scores evolve over time in controlled scenarios and whether detection occurs before a simulated SaaS export event.

## 2.2 Synthetic event schema

Each event is represented as an `IdentityEvent` object with the following core fields: user identifier, timestamp, source, event type, IP address, user agent, optional risk score, and event-specific attributes. The current event types include login, logout, document read, SaaS export, lure received, help-desk reset, new-device enrollment, and OAuth consent.

The schema is intentionally compact. It is designed to support transparent detection logic while remaining simple enough for reviewers to inspect and reproduce.

## 2.3 Scenario families

The baseline scenario models ordinary SaaS activity, including login, document reads, a low-volume export, and logout. The manual abuse scenario models a slower account-abuse chain involving an initial lure marker, abnormal login, new-device enrollment, OAuth consent, and high-volume SaaS export. The AI-assisted abuse scenario uses the same general chain but compresses the timeline and increases selected risk attributes to represent faster campaign iteration and execution.

An enriched scenario generator adds additional context fields, including unfamiliar user-agent markers, anonymous network markers, reset-linked device enrollment, and geographic-change context. This keeps the original simple scenario stable while allowing expanded telemetry realism.

## 2.4 Detection logic

The lab implements modular detectors through a shared detector interface. Each detector receives a normalized event and returns a transparent normalized score. Current detectors include abnormal login context, help-desk reset risk, new-device risk, OAuth scope risk, and SaaS export anomaly scoring.

Detector scores are heuristic and interpretable. They are not calibrated probabilities. Their purpose is to support reproducible scenario comparison and defensible discussion of detection windows.

## 2.5 Timeline correlation

Event-level scores are combined through cumulative timeline scoring. Events are sorted chronologically. At each event, the timeline scorer applies decay to the previous cumulative score and adds the current event score. Detection occurs when the cumulative score crosses a configured threshold.

The primary outcome is detection before simulated export. A secondary outcome is the intervention window, defined as the time between first detection and first SaaS export.

## 2.6 Reproducibility

The repository includes unit tests, reproducible scripts, a Makefile, synthetic generation utilities, scored event export logic, scenario metrics reporting, paper result tables, and Sigma-style detection rules. A reviewer can inspect detector logic, run tests, generate synthetic events, export scored events, and reproduce the reported scenario-level outputs.
