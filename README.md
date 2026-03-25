# Putline / iad-detector

**IAD Detector:** Intent–Action Decoupling detection for agent execution loops. This repo also documents **Putline**, the Surface-Line / Execution Surface protocol: one compact line for loop integrity (state, task, proof, next, and in v2/v3 receipt, mode, gate, owner). It includes the **receipts-first scaffold** for tooling plus the doc spine agents use to avoid drift.

- **Narrative spec:** `putline-CONTEXT.txt`
- **Scaffold rules:** `scaffold-template.txt`
- **Mission & architecture:** `docs/00_MISSION.md`, `docs/01_ARCHITECTURE.md`
- **Agent rules:** `AGENT_CONTRACT.md`

## Layout

- `docs/` — `00_MISSION` … `08_DECISIONS` (append-only where noted)
- `src/iad_detector/` — Python package
- `tests/` — Pytest
- `scripts/` — Local examples
- `.learnings/` — Notes that do not belong in append-only logs

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -e ".[dev]"
python -m pytest
python -m iad_detector   # sample CLI run (example packet)
```

## Git workflow

1. Implement the active task from `docs/02_TASKS.md`
2. Write an **INSITU** entry (`docs/05_INSITU.md`)
3. Write a **RECEIPT** entry (`docs/06_RECEIPTS.md`)
4. Run verification (`python -m pytest`, etc.)
5. Commit using the structured format below
6. Append a **BUILD SUMMARY** (`docs/07_BUILD_SUMMARIES.md`) when a phase or acceptance criteria passes

### Commit message format

```
[type]: short summary

TASK: T### SCOPE: path/component WHY: reason PROOF: test/output/hash
```

**Allowed types:** `feat` | `fix` | `refactor` | `docs` | `test` | `chore`

If no **PROOF** exists, the task is incomplete.

### Optional `.gitmessage` template

Save as `.gitmessage` and run `git config commit.template .gitmessage`:

```
# [type]: 50-char subject

# Body (wrap ~72 chars):
# TASK: T###
# SCOPE:
# WHY:
# PROOF:

# types: feat | fix | refactor | docs | test | chore
```

## Putline reminder (v1)

`[STATE] · TASK · PROOF · NEXT`

Example: `[BUILDING] · implement receipt serializer · receipt JSON emitted · validate schema`

## License

MIT — see [`LICENSE`](LICENSE).
