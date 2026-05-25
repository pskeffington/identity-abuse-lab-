"""Detector implementations for Identity Abuse Lab."""

from identity_abuse_lab.detectors.abnormal_login import AbnormalLoginDetector
from identity_abuse_lab.detectors.base import Detector
from identity_abuse_lab.detectors.export_anomaly import SaaSExportAnomalyDetector
from identity_abuse_lab.detectors.helpdesk_reset import HelpdeskResetDetector
from identity_abuse_lab.detectors.new_device import NewDeviceRiskDetector
from identity_abuse_lab.detectors.oauth_scope_risk import OAuthScopeRiskDetector

__all__ = [
    "AbnormalLoginDetector",
    "Detector",
    "HelpdeskResetDetector",
    "NewDeviceRiskDetector",
    "OAuthScopeRiskDetector",
    "SaaSExportAnomalyDetector",
]
