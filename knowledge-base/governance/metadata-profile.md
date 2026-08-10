---
type: governance
title: Metadata Profile
description: "Single metadata authority for the Unified Project Execution knowledge bundle - OKF fields, the upe extension, lifecycle, status projection, type dictionary, and typed relations."
tags: [governance, metadata, okf, contract, lifecycle]
sources:
  - raw-input/knowledge-base/00_principles.md
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
| `sources` | yes | raw source paths backing this record (bundle-relative) |
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

## 4. Status projection (OKF)
`OKF status` is a **projection** of the lifecycle, restricted to `draft | stable | deprecated`.
- New records use `status: draft`.
- **No `approved`** is assigned in this cycle. A separate `upe.lifecycle` value must not contradict `status`.

## 5. Type dictionary
Concept types (DDD): `domain`, `subdomain`, `capability`, `problem`, `use-case`, `event`, `solution-candidate`, `module`.
Structural/record types: `governance`, `architecture`, `decision`, `lab`, `navigation`, `log`.
`module` is used only for a solution candidate where a recurring explicit module pattern is evidenced.

## 6. Typed relations (minimal vocabulary)
`supports`, `derived-from`, `evaluates`, `evidenced-by`, `refutes`, `decided-by`, `supersedes`, `derived-document-of`.
Relations are stored as `{type, target}` with bundle-relative targets. No DDD context-map edge taxonomy in this cycle.

## 7. Identity
- OKF path-as-ID: concept identity = file path without `.md`.
- Links are bundle-relative Markdown links.
