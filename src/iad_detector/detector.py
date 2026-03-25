from __future__ import annotations

from iad_detector.constants import WEIGHTS
from iad_detector.models import DetectionResult, Gate, Mode, Packet
from iad_detector.reframe import suggest_reframe
from iad_detector.rules import IRREVERSIBLE_HINTS
from iad_detector.scorer import score_packet


def is_irreversible(action: str) -> bool:
    lower = action.lower()
    return any(word in lower for word in IRREVERSIBLE_HINTS)


def violates_constraints(packet: Packet) -> bool:
    action = f"{packet.task} {packet.proposed_action}".lower()
    constraints = " ".join(packet.constraints).lower()

    if "do not rename" in constraints and "rename" in action:
        return True
    if "do not modify source files" in constraints and (
        "modify" in action or "patch" in action
    ):
        return True
    if "minimize surface area" in constraints and "architecture" in action:
        return True

    return False


def detect(packet: Packet) -> DetectionResult:
    scores, tags = score_packet(packet)
    hard_failures: list[str] = []

    if scores.mission_alignment == 0.0:
        hard_failures.append("HF-1 mission mismatch")

    if is_irreversible(packet.proposed_action) and scores.proof_sufficiency < 1.0:
        hard_failures.append("HF-2 irreversible action without proof")

    if violates_constraints(packet):
        hard_failures.append("HF-3 explicit constraint violation")

    if packet.mode == Mode.AUTO and scores.task_singularity == 0.0:
        hard_failures.append("HF-4 compound tasking under AUTO")

    coherence = round(
        WEIGHTS["mission_alignment"] * scores.mission_alignment
        + WEIGHTS["task_singularity"] * scores.task_singularity
        + WEIGHTS["constraint_freshness"] * scores.constraint_freshness
        + WEIGHTS["proof_sufficiency"] * scores.proof_sufficiency
        + WEIGHTS["tool_fit"] * scores.tool_fit
        + WEIGHTS["next_legitimacy"] * scores.next_legitimacy,
        3,
    )

    if hard_failures:
        gate = Gate.BLOCK
        reason = "; ".join(hard_failures)
    elif coherence >= 0.85:
        gate = Gate.PASS
        reason = "Packet is coherent enough to proceed."
    elif coherence >= 0.60:
        gate = Gate.REVIEW
        reason = "Packet is partially aligned but needs review."
    else:
        gate = Gate.WAIT
        reason = "Packet lacks sufficient alignment or proof to continue."

    return DetectionResult(
        scores=scores,
        coherence_score=coherence,
        hard_failures=hard_failures,
        gate=gate,
        tags=tags,
        reason=reason,
        suggested_reframe=suggest_reframe(packet, reason),
    )
