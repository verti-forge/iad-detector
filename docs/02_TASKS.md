# Tasks

Ordered, small, acceptance-first. Execute one task at a time per `AGENT_CONTRACT.md`.

---

### T001 — Lock scaffold and doc spine

- **Description:** Ensure `docs/00`–`08`, `README`, `AGENT_CONTRACT`, `.gitignore`, `src/`, `tests/`, `scripts/`, `.learnings/` exist per template; no renamed or omitted template files.
- **Files likely touched:** `docs/*`, root manifests, `.learnings/.gitkeep`
- **Acceptance:**
  - [x] Folder tree matches template file map
  - [x] Every required doc file exists with non-empty purpose-aligned content
  - [x] Initial entries exist in `04_PROGRESS`, `05_INSITU`, `06_RECEIPTS`, `07_BUILD_SUMMARIES`
- **Verification:** Manual tree check; read `docs/00_MISSION.md` and `AGENT_CONTRACT.md`
- **Safety / rollback:** Delete mistaken files; docs are version-controlled and append-only thereafter
- **Status:** Complete. Follow-on: repo initialized and pushed to `origin` (`verti-forge/iad-detector`).

---

### T002 — IAD v0 package and tests green

- **Description:** Implement `iad_detector` under `src/` with `detect()` and tests from project context; `pytest` passes.
- **Files likely touched:** `src/iad_detector/*`, `tests/*`, `pyproject.toml`
- **Acceptance:**
  - [x] `pytest` exits 0
  - [x] `BAD_PACKET` yields BLOCK with expected hard-fail strings
  - [x] `GOOD_PACKET` yields PASS and coherence ≥ 0.85
- **Verification:** `python -m pytest`
- **Safety / rollback:** Revert package directory; keep docs spine
- **Status:** Complete. Includes `constants.WEIGHTS`, `python -m iad_detector` (`__main__.py`), and shared `test_traces` checks for `GOOD_PACKET` / `BAD_PACKET`.

---

### T003 — Ten fake traces (manual or scripted)

- **Description:** Capture ten representative packets (pass, review, wait, block variants) in `tests/fixtures.py` or `scripts/`; record outcomes in `docs/06_RECEIPTS.md` or test parametrization.
- **Files likely touched:** `tests/fixtures.py`, `tests/test_traces.py` (optional), `docs/06_RECEIPTS.md`
- **Acceptance:**
  - [x] Ten distinct packets documented or tested
  - [x] At least one trace per gate outcome type where feasible
- **Verification:** Pytest or documented table in receipt entries
- **Safety / rollback:** Remove experimental traces; keep core fixtures
- **Status:** Complete. See `TRACE_CASES` in `tests/fixtures.py`, `test_t003_trace_matrix` + `test_t003_covers_all_gates` in `tests/test_traces.py`. v0 does not emit `ESCALATE`; coverage is PASS / REVIEW / WAIT / BLOCK.

---

### T004 — Putline v2/v3 parser (optional)

- **Description:** Parse or emit canonical Putline v2/v3 strings into `Packet` or a sibling model.
- **Files likely touched:** `src/iad_detector/putline.py` (new), `tests/test_putline.py`
- **Acceptance:**
  - [ ] Round-trip or golden-file tests for examples from context
- **Verification:** `pytest` targeted module
- **Safety / rollback:** Feature-flag or separate module; do not break `detect()` API

---

### T005 — Service boundary (optional)

- **Description:** HTTP or queue adapter for `detect()` (e.g., FastAPI)—only if runtime integration requires it.
- **Files likely touched:** new `src/` service module, manifest deps
- **Acceptance:**
  - [ ] Contract tests for request/response schema
  - [ ] Dependency approved per agent contract
- **Verification:** Automated API tests
- **Safety / rollback:** Keep package pure; adapter in optional extra
