---
type: governance
title: Metadata Profile
description: "Single metadata authority for the Unified Project Execution knowledge bundle - OKF fields, the upe extension, lifecycle, status projection, type dictionary, and typed relations."
tags: [governance, metadata, okf, contract, lifecycle]
sources:
  - ../sources/legacy/knowledge-base/00_principles.md
generated: 2026-08-10T07:48:05Z
verified: false
status: draft
stale_after: 2027-08-10
upe:
  lifecycle: draft
  owner: "@chief-architect"
  relations: []
---

# Metadata Profile

> Attribution: structure/conventions adopted from `GoogleCloudPlatform/knowledge-catalog/okf` (SPEC v0.2, Apache-2.0); no upstream content copied.

This is the **single metadata authority** for the bundle. Structure/conventions follow OKF; the `upe:` block is the minimal UPE extension.

## 1. OKF frontmatter fields (required unless noted)
| Field | Required | Allowed / notes |
|---|---|---|
| `type` | yes | see Type dictionary below |
| `title` | yes | short title |
| `description` | yes | one-paragraph description |
| `tags` | yes | keywords |
| `sources` | yes | evidence paths backing this record: `../sources/...` (payloads now live outside the bundle) or a bundle-relative KB record path (e.g. `evidence/src-...`) |
| `generated` | yes | ISO-8601 creation timestamp |
| `verified` | yes | `true`/`false` |
| `status` | yes | see Status projection |
| `stale_after` | yes | ISO-8601 after which the record is considered stale |

## 2. `upe:` extension (minimal)
| Field | Meaning |
|---|---|
| `upe.id` | set only when an existing DDDM stable ID applies (e.g. `M01`–`M14`, `ADR-0001`). Never invent a new scheme. |
| `upe.lifecycle` | DDDM authoritative lifecycle phase (see below) |
| `upe.owner` | responsible owner (e.g. `@chief-architect`) |
| `upe.relations` | list of `{type, target}` records (see relations) |

## 3. Lifecycle (authoritative, DDDM)
`idea → draft → in-review → approved → superseded → deprecated`

- This is the **authoritative** lifecycle sequence.
- In this cycle only `idea` and `draft` are used for new content.

### 3.1 Analysis lifecycle (separate — do not reuse the canonical sequence)

`working → review-ready → reviewed → superseded`

- Applies to artifacts under `analysis/**` only. Analysis is never `approved`.
- The canonical KB lifecycle above is **not** applied to analysis, reports, sources or labs.
- Promotion from analysis to the KB creates a *new* KB record carrying the canonical lifecycle; the
  analysis artifact records the outcome in its own `promoted:` field. See
  [`operating-model.md`](operating-model.md).
## 4. Status projection (OKF)
`OKF status` is a **projection** of the lifecycle, restricted to `draft | stable | deprecated`.
- New records use `status: draft`.
- **No `approved`** is assigned in this cycle. A separate `upe.lifecycle` value must not contradict `status`.

## 5. Type dictionary
Concept types (DDD): `domain`, `subdomain`, `capability`, `problem`, `use-case`, `event`, `solution-candidate`, `module`, `requirement`.
Structural/record types: `governance`, `architecture`, `decision`, `lab`, `navigation`, `log`, `view`, `source-reference`.
`module` is used only for a solution candidate where a recurring explicit module pattern is evidenced.
`requirement` is the first-class traceability layer between evidence, problems, capabilities and architecture (kinds in §8).
`source-reference` is canonical metadata *about* a received source; the payload itself lives in `sources/` and is not canonical (see §9).
`view` is a generated or curated, explicitly **non-authoritative** projection of canonical records, living in `views/`.
Types used **outside** the bundle and therefore never canonical: `analysis` (`analysis/**`) and `report` (`reports/**`). Their lifecycle is in §3.1.

## 6. Typed relations (minimal vocabulary)
`supports`, `derived-from`, `evaluates`, `evidenced-by`, `refutes`, `decided-by`, `supersedes`, `derived-document-of`.
Relations are stored as `{type, target}`. Targets are bundle-relative concept paths, or paths pointing outside the bundle when the relation refers to evidence (e.g. `../sources/...`). No DDD context-map edge taxonomy in this cycle.

## 7. Identity
- OKF path-as-ID: concept identity = file path without `.md`.
- Links are bundle-relative Markdown links.

## 8. `requirement:` extension

```yaml
requirement:
  kind: functional        # business | functional | non-functional | stakeholder | constraint
  priority: must          # optional: must | should | could
```

Requirements are identified by path (§7) — no `REQ-*` scheme. Traceability uses §6 relations only:
a requirement points at its evidence with `derived-from`; capability records point at the
requirement with `supports`. Contract: [`../requirements/requirements-guide.md`](../requirements/requirements-guide.md).

## 9. `source:` extension (source-reference records)

```yaml
source:
  source_type: spreadsheet   # spreadsheet | document | transcript | standard | vendor-doc | diagram | presentation
  location: sources/transport/2026-10-09-....xlsx
  revision: "as received 2026-10-09"
  hash: sha256:...
  received: 2026-10-09
  origin: <who sent it>
```

A source-reference record is canonical **metadata about** a payload; the payload in `sources/` is
not canonical. Identified by path (§7) — no `SRC-*` scheme (see
[`principles.md`](principles.md) → Open questions). Contract:
[`../evidence/evidence-guide.md`](../evidence/evidence-guide.md).
