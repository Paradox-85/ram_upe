---
type: governance
title: Governance — Principles
description: KB-first operating principles for the Unified Project Execution knowledge bundle, including evidence immutability, draft-only scope, contradiction handling, identity rules and the hybrid human/AI operating model.
tags: [governance, principles, okf, ddd, kb-first, operating-model]
sources:
  - ../sources/ramboll/DDD.md
  - ../sources/legacy/knowledge-base/00_principles.md
generated: 2026-08-10T07:48:05Z
verified: false
status: draft
stale_after: 2027-08-10
upe:
  lifecycle: draft
  owner: "@chief-architect"
  relations:
    - type: supports
      target: index
---

# Governance Principles

> Attribution: structure/conventions adopted from `GoogleCloudPlatform/knowledge-catalog/okf` (Apache-2.0); no upstream content copied. See `../log.md`.

## 1. KB-first

- All canonical current knowledge lives in `knowledge-base/`. Derived documents (reports, views, summaries, diagrams) never override their KB inputs.
- Update the KB before changing derived documentation.
- No other directory may introduce a canonical architectural fact. `sources/`, `analysis/`, `reports/`, `labs/` and `.pi/` may hold evidence, work and presentation — never canonical knowledge.

## 2. Evidence immutability

- `sources/**` is immutable evidence. Never edit a payload — not to fix links, not to rename the legacy product, not to reconcile references. Supersede it with a new dated file instead.
- Provenance is preserved: the paths recorded by canonical records are the source references for those records.
- The legacy corpus migrated out of `knowledge-base/raw-input/` (2026-10-09) keeps its original bytes; only its location and the referencing paths changed.

## 3. Draft-only scope (this cycle)

- All newly created concepts are `status: draft` (OKF projection) with `upe.lifecycle: idea|draft`.
- No promotion to `in-review` or `approved` is performed without an explicit human decision. Existing historical `approved` raw files are not edited.

## 4. Source contradiction handling

- Conflicting source claims are preserved as **separate statements/records** with individual source attribution and `upe.lifecycle: draft`.
- Contradictions are never silently reconciled. Unresolved wordings are recorded in the concept body under `## Open questions`.

## 5. Minimal relation vocabulary

- Typed relations are restricted to: `supports`, `derived-from`, `evaluates`, `evidenced-by`, `refutes`, `decided-by`, `supersedes`, `derived-document-of`.
- DDD context-map edge taxonomy is **not** introduced in this cycle; M01–M14 remain candidate functional domains.
- New concept types (e.g. `requirement`) reuse this vocabulary rather than extending it.

## 6. Identity

- OKF path-as-ID: a concept's identity is its file path without the `.md` suffix.
- `upe.id` is set only when an existing DDDM stable ID applies (e.g. `M01`–`M14`, `ADR-0001`); no new stable-ID scheme is invented. This is why `requirements/`, `evidence/` and `views/` records are identified by path and carry no `REQ-*`/`SRC-*` number.

## 7. Hybrid human/AI operating model

- There is **one** canonical KB with **two** analysis workflows (human and AI) feeding it through one review and promotion gate. There is no separate machine truth and no separate human truth.
- Analysis (`analysis/**`) is non-canonical in every case — including human-written analysis. Sources do not become knowledge by proximity; AI output is candidate knowledge, never authority.
- Promotion is per finding, decided by humans, and recorded on both sides (the KB record cites its `sources:`; the analysis records `promoted:`).
- Analysis uses its own lifecycle (`working → review-ready → reviewed → superseded`) and never the canonical one.
- Agents must not approve requirements or architecture, mark an ADR accepted, change approved domain boundaries, or promote analysis into the KB.

Full model: [`operating-model.md`](operating-model.md).

## Open questions

- **Stable IDs for new concept types.** The UPE refactoring brief proposed `SRC-*` source-reference numbers (and requirement numbers by implication). That conflicts with §6, so path-as-ID is used instead. Introducing a formal `SRC-*`/`REQ-*` scheme is an ontology change and requires explicit approval.
- **Master Architecture scope.** `architecture/master.md` is designated the primary human-readable integration view over governed architecture state; whether additional component/contract records become canonical in this cycle is unresolved.
- **Domain boundary status.** M01–M14 remain candidate functional domains; none is a proven bounded context.
