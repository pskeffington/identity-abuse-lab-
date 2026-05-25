from __future__ import annotations

from identity_abuse_lab.detectors.base import Detector
from identity_abuse_lab.telemetry.event import IdentityEvent


class OAuthScopeRiskDetector(Detector):
    """Scores OAuth consent events based on requested scope sensitivity."""

    name = "oauth_scope_risk"

    high_risk_scopes = {
        "mail.read",
        "mail.readwrite",
        "files.read.all",
        "files.readwrite.all",
        "offline_access",
        "directory.read.all",
        "user.read.all",
    }

    def score(self, event: IdentityEvent) -> float:
        if event.event_type != "oauth_consent":
            return 0.0

        scopes = {str(scope).lower() for scope in event.attributes.get("scopes", [])}
        if not scopes:
            return 0.2

        overlap = scopes.intersection(self.high_risk_scopes)
        if len(overlap) >= 3:
            return 1.0
        if len(overlap) == 2:
            return 0.8
        if len(overlap) == 1:
            return 0.6
        return 0.3
