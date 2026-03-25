# Architecture

## Components

- **Putline (conceptual):** v1 `[STATE] · TASK · PROOF · NEXT`; v2 adds `→ PROOF ▸ NEXT ⟂ RECEIPT`; v3 adds `<SCOPE> ::`, `#MODE`, `!GATE`, `@OWNER`. This repo documents and may later parse/format these lines; v0 focuses on IAD.
- **`iad_detector` package (`src/iad_detector/`):** Pydantic models (`models`), heuristic rules and hints (`rules`), coherence **weights** (`constants`), per-dimension scorers (`scorer`), hard-fail and gate orchestration (`detector`), reframe text (`reframe`), optional receipt writer (`receipts`), **CLI entry** via `python -m iad_detector` (`__main__.py`).
- **Tests (`tests/`):** Fixtures for a coherent packet and a drifted packet; tests for scoring/gates and hard-fails.
- **Scripts (`scripts/`):** Optional local runner examples.
- **Docs spine (`docs/`):** Mission, architecture, tasks, risks, append-only session/receipt/progress/decision logs.

## Data flow

1. Caller builds an **execution packet** (mission, state, task, proposed_action, proof, next, owner, mode, constraints, tool).
2. **`detect(packet)`** scores six dimensions, collects tags, applies hard-fail overrides, computes weighted coherence, assigns **gate** (PASS / REVIEW / WAIT / BLOCK).
3. Optionally **`write_receipt`** serializes an **IAD receipt** to disk under `receipts/`.

## Interfaces / contracts

- **Input:** `Packet` (Pydantic model)—stable field names for orchestrators and agents.
- **Output:** `DetectionResult`—scores, coherence_score, hard_failures, gate, tags, reason, suggested_reframe.
- **Receipt:** `IADReceipt` JSON (append-only discipline at repo level via `docs/06_RECEIPTS.md` for human/agent provenance).

## Invariants

1. One live primary task per packet (singularity enforced heuristically and via HF-4 under AUTO).
2. Proof must be observable for high-trust continuation; vague or missing proof lowers scores and can trigger hard-fails with irreversible actions.
3. Hard-fails override numeric coherence when structural rules fire (mission mismatch, constraint violation, etc.).
4. Gate set remains finite: PASS, REVIEW, WAIT, BLOCK (ESCALATE reserved in model for future policy).
5. Doc logs `04`–`08` are append-only; do not rewrite history.
6. Agents follow `AGENT_CONTRACT.md` for INSITU, RECEIPT, and BUILD SUMMARY discipline.

## Failure modes

1. **False PASS:** Heuristics miss semantic drift (e.g., wrong test passes)—coherence is structural, not truth.
2. **False BLOCK/REVIEW:** Short missions or tasks share too few lexical tokens with mission text—requires tuning or richer alignment later.
3. **Tool-fit blind spots:** Unknown tools default to neutral scoring; sensitive operations need explicit policy.
4. **Compound-task detection:** Separator list may miss natural bundling in free text.
5. **Constraint coverage:** Only explicit constraint phrases in code are enforced; others ignored until encoded.
6. **Receipt collision:** `write_receipt` uses a fixed filename unless changed—parallel writers could clobber; use unique paths in production.
7. **Context filename drift:** Project context may live outside `docs/`; canonical decisions belong in `08_DECISIONS.md`.
