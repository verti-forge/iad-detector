"""Intent–Action Decoupling detector v0 (Putline-adjacent)."""

from iad_detector.detector import detect
from iad_detector.models import (
    DetectionResult,
    DetectionTag,
    Gate,
    Mode,
    Packet,
)

__all__ = [
    "detect",
    "DetectionResult",
    "DetectionTag",
    "Gate",
    "Mode",
    "Packet",
]
