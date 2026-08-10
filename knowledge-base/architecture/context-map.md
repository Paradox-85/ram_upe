---
type: architecture
title: Context Map (Framework)
description: Draft context-map framework enumerating M01–M14 as candidate functional domains only; no bounded-context boundaries or typed context-map edges are defined yet.
tags: [architecture, context-map, ddd, draft, upe]
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

# Context Map (Framework)

> **Status: draft framework.** This map enumerates **candidate functional domains** only. **No bounded-context boundaries and no typed context-map edges are defined** in this cycle.

## Candidate functional domains
| ID | Candidate domain |
|---|---|
| M01 | Project Lifecycle & Environment Management |
| M02 | User & Access Management |
| M03 | Project Planning & Delivery Management |
| M04 | Data Quality & Validation |
| M05 | Information Governance & Knowledge Management |
| M06 | AI Integration & Intelligence Capabilities |
| M07 | System Integration & Interoperability |
| M08 | Embedded Process Automation & Workflow |
| M09 | User Experience & Interface Design |
| M10 | Foundational Requirements & Technical Enablement |
| M11 | Platform Governance & Roadmap Management |
| M12 | Monitoring, Diagnostics & Operational Support |
| M13 | Technology Enablement & Build vs. Buy |
| M14 | Special Capability Domains (BIM/GIS, Time, Contracts) |

Each is a candidate (see [`../domains/m01-project-lifecycle-environment-management.md`](../domains/m01-project-lifecycle-environment-management.md)) — not a bounded context.

## Not defined yet
- Bounded-context boundaries: **unproven**.
- Typed DDD context-map edges (partnership, shared-kernel, anti-corruption layer, etc.): **out of scope** this cycle.

## Related
- [`../governance/glossary.md`](../governance/glossary.md) — `bounded context` marked unproven.
- [`../governance/metadata-profile.md`](../governance/metadata-profile.md) — relation vocabulary excludes context-map edges.
- [`master.md`](master.md) — integration view.
