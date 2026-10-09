---
id: stakeholder-brief-2026-05-26
type: report
status: draft
owner: "@chief-architect"
version: 0.1
last_updated: 2026-05-26
parent: ../master.md
tags: [report, stakeholder, brief, demo]
---

> ⚠️ **This is a derived snapshot generated on 2026-05-26. For current authoritative knowledge, refer to [../master.md](../master.md) and [../modules/](../modules/).**

# Stakeholder Brief — DDDM for Unified Project Execution

**Date:** 2026-05-26
**Status:** Draft (pending review)
**Audience:** Architects and module owners attending the demo session

---

## Why DDDM Matters for Unified Project Execution

We are building UPE (Unified Project Execution) — a coordination and intelligence layer that connects CRM, ERP, CDE, and collaboration tools into a single delivery platform. The design is complex, spans 14 functional domains, and must evolve through continuous dialogue between architects, module owners, and AI assistants.

Traditional specification documents fail us: Word files go stale, Visio diagrams drift from reality, and Confluence pages become write-only graveyards. We need a design method that keeps pace with our thinking.

**DDDM (Dialogue-Driven Design Method)** replaces document-centric design with a living knowledge base. Every requirement, every data entity, every interface contract, every architecture decision lives as structured Markdown in a Git-style repository. Mermaid diagrams are embedded directly in the text — they update when the knowledge updates. AI sessions are logged as first-class artifacts.

The result: a knowledge base that is always current, always queryable, and always ready for the next design dialogue.

---

## Key Concepts (in plain language)

| Concept | What it means |
|---|---|
| **Master** | The reviewed, shared truth. Like the `main` branch in Git — protected, approved, canonical. Contains all requirements, data models, and decisions that the team has agreed on. |
| **Fork** | A safe working copy for a module owner to explore changes, propose new requirements, or test hypotheses. Like a feature branch — you can experiment freely without affecting the shared truth. |
| **Prototype** | A clickable mock-up generated from the knowledge base to validate ideas with stakeholders. It is NOT the source of truth — the knowledge base is. If the prototype and the knowledge base disagree, the knowledge base wins. |

---

## What We Will Show in the Demo

We will walk through the M01 (Project Initialization & Provisioning) module as a complete example of DDDM in action:

1. **The knowledge base** — how requirements, data models, workflows, and interface contracts are organised as structured Markdown with YAML metadata and Mermaid diagrams.
2. **The fork workflow** — how a module owner proposes changes without affecting the shared truth.
3. **A generated prototype prompt** — how the knowledge base produces a ready-to-use prompt for building clickable UI mock-ups.
4. **Interface contracts** — how seven integration boundaries with CRM, ERP, HR, M365, CDE, Template Library, and Knowledge Graph are specified.

For the detailed demo flow and timing, see [../demo_script.md](../demo_script.md).

---

## Decisions Requested from Colleagues

| # | Decision | Why Now |
|---|---|---|
| 1 | **Adopt this framework as the working method for UPE design?** | We need to commit to a consistent methodology before scaling to M02–M05. A pilot with M01 has validated the approach. |
| 2 | **Assign module owners for M02–M05?** | Each module needs a designated owner who can create forks, run LLM design sessions, and submit for merge review. Without owners, knowledge base evolution stalls. |
| 3 | **Agree on branching convention and review cadence?** | We need to decide: naming conventions for forks, how often merge reviews happen, and who approves. This ensures the knowledge base evolves in a controlled, predictable rhythm. |

---

## Next Steps

1. **This session:** Review this brief, attend the demo, discuss the three decisions above.
2. **This week:** Provide feedback on [../master.md](../master.md) and M01 artifacts.
3. **Week 2:** Confirm decisions and assign module owners.
4. **Week 3–4:** Sprint 1 implementation begins; UI prototype generated from prototype prompt.

---

**Document Type:** Derived Snapshot (NOT source of truth)
**Generated from:** [../master.md](../master.md) and [../modules/m01_project_initialization/](../modules/m01_project_initialization/)
**Contact:** @chief-architect
