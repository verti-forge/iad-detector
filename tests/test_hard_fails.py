from iad_detector.detector import detect

from tests.fixtures import BAD_PACKET


def test_bad_packet_blocks():
    result = detect(BAD_PACKET)
    assert result.gate.value == "BLOCK"
    assert "HF-1 mission mismatch" in result.hard_failures
    assert "HF-3 explicit constraint violation" in result.hard_failures
