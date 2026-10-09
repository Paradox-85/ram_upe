---
type: requirement
title: Access is role-based and scoped to project membership
description: "Permissions are derived from a member's role within a specific project, so the same person can hold different rights in different projects."
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
      target: problems/governance-and-approval-process-friction
requirement:
  kind: functional
---

# Access is role-based and scoped to project membership

## Statement
> Permissions are derived from a member's role within a specific project, so the same person can hold different rights in different projects.

## Rationale
Membership-scoped roles are the mechanism that keeps authoring-tool and CDE permissions aligned with project reality.

## Traceability
- Source/analysis: [`UPE_Functional_Blocks_v1.md`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/sources/legacy/docs/UPE_Functional_Blocks_v1.md&version=GBmain) (functional block 2.3; functional block heading)
- Problem: [`governance-and-approval-process-friction`](../problems/governance-and-approval-process-friction.md)
- Realising capabilities: [`ability-to-assign-user-roles-within-project-context`](../capabilities/ability-to-assign-user-roles-within-project-context.md), [`ability-to-establish-role-based-access-control-rbac`](../capabilities/ability-to-establish-role-based-access-control-rbac.md), [`ability-to-provision-access-control-rules-for-folderspermissions`](../capabilities/ability-to-provision-access-control-rules-for-folderspermissions.md), [`ability-to-apply-discipline-specific-tool-access-rules`](../capabilities/ability-to-apply-discipline-specific-tool-access-rules.md)
- Architecture: see [`../views/architecture-overview.md`](../views/architecture-overview.md) (candidate layers; no approved component assignment yet)
- Verification: Verify that role changes propagate to tool/CDE permissions for that project only.

## Open questions
- No architecture component or decision is assigned to this requirement yet; promotion to
  `in-review` requires a review that also records the realising capability relations in the
  capability records themselves.
