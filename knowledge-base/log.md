---
type: log
title: Knowledge Base Change Log
description: Change log for the Unified Project Execution knowledge bundle, recording migration and creation batches and OKF attribution.
tags: [log, changelog, okf, upe]
status: draft
stale_after: 2027-08-10
upe:
  lifecycle: draft
  owner: "@chief-architect"
  relations: []
---

# Change Log

> **Attribution:** structure/conventions adopted from [`GoogleCloudPlatform/knowledge-catalog/okf`](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) (SPEC v0.2) under **Apache-2.0**. No upstream content was copied. Only structure and conventions are adopted.

Record of batches as the bundle was deployed (harness `20260810-074805-upe-harmonization`). **Status:** draft; log entries track mutations in creation order.

## 2026-08-10 — bundle deployment
1. **Raw migration.** Moved 73 tracked artifacts (legacy `knowledge-base/**`, `docs/**`, `src/**`, `prompts/**`) into `raw-input/` via `git mv` (path-preserving), after removing the byte-identical duplicate `docs/deployment-pi-coding-agent.md`. Legacy `.plans/**` moved to existing track under `.pi/plan/legacy/`. Root `docs/`, `src/`, `prompts/` removed; `nul` confirmed absent.
2. **OKF shell + governance.** Created `index.md`, `log.md`, `governance/{principles,glossary,metadata-profile,terminology-aliases}.md` (all `draft`).
3. **Domains.** Created 14 candidate functional-domain records M01–M14 (`type: domain`, `upe.id M01…M14`, draft).
4. **Capabilities.** Extracted 100+ source-backed capability records from raw functional-block/eference sources.
5. **Concepts.** Created source-backed `problems/`, `use-cases/`, `events/`, `solution-candidates/` records (≥3 each).
6. **Architecture.** Created draft `architecture/master.md`, `architecture/context-map.md`, and `architecture/decisions/{index.md,adr-template.md,adr-0001-history.md}`.
7. **Labs.** Created empty `labs/README.md` framework + manifest template.
8. **Navigation.** Rewrote root `README.md` (KB-first); aligned `AGENTS.md` navigation wording; updated `index.md`/`log.md` per batch.

## Conventions
- OKF path-as-ID; bundle-relative links; `upe.id` only for existing DDDM stable IDs.
- New content only `status: draft`, `upe.lifecycle: idea|draft`; no `approved`.
- Raw never edited; validators exclude `raw-input/**`.
