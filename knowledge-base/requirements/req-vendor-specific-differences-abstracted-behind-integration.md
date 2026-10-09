---
type: requirement
title: Vendor-specific differences are abstracted behind the integration layer
description: "Integrations must isolate vendor-specific behaviour so that adding or replacing a vendor does not force changes to other integrations or to shared data contracts."
tags: [requirement, non-functional, draft]
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
    - type: derived-from
      target: problems/cde-interoperability-and-manual-syncing
    - type: derived-from
      target: problems/monolith-architecture-risk
requirement:
  kind: non-functional
---

# Vendor-specific differences are abstracted behind the integration layer

## Statement
> Integrations must isolate vendor-specific behaviour so that adding or replacing a vendor does not force changes to other integrations or to shared data contracts.

## Rationale
Prevents lock-in and keeps the integration surface maintainable as the vendor stack evolves.

## Traceability
- Source/analysis: [`UPE_Functional_Blocks_v1.md`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/sources/legacy/docs/UPE_Functional_Blocks_v1.md&version=GBmain) (functional block 7.3; functional block heading)
- Problem: [`cde-interoperability-and-manual-syncing`](../problems/cde-interoperability-and-manual-syncing.md), [`monolith-architecture-risk`](../problems/monolith-architecture-risk.md)
- Realising capabilities: [`ability-to-abstract-vendor-specific-differences`](../capabilities/ability-to-abstract-vendor-specific-differences.md), [`ability-to-add-new-vendors-without-breaking-existing-integrations`](../capabilities/ability-to-add-new-vendors-without-breaking-existing-integrations.md)
- Architecture: see [`../views/architecture-overview.md`](../views/architecture-overview.md) (candidate layers; no approved component assignment yet)
- Verification: Replace or stub one vendor adapter in a test environment without touching other adapters or shared contracts.

## Open questions
- No architecture component or decision is assigned to this requirement yet; promotion to
  `in-review` requires a review that also records the realising capability relations in the
  capability records themselves.
