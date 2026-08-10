---
type: use-case
title: Raise an approval request from an authoring tool add-in
description: A designer, inside Revit/CAD, clicks "Request Approval" in a process-aware add-in, invoking a backend API and triggering the approval workflow.
tags: [use-case, approval, authoring-tool, add-in, draft]
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
      target: events/approval-requested
    - type: evaluates
      target: solution-candidates/authoring-tool-addin-process-ui
---

# Raise an approval request from an authoring tool add-in

## Use case
> The UI in each authoring tool allows users to mark checks and raise approval requests via an API call to a backend service. In Revit/CAD, the designer clicks "Request Approval"; the backend validates the checklist, transitions state, creates the approval item, updates the SharePoint List, and triggers a Teams notification.

## Primary actor
Designer (inside the authoring tool).

## Source
**Prompt 1 / Answer 1** in [`raw-input/knowledge-base/raw-input/event-driven work management system.md`](../raw-input/knowledge-base/raw-input/event-driven%20work%20management%20system.md).

## Open questions
- Approval routing and reviewer-queue rules not exhaustively specified.
