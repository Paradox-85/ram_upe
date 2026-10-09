---
type: requirement
title: The platform operates at multi-project scale
description: "Aggregation, search and reporting must remain usable across all projects of the portfolio, not only within one project."
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
requirement:
  kind: non-functional
---

# The platform operates at multi-project scale

## Statement
> Aggregation, search and reporting must remain usable across all projects of the portfolio, not only within one project.

## Rationale
The value of UPE is portfolio-level visibility; per-project-only performance would not deliver the cross-project outcomes.

## Traceability
- Source/analysis: [`UPE_Functional_Blocks_v1.md`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/sources/legacy/docs/UPE_Functional_Blocks_v1.md&version=GBmain) (functional block 10.3; functional block heading)
- Problem: none recorded
- Realising capabilities: [`ability-to-aggregate-tasks-across-all-projects`](../capabilities/ability-to-aggregate-tasks-across-all-projects.md), [`ability-to-aggregate-data-from-multiple-projects`](../capabilities/ability-to-aggregate-data-from-multiple-projects.md), [`ability-to-provide-consolidated-view-like-ms-planner`](../capabilities/ability-to-provide-consolidated-view-like-ms-planner.md)
- Architecture: see [`../views/architecture-overview.md`](../views/architecture-overview.md) (candidate layers; no approved component assignment yet)
- Verification: Load representative portfolio-scale data and measure aggregation/report latency.

## Open questions
- No architecture component or decision is assigned to this requirement yet; promotion to
  `in-review` requires a review that also records the realising capability relations in the
  capability records themselves.
