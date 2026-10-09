---
type: solution-candidate
title: SharePoint Lists as a state and projection layer
description: Use Microsoft Lists as a structured, event-enabled data and projection layer, never as the workflow engine or decision maker.
tags: [solution-candidate, sharepoint, m365, projection, draft]
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
      target: solution-candidates/backend-controlled-workflow-engine
---

# SharePoint Lists as a state and projection layer

## Candidate
> In the hybrid model, SharePoint Lists act as the structured, event-enabled data layer (deliveries, relationships, checklist), while the backend is the decision-maker. Use a "RequestedState vs ActualState" pattern and controlled edit model so users propose changes the backend validates and enforces.

## Source
**Answers 2–4** in [`../sources/ramboll/event-driven work management system.md`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/sources/ramboll/event-driven%20work%20management%20system.md&version=GBmain).

## Addressed problems / capabilities
- Supports governance/approval friction reduction and event-driven automation.

## Open questions
- Read-only vs controlled-edit balance depends on UX maturity phase.
