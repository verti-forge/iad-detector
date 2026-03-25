import pytest

from iad_detector.detector import detect

from tests.fixtures import BAD_PACKET, GOOD_PACKET


@pytest.mark.parametrize(
    "packet,expected",
    [
        (GOOD_PACKET, "PASS"),
        (BAD_PACKET, "BLOCK"),
    ],
)
def test_trace_packets(packet, expected):
    result = detect(packet)
    assert result.gate.value == expected
