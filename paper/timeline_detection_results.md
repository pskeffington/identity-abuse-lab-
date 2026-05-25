# Timeline Detection Results

This table summarizes the first chain-level scoring pass for the synthetic identity-abuse scenarios.

| Scenario | Detected | Detected before export | Intervention window |
|---|---:|---:|---:|
| baseline | No | No | N/A |
| manual_abuse | Yes | Yes | 15.0 minutes |
| ai_assisted_abuse | Yes | Yes | 6.0 minutes |

## Initial interpretation

The timeline correlation model detects both simulated abuse chains before the SaaS export event. In the current synthetic design, the manual abuse scenario leaves a 15-minute intervention window, while the AI-assisted scenario leaves only a 6-minute intervention window.

The operational implication is that AI-assisted identity abuse may not require fundamentally different telemetry to detect, but it can compress the response window enough that manual review and slow escalation processes become less reliable.

## Publication claim to test further

Correlated identity telemetry can detect synthetic identity-abuse chains before exfiltration, but AI-assisted scenario compression materially reduces the time available for human intervention.
