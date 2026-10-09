---
type: use-case
title: Track a delivery through its workflow lifecycle
description: A delivery artifact (model, drawing, report) progresses through checklist steps and approvals so its state is visible to the team.
tags: [use-case, workflow, delivery, event-driven, draft]
sources:
  - ../sources/ramboll/event-driven work management system.md
generated: 2026-08-10T07:48:05Z
verified: false
status: draft
stale_after: 2027-08-10
upe:
  lifecycle: idea
  owner: "@chief-architect"
  relations:
    - type: derived-from
      target: ../sources/ramboll/event-driven work management system.md
    - type: supports
      target: events/delivery-state-transitioned
    - type: supports
      target: capabilities/ability-to-track-deliverable-status-not-started-in-progress-complete
---

# Track a delivery through its workflow lifecycle

## Use case
> A delivery relates to one or more disciplines; depending on its type it is the object of a process involving a checklist and, in some cases, a workflow describing the lifecycle from creation to delivery — including self-checks, cross-discipline checks, and approvals. The system persists the delivery's state during its lifecycle.

## Primary actor
Designer/author + Project Manager (observability).

## Supporting capability
- Ability to track deliverable status (not started, in progress, complete, delivered)

## Source
**Prompt 1** in [`../sources/ramboll/event-driven work management system.md`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/sources/ramboll/event-driven%20work%20management%20system.md&version=GBmain).

## Open questions
- Checklist variant rules per delivery type not fully enumerated.
