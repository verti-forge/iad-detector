from iad_detector.detector import detect
from iad_detector.models import Mode, Packet


def main() -> None:
    packet = Packet(
        mission="example mission",
        state="VERIFYING",
        task="example task",
        proposed_action="example action",
        proof="None",
        next="example next",
        owner="agent",
        mode=Mode.AUTO,
        constraints=[],
        tool="runner.test",
    )

    result = detect(packet)
    print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
