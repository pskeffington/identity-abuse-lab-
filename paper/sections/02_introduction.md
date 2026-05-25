# 1. Introduction

Enterprise intrusion patterns increasingly reflect an identity-first operating environment. In many modern incidents, the decisive security boundary is not a vulnerable endpoint or an exposed network service, but the integrity of authentication, account recovery, OAuth consent, device enrollment, and SaaS access workflows. These workflows create a detection challenge because the relevant signals often appear as ordinary business telemetry: a login, a reset, a new device, an application consent, or a document export. Individually, these events may not be sufficient to justify a major response. Correlated in sequence, they may represent an account-abuse chain.

AI assistance may intensify this problem by compressing the time required to prepare social-engineering content, tailor lures, iterate messages, simulate personas, or move from access to collection. The defensive question is therefore not only whether identity-abuse telemetry can be detected, but whether defenders can detect it early enough to act before SaaS data is exported.

This paper introduces Identity Abuse Lab, a synthetic research environment designed to test that question in a controlled and reproducible way. The lab generates synthetic event sequences for baseline user behavior, manually simulated identity abuse, and AI-assisted identity abuse. It then applies transparent detector logic and cumulative timeline scoring to measure whether detection occurs before simulated export and how much intervention time remains.

The project is deliberately narrow. It does not simulate real phishing campaigns, collect credentials, target real users, exploit real systems, or publish offensive procedures. Instead, it focuses on defensive telemetry modeling: which synthetic signals appear, when they appear, how they can be scored, and how response windows differ between manual and AI-assisted scenarios.

The central research question is: which telemetry signals most reliably distinguish normal SaaS identity behavior from simulated AI-assisted identity-abuse chains in a controlled enterprise lab?

The initial contribution is threefold. First, the project provides a reproducible synthetic dataset design and normalized event schema. Second, it implements Python-based detectors for abnormal login context, help-desk reset risk, new-device risk, OAuth scope risk, and SaaS export anomalies. Third, it translates those detectors into Sigma-style rule artifacts and uses timeline scoring to quantify detection-before-export windows.
