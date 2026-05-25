# Project Style Guide

## Voice

Use precise, bounded language. The project is a synthetic defensive lab, not a production benchmark or incident-response authority.

Prefer:

- "synthetic scenario"
- "controlled lab finding"
- "working finding"
- "bounded result"
- "intervention window"
- "defensive telemetry"
- "requires production validation"

Avoid:

- "proves"
- "guarantees detection"
- "stops attackers"
- "real-world rate"
- "production-ready detector"
- "attack playbook"

## Safety wording

Always make clear that the repository excludes:

- real phishing;
- credential collection;
- malware;
- exploit development;
- unauthorized access guidance;
- production logs;
- real user data; and
- real incident-sensitive information.

## Results wording

Results should be described as synthetic and scenario-bound.

Good:

> In the enriched synthetic scenario set, manual abuse is detected 28 minutes before export, while AI-assisted abuse is detected 11 minutes before export.

Avoid:

> This detects AI-assisted abuse 11 minutes before exfiltration in the real world.

## Citation wording

If a source has not been fully verified, mark it as working or pending verification. Do not present unverified vendor or government report details as final manuscript citations.

## Detector wording

Detector scores are heuristics, not probabilities. A score of 1.00 means maximum detector concern in the lab model, not a 100% probability of compromise.

## Release wording

Before v0.1, use "internal review" or "portfolio preview." After validation gates pass, use "baseline release."
