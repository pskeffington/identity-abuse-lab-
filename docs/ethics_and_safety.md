# Ethics and Safety Statement

## Defensive intent

This repository is a defensive research and education project. It is intended to study how synthetic identity and SaaS telemetry can be used to detect simulated account-abuse chains before data export.

The project does not provide instructions for attacking real systems. It does not include live phishing workflows, credential collection, exploit code, malware, or operational guidance for unauthorized access.

## Synthetic-only data policy

All data used in this repository must be synthetic, generated, sanitized, or otherwise non-sensitive. The repository should not contain:

- Real credentials
- Real access tokens
- Real user audit logs
- Real customer data
- Real employee records
- Real victim information
- Real phishing targets
- Production tenant identifiers

## Lab boundaries

Permitted activity:

- Generating synthetic telemetry
- Writing defensive detectors
- Testing scoring logic
- Producing aggregate metrics
- Writing detection rules against the synthetic schema
- Documenting limitations and defensive findings

Prohibited activity:

- Running real phishing or vishing campaigns
- Collecting credentials or session tokens
- Targeting real users or organizations
- Testing against systems without authorization
- Publishing evasion instructions
- Publishing operational abuse playbooks

## Dual-use risk handling

Identity-abuse research can be dual-use. This project reduces risk by keeping scenarios abstract, synthetic, and detector-focused. The repository emphasizes defensive signals, transparent scoring, and response-window measurement rather than operational attacker procedure.

## Publication safety

Before publication, review the repository for:

- Secrets or tokens accidentally committed
- Real organization names not used as public examples
- Attack instructions that are more actionable than necessary
- Sensitive operational details
- Ambiguous wording that could imply real-world targeting

## Human-subjects considerations

The current project does not involve human subjects. It uses generated telemetry and synthetic personas only. If future work includes surveys, interviews, real incident data, or user studies, additional ethics review and consent procedures may be required.

## Responsible framing

Claims should remain bounded. Results from this lab should be described as findings from controlled synthetic scenarios, not as proof of real-world detection rates. Any production use would require validation with authorized telemetry, legal review, security review, and organization-specific tuning.
