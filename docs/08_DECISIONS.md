# Decisions (append-only — ADR-lite)

Context → Decision → Consequence

---

**Context:** Scaffold template requires `context.md`; repository had `putline-CONTEXT.txt` only.  
**Decision:** Treat `putline-CONTEXT.txt` as authoritative project context for mission and IAD v0 code; do not duplicate as `docs/context.md` unless template is amended.  
**Consequence:** Contributors read `putline-CONTEXT.txt` for narrative spec; `docs/00_MISSION.md` summarizes scope.

---

**Context:** Template allows a minimal runtime manifest only if required.  
**Decision:** Add `pyproject.toml` with `pydantic>=2` because `iad_detector` uses Pydantic models.  
**Consequence:** Python 3.11+ and venv install expected; no `package.json`.

---

**Context:** `write_receipt` defaults to `receipts/iad_check.json`.  
**Decision:** Gitignore `receipts/` for local runs; canonical human trail remains `docs/06_RECEIPTS.md`.  
**Consequence:** Generated JSON is not committed by default; CI can write to a temp dir.

---

**Context:** Original `BAD_PACKET` task text shared two tokens with the mission (`serializer`, `refactor`), so `score_mission_alignment` returned 1.0 and skipped HF-1 despite scope drift.  
**Decision:** Adjust `BAD_PACKET` in `tests/fixtures.py` to a compound, rename-heavy task with fewer lexical overlaps so v0 heuristics match the intended failure demo.  
**Consequence:** `scripts/run_example.py` uses the same packet; regression tests stay aligned with HF-1 + HF-3 expectations.
