# Data Dictionary

## Core event schema

All synthetic telemetry records are represented as normalized `IdentityEvent` objects.

| Field | Type | Required | Description |
|---|---|---:|---|
| `user_id` | string | Yes | Synthetic user identifier |
| `timestamp` | datetime | Yes | Event timestamp in ISO-compatible format |
| `source` | string | Yes | Synthetic telemetry source, such as `idp`, `saas`, or `email` |
| `event_type` | string | Yes | Normalized event category |
| `ip_address` | string or null | No | Synthetic IP address, generally from documentation-safe address ranges |
| `user_agent` | string or null | No | Synthetic browser or client identifier |
| `risk_score` | float | No | Optional event-level risk score, defaulting to `0.0` |
| `attributes` | object | No | Event-specific structured attributes |

## Event types

| Event type | Source | Description |
|---|---|---|
| `login` | `idp` | User login or authentication event |
| `logout` | `idp` | User logout event |
| `new_device` | `idp` | First-seen device or device enrollment event |
| `oauth_consent` | `idp` | OAuth application consent event |
| `saas_export` | `saas` | SaaS object export event |
| `document_read` | `saas` | Normal document access event |
| `lure_received` | `email` | Synthetic lure marker used to start an abuse timeline |
| `helpdesk_reset` | `idp` | Synthetic help-desk reset or account recovery event |

## Common attributes

| Attribute | Type | Event types | Description |
|---|---|---|---|
| `object_count` | integer | `document_read`, `saas_export` | Number of objects read or exported |
| `scopes` | list[string] | `oauth_consent` | OAuth scopes requested by a synthetic application |
| `geo_change` | boolean | `login`, `new_device`, `helpdesk_reset` | Indicates abnormal location context |
| `impossible_travel` | boolean | `login` | Indicates impossible-travel-style context in synthetic telemetry |
| `unfamiliar_user_agent` | boolean | `login` | Indicates unfamiliar browser/client context |
| `anonymous_network` | boolean | `login` | Indicates synthetic anonymous network context |
| `device_trust` | string | `new_device` | Device trust state, such as `known`, `unknown`, `blocked`, or `malicious` |
| `after_reset` | boolean | `new_device` | Indicates new-device activity after a reset event |
| `reset_channel` | string | `helpdesk_reset` | Reset channel, such as `helpdesk`, `self_service`, or `admin` |
| `identity_verified` | boolean | `helpdesk_reset` | Whether identity verification was completed in the synthetic event |
| `urgent_request` | boolean | `helpdesk_reset` | Indicates urgency pressure in the synthetic reset request |
| `variant` | string | `lure_received` | Scenario variant, such as `manual` or `ai_assisted` |

## Scenario-level metrics

| Metric | Description |
|---|---|
| `event_count` | Number of events in a scenario |
| `duration_minutes` | Minutes between first and last event |
| `max_detector_score` | Maximum event-level detector score in a scenario |
| `high_risk_event_count` | Count of events with detector score above configured threshold |
| `export_volume` | Sum of exported objects across `saas_export` events |
| `oauth_consent_count` | Count of OAuth consent events |

## Timeline metrics

| Metric | Description |
|---|---|
| `first_detection_time` | First timestamp when cumulative score crosses the detection threshold |
| `export_time` | Timestamp of first SaaS export event |
| `detected_before_export` | Whether detection occurred before export |
| `minutes_before_export` | Intervention window between detection and export |
| `final_cumulative_score` | Final cumulative timeline score |

## Data handling notes

The repository should only contain synthetic data. Documentation-safe IP ranges are preferred for examples. Do not commit production logs, real user identifiers, access tokens, credentials, or customer data.
