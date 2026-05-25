# 2. Related Work and Literature Review

## 2.1 Identity-first intrusion and valid-account abuse

Enterprise compromise increasingly reflects an identity-centered operating environment. In many modern incidents, the decisive security boundary is not a vulnerable endpoint or an exposed network service, but the integrity of authentication, account recovery, OAuth consent, device enrollment, and SaaS access workflows. Hays, Sandborn, and White (2024) frame this problem in the context of stolen credentials and SSO, emphasizing that adversaries who possess valid credentials can operate inside trusted authentication systems unless defenders reduce credential usefulness and strengthen identity-side controls.

This identity-first framing motivates the lab's emphasis on login context, device state, help-desk reset events, OAuth consent, and SaaS export telemetry. These events are not peripheral signals. In SaaS-first environments, they may be the primary observable evidence before collection, extortion, or external disclosure.

## 2.2 Help-desk social engineering and account recovery abuse

Public reporting on Scattered Spider and related social-engineering activity emphasizes the operational importance of help-desk impersonation, MFA transfer, password-reset manipulation, and employee impersonation. These campaigns show that account recovery workflows can become intrusion pathways when adversaries defeat procedural controls through urgency pressure, identity claims, or targeted impersonation (Cybersecurity and Infrastructure Security Agency et al., 2025; Google Threat Intelligence Group, 2025).

This literature supports the inclusion of a help-desk reset detector in the lab. The detector does not model a real attack workflow. Instead, it scores synthetic reset events based on defensive attributes such as verification failure, urgency pressure, geographic context, and executive-impersonation claims. This allows the lab to study whether recovery-related telemetry can contribute to earlier detection before later OAuth or SaaS export activity.

## 2.3 OAuth, consent abuse, and SaaS token risk

OAuth and SaaS integration abuse represent another major strand of relevant work. OAuth grants and refresh tokens can create durable access that may not resemble traditional credential theft. Vendor guidance and threat reporting describe abuse patterns involving consent prompts, device-code workflows, application permissions, and token or integration misuse in Microsoft 365, Entra, Salesforce, and other SaaS environments (Microsoft Security, n.d.; Proofpoint, 2026; Google Threat Intelligence Group, 2025).

Mahara (2025) is especially relevant because it applies LLM-based permission-risk scoring to malicious Entra OAuth applications. This aligns closely with the lab's OAuth scope-risk detector, which scores consent events according to requested scope sensitivity, including mail access, file access, offline access, directory access, and broad user-read scopes.

## 2.4 AI-assisted cyber operations and tempo compression

The strongest justification for this lab is not that AI creates entirely new identity telemetry, but that AI may compress the time available for defenders to interpret it. Current threat reporting and industry analysis describe AI as an accelerator for phishing content, credential workflows, triage overload, vulnerability analysis, and operational speed (CrowdStrike, 2026). The lab converts this broad concern into a measurable defensive variable: the intervention window between first detection and simulated SaaS export.

In the current enriched scenarios, manual abuse is detected 28 minutes before export, while AI-assisted abuse is detected 11 minutes before export. These are synthetic results, not production rates. Their value is methodological: they show how response-window compression can be measured and compared inside a controlled lab.

## 2.5 Synthetic telemetry and reproducible CTI research

Synthetic data has an important role in cyber threat intelligence research, especially where real incident data are sensitive, incomplete, legally restricted, or unsafe to publish. Ruiz-Ródenas et al. (2025) propose SynthCTI as an LLM-driven synthetic CTI generation method to improve MITRE technique mapping. Nguyen et al. (2025) similarly examine LLM-supported identification of attack techniques in CTI reports. These works support the broader methodological premise that synthetic artifacts can help researchers study defensive classification, mapping, and detection problems when real-world telemetry is unavailable.

This lab does not train a CTI classifier, but it uses a similar synthetic-research logic. It generates synthetic identity events, scores them with transparent detectors, maps them to Sigma-style rules, and exports reproducible result tables. This combination turns a qualitative threat claim into an inspectable research artifact.

## 2.6 Phishing detection and triage automation

Prior work on phishing detection and triage automation is relevant to future extensions of the lab. Bono (2025) evaluates randomized controlled trials for phishing triage agents, while Shang et al. (2026) develop typed entity-relation methods for malicious email detection. These works are adjacent rather than central to the current lab because Identity Abuse Lab does not yet model email-content classification. They are useful, however, for future expansion into lure-generation artifacts, triage queues, and analyst-assistance workflows.

## 2.7 Gap addressed by this project

The literature contains substantial discussion of identity attacks, OAuth abuse, social engineering, AI-enabled threat acceleration, phishing triage, and synthetic CTI generation. Less common is a compact, reproducible lab that links all of the following in one workflow:

- synthetic identity and SaaS telemetry;
- transparent event-level detectors;
- cumulative timeline scoring;
- detection-before-export measurement;
- intervention-window comparison between manual and AI-assisted scenarios;
- Sigma-style rule translation; and
- publication-ready documentation with explicit safety boundaries.

Identity Abuse Lab addresses that gap. Its contribution is not a production-grade detector or a real-world incident benchmark. Its contribution is a defensible, synthetic, reproducible framework for reasoning about whether AI-assisted identity abuse changes the type of telemetry defenders need, the speed at which defenders must act, or both.
