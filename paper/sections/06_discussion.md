# 5. Discussion

The current lab results suggest that AI-assisted identity abuse should be analyzed not only as a problem of new indicators, but as a problem of compressed operational tempo. In the synthetic scenarios, the same broad telemetry families remain informative: abnormal login context, device enrollment, OAuth consent, and SaaS export behavior. The differentiating factor is the reduced time between the initial lure marker and the simulated export event.

This distinction matters for defensive operations. Many organizations rely on alert triage, manual review, ticket routing, escalation queues, and human approval processes. If AI assistance compresses an abuse chain from more than an hour to less than half an hour, a detector may technically fire before exfiltration while still failing operationally because the response process is too slow.

The enriched results also show the value of early identity signals. Export-only detection is inherently late. OAuth consent detection is earlier, but still occurs after account access has already moved into an application-permission stage. Abnormal login and new-device signals can move detection closer to initial access and persistence, creating more time for containment.

The lab therefore supports a practical defensive priority: identity-abuse detection should correlate low-friction early signals before waiting for high-volume export or other late-stage evidence. In operational terms, this favors risk aggregation, rapid identity containment, conditional access review, token revocation, and device/session invalidation workflows.

The current model is intentionally transparent rather than complex. That is a strength for early publication and review because the detector logic can be inspected directly. It is also a limitation because the scores are not calibrated against production telemetry. Future work should evaluate false-positive scenarios, benign travel, approved help-desk resets, normal application onboarding, administrative exports, and multi-user baselines.
