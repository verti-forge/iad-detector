# INSITU (append-only — heartbeat / jump-back-in)

### 2026-03-25 12:00

DONE: Initialized Git-ready scaffold from `scaffold-template.txt` using `putline-CONTEXT.txt` (Putline protocol + IAD v0).  
PROOF: Files on disk: `docs/00`–`08`, `src/iad_detector/*`, `tests/*`, `pyproject.toml`, `README.md`, `AGENT_CONTRACT.md`.  
NEXT: `python -m pytest`; then T003 fake traces; tighten heuristics only after false-positive review.

### 2026-03-25 14:30

DONE: Added `__main__.py` (`python -m iad_detector`), `constants.WEIGHTS` for coherence tuning, `tests/test_traces.py` regression harness.  
PROOF: `python -m pytest -q` → 4 passed; `python -m iad_detector` prints JSON.  
NEXT: Extend `test_traces` with more packets for T003; tune `WEIGHTS` only after trace review.

### 2026-03-25 15:00

DONE: `git init`, merged remote `LICENSE` + template README into full README, pushed `main` to [verti-forge/iad-detector](https://github.com/verti-forge/iad-detector).  
PROOF: `git push -u origin main` succeeded; tip `afd0629`.  
NEXT: Optional follow-up commit to sync this INSITU/RECEIPT to remote.

### 2026-03-25 16:00

DONE: Marked T001–T003 complete in `docs/02_TASKS.md`; added `TRACE_CASES` (10 packets) + gate coverage test for T003.  
PROOF: `python -m pytest -q` → 15 passed.  
NEXT: T004 Putline parser or tune `WEIGHTS` / heuristics using trace false positives.
