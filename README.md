
**IAD Detector** is a lightweight execution-integrity primitive for autonomous systems.

It catches **Intent–Action Decoupling** before an agent acts: cases where the current mission, proposed action, available proof, and declared next step are no longer aligned strongly enough to justify execution.

Rather than scoring outputs after the fact, `iad-detector` works as a **pre-action coherence gate**. Given a structured packet, it evaluates:

- whether the task still serves the mission
- whether the action respects active constraints
- whether available proof is sufficient for the step being attempted
- whether the chosen tool fits the task
- whether the proposed next step is actually justified

The result is a compact decision surface for runtime systems:
`PASS`, `REVIEW`, `WAIT`, `BLOCK`, or `ESCALATE`.

This repository contains the v0 detector core, test fixtures, receipt-ready models, and the initial doc spine for the broader **Putline** protocol direction.
