# Glossary

## AI-assisted abuse

A synthetic scenario variant in which the abuse chain is compressed to represent faster drafting, targeting, iteration, or operational movement. The lab does not implement real abuse automation.

## Baseline scenario

A synthetic normal-activity scenario used as a low-risk comparison case.

## Cumulative risk score

A timeline-level score produced by applying decay to prior event risk and adding the current event score.

## Detection before export

The primary defensive outcome measured by the lab. It indicates whether cumulative timeline risk crossed the detection threshold before the simulated SaaS export event.

## Detector

A small object-oriented scoring component that evaluates one `IdentityEvent` and returns a normalized risk score.

## Enriched scenario

A scenario variant with additional contextual fields such as unfamiliar user agent, anonymous network, reset-linked device enrollment, or geographic change.

## Help-desk reset risk

A synthetic account-recovery risk signal involving reset channel, verification status, urgency pressure, geographic context, or executive-impersonation claims.

## IdentityEvent

The normalized event model used across the project. It includes user ID, timestamp, source, event type, IP address, user agent, optional risk score, and event-specific attributes.

## Intervention window

The number of minutes between first detection and simulated SaaS export. A smaller window implies less time for triage and response.

## Manual abuse

A synthetic abuse scenario with a slower timeline than the AI-assisted variant.

## OAuth scope risk

A synthetic permission-risk signal based on requested OAuth scopes such as mail access, file access, offline access, directory access, or broad user-read scopes.

## SaaS export anomaly

A synthetic signal based on unusually high object-export volume from a SaaS system.

## Sigma-style rule

A portable detection-rule artifact written in a Sigma-like structure against the synthetic event schema. These rules are experimental and require adaptation before production use.

## Synthetic telemetry

Generated event data that does not represent real users, real credentials, real incidents, production logs, or customer data.

## Timeline correlation

The process of scoring events in chronological order to identify when cumulative risk crosses a detection threshold.
