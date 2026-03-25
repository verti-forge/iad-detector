# Agent contract

All automated or human agents working in this repository MUST:

1. **One task at a time** — Work from `docs/02_TASKS.md`; complete or explicitly defer a task before switching.
2. **No silent refactors** — Changes outside the stated task scope require a new task or documented decision in `docs/08_DECISIONS.md`.
3. **Ask before adding dependencies** — New packages, services, or toolchain requirements need explicit approval; log the outcome in `docs/08_DECISIONS.md`.
4. **Every meaningful change requires:**
   - An **INSITU** entry in `docs/05_INSITU.md` (append-only).
   - A **RECEIPT** entry in `docs/06_RECEIPTS.md` (append-only).
5. **After completing a phase or passing acceptance** — Append a **BUILD SUMMARY** to `docs/07_BUILD_SUMMARIES.md`.
6. **If stopping** — Append a **PROGRESS** entry to `docs/04_PROGRESS.md` derived from the latest INSITU tail (state, open loops, next steps).
7. **If confused** — Ask at most **three precise questions**; do not guess mission-critical behavior.
8. **If context bloats** — Propose a clean handoff: active task ID, pointers to last INSITU / RECEIPT / PROGRESS entries, and blockers.

Violations of this contract should be corrected before merge or release.
