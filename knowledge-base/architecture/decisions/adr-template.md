---
type: decision
title: ADR Template
description: Template for Architecture Decision Records with standard sections (Context, Options, Decision, Consequences) and conforming draft frontmatter.
tags: [architecture, decisions, adr, template, draft]
sources: []
generated: 2026-08-10T07:48:05Z
verified: false
status: draft
stale_after: 2027-08-10
upe:
  lifecycle: draft
  owner: "@chief-architect"
  relations: []
---

# ADR-0000 — Title

> Copy this template for a new decision. Keep `status: draft`; never promote to `approved` in this cycle.

## Frontmatter
```yaml
---
type: decision
title: ADR-0000 — <title>
upe:
  id: ADR-
  lifecycle: idea|draft
  owner: "@chief-architect"
  relations: []
description: <one-line>
tags: [architecture, decisions, adr]
sources:
  - <raw source path, if any>
generated: <ISO-8601>
verified: false
status: draft
stale_after: <generated + 1y>
---
```

## Context
Describe the background and why a decision is needed.

## Options
- **Option A** — ...
- **Option B** — ...

## Decision
State the chosen option and rationale.

## Consequences
List expected consequences, trade-offs, and follow-ups.

## Evidence
Raw/source links backing the decision (bundle-relative).

## Status
Draft (this cycle: no promotion to approved).

## Open questions
- ...
