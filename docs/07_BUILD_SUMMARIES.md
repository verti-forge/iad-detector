# Build summaries (append-only)

### 2026-03-25 — Phase: repository scaffold

- **What shipped:** Full doc spine (`00`–`08`), agent contract, `.gitignore`, Python `pyproject.toml`, `src/iad_detector` v0 (models, rules, scorer, detector, reframe, receipts), tests (`test_hard_fails`, `test_scoring`), `scripts/run_example.py`, `.learnings/`.  
- **What did not ship:** Putline v2/v3 line parser; HTTP service; CI config; ten-trace suite (tracked as T003).  
- **Notes:** Context source file retained as `putline-CONTEXT.txt`; template retained as `scaffold-template.txt`. Initialize git when ready; then attach real commit hashes to receipt entries.

### 2026-03-25 — T003: ten-trace matrix

- **What shipped:** `TRACE_CASES` in `tests/fixtures.py` (10 named packets), `test_t003_trace_matrix` + `test_t003_covers_all_gates` in `tests/test_traces.py`; T001–T003 marked done in `docs/02_TASKS.md`.  
- **What did not ship:** ESCALATE traces (detector v0 never returns that gate).  
- **Notes:** Gates covered: PASS, REVIEW, WAIT, BLOCK. Heuristic tuning should use failing trace IDs as fixtures.
