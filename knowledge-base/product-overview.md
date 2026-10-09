---
type: navigation
title: Product Overview
description: "Short, curated introduction to UPE for business readers: what the platform is, what it is not, and where the governed detail lives."
tags: [navigation, product, overview, wiki, upe]
sources:
  - ../sources/legacy/docs/UPE_Executive_Summary_v1.md
generated: 2026-10-09T12:00:00Z
verified: false
status: draft
stale_after: 2027-10-09
upe:
  lifecycle: draft
  owner: "@chief-architect"
  relations:
    - type: derived-from
      target: ../sources/legacy/docs/UPE_Executive_Summary_v1.md
    - type: supports
      target: index
---

# Product Overview

> **Curated entry page.** It summarises; it does not decide. Where this page and a canonical record
> disagree, the record wins. Every claim below is traceable to a source or a KB record.

## In one line

UPE (**U**nified **P**roject **E**xecution) is Ramboll's enterprise digital backbone: a coordination
and intelligence layer that orchestrates project delivery across the full lifecycle — a stable core
with modular, configurable variations.

## What UPE is

- **Coordination & intelligence layer** — sits above the CDE and authoring tools rather than replacing them.
- **Process orchestration** — automates project workflows across systems (CRM, ERP, HR, CDE).
- **Knowledge platform** — captures, organises and reuses organisational knowledge instead of rebuilding it per project.
- **Integration hub** — connects enterprise systems through defined interface contracts.
- **Decision support** — turns project data into insight for delivery decisions.

## What UPE is not

- Does **not** replace the CDE (ACC, ProjectWise) — the CDE remains the project system of record for documents.
- Does **not** replace DMS or authoring tools (Revit, Bentley, AVEVA).
- Does **not** replace ERP or CRM — it integrates with them.
- Does **not** replace document stores — it is a coordination and intelligence surface.

These boundaries are not marketing: they are recorded as requirements, e.g.
[UPE does not displace the CDE or authoring tools](requirements/req-upe-does-not-displace-cde-or-authoring-tools.md)
and [vendor differences are abstracted behind integration](requirements/req-vendor-specific-differences-abstracted-behind-integration.md).

## Who this is for

| Reader | Start at |
|---|---|
| Business / GBA stakeholder | [GBA Needs & Coverage](views/gba-overview.md) → [Requirements Coverage](views/requirements-coverage.md) |
| Architect | [Architecture Overview](views/architecture-overview.md) → [master view](architecture/master.md) → [ADRs](architecture/decisions/) |
| Product Owner | [Capability Map](views/capability-map.md) → [Requirements Coverage](views/requirements-coverage.md) → [Roadmap projection](views/roadmap.md) |
| Contributor (any role) | [How to Contribute](contributing.md) |

## Where the detail lives

- **Structure of the solution:** [architecture/master.md](architecture/master.md) and its
  [context map](architecture/context-map.md). Note that M01–M14 are **candidate functional domains**,
  not proven bounded contexts.
- **What the platform must do:** 520 atomic capability records, indexed by the
  [Capability Map](views/capability-map.md).
- **What the business requires:** the [requirements collection](requirements/) with its
  [coverage view](views/requirements-coverage.md).
- **Evidence behind all of it:** [Sources & Evidence](views/sources-and-evidence.md).

## Status and caveats

- Everything in the knowledge base is `draft`/`candidate`; no record is `approved` in this cycle.
- The domain list (M01–M14) is a candidate grouping extracted from source material.
- Capability records are extracted statements, not an approved scope commitment.
- Open questions are tracked per record and collected in [Open Decisions](views/open-decisions.md).
