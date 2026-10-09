---
type: navigation
title: Evidence — Source Reference Contract
description: "Contract for source-reference records: canonical metadata about a received source (location, revision, hash), kept separate from the evidence payload itself."
tags: [evidence, provenance, source-reference, contract, draft]
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

# Evidence — Source Reference Contract

## Record vs payload

| | Source **record** (here) | Source **payload** |
|---|---|---|
| What | canonical metadata *about* a source | the received file itself |
| Where | `knowledge-base/evidence/src-*.md` | `sources/<topic>/…` |
| Canonical? | yes — a governed KB record | no — evidence, stored for traceability |
| Identity | OKF path-as-ID (`evidence/src-*`) | filesystem path |

A source record answers: *what did we receive, from where, which revision, and is it still the
current one?* It lets a concept cite a stable KB record instead of a fragile filesystem path.

## Record template

```yaml
---
type: source-reference
title: <what the source is>
description: <origin, scope and why it matters>
tags: [source-reference, <topic>, draft]
sources:
  - ../sources/transport/2026-10-09-....xlsx
generated: 2026-10-09T00:00:00Z
verified: false
status: draft
stale_after: 2027-10-09
upe:
  lifecycle: draft
  owner: "@chief-architect"
  relations: []
source:
  source_type: spreadsheet        # spreadsheet | document | transcript | standard | vendor-doc | diagram | presentation
  location: sources/transport/2026-10-09-....xlsx
  revision: "as received 2026-10-09"
  hash: sha256:0000…              # recorded at intake
  received: 2026-10-09
  origin: <who/which unit sent it>
---

# <Title>

## What this source is
## Provenance and handling
## Concepts derived from it
```

## Rules

1. **`sources:` must resolve** — enforced by `tools/kb-validate/check_sources.py`.
2. **Record the hash at intake.** If the payload's hash changes, that is a *new* revision →
   a new payload file and a new record; never edit the old one.
3. **Identity is path-based.** No `SRC-*` numbering scheme is introduced: governance
   principle §6 forbids inventing new stable-id schemes. If a formal `SRC-*` vocabulary is
   wanted later, that is an ontology change requiring explicit approval (tracked in
   `../log.md`).
4. **Records are metadata, not copies.** Never paste the payload's content here.
5. **Supersession is explicit**: use the `supersedes` relation and set
   `upe.lifecycle: superseded` — never delete an evidence record.

Contract owner: `@chief-architect`. See [`../governance/operating-model.md`](../governance/operating-model.md).
