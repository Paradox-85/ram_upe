---
type: event
title: Automated action executed in response to an event
description: An automated action runs in response to a detected event, with an audit trail, notifications, and escalations.
tags: [event, automation, audit, draft]
sources:
  - ../sources/legacy/docs/UPE_Functional_Blocks_v1.md
generated: 2026-08-10T07:48:05Z
verified: false
status: draft
stale_after: 2027-08-10
upe:
  lifecycle: idea
  owner: "@chief-architect"
  relations:
    - type: derived-from
      target: ../sources/legacy/docs/UPE_Functional_Blocks_v1.md
---

# Automated action executed in response to an event

## Event
> The platform executes an automated action in response to a detected event, maintaining an audit trail and supporting notifications and escalations.

## Trigger sources
- Detected event (data change / rule match / cascade)

## Source
Functional block **8.3 Event-Driven Automation (Automated Actions)** in [`../sources/legacy/docs/UPE_Functional_Blocks_v1.md`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/sources/legacy/docs/UPE_Functional_Blocks_v1.md&version=GBmain).

## Open questions
- Audit-trail granularity for automated actions is open.
