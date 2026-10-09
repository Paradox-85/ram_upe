---
type: requirement
title: New projects are initialized from a class-based template
description: "A project is created by selecting its class/category, and the environment, tools, templates and initial access are provisioned consistently from that class."
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

# New projects are initialized from a class-based template

## Statement
> A project is created by selecting its class/category, and the environment, tools, templates and initial access are provisioned consistently from that class.

## Rationale
Removes per-project manual setup and is the precondition for a consistent project start across GBAs.

## Traceability
- Source/analysis: [`UPE_Functional_Blocks_v1.md`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/sources/legacy/docs/UPE_Functional_Blocks_v1.md&version=GBmain) (functional block 1.1; use-case: initialize-project-from-class-template)
- Problem: none recorded
- Realising capabilities: [`ability-to-select-project-type-from-portfoliotaxonomy`](../capabilities/ability-to-select-project-type-from-portfoliotaxonomy.md), [`ability-to-apply-templates-to-new-projects`](../capabilities/ability-to-apply-templates-to-new-projects.md)
- Architecture: see [`../views/architecture-overview.md`](../views/architecture-overview.md) (candidate layers; no approved component assignment yet)
- Verification: Create a project from each defined class and confirm the provisioned environment matches the class definition.

## Open questions
- No architecture component or decision is assigned to this requirement yet; promotion to
  `in-review` requires a review that also records the realising capability relations in the
  capability records themselves.
