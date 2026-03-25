# Risks

| Risk | Mitigation hint |
|------|-----------------|
| Heuristic IAD scores misfire on short or jargon-heavy missions | Add mission keywords, embeddings, or human REVIEW path; log false positives in `.learnings/` |
| Putline string over-encoded and unreadable | Keep surface line compact; use JSON substrate in tools |
| Receipt files overwritten or lost | Unique filenames (timestamp+hash); append-only store or DB later |
| Parallel agents append conflicting doc edits | Serialize writes or use per-agent receipt files + merge policy |
| Scope creep into full orchestrator | Enforce non-goals in `00_MISSION.md`; ADR in `08_DECISIONS.md` |
| pydantic major version drift | Pin ranges in `pyproject.toml`; run CI on upgrade |
| Sensitive data in receipts or logs | Redact in `06_RECEIPTS.md`; gitignore local `receipts/` secrets |
| Unknowns: production traffic shape | Ship v0 thin detector; measure tags and gates before tuning weights |
