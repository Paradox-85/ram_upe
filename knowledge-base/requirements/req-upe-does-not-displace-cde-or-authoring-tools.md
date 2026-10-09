---
type: requirement
title: UPE does not displace the CDE or authoring tools
description: "UPE is a coordination and intelligence layer above existing systems: it must not become the project system of record in place of the CDE (ACC, ProjectWise) or replace DMS, ERP, CRM or authoring tools."
tags: [requirement, constraint, draft]
sources:
  - ../../sources/legacy/docs/UPE_Functional_Blocks_v1.md
  - ../../sources/legacy/docs/UPE_Executive_Summary_v1.md
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
    - type: derived-from
      target: ../../sources/legacy/docs/UPE_Executive_Summary_v1.md
    - type: derived-from
      target: problems/cde-interoperability-and-manual-syncing
requirement:
  kind: constraint
---

# UPE does not displace the CDE or authoring tools

## Statement
> UPE is a coordination and intelligence layer above existing systems: it must not become the project system of record in place of the CDE (ACC, ProjectWise) or replace DMS, ERP, CRM or authoring tools.

## Rationale
Stacking a second system of record on top of the CDE would duplicate truth and break information-management accountability.

## Traceability
- Source/analysis: [`UPE_Functional_Blocks_v1.md`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/sources/legacy/docs/UPE_Functional_Blocks_v1.md&version=GBmain), [`UPE_Executive_Summary_v1.md`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/sources/legacy/docs/UPE_Executive_Summary_v1.md&version=GBmain) (functional block 7.3; product boundary stated in the executive summary)
- Problem: [`cde-interoperability-and-manual-syncing`](../problems/cde-interoperability-and-manual-syncing.md)
- Realising capabilities: none recorded
- Architecture: see [`../views/architecture-overview.md`](../views/architecture-overview.md) (candidate layers; no approved component assignment yet)
- Verification: Architecture review: no UPE component is the authoritative store for project deliverables, ERP or CRM records.

## Open questions
- No architecture component or decision is assigned to this requirement yet; promotion to
  `in-review` requires a review that also records the realising capability relations in the
  capability records themselves.
