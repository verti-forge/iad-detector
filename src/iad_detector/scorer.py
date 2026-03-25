from __future__ import annotations

from iad_detector.models import DetectionTag, Packet, ScoreCard
from iad_detector.rules import COMPOUND_SEPARATORS, TOOL_HINTS


def score_mission_alignment(packet: Packet) -> float:
    mission = packet.mission.lower()
    task = packet.task.lower()
    action = packet.proposed_action.lower()

    shared_terms = sum(1 for word in task.split() if word in mission)
    if shared_terms >= 2:
        return 1.0

    drift_words = ["architecture", "cleanup", "refactor", "docs", "rename"]
    if any(word in task or word in action for word in drift_words):
        return 0.0

    return 0.5


def score_task_singularity(packet: Packet) -> float:
    task = packet.task.lower()
    if any(sep in task for sep in COMPOUND_SEPARATORS):
        return 0.0
    return 1.0


def score_constraint_freshness(packet: Packet) -> float:
    action = f"{packet.task} {packet.proposed_action}".lower()
    constraints = " ".join(packet.constraints).lower()

    if "do not rename" in constraints and "rename" in action:
        return 0.0
    if "minimize surface area" in constraints and "architecture" in action:
        return 0.0
    return 1.0 if packet.constraints else 0.5


def score_proof_sufficiency(packet: Packet) -> float:
    proof = packet.proof.strip().lower()
    if proof in {"none", "", "likely fixed", "should work now", "seems aligned"}:
        return 0.0
    return 1.0


def score_tool_fit(packet: Packet) -> float:
    task = f"{packet.task} {packet.proposed_action}".lower()
    tool = packet.tool.lower()

    for intent, valid_tools in TOOL_HINTS.items():
        if intent in task:
            return 1.0 if tool in valid_tools else 0.0

    return 0.5


def score_next_legitimacy(packet: Packet) -> float:
    nxt = packet.next.lower()
    proof = packet.proof.lower()

    if "deploy" in nxt and proof in {"none", "", "likely fixed", "should work now"}:
        return 0.0
    return 1.0


def score_packet(packet: Packet) -> tuple[ScoreCard, list[DetectionTag]]:
    scores = ScoreCard(
        mission_alignment=score_mission_alignment(packet),
        task_singularity=score_task_singularity(packet),
        constraint_freshness=score_constraint_freshness(packet),
        proof_sufficiency=score_proof_sufficiency(packet),
        tool_fit=score_tool_fit(packet),
        next_legitimacy=score_next_legitimacy(packet),
    )

    tags: list[DetectionTag] = []
    if scores.mission_alignment == 0.0:
        tags.append(DetectionTag.SCOPE_INFLATION)
    if scores.task_singularity == 0.0:
        tags.append(DetectionTag.COMPOUND_TASKING)
    if scores.constraint_freshness == 0.0:
        tags.append(DetectionTag.STALE_CONTEXT)
    if scores.proof_sufficiency == 0.0:
        tags.append(DetectionTag.PROOFLESS_CONTINUATION)
    if scores.tool_fit == 0.0:
        tags.append(DetectionTag.TOOL_MISMATCH)
    if scores.next_legitimacy == 0.0:
        tags.append(DetectionTag.PREMATURE_NEXT)

    return scores, tags
