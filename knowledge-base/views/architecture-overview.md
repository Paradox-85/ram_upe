---
type: view
title: Architecture Overview
description: "Current UPE architecture state and its major parts, as recorded in the canonical KB."
tags: [view, generated, architecture-overview, draft]
sources: []
generated: 2026-10-09T00:00:00Z
verified: false
status: draft
stale_after: 2027-10-09
upe:
  lifecycle: draft
  owner: "@chief-architect"
  relations:
    - type: supports
      target: index
---

# Architecture Overview

> **Generated / non-authoritative projection of canonical KB entities.**
> Regenerate: `python tools/kb-views/generate.py`. Do not hand-edit; the records win.

## Governed architecture records

| Record | Description |
|---|---|
| [`context-map`](../architecture/context-map.md) | Draft context-map framework enumerating M01–M14 as candidate functional domains only; no bounded-context boundaries or typed context-map edges are defined yet. |
| [`master`](../architecture/master.md) | Draft integration architecture view over the Unified Project Execution KB — domain/capability collections, architecture-related solution candidates, decision catalog, and historical evidence under sources/. |

## Decision catalog

| Decision | Title | Status | Lifecycle |
|---|---|---|---|
| [`adr-0001-history`](../architecture/decisions/adr-0001-history.md) | ADR-0001 — Docs-as-Data (History) | draft | draft |
| [`index`](../architecture/decisions/index.md) | Architecture Decision Catalog | draft | draft |

## Candidate functional domains (not bounded contexts)

| ID | Domain | Priority | Key outcome |
|---|---|---|---|
| M01 | [`M01 — Project Lifecycle & Environment Management`](../domains/m01-project-lifecycle-environment-management.md) | High | Consistent project startup, knowledge preservation |
| M02 | [`M02 — User & Access Management`](../domains/m02-user-access-management.md) | High | Faster team assembly, security, audit compliance |
| M03 | [`M03 — Project Planning & Delivery Management`](../domains/m03-project-planning-delivery-management.md) | High | Clear accountability, early warning systems |
| M04 | [`M04 — Data Quality & Validation`](../domains/m04-data-quality-validation.md) | Medium | Reliable data, error prevention, design reuse |
| M05 | [`M05 — Information Governance & Knowledge Management`](../domains/m05-information-governance-knowledge-management.md) | Medium | Reduced knowledge loss, AI-ready data |
| M06 | [`M06 — AI Integration & Intelligence Capabilities`](../domains/m06-ai-integration-intelligence-capabilities.md) | Strategic | Automation at scale, smarter workflows |
| M07 | [`M07 — System Integration & Interoperability`](../domains/m07-system-integration-interoperability.md) | Medium | Flexible architecture, seamless data flow |
| M08 | [`M08 — Embedded Process Automation & Workflow`](../domains/m08-embedded-process-automation-workflow.md) | Medium | Simpler workflows, higher compliance |
| M09 | [`M09 — User Experience & Interface Design`](../domains/m09-user-experience-interface-design.md) | Medium | Reduced friction, better situational awareness |
| M10 | [`M10 — Foundational Requirements & Technical Enablement`](../domains/m10-foundational-requirements-technical-enablement.md) | High | Reliable foundation, extensibility |
| M11 | [`M11 — Platform Governance & Roadmap Management`](../domains/m11-platform-governance-roadmap-management.md) | Strategic | Coherent evolution, stakeholder alignment |
| M12 | [`M12 — Monitoring, Diagnostics & Operational Support`](../domains/m12-monitoring-diagnostics-operational-support.md) | Strategic | Reliable operations, data-driven optimization |
| M13 | [`M13 — Technology Enablement & Build vs. Buy`](../domains/m13-technology-enablement-build-buy.md) | Medium | Cost efficiency, rapid capability delivery |
| M14 | [`M14 — Special Capability Domains (BIM/GIS, Time, Contracts)`](../domains/m14-special-capability-domains.md) | Strategic | End-to-end project coverage |

---

_Generated 2026-10-09 from 582 canonical records._
