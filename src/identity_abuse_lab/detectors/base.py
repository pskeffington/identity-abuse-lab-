from __future__ import annotations

from abc import ABC, abstractmethod

from identity_abuse_lab.telemetry.event import IdentityEvent


class Detector(ABC):
    """Abstract detector interface."""

    name: str

    @abstractmethod
    def score(self, event: IdentityEvent) -> float:
        """Return normalized risk score between 0 and 1."""
        raise NotImplementedError
