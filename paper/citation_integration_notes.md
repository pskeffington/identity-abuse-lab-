# Citation Integration Notes

These notes map the working bibliography to manuscript claims. They are intended to guide the next citation pass and should be converted into formal inline citations before submission.

## Identity-first intrusion and SSO credential abuse

Use Hays, Sandborn, and White (2024) to support discussion of stolen credentials, SSO contexts, and MFA pressure. This source fits the related-work subsection on valid-account abuse and the introduction's framing that identity systems are core enterprise security boundaries.

Relevant manuscript locations:

- `sections/02_introduction.md`
- `sections/02_related_work.md`
- `sections/06_discussion.md`

## Synthetic CTI generation

Use Ruiz-Ródenas et al. (2025) to support synthetic CTI as a method for addressing data scarcity and safe reproducibility. Use Nguyen et al. (2025) as a broader CTI/LLM mapping reference.

Relevant manuscript locations:

- `sections/02_related_work.md`
- `sections/03_methods.md`
- `sections/09_reproducibility_appendix.md`

## OAuth and Entra permission-risk scoring

Use Mahara (2025) to support OAuth and Entra application permission risk scoring. This source maps directly to the OAuth scope-risk detector and the related-work discussion of consent abuse.

Relevant manuscript locations:

- `sections/02_related_work.md`
- `sections/04_detection_model.md`
- `paper/detection_rule_mapping.md`

## Social engineering and help-desk abuse

Use government and vendor reporting on Scattered Spider, help-desk impersonation, and Salesforce-focused vishing campaigns after final URL verification. These sources should support the help-desk reset detector and the related-work account-recovery abuse section.

Relevant manuscript locations:

- `sections/02_related_work.md`
- `sections/04_detection_model.md`
- `docs/threat_model.md`

## AI-assisted tempo compression

Use CrowdStrike reporting and public coverage on adversary speed and AI-enabled operations to support response-window compression as a research variable. Keep claims bounded: the lab demonstrates synthetic intervention-window compression, not real-world rates.

Relevant manuscript locations:

- `sections/01_abstract.md`
- `sections/02_introduction.md`
- `sections/05_results.md`
- `sections/06_discussion.md`

## Phishing detection and triage automation

Use Bono (2025) and Shang et al. (2026) as supporting literature for phishing triage and machine-learning-assisted malicious email detection. These are secondary to the current lab but useful for future expansion.

Relevant manuscript locations:

- `sections/02_related_work.md`
- future phishing-specific appendix or extension paper
