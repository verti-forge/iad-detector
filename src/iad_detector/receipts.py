from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from iad_detector.models import DetectionResult, IADReceipt, Packet


def write_receipt(
    packet: Packet, result: DetectionResult, out_dir: str = "receipts"
) -> Path:
    Path(out_dir).mkdir(parents=True, exist_ok=True)

    ts = datetime.now(timezone.utc).isoformat()
    receipt = IADReceipt(
        timestamp=ts,
        mission=packet.mission,
        task=packet.task,
        proposed_action=packet.proposed_action,
        tool=packet.tool,
        scores=result.scores,
        coherence_score=result.coherence_score,
        hard_failures=result.hard_failures,
        gate=result.gate,
        tags=result.tags,
        reason=result.reason,
        suggested_reframe=result.suggested_reframe,
    )

    path = Path(out_dir) / "iad_check.json"
    path.write_text(receipt.model_dump_json(indent=2), encoding="utf-8")
    return path
