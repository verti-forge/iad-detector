from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class Mode(str, Enum):
    AUTO = "AUTO"
    MANUAL = "MANUAL"
    CHECK = "CHECK"
    SAFE = "SAFE"
    DRYRUN = "DRYRUN"


class Gate(str, Enum):
    PASS = "PASS"
    REVIEW = "REVIEW"
    WAIT = "WAIT"
    BLOCK = "BLOCK"
    ESCALATE = "ESCALATE"


class ScoreName(str, Enum):
    MISSION_ALIGNMENT = "mission_alignment"
    TASK_SINGULARITY = "task_singularity"
    CONSTRAINT_FRESHNESS = "constraint_freshness"
    PROOF_SUFFICIENCY = "proof_sufficiency"
    TOOL_FIT = "tool_fit"
    NEXT_LEGITIMACY = "next_legitimacy"


class DetectionTag(str, Enum):
    SCOPE_INFLATION = "scope_inflation"
    PROXY_SUBSTITUTION = "proxy_substitution"
    STALE_CONTEXT = "stale_context"
    PROOFLESS_CONTINUATION = "proofless_continuation"
    TOOL_MISMATCH = "tool_mismatch"
    PREMATURE_NEXT = "premature_next"
    COMPOUND_TASKING = "compound_tasking"
    POSTHOC_JUSTIFICATION = "posthoc_justification"


class Packet(BaseModel):
    mission: str
    state: str
    task: str
    proposed_action: str
    proof: str = "None"
    next: str
    owner: str
    mode: Mode
    constraints: List[str] = Field(default_factory=list)
    tool: str


class ScoreCard(BaseModel):
    mission_alignment: float
    task_singularity: float
    constraint_freshness: float
    proof_sufficiency: float
    tool_fit: float
    next_legitimacy: float


class DetectionResult(BaseModel):
    scores: ScoreCard
    coherence_score: float
    hard_failures: List[str]
    gate: Gate
    tags: List[DetectionTag]
    reason: str
    suggested_reframe: str


class IADReceipt(BaseModel):
    receipt_type: str = "iad_check"
    timestamp: Optional[str] = None
    mission: str
    task: str
    proposed_action: str
    tool: str
    scores: ScoreCard
    coherence_score: float
    hard_failures: List[str]
    gate: Gate
    tags: List[DetectionTag]
    reason: str
    suggested_reframe: str
