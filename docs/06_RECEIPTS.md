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

---

### 2026-03-25T15:00:00Z

- **Task ID:** publish  
- **Files changed:** `.git/` (init); merge brought `LICENSE`; `README.md` (conflict resolved); push to `origin`  
- **Commands run:** `git init`; `git add -A`; `git commit`; `git remote add origin https://github.com/verti-forge/iad-detector.git`; `git fetch`; `git merge origin/main --allow-unrelated-histories`; `git push -u origin main`  
- **Verification output:** push reported `main -> main`  
- **Commit hash:** `afd0629` (merge tip on `main`)

---

### 2026-03-25T15:05:00Z

- **Task ID:** publish (doc trail)  
- **Files changed:** `docs/05_INSITU.md`, `docs/06_RECEIPTS.md`  
- **Commands run:** `git commit`; `git push`  
- **Verification output:** `8f4106c..main` on origin  
- **Commit hash:** `8f4106c`
