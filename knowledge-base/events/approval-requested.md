---
type: event
title: Approval requested
description: An author or designer raises an approval request for a delivery, creating an approval step and routing it for review.
tags: [event, approval, workflow, draft]
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
      target: capabilities/ability-to-configure-approval-workflows-for-project-artifacts
---

# Approval requested

## Event
> A user requests approval for a delivery (from an add-in or Teams). The backend validates the checklist/dependencies, creates an approval item, transitions state, and triggers a Teams notification.

## Trigger sources
- Add-in "Request Approval" action (API call)
- Teams interaction

## Source
**Answers 1–2** in [`../sources/ramboll/event-driven work management system.md`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/sources/ramboll/event-driven%20work%20management%20system.md&version=GBmain).

## Open questions
- Approval SLA and routing rules not exhaustively captured.
