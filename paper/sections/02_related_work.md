# 2. Related Work and Literature Review

## 2.1 Identity-first intrusion and valid-account abuse

Recent cybersecurity literature and incident reporting increasingly describe enterprise compromise as an identity-centered problem. Rather than beginning with malware or direct exploitation, many intrusions begin with valid credentials, session access, account recovery manipulation, or social-engineering workflows that convert ordinary identity operations into attacker-controlled access. This is especially important in SaaS environments, where an attacker may achieve meaningful collection or exfiltration through legitimate application interfaces once an account, token, or OAuth grant is obtained.

Research on single sign-on and stolen credentials reinforces this framing. Hays, Sandborn, and White argue that a substantial share of attacks involve adversaries in possession of valid credentials and that MFA can still be pressured through mechanisms such as repeated step-up requests. Their work is relevant to this lab because it shifts attention from perimeter compromise to the usefulness of stolen or socially acquired identity material inside modern SSO environments.

The identity-first framing motivates the lab's emphasis on login context, device state, help-desk reset events, OAuth consent, and SaaS export telemetry. These are not peripheral signals. In many modern environments they are the core observable evidence available before collection or extortion.

## 2.2 Help-desk social engineering and account recovery abuse

Public reporting on groups such as Scattered Spider emphasizes the operational importance of help-desk impersonation, MFA transfer, password reset manipulation, and employee impersonation. These campaigns demonstrate that account recovery workflows can become intrusion pathways when social engineering defeats procedural controls. In this context, the help desk is not merely a support function; it becomes part of the identity security boundary.

This literature supports the inclusion of a help-desk reset detector in the lab. The detector does not model a real attack workflow. Instead, it scores synthetic reset events based on defensive attributes such as verification failure, urgency pressure, geographic context, and executive-impersonation claims. This allows the lab to study whether recovery-related telemetry can contribute to earlier detection before later OAuth or SaaS export activity.

## 2.3 OAuth, consent abuse, and SaaS token risk

OAuth and SaaS integration abuse represent another major strand of relevant work. OAuth grants and refresh tokens can create durable access that does not resemble traditional credential theft. Public reporting has described phishing and consent-style attacks that abuse trusted authentication flows, including device-code workflows, consent prompts, redirect behavior, and application permissions.

Recent incidents involving Salesforce-connected applications and token exposure underscore the practical importance of SaaS and OAuth telemetry. These incidents show that attackers can abuse legitimate integrations, tokens, or user-approved applications to access cloud data at scale. This supports the lab's decision to model OAuth scope risk and SaaS export volume as distinct but related signals.

The lab's OAuth detector is intentionally simple: it scores consent events according to requested scope sensitivity, including mail access, file access, offline access, directory access, and broad user-read scopes. This aligns with emerging work on permission-risk scoring for Entra and Microsoft Graph environments, while remaining synthetic and platform-agnostic.

## 2.4 AI-assisted cyber operations and tempo compression

The strongest justification for this lab is not that AI creates entirely new identity telemetry, but that AI may compress the time available for defenders to interpret it. Current reporting and industry analysis describe AI as an accelerator for phishing content, credential theft workflows, triage overload, vulnerability discovery, and operational speed. CrowdStrike reporting summarized in public coverage argues that attackers are moving through environments faster and that defenders must operate at comparable speed.

This supports the lab's central measurement strategy: the intervention window. Rather than only asking whether a detector fires, the lab measures whether detection occurs before simulated export and how many minutes remain for response. In the current enriched scenarios, manual abuse is detected 28 minutes before export, while AI-assisted abuse is detected 11 minutes before export. The literature therefore supports treating time-to-detection and response-window compression as first-class variables.

## 2.5 Synthetic telemetry and reproducible CTI research

Synthetic data has a growing role in cyber threat intelligence research, especially where real incident data are sensitive, incomplete, legally restricted, or too dangerous to publish. Recent work on synthetic CTI generation, such as SynthCTI, argues that synthetic examples can help address data scarcity and class imbalance in MITRE technique mapping. Although this lab does not train a CTI classifier, it shares the same methodological logic: synthetic artifacts can support reproducible defensive research when real telemetry cannot be safely released.

The lab contributes to this area by generating synthetic identity events, scoring them with transparent detectors, mapping them to Sigma-style rules, and exporting reproducible result tables. This combination turns a qualitative threat claim into an inspectable research artifact.

## 2.6 Gap addressed by this project

The literature contains substantial discussion of identity attacks, OAuth abuse, social engineering, AI-enabled threat acceleration, and synthetic CTI generation. Less common is a compact, reproducible lab that links all of the following in one workflow:

- synthetic identity and SaaS telemetry;
- transparent event-level detectors;
- cumulative timeline scoring;
- detection-before-export measurement;
- intervention-window comparison between manual and AI-assisted scenarios;
- Sigma-style rule translation; and
- publication-ready documentation with explicit safety boundaries.

Identity Abuse Lab addresses that gap. Its contribution is not a production-grade detector or a real-world incident benchmark. Its contribution is a defensible, synthetic, reproducible framework for reasoning about whether AI-assisted identity abuse changes the type of telemetry defenders need, the speed at which defenders must act, or both.

## References to verify and format

- Hays, S., Sandborn, M., & White, J. (2024). Reducing usefulness of stolen credentials in SSO contexts.
- Ruiz-Rodenas, A., Pujante Saez, J., Garcia-Algora, D., Rodriguez Bejar, M., Blasco, J., & Hernandez-Ramos, J. L. (2025). SynthCTI: LLM-driven synthetic CTI generation to enhance MITRE technique mapping.
- Mahara, A. (2025). Detecting malicious Entra OAuth apps with LLM-based permission risk scoring.
- CISA, FBI, and international partners. Scattered Spider advisory materials on social engineering and identity-focused intrusion.
- Microsoft Security materials on OAuth consent abuse, device-code phishing, and Entra application governance.
- Google Threat Intelligence Group materials on Salesforce-focused social engineering and OAuth/token-related SaaS compromise.
- CrowdStrike Global Threat Report materials on identity abuse, cloud intrusions, adversary speed, and AI-enabled operations.
- Proofpoint and other threat-research materials on OAuth device-code phishing and Microsoft 365 account takeover.
