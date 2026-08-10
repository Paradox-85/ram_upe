---
type: event
title: Delivery blocked by dependency
description: A delivery cannot progress because a dependency is incomplete, and the team is notified.
tags: [event, dependency, blocker, notification, draft]
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

# Delivery blocked by dependency

## Event
> When a delivery's dependency is not complete, the transition is blocked. A bot/notification posts to Teams, e.g. "⚠️ Delivery A blocked by B".

## Trigger sources
- Dependency resolution at transition time
- Cross-discipline model update that marks dependent deliveries "needs recheck"

## Source
**Answer 1 (Notifications)** and **Answer 1 (cross-discipline logic)** in [`raw-input/knowledge-base/raw-input/event-driven work management system.md`](../raw-input/knowledge-base/raw-input/event-driven%20work%20management%20system.md).

## Open questions
- Which notifications are surfaced vs. suppressed (fatigue) is open.
