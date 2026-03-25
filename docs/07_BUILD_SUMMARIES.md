# Build summaries (append-only)

### 2026-03-25 — Phase: repository scaffold

- **What shipped:** Full doc spine (`00`–`08`), agent contract, `.gitignore`, Python `pyproject.toml`, `src/iad_detector` v0 (models, rules, scorer, detector, reframe, receipts), tests (`test_hard_fails`, `test_scoring`), `scripts/run_example.py`, `.learnings/`.  
- **What did not ship:** Putline v2/v3 line parser; HTTP service; CI config; ten-trace suite (tracked as T003).  
- **Notes:** Context source file retained as `putline-CONTEXT.txt`; template retained as `scaffold-template.txt`. Initialize git when ready; then attach real commit hashes to receipt entries.
