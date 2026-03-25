# Mission

Putline is a protocol for a minimal, human-readable, machine-routable execution surface: one line that answers where we are, what we are doing, what proved it, what happens next, and (in v2/v3) receipt linkage, gates, mode, and owner. This repository implements supporting tooling—starting with the Intent–Action Decoupling (IAD) Detector v0—a pre-action coherence gate that blocks execution when declared mission and proposed action have structurally decoupled, aligned with receipts-first and anti-drift practice.

**Target user:** Developers and agent operators who want a shared control-line format and a thin structural gate before irreversible or misaligned actions—not a replacement for human review or semantic correctness checks.

**Definition of done:** The repo ships a deterministic doc spine (`docs/00`–`08`), agent contract, git-oriented workflow, and a minimal Python package that parses evaluation packets, scores coherence dimensions, applies hard-fail rules, emits structured results and optional receipt JSON, with tests that prove the happy path and a known bad path.

**Non-goals:** Full natural-language understanding of missions; proving code or business correctness; replacing Arena, Check Loop, or orchestration layers; UI/dashboards in this scaffold; bloating the on-wire Putline string beyond the compact v3 shape described in project context.
