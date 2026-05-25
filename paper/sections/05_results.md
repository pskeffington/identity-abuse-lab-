# 4. Results

## 4.1 Scenario-level separation

The initial synthetic result set separates baseline behavior from abuse scenarios. Baseline activity contains five events over forty minutes, produces a maximum detector score of 0.20, and includes only a low-volume export of four objects. Manual abuse and AI-assisted abuse each contain five events and produce maximum detector scores of 1.00. Manual abuse includes a simulated export volume of 650 objects, while AI-assisted abuse includes a simulated export volume of 900 objects.

| Scenario | Events | Duration min | Max score | High-risk events | Export volume | OAuth consents |
|---|---:|---:|---:|---:|---:|---:|
| baseline | 5 | 40.0 | 0.20 | 0 | 4 | 0 |
| manual_abuse | 5 | 77.0 | 1.00 | 2 | 650 | 1 |
| ai_assisted_abuse | 5 | 24.0 | 1.00 | 2 | 900 | 1 |

The first result demonstrates that the detector set can distinguish low-risk baseline activity from synthetic abuse chains in the controlled scenario design.

## 4.2 Timeline detection before export

The first timeline correlation pass detects both abuse scenarios before the simulated SaaS export event. In the simple scenario set, manual abuse is detected 15 minutes before export, while AI-assisted abuse is detected 6 minutes before export.

| Scenario | Detected | Detected before export | Intervention window |
|---|---:|---:|---:|
| baseline | No | No | N/A |
| manual_abuse | Yes | Yes | 15.0 minutes |
| ai_assisted_abuse | Yes | Yes | 6.0 minutes |

This supports the preliminary interpretation that the AI-assisted scenario can reduce the available intervention window even when detection remains possible.

## 4.3 Enriched early-signal detection

The enriched detector set adds abnormal-login and new-device context to the original OAuth and SaaS export signals. With these additional early signals, detection moves earlier in both abuse scenarios.

| Scenario | Detected before export | Intervention window | Additional early signals |
|---|---:|---:|---|
| manual_abuse | Yes | 28.0 minutes | abnormal login, unknown new device |
| ai_assisted_abuse | Yes | 11.0 minutes | abnormal login, reset-linked new device |

The enriched result is operationally important. It shows that early identity telemetry can detect abuse before OAuth consent or export. At the same time, the AI-assisted chain still leaves a shorter response window than the manual chain.

## 4.4 Interpretation of response-window compression

Across the current synthetic scenarios, AI-assisted abuse does not eliminate detectable telemetry. The same broad categories remain useful: login context, device state, OAuth consent, and export volume. The major difference is temporal. The AI-assisted scenario compresses the chain from initial lure marker to export, reducing the time available for human review or manual escalation.

This result should be interpreted as a synthetic lab finding. It is not a production detection benchmark. It is, however, a useful research result because it converts a broad claim about AI-enabled acceleration into a measurable defensive variable: minutes of intervention time before export.
