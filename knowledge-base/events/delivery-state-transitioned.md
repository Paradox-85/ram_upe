---
type: event
title: Delivery state transitioned
description: A delivery artifact transitions to a new workflow state as checklist steps and approvals are completed.
tags: [event, workflow, delivery, draft]
sources:
  - raw-input/knowledge-base/raw-input/event-driven work management system.md
generated: 2026-08-10T07:48:05Z
verified: false
status: draft
stale_after: 2027-08-10
upe:
  lifecycle: idea
  owner: "@chief-architect"
  relations:
    - type: derived-from
      target: raw-input/knowledge-base/raw-input/event-driven work management system.md
---

# Delivery state transitioned

## Event
> A delivery changes state (e.g. from `SelfCheck` to `Review`), typically when checklist items are completed and validated by the backend. The system updates the SharePoint List and can trigger follow-on actions/notifications.

## Trigger sources
- Checklist item completed
- API-triggered transition request

## Source
**Answer 1 (Event pipeline / example)** in [`raw-input/knowledge-base/raw-input/event-driven work management system.md`](../raw-input/knowledge-base/raw-input/event-driven%20work%20management%20system.md).

## Open questions
- Full state machine (states/transitions) not yet standardized.
