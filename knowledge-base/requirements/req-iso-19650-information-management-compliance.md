---
type: requirement
title: Information management complies with ISO 19650
description: "Information containers, naming, status and metadata handling must remain compatible with the ISO 19650 information-management requirements already adopted by the CDE."
tags: [requirement, constraint, draft]
sources:
  - ../../sources/standards/iso-19650.md
generated: 2026-10-09T11:20:00Z
verified: false
status: draft
stale_after: 2027-10-09
upe:
  lifecycle: draft
  owner: "@chief-architect"
  relations:
    - type: derived-from
      target: ../../sources/standards/iso-19650.md
requirement:
  kind: constraint
---

# Information management complies with ISO 19650

## Statement
> Information containers, naming, status and metadata handling must remain compatible with the ISO 19650 information-management requirements already adopted by the CDE.

## Rationale
The CDE and Ramboll's delivery obligations already operate under ISO 19650; UPE metadata must not diverge from it.

## Traceability
- Source/analysis: [`iso-19650.md`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/sources/standards/iso-19650.md&version=GBmain) (functional block external; external standard document)
- Problem: none recorded
- Realising capabilities: none recorded
- Architecture: see [`../views/architecture-overview.md`](../views/architecture-overview.md) (candidate layers; no approved component assignment yet)
- Verification: Map UPE metadata fields against the standard's information-container requirements and record the gaps.

## Open questions
- No architecture component or decision is assigned to this requirement yet; promotion to
  `in-review` requires a review that also records the realising capability relations in the
  capability records themselves.
