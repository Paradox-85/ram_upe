---
type: requirement
title: Improvement opportunities are assessed against existing practices and initiatives
description: "A proposed improvement must be assessed against practices already in use and initiatives already running in Ramboll, so that investment is not duplicated."
tags: [requirement, stakeholder, draft]
sources:
  - ../../sources/transport/rtr-production-improvement-opportunity-space.xlsx
generated: 2026-10-09T11:20:00Z
verified: false
status: draft
stale_after: 2027-10-09
upe:
  lifecycle: draft
  owner: "@chief-architect"
  relations:
    - type: derived-from
      target: ../../sources/transport/rtr-production-improvement-opportunity-space.xlsx
    - type: derived-from
      target: problems/misalignment-with-ramboll-enterprise-architecture
    - type: evidenced-by
      target: ../evidence/src-transport-rtr-opportunity-space
requirement:
  kind: stakeholder
---

# Improvement opportunities are assessed against existing practices and initiatives

## Statement
> A proposed improvement must be assessed against practices already in use and initiatives already running in Ramboll, so that investment is not duplicated.

## Rationale
Requested implicitly by the structure of the Transport opportunity-space workbook: it carries practice and initiative mapping tables and a review gate precisely so that opportunities are consolidated rather than re-proposed.

## Traceability
- Source/analysis: [`rtr-production-improvement-opportunity-space.xlsx`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/sources/transport/rtr-production-improvement-opportunity-space.xlsx&version=GBmain) (functional block Transport, WS1/WS2; Transport workbook mapping sheets and review log)
- Problem: [`misalignment-with-ramboll-enterprise-architecture`](../problems/misalignment-with-ramboll-enterprise-architecture.md)
- Realising capabilities: none recorded
- Architecture: see [`../views/architecture-overview.md`](../views/architecture-overview.md) (candidate layers; no approved component assignment yet)
- Verification: Every accepted opportunity in a review round cites the existing practices and initiatives it was compared against.

## Open questions
- No architecture component or decision is assigned to this requirement yet; promotion to
  `in-review` requires a review that also records the realising capability relations in the
  capability records themselves.
