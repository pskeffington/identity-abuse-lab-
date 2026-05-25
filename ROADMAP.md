# Project Roadmap

This roadmap turns the identity-abuse lab into a complete research-engineering and publication artifact.

## Current state

The repository currently includes:

- Synthetic baseline, manual-abuse, and AI-assisted abuse scenarios
- Normalized identity telemetry model
- Detector interface and event-level scoring
- OAuth scope risk detector
- SaaS export anomaly detector
- Abnormal-login detector
- New-device risk detector
- Timeline correlation scoring
- Scenario metrics reporting
- Test-backed result claims
- Sigma-style experimental detection rules
- Initial paper result tables

## Phase 1: Stabilize the research foundation

Goal: make the lab safe, reproducible, and clearly scoped.

Planned work:

- Add `docs/threat_model.md`
- Add `docs/ethics_and_safety.md`
- Add `docs/lab_design.md`
- Add `docs/data_dictionary.md`
- Add explicit synthetic-data disclaimer to README
- Add MITRE ATT&CK mapping table
- Add limitations section for synthetic inference boundaries

Expected result:

A reviewer can understand what the lab does, what it does not do, and why it is safe to publish.

## Phase 2: Expand telemetry realism

Goal: add more realistic identity and SaaS telemetry without introducing real targets or offensive instructions.

Planned work:

- Add help-desk reset events
- Add MFA challenge and MFA reset events
- Add session-token reuse simulation
- Add OAuth application metadata
- Add SaaS document-search events
- Add admin-role escalation simulation
- Add benign travel and false-positive scenarios
- Add multiple synthetic users and departments

Expected result:

The dataset becomes more useful for detection testing and false-positive analysis.

## Phase 3: Strengthen detection logic

Goal: move from isolated event detectors to richer chain-level detection.

Planned work:

- Add help-desk reset detector
- Add MFA fatigue/reset detector
- Add suspicious session reuse detector
- Add SaaS search-and-export sequence detector
- Add OAuth consent-after-abnormal-login correlation
- Add user baseline deviation scoring
- Add configurable detector thresholds
- Add detector metadata and explainability fields

Expected result:

The scoring system can explain why a chain was detected and which early signals mattered most.

## Phase 4: Produce reproducible datasets and outputs

Goal: generate artifacts that can be included in the paper and reviewed in GitHub.

Planned work:

- Add `data/synthetic/*.jsonl` generated examples
- Add `data/processed/*.csv` scored outputs
- Add script to regenerate all datasets
- Add script to regenerate all result tables
- Add summary CSV for scenario-level metrics
- Add timeline CSV for event-level cumulative risk
- Add Makefile targets for repeatability

Expected result:

A reviewer can clone the repo, run one command, and regenerate the lab outputs.

## Phase 5: Build figures and notebook analysis

Goal: create visual evidence for the paper.

Planned work:

- Add timeline-risk plot
- Add intervention-window comparison chart
- Add detector-contribution table
- Add false-positive comparison table
- Add notebook for scenario generation
- Add notebook for scoring and evaluation
- Add notebook for paper figures

Expected result:

The project has publication-ready figures and reproducible notebooks.

## Phase 6: Write the paper

Goal: convert the lab into a clear cyber threat analysis publication.

Planned sections:

- Abstract
- Introduction
- Background: identity-first intrusions and AI-assisted abuse
- Threat model
- Lab design
- Synthetic telemetry schema
- Detector design
- Timeline correlation method
- Results
- Detection rule mapping
- Limitations
- Ethics and safety
- Future work
- Conclusion

Expected result:

A complete manuscript suitable for SSRN, arXiv, a technical blog, or a professional cybersecurity venue.

## Phase 7: Portfolio and job-market packaging

Goal: make the project useful as evidence for AI abuse, trust and safety, cyber threat intelligence, and technical investigation roles.

Planned work:

- Add executive summary
- Add recruiter-facing project brief
- Add architecture diagram
- Add short results summary in README
- Add role-alignment note for abuse investigation and AI risk roles
- Add release tag `v0.1-lab-baseline`

Expected result:

The repository becomes a polished portfolio artifact demonstrating threat analysis, Python engineering, detection logic, documentation, and publication discipline.

## Near-term priority queue

1. `docs: add threat model`
2. `docs: add ethics and safety statement`
3. `docs: add data dictionary`
4. `feat: add helpdesk reset detector`
5. `feat: add scored event export pipeline`
6. `feat: add makefile for reproducible lab outputs`
7. `paper: initialize manuscript draft`
8. `docs: add executive summary`

## Working thesis

AI-assisted identity abuse may not require fundamentally different telemetry to detect, but it compresses the response window enough that slow manual review and late-stage exfiltration alerts become less reliable. Early identity signals such as abnormal login context, suspicious new-device enrollment, risky OAuth consent, and SaaS export behavior can be combined into a transparent detection chain that produces measurable intervention windows in a controlled synthetic lab.
