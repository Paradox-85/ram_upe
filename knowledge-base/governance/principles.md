---
type: governance
title: Governance — Principles
description: KB-first operating principles for the Unified Project Execution knowledge bundle.
tags: [governance, principles, okf, ddd, kb-first]
sources:
  - raw-input/DDD.md
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

# Governance Principles

> Attribution: structure/conventions adopted from `GoogleCloudPlatform/knowledge-catalog/okf` (Apache-2.0); no upstream content copied. See `../log.md`.

## 1. KB-first
- All canonical current knowledge lives in `knowledge-base/`. Derived documents (reports, summaries, diagrams) never override their KB inputs.
- Update the KB before changing derived documentation.

## 2. Raw immutability
- `knowledge-base/raw-input/**` is immutable evidence. Never edit raw payloads — even to fix links, the legacy product name, or internal references.
- Raw provenance is preserved; the post-move raw paths are the source references for concept records.

## 3. Draft-only scope (this cycle)
- All newly created concepts are `status: draft` (OKF projection) with `upe.lifecycle: idea|draft`.
- No promotion to `in-review` or `approved` is performed in this deployment. Existing historical `approved` raw files are not edited.

## 4. Source contradiction handling
- Conflicting source claims are preserved as **separate statements/records** with individual source attribution and `upe.lifecycle: draft`.
- Contradictions are never silently reconciled. Unresolved wordings are recorded in the concept body under `## Open questions`.

## 5. Minimal relation vocabulary
- Typed relations are restricted to: `supports`, `derived-from`, `evaluates`, `evidenced-by`, `refutes`, `decided-by`, `supersedes`, `derived-document-of`.
- DDD context-map edge taxonomy is **not** introduced in this cycle; M01–M14 remain candidate functional domains.

## 6. Identity
- OKF path-as-ID: a concept's identity is its file path without the `.md` suffix.
- `upe.id` is set only when an existing DDDM stable ID applies (e.g. `M01`–`M14`, `ADR-0001`); no new stable-ID scheme is invented.
