from iad_detector.models import Mode, Packet

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
