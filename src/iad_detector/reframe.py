from __future__ import annotations

from iad_detector.models import Packet


def suggest_reframe(packet: Packet, reason: str) -> str:
    return (
        f"Mission remains: {packet.mission}\n"
        f"Current action drifts because: {reason}\n"
        f"Safer next move: reduce to one local action that directly serves the mission.\n"
        f"Required proof: observable evidence tied to that action."
    )
