---
type: governance
title: Glossary — Ubiquitous Language
description: Canonical DDD and UPE terminology (ubiquitous language) for the Unified Project Execution knowledge bundle, with bounded-context scope notes.
tags: [governance, glossary, ddd, ubiquitous-language, upe]
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

# Glossary (Ubiquitous Language)

Definitions use the **Unified Project Execution** (UPE) product context.

## DDD terms
- **Domain** — an area of the UPE knowledge/business space modelled for a purpose. This bundle models **functional domains**, which are groupings, not implementation units.
- **Capability** — a discrete ability the system or organization can perform, stated as an individual, source-backed statement (a normalized "Ability to …").
- **Problem** — a pain point or gap surfaced in evidence that UPE is expected to address.
- **Use case** — a user/system interaction scenario describing an outcome; links to capabilities/events where the source supports it.
- **Event** — a business event: a notable state change or trigger within UPE workflows.
- **Bounded context** — a DDD term for a decoupled modelling boundary with explicit consistency. **Not proven for M01–M14 in this cycle:** the domain records are *candidate functional domains*, not bounded contexts.
- **Solution candidate** — a candidate solution/module or recurring pattern proposed to address a problem/capability; `type: module` is used only when a recurring explicit module pattern is evidenced.
- **Ubiquitous language** — a shared, consistent vocabulary used by domain experts and design/model, defined here and in `terminology-aliases.md`.

## UPE terms
- **UPE = Unified Project Execution** — Ramboll's enterprise digital backbone (a coordination and intelligence layer). Legacy spelling "Unified Production Environment" appears only in raw verbatim sources.
- **ADR** — Architecture Decision Record; a structured record of an architecture decision (Context, Options, Decision, Consequences).
- **Module** — a candidate implementation grouping; in this bundle only represented as `type: module` solution candidates when a recurring explicit module pattern is evidenced.
- **OKF** — Open Knowledge Framework; the structure/conventions adopted from `GoogleCloudPlatform/knowledge-catalog/okf` (Apache-2.0).
- **DDDM** — Dialogue-Driven Design Method; the LLM-native design method (Markdown+Mermaid+Git, stable IDs, lifecycle).
- **Requirement** — a first-class canonical statement of what the business or platform needs, classified by `requirement.kind` (`business`, `functional`, `non-functional`, `stakeholder`, `constraint`). It is the traceability layer between evidence/problems and capabilities.
- **Source** — a received evidence payload under `sources/`. A source is **not** knowledge: it supports knowledge.
- **Source reference** — a canonical KB record (`evidence/src-*`, `type: source-reference`) holding *metadata about* a source: location, revision, hash, origin. Not to be confused with the payload itself.
- **Analysis** — what a human or an AI concluded from sources. Always **non-canonical**; lives in `analysis/`. Human and AI analysis have identical standing.
- **Promotion gate** — the human review step that turns a specific *finding* into canonical knowledge. Promotion is per finding, never per document, and never automatic.
- **View** — a generated or curated, explicitly **non-authoritative** projection of canonical records (e.g. `views/capability-map.md`). A view renders records; it never overrides them.
- **Report** — an audience-facing deliverable under `reports/`. Also non-canonical: a report references knowledge or analysis and cannot create it.
- **Master Architecture** — the current governed architectural state (accepted decisions, contexts, capabilities, components, interfaces, relationships). `architecture/master.md` is its primary human-readable *view*, not the authority itself.

## Scope notes
- `bounded context` is **unproven** for M01–M14; do not treat candidate domains as bounded contexts without explicit evidence.
- See [`terminology-aliases.md`](terminology-aliases.md) for legacy/ambiguous spellings.
