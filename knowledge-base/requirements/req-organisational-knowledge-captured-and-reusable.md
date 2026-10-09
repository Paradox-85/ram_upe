---
type: requirement
title: Organisational knowledge is captured once and reused
description: "Project knowledge — reference data, templates, lessons and standards — is captured in a reusable form and made available to subsequent projects instead of being rebuilt per project."
tags: [requirement, business, draft]
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
  kind: business
---

# Organisational knowledge is captured once and reused

## Statement
> Project knowledge — reference data, templates, lessons and standards — is captured in a reusable form and made available to subsequent projects instead of being rebuilt per project.

## Rationale
The business case for UPE rests on not re-deriving the same project knowledge for every new engagement.

## Traceability
- Source/analysis: [`UPE_Functional_Blocks_v1.md`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/sources/legacy/docs/UPE_Functional_Blocks_v1.md&version=GBmain) (functional block 5.1; functional block heading)
- Problem: none recorded
- Realising capabilities: [`ability-to-maintain-scalable-knowledge-capture-not-manual-10-hour-pr`](../capabilities/ability-to-maintain-scalable-knowledge-capture-not-manual-10-hour-pr.md), [`ability-to-make-reference-data-available-for-project-reuse`](../capabilities/ability-to-make-reference-data-available-for-project-reuse.md), [`ability-to-apply-reference-data-to-new-projects`](../capabilities/ability-to-apply-reference-data-to-new-projects.md)
- Architecture: see [`../views/architecture-overview.md`](../views/architecture-overview.md) (candidate layers; no approved component assignment yet)
- Verification: Show a knowledge artefact captured in one project being applied in another.

## Open questions
- No architecture component or decision is assigned to this requirement yet; promotion to
  `in-review` requires a review that also records the realising capability relations in the
  capability records themselves.
