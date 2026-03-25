"""Minimal local runner for IAD detect (optional dev use)."""

from iad_detector.detector import detect
from iad_detector.models import Mode, Packet

if __name__ == "__main__":
    packet = Packet(
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

    result = detect(packet)
    print(result.model_dump_json(indent=2))
