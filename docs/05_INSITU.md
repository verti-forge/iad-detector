# INSITU (append-only — heartbeat / jump-back-in)

### 2026-03-25 12:00

DONE: Initialized Git-ready scaffold from `scaffold-template.txt` using `putline-CONTEXT.txt` (Putline protocol + IAD v0).  
PROOF: Files on disk: `docs/00`–`08`, `src/iad_detector/*`, `tests/*`, `pyproject.toml`, `README.md`, `AGENT_CONTRACT.md`.  
NEXT: `python -m pytest`; then T003 fake traces; tighten heuristics only after false-positive review.

### 2026-03-25 14:30

DONE: Added `__main__.py` (`python -m iad_detector`), `constants.WEIGHTS` for coherence tuning, `tests/test_traces.py` regression harness.  
PROOF: `python -m pytest -q` → 4 passed; `python -m iad_detector` prints JSON.  
NEXT: Extend `test_traces` with more packets for T003; tune `WEIGHTS` only after trace review.
