---
type: requirement
title: Project data is archived and dispositioned at closeout
description: "At project completion the platform archives project data, records the closure state, and optimises the archived set while keeping it retrievable with an audit trail."
tags: [requirement, functional, draft]
sources:
  - ../../sources/legacy/docs/UPE_Functional_Blocks_v1.md
generated: 2026-10-09T11:20:00Z
verified: false
status: draft
stale_after: 2027-10-09
upe:
  lifecycle: draft
  owner: "@chief-architect"
  relations:
    - type: derived-from
      target: ../../sources/legacy/docs/UPE_Functional_Blocks_v1.md
requirement:
  kind: functional
---

# Project data is archived and dispositioned at closeout

## Statement
> At project completion the platform archives project data, records the closure state, and optimises the archived set while keeping it retrievable with an audit trail.

## Rationale
Delivers the 'knowledge preservation' outcome of M01 and protects deliverables after the project team disbands.

## Traceability
- Source/analysis: [`UPE_Functional_Blocks_v1.md`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/sources/legacy/docs/UPE_Functional_Blocks_v1.md&version=GBmain) (functional block 1.2; functional block heading)
- Problem: none recorded
- Realising capabilities: [`ability-to-archive-project-data-at-project-completion`](../capabilities/ability-to-archive-project-data-at-project-completion.md), [`ability-to-mark-project-as-closedarchived`](../capabilities/ability-to-mark-project-as-closedarchived.md), [`ability-to-compressoptimize-archived-data`](../capabilities/ability-to-compressoptimize-archived-data.md), [`ability-to-maintain-audit-trail-for-archived-content`](../capabilities/ability-to-maintain-audit-trail-for-archived-content.md)
- Architecture: see [`../views/architecture-overview.md`](../views/architecture-overview.md) (candidate layers; no approved component assignment yet)
- Verification: Close a project and confirm archived content, closure state and audit trail.

## Open questions
- No architecture component or decision is assigned to this requirement yet; promotion to
  `in-review` requires a review that also records the realising capability relations in the
  capability records themselves.
