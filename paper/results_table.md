# Initial Synthetic Results Table

This table is generated from the current controlled synthetic scenarios and should be treated as a first-pass lab output rather than a final empirical finding.

| Scenario | Events | Duration min | Max score | High-risk events | Export volume | OAuth consents |
|---|---:|---:|---:|---:|---:|---:|
| baseline | 5 | 40.0 | 0.20 | 0 | 4 | 0 |
| manual_abuse | 5 | 77.0 | 1.00 | 2 | 650 | 1 |
| ai_assisted_abuse | 5 | 24.0 | 1.00 | 2 | 900 | 1 |

## Initial interpretation

The first synthetic run demonstrates the intended scenario separation. Baseline activity produces low detector scores and low export volume. Both abuse scenarios produce high-risk detector scores, but the AI-assisted scenario compresses the lure-to-export timeline from 77 minutes to 24 minutes in the current design while increasing simulated export volume from 650 to 900 objects.

## Next analysis step

The next phase should add correlated timeline scoring so the lab can evaluate whether multi-signal detection identifies abuse before the simulated export event.
