from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class IdentityEvent(BaseModel):
    """Normalized identity telemetry event."""

    user_id: str
    timestamp: datetime
    source: str
    event_type: str
    ip_address: str | None = None
    user_agent: str | None = None
    risk_score: float = Field(default=0.0, ge=0.0)
    attributes: dict[str, Any] = Field(default_factory=dict)

    def is_high_risk(self, threshold: float = 0.7) -> bool:
        return self.risk_score >= threshold
