# Threat Model

## Purpose

This threat model defines the defensive research scope for the identity-abuse lab. The lab studies synthetic SaaS and identity-provider telemetry generated inside a controlled environment. It does not model or enable real unauthorized access, real credential capture, real phishing operations, or real victim targeting.

## Protected assets

The lab treats the following as protected assets:

- User identity accounts
- SaaS documents and exports
- OAuth grants and application permissions
- Device enrollment state
- Authentication sessions
- Help-desk reset workflows
- Identity-provider audit logs

## Adversary model

The simulated adversary is an identity-first abuse actor attempting to move from social-engineering contact to account access, persistence, collection, and SaaS export.

The adversary is modeled as capable of:

- Sending a synthetic lure event
- Triggering abnormal login context
- Registering or simulating a new-device event
- Requesting OAuth consent with risky scopes
- Initiating a high-volume SaaS export
- Compressing the timeline when AI assistance is simulated

The adversary is not modeled as capable of:

- Exploiting real software vulnerabilities
- Capturing real credentials
- Targeting real users
- Evading real production controls
- Running live phishing or vishing campaigns
- Bypassing MFA in real systems

## Defender model

The defender has access to normalized synthetic telemetry from identity and SaaS systems. The defender can run event-level detectors, correlated timeline scoring, and Sigma-style rules against the synthetic event stream.

The defender is modeled as capable of:

- Reading login telemetry
- Reading new-device telemetry
- Reading OAuth consent telemetry
- Reading SaaS export telemetry
- Applying detector-level risk scores
- Correlating risk across a scenario timeline
- Measuring whether detection occurs before export

## In-scope scenarios

The current lab includes three primary scenario families:

| Scenario | Description |
|---|---|
| Baseline | Normal synthetic SaaS user behavior |
| Manual abuse | Slower identity-abuse chain with abnormal access, OAuth consent, and export |
| AI-assisted abuse | Faster identity-abuse chain that compresses time from lure to export |

## Out-of-scope activity

The following are explicitly out of scope:

- Real phishing, vishing, smishing, or social-engineering attempts
- Real credential collection
- Production tenant attacks
- Malware development
- Exploit development
- Evasion guidance
- Persistence on real systems
- Instructions for unauthorized access

## Security hypothesis

The lab evaluates whether early identity signals can detect synthetic abuse chains before simulated SaaS export. The central hypothesis is that AI assistance compresses the response window even when the detectable telemetry categories remain similar.

## Assumptions

- Synthetic events approximate selected properties of identity-abuse telemetry but do not claim full production realism.
- Detector scores are transparent research heuristics, not calibrated production probabilities.
- Timeline compression is a scenario-design variable and should be tested across additional generated samples in future work.
- Detection-before-export is used as a defensive metric, not as a claim about real-world attacker success rates.

## Limitations

The threat model is intentionally narrow. It is designed for reproducible defensive research and portfolio demonstration, not for operational deployment without additional validation against real enterprise telemetry and approved security controls.
