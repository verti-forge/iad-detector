from iad_detector.detector import detect

from tests.fixtures import GOOD_PACKET


def test_good_packet_passes():
    result = detect(GOOD_PACKET)
    assert result.gate.value == "PASS"
    assert result.coherence_score >= 0.85
