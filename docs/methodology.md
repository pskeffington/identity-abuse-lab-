# Methodology

## Study design

This project uses a controlled synthetic lab design to compare three identity telemetry scenarios:

1. Baseline SaaS activity
2. Manual identity-abuse simulation
3. AI-assisted identity-abuse simulation

All events are synthetic. No real users, credentials, targets, tenants, or phishing campaigns are used.

## Scenario construction

Each scenario is represented as a chronological sequence of normalized `IdentityEvent` records. Events include user identity, timestamp, source system, event type, IP address, user agent, and scenario-specific attributes.

## Initial scenarios

### Baseline

The baseline scenario represents normal user behavior: login, document reads, low-volume export, and logout.

### Manual abuse

The manual abuse scenario represents a slower identity-abuse chain involving a lure, abnormal login, new-device event, OAuth consent, and high-volume SaaS export.

### AI-assisted abuse

The AI-assisted abuse scenario represents the same general abuse chain occurring over a compressed timeline with higher-risk OAuth scope requests and larger export volume.

## Detection approach

Initial detectors score individual event types:

- OAuth scope risk
- SaaS export anomaly

The scoring engine runs detectors across events and retains detector-level scores for reproducible analysis.

## Planned evaluation

The first evaluation will compare:

- Time from lure to export
- Highest detector score per scenario
- Number of high-risk events per scenario
- Detection before exfiltration simulation
- Single-detector versus correlated-risk performance
