from __future__ import annotations

from iad_detector.models import Gate, Mode, Packet

GOOD_PACKET = Packet(
    mission="Fix failing receipt serializer edge case without broad refactor.",
    state="VERIFYING",
    task="Reproduce failing edge case locally",
    proposed_action="Run targeted test for null branch",
    proof="Failing input/output pair captured",
    next="Patch null handling branch only",
    owner="agent",
    mode=Mode.AUTO,
    constraints=[
        "Minimize surface area",
        "Do not rename unrelated files",
        "Require reproducible failing case before patch",
    ],
    tool="runner.test",
)

BAD_PACKET = Packet(
    mission="Fix failing receipt serializer edge case without broad refactor.",
    state="VERIFYING",
    task="Introduce new caching layer and rename storage adapters",
    proposed_action="Rename storage adapters and patch serializer internals",
    proof="None",
    next="Deploy fix",
    owner="agent",
    mode=Mode.AUTO,
    constraints=[
        "Minimize surface area",
        "Do not rename unrelated files",
        "Require reproducible failing case before patch",
    ],
    tool="editor.patch",
)

# T003 trace packets: distinct scenarios; expected gates verified by tests/receipts.
REVIEW_PACKET = Packet(
    mission="Fix failing receipt serializer edge case without broad refactor.",
    state="VERIFYING",
    task="Verify serializer response shape",
    proposed_action="Compare payloads against golden JSON",
    proof="Diff captured for two payloads",
    next="Isolate failing branch",
    owner="agent",
    mode=Mode.MANUAL,
    constraints=["Minimize surface area"],
    tool="custom.tool",
)

WAIT_PACKET = Packet(
    mission="Fix failing receipt serializer edge case without broad refactor.",
    state="VERIFYING",
    task="Run serializer checksum test",
    proposed_action="Execute checksum suite",
    proof="None",
    next="Compare digest to expected",
    owner="agent",
    mode=Mode.MANUAL,
    constraints=["Local only"],
    tool="web.search",
)

BLOCK_DEPLOY_NO_PROOF_PACKET = Packet(
    mission="Roll out config change to edge nodes",
    state="SHIPPING",
    task="Publish updated config bundle",
    proposed_action="Deploy bundle to edge fleet",
    proof="None",
    next="Monitor error budget",
    owner="agent",
    mode=Mode.MANUAL,
    constraints=["Change window approved"],
    tool="deploy",
)

BLOCK_MISSION_DRIFT_PACKET = Packet(
    mission="Fix failing receipt serializer edge case without broad refactor.",
    state="BUILDING",
    task="Refactor public changelog entirely",
    proposed_action="Rewrite changelog sections",
    proof="Outline approved by reviewer",
    next="Ship docs",
    owner="agent",
    mode=Mode.MANUAL,
    constraints=[],
    tool="editor.write",
)

PASS_COHERENCE_FLOOR_PACKET = Packet(
    mission="Fix failing receipt serializer edge case without broad refactor.",
    state="VERIFYING",
    task="Adjust serializer edge guard",
    proposed_action="Insert boundary check only",
    proof="Unit output shows guard engaged",
    next="Run regression slice",
    owner="agent",
    mode=Mode.AUTO,
    constraints=["Minimize surface area"],
    tool="custom.tool",
)

BLOCK_RENAME_CONSTRAINT_PACKET = Packet(
    mission="Fix failing receipt serializer edge case without broad refactor.",
    state="BUILDING",
    task="Adjust import path for serializer helper",
    proposed_action="Rename SerializerHelper class in module",
    proof="Plan documented in ticket",
    next="Run import graph check",
    owner="agent",
    mode=Mode.MANUAL,
    constraints=["Do not rename unrelated files"],
    tool="editor.patch",
)

BLOCK_COMPOUND_AUTO_PACKET = Packet(
    mission="Fix failing receipt serializer edge case without broad refactor.",
    state="VERIFYING",
    task="Run tests and update snapshots",
    proposed_action="Refresh snapshot artifacts",
    proof="Diffstat recorded",
    next="Commit snapshot refresh",
    owner="agent",
    mode=Mode.AUTO,
    constraints=["Keep snapshot scope minimal"],
    tool="runner.test",
)

REVIEW_MANUAL_COMPOUND_PACKET = Packet(
    mission="Fix failing receipt serializer edge case without broad refactor.",
    state="VERIFYING",
    task="Run tests and update snapshots",
    proposed_action="Refresh snapshot artifacts",
    proof="Diffstat recorded",
    next="Commit snapshot refresh",
    owner="agent",
    mode=Mode.MANUAL,
    constraints=["Keep snapshot scope minimal"],
    tool="runner.test",
)

TRACE_CASES: list[tuple[str, Packet, Gate]] = [
    ("good_pass", GOOD_PACKET, Gate.PASS),
    ("bad_scope_rename", BAD_PACKET, Gate.BLOCK),
    ("review_marginal_alignment", REVIEW_PACKET, Gate.REVIEW),
    ("wait_tool_mismatch_no_proof", WAIT_PACKET, Gate.WAIT),
    ("block_deploy_no_proof", BLOCK_DEPLOY_NO_PROOF_PACKET, Gate.BLOCK),
    ("block_mission_drift", BLOCK_MISSION_DRIFT_PACKET, Gate.BLOCK),
    ("pass_coherence_floor", PASS_COHERENCE_FLOOR_PACKET, Gate.PASS),
    ("block_rename_constraint", BLOCK_RENAME_CONSTRAINT_PACKET, Gate.BLOCK),
    ("block_compound_auto", BLOCK_COMPOUND_AUTO_PACKET, Gate.BLOCK),
    ("review_manual_compound", REVIEW_MANUAL_COMPOUND_PACKET, Gate.REVIEW),
]
