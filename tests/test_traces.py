import pytest

from iad_detector.detector import detect
from iad_detector.models import Gate

from tests.fixtures import BAD_PACKET, GOOD_PACKET, TRACE_CASES


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


@pytest.mark.parametrize(
    "trace_id,packet,expected_gate",
    TRACE_CASES,
    ids=[c[0] for c in TRACE_CASES],
)
def test_t003_trace_matrix(trace_id, packet, expected_gate):
    result = detect(packet)
    assert result.gate == expected_gate, (
        f"{trace_id}: expected {expected_gate}, got {result.gate} "
        f"(coherence={result.coherence_score}, hard_failures={result.hard_failures})"
    )


def test_t003_covers_all_gates():
    """Regression: at least one trace per gate the detector emits (v0 has no ESCALATE path)."""
    gates = {expected for _, _, expected in TRACE_CASES}
    assert gates == {Gate.PASS, Gate.REVIEW, Gate.WAIT, Gate.BLOCK}
