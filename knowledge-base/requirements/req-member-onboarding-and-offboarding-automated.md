---
type: requirement
title: Member onboarding and offboarding are automated
description: "Adding a member to a project grants the required tools and services access without manual ticket chains, and removal records the offboarding date and revokes access."
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

# Member onboarding and offboarding are automated

## Statement
> Adding a member to a project grants the required tools and services access without manual ticket chains, and removal records the offboarding date and revokes access.

## Rationale
Access administration is a recurring, error-prone manual activity and a security exposure when revocation is delayed.

## Traceability
- Source/analysis: [`UPE_Functional_Blocks_v1.md`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/sources/legacy/docs/UPE_Functional_Blocks_v1.md&version=GBmain) (functional block 2.1 / 2.2; functional block heading)
- Problem: none recorded
- Realising capabilities: [`ability-to-add-users-to-project-team`](../capabilities/ability-to-add-users-to-project-team.md), [`ability-to-log-offboarding-date-and-reason`](../capabilities/ability-to-log-offboarding-date-and-reason.md), [`ability-to-assign-initial-project-stakeholdersroles`](../capabilities/ability-to-assign-initial-project-stakeholdersroles.md)
- Architecture: see [`../views/architecture-overview.md`](../views/architecture-overview.md) (candidate layers; no approved component assignment yet)
- Verification: Onboard and offboard a member and confirm granted/revoked access and the recorded offboarding metadata.

## Open questions
- No architecture component or decision is assigned to this requirement yet; promotion to
  `in-review` requires a review that also records the realising capability relations in the
  capability records themselves.
