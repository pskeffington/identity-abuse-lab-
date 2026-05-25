# Project Brief: Identity Abuse Lab

## One-sentence summary

Identity Abuse Lab is a defensive synthetic research environment for measuring whether correlated identity and SaaS telemetry can detect simulated manual and AI-assisted account-abuse chains before data export.

## Problem

Modern enterprise abuse often moves through identity systems rather than traditional perimeter compromise. Login context, help-desk reset workflows, new-device enrollment, OAuth consent, and SaaS export activity may each look ordinary in isolation, but together they can represent a high-risk abuse chain.

AI assistance may compress that chain, leaving defenders less time to review alerts and act before collection or export.

## Research question

Which telemetry signals most reliably distinguish normal SaaS identity behavior from simulated AI-assisted identity-abuse chains in a controlled enterprise lab?

## Current finding

In the enriched synthetic scenario set, correlated identity telemetry detects both abuse chains before export:

| Scenario | Detected before export | Intervention window |
|---|---:|---:|
| Manual abuse | Yes | 28.0 minutes |
| AI-assisted abuse | Yes | 11.0 minutes |

The working finding is that AI assistance may not require fundamentally different telemetry categories to detect, but it can compress the response window enough that slow manual review becomes less reliable.

## What is implemented

- Synthetic identity/SaaS telemetry generation
- Normalized `IdentityEvent` model
- Event-level detector interface
- Abnormal login detector
- Help-desk reset detector
- New-device risk detector
- OAuth scope-risk detector
- SaaS export anomaly detector
- Cumulative timeline scoring
- Scenario metrics reporting
- Scored event CSV export
- Figure generation utilities
- Sigma-style experimental rules
- Tests and CI
- Manuscript sections and reproducibility appendix

## Why this matters

The project demonstrates the overlap of cyber threat intelligence, identity security, trust and safety, AI abuse analysis, detection engineering, and reproducible research. It converts a broad AI-risk claim into a measurable defensive variable: intervention time before simulated data export.

## Safety boundary

The project is synthetic-only. It does not include real phishing, credential collection, malware, exploit development, unauthorized access guidance, real user records, or production telemetry.

## Best use cases

- Cyber threat intelligence portfolio artifact
- AI abuse investigation portfolio artifact
- Trust and safety technical assessment example
- Detection engineering research lab
- Technical white paper foundation
- Reproducible security research demo
