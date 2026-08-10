---
type: event
title: Data change detected in a project system
description: A data change in a linked system is detected and used to trigger workflow automation, per the event-driven automation capabilities.
tags: [event, automation, event-driven, draft]
sources:
  - raw-input/docs/UPE_Functional_Blocks_v1.md
generated: 2026-08-10T07:48:05Z
verified: false
status: draft
stale_after: 2027-08-10
upe:
  lifecycle: idea
  owner: "@chief-architect"
  relations:
    - type: derived-from
      target: raw-input/docs/UPE_Functional_Blocks_v1.md
    - type: supports
      target: capabilities/ability-to-detect-data-changes
---

# Data change detected in a project system

## Event
> A data change in a project system is detected (event detection) and can trigger workflows based on event rules, cascading through related entities.

## Trigger sources
- Data change in a source system
- Event rule match

## Source
Functional block **8.3 Event-Driven Automation** in [`raw-input/docs/UPE_Functional_Blocks_v1.md`](../raw-input/docs/UPE_Functional_Blocks_v1.md).

## Open questions
- Event-rule vocabulary and cascade depth not fully specified.
