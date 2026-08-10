---
type: architecture
title: Master Architecture Integration View
description: Draft integration architecture view over the Unified Project Execution KB — domain/capability collections, architecture-related solution candidates, decision catalog, and raw historical sources.
tags: [architecture, integration-view, draft, upe]
sources: []
generated: 2026-08-10T07:48:05Z
verified: false
status: draft
stale_after: 2027-08-10
upe:
  lifecycle: draft
  owner: "@chief-architect"
  relations: []
---

# Master Architecture (Integration View)

> **Status: draft.** This integration view relates the DDD concept collections and decisions. It does **not** restate the legacy approved master as approved fact; all canonical content is candidate.

## Purpose
Provide the single entry point that connects, from the Unified Project Execution KB:

- **Domains:** 14 candidate functional domains (from [`m01-project-lifecycle-environment-management`](../domains/m01-project-lifecycle-environment-management.md)) — candidates, not bounded contexts.
- **Capabilities:** 520 source-backed capability records (e.g. [`ability-to-add-users-to-project-team`](../capabilities/ability-to-add-users-to-project-team.md)) in `../capabilities/`.
- **Concepts:** problems, use-cases, events, and solution-candidates backing the architecture.
- **Decisions:** ADR catalog at [`decisions/`](decisions/index.md) (incl. historic ADR-0001).
- **Raw evidence:** legacy architecture sources under `raw-input/` (immutable).

## Layered view (candidate, per raw sources)
Candidate functional layers (from raw `master.md` / `UPE_Functional_Blocks_v1.md`):
1. Collaboration UX (Portal, Dashboards, Copilot) — `m09` candidate domain.
2. Process Orchestration (Workflows, Approvals) — `m08`.
3. Intelligence & Data (AI/ML, Knowledge Graph, Data Quality) — `m06`, `m05`.
4. Integration & API Hub — `m07`.
5. CDE & Authoring Tools (independent).
6. Enterprise Systems (CRM, ERP, HR).
7. Cross-cutting Governance & Security (`m10`, `m11`).

## Related solution candidates
- [`authoring-tool-addin-process-ui`](../solution-candidates/authoring-tool-addin-process-ui.md)
- [`backend-controlled-workflow-engine`](../solution-candidates/backend-controlled-workflow-engine.md)
- [`sharepoint-lists-as-state-projection-layer`](../solution-candidates/sharepoint-lists-as-state-projection-layer.md)
- [`microsoft-365-centric-stack`](../solution-candidates/microsoft-365-centric-stack.md)

## Decision catalog
See [`decisions/index.md`](decisions/index.md) and the historic raw ADR-0001 (docs-as-data) referenced from [`decisions/adr-0001-history.md`](decisions/adr-0001-history.md).

## Open questions
- Bounded-context boundaries for M01–M14 are unproven (see [`context-map.md`](context-map.md)).
- This view is candidate; do not treat any layer assignment as approved.
