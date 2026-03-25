# Receipts log (append-only)

Project proof entries. Mirror or supplement JSON receipts under `receipts/` when tooling emits them.

---

### 2026-03-25T12:00:00Z

- **Task ID:** T001 / T002 (scaffold + package)  
- **Files changed:** `docs/*`, `src/iad_detector/*`, `tests/*`, `scripts/run_example.py`, `README.md`, `AGENT_CONTRACT.md`, `.gitignore`, `pyproject.toml`, `.learnings/.gitkeep`  
- **Commands run:** `python -m pip install -e ".[dev]"`; `python -m pytest -q`  
- **Verification output:** `2 passed` (2026-03-25)  
- **Commit hash:** (none — workspace not yet git-init’d at scaffold time)

---

### 2026-03-25T14:30:00Z

- **Task ID:** DX (CLI + weights + trace harness)  
- **Files changed:** `src/iad_detector/__main__.py`, `src/iad_detector/constants.py`, `src/iad_detector/detector.py`, `tests/test_traces.py`, `docs/05_INSITU.md`, `docs/06_RECEIPTS.md`  
- **Commands run:** `python -m pytest -q`; `python -m iad_detector`  
- **Verification output:** `4 passed`  
- **Commit hash:** (n/a)
