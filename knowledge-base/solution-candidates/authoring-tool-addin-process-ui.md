---
type: solution-candidate
title: Authoring-tool add-in with process-aware UI
description: Embed a process-aware add-in inside authoring tools (Revit/CAD) that lets users complete checks, request approval, and view dependencies in-context.
tags: [solution-candidate, authoring-tool, add-in, ux, draft]
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
      target: capabilities/ability-to-embed-validation-in-design-tools-revit-etc
---

# Authoring-tool add-in with process-aware UI

## Candidate
> Each authoring tool carries an add-in with a process-aware UI based on the same process state baked into the model. The add-in displays process state, lets users mark checks, raise approval requests (via API to a backend service), and view dependencies.

## Source
**Prompt 1 / Answer 1 (Authoring tool integration)** in [`raw-input/knowledge-base/raw-input/event-driven work management system.md`](../raw-input/knowledge-base/raw-input/event-driven%20work%20management%20system.md).

## Addressed problems / capabilities
- Supports in-context capability to embed validation in design tools.

## Open questions
- Add-in build/toolchain per authoring tool is not specified.
