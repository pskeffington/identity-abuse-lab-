# Executive Summary

## Project overview

Identity Abuse Lab is a defensive research and engineering project that models synthetic identity-abuse chains in SaaS environments. It compares normal user activity, manually simulated abuse, and AI-assisted abuse using normalized telemetry, transparent Python detectors, timeline correlation scoring, and Sigma-style detection rules.

## Core finding

The current synthetic results support a bounded research claim: AI-assisted identity abuse may not require fundamentally different telemetry to detect, but it can compress the response window enough that slow manual review and late-stage exfiltration alerts become less reliable.

## Current enriched result

| Scenario | Detected before export | Intervention window | Early signals |
|---|---:|---:|---|
| Manual abuse | Yes | 28.0 minutes | abnormal login, unknown new device |
| AI-assisted abuse | Yes | 11.0 minutes | abnormal login, reset-linked new device |

## What the repo demonstrates

The repository demonstrates:

- Synthetic telemetry generation
- Object-oriented Python event modeling
- Detector interface design
- Event-level risk scoring
- Timeline correlation scoring
- Reproducible metrics generation
- Scored event export pipeline
- Sigma-style detection logic
- Defensive threat modeling
- Safety-aware publication framing

## Why it matters

Identity-first intrusions often depend on account access, help-desk workflows, device state, OAuth consent, and SaaS export behavior. These signals may be weak individually but meaningful when correlated. This lab shows how a defender can measure whether detection occurs before simulated export and how much intervention time remains.

## Intended audience

This project is useful for:

- Cyber threat intelligence teams
- Trust and safety investigators
- AI abuse investigators
- Identity security teams
- SaaS security teams
- Detection engineers
- Security researchers

## Safety boundary

The lab is synthetic-only. It does not include live phishing, credential collection, malware, exploit development, production tenant attacks, or instructions for unauthorized access.

## Next priorities

Near-term development should focus on adding multi-user synthetic data, false-positive scenarios, help-desk workflow variants, MFA reset events, notebook visualizations, and a polished manuscript suitable for technical publication.
