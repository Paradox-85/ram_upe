---
type: requirement
title: Data quality rules are enforced across pipeline stages
description: "Validation and quality rules are applied at defined pipeline stages, including inside design tools, so that non-conforming data is caught before it propagates."
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
    - type: derived-from
      target: problems/manual-property-set-ifc-conversion-work
requirement:
  kind: functional
---

# Data quality rules are enforced across pipeline stages

## Statement
> Validation and quality rules are applied at defined pipeline stages, including inside design tools, so that non-conforming data is caught before it propagates.

## Rationale
Manual property-set and IFC conversion work is a documented pain point caused precisely by checks happening late or not at all.

## Traceability
- Source/analysis: [`UPE_Functional_Blocks_v1.md`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/sources/legacy/docs/UPE_Functional_Blocks_v1.md&version=GBmain) (functional block 4.2; functional block heading)
- Problem: [`manual-property-set-ifc-conversion-work`](../problems/manual-property-set-ifc-conversion-work.md)
- Realising capabilities: [`ability-to-apply-quality-checks-at-pipeline-stages`](../capabilities/ability-to-apply-quality-checks-at-pipeline-stages.md), [`ability-to-embed-validation-in-design-tools-revit-etc`](../capabilities/ability-to-embed-validation-in-design-tools-revit-etc.md), [`ability-to-apply-machine-learning-models-to-detect-anomalies`](../capabilities/ability-to-apply-machine-learning-models-to-detect-anomalies.md)
- Architecture: see [`../views/architecture-overview.md`](../views/architecture-overview.md) (candidate layers; no approved component assignment yet)
- Verification: Inject non-conforming data and confirm it is flagged at the intended stage.

## Open questions
- No architecture component or decision is assigned to this requirement yet; promotion to
  `in-review` requires a review that also records the realising capability relations in the
  capability records themselves.
