---
type: solution-candidate
title: Backend-controlled workflow engine
description: A backend (Azure) owns workflow state machines, transition rules, and side effects, while other layers project into M365.
tags: [solution-candidate, workflow, backend, azure, draft]
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
    - type: supports
      target: events/delivery-state-transitioned
---

# Backend-controlled workflow engine

## Candidate
> Represent workflow as a state machine (states/transitions) stored in the backend (DB/config), and let the backend validate and enforce every transition. **Option A (recommended)** in the source separates workflow logic (backend) from data (Lists/DB) and UX (Teams/add-ins).

## Source
**Answer 1 / Answer 2 (Option A)** in [`raw-input/knowledge-base/raw-input/event-driven work management system.md`](../raw-input/knowledge-base/raw-input/event-driven%20work%20management%20system.md).

## Addressed problems / capabilities
- Backs capability to track deliverable status and enforce approvals.

## Open questions
- Exact state machine and rules require further specification.
