---
type: navigation
title: Requirements — Collection Contract
description: "Contract for the requirements collection: the first-class traceability layer between evidence, problems, capabilities and architecture. Defines requirement kinds, the traceability chain, and the record template."
tags: [requirements, traceability, contract, governance, draft]
sources: []
generated: 2026-10-09T10:40:47Z
verified: false
status: draft
stale_after: 2027-10-09
upe:
  lifecycle: draft
  owner: "@chief-architect"
  relations:
    - type: supports
      target: governance/operating-model
---

# Requirements — Collection Contract

Requirements are a **first-class canonical concept**: the layer that connects what the business
asked for to what UPE is designed to do.

```text
Source → Problem / Pain → Requirement → Capability → Architecture feature/component → Decision → Lab / Implementation → Evidence
```

## Identity

Requirement identity is the **OKF path-as-ID** (`requirements/<slug>` minus `.md`).
No `REQ-*` scheme is introduced: governance principle §6 permits `upe.id` only for existing DDDM
stable ids (`M01`–`M14`, `ADR-*`). See `## Open questions` in `governance/principles.md`.

## Kinds (metadata, not directories)

```yaml
requirement:
  kind: functional        # business | functional | non-functional | stakeholder | constraint
  priority: must          # must | should | could  (optional)
```

| Kind | Meaning |
|---|---|
| `business` | a business outcome or value the organisation requires |
| `functional` | behaviour the platform must exhibit |
| `non-functional` | quality attribute: performance, security, scalability, usability |
| `stakeholder` | a need voiced by a named stakeholder or GBA |
| `constraint` | a boundary we must work within (technology, licence, standard, funding) |

## Record template

```yaml
---
type: requirement
title: <imperative short title>
description: <one paragraph, testable where possible>
tags: [requirement, <topic>, draft]
sources:
  - ../sources/transport/2026-10-09-....xlsx        # required evidence
generated: 2026-10-09T00:00:00Z
verified: false
status: draft
stale_after: 2027-10-09
upe:
  lifecycle: draft
  owner: "@chief-architect"
  relations:
    - type: derived-from
      target: <source or analysis path>
    - type: derived-from
      target: problems/<related problem>
requirement:
  kind: functional
---

# <Title>

## Statement
> <the requirement, stated once, in reviewable language>

## Rationale
<why this is required; what breaks without it>

## Traceability
- Source/analysis: [...]
- Problem: [...]
- Realising capabilities: [...]
- Architecture: [...]
- Verification: <how we would demonstrate it is met>

## Open questions
```

## Rules

1. **Draft only.** New requirements are `status: draft`, `upe.lifecycle: idea|draft`. Promotion
   to `in-review`/`approved` is a gated human decision and is not performed by agents.
2. **Every requirement is source-backed.** No `sources:` → not promotable.
3. **One statement per record.** Do not bundle related-but-distinct needs.
4. **Do not invent requirements.** Extract from evidence or record a reviewed analysis finding;
   never synthesize a requirement to fill out a matrix.
5. **Traceability uses the existing minimal relation vocabulary** (`supports`, `derived-from`,
   `evidenced-by`, `refutes`). Capability records point *at* requirements with `supports`; a
   requirement points *from* its evidence with `derived-from`. No new relation types.
6. **Preserve disagreement.** Conflicting source claims become separate records or an
   `## Open questions` entry — never a silent reconciliation.

Contract owner: `@chief-architect`. See [`../governance/operating-model.md`](../governance/operating-model.md).
