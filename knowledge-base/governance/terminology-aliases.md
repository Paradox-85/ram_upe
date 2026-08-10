---
type: governance
title: Terminology Aliases
description: Maps legacy/ambiguous spellings (including the historical product name) to the canonical Unified Project Execution vocabulary, without rewriting raw sources.
tags: [governance, terminology, aliases, upe]
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

# Terminology Aliases

Mappings from legacy/ambiguous spellings to the canonical term. Raw sources are **never rewritten**; this alias map lets readers/interfaces canonicalize names at read time.

| Legacy / ambiguous spelling | Canonical | Notes |
|---|---|---|
| Unified Production Environment | **Unified Project Execution** | historic product name; retained verbatim only in raw sources |
| UPE (ambiguous) | **Unified Project Execution** | canonical expansion |
| master | domains + capabilities + architecture concepts | legacy single-master decomposed into DDD collection records |
| domain (as bounded context) | functional-domain candidate | M01–M14 are *candidates*, not bounded contexts |
| module (loose) | solution-candidate / `module`-typed candidate | only when an explicit recurring module pattern is evidenced |
| REQ-*/ENT-*/WF-* (loose) | source-backed concept records | existing DDDM IDs kept in `upe.id` where they apply; no invented IDs |

## Rules
- Aliases are documented, never silently rewritten inside `raw-input/**`.
- Active (non-raw) prose uses the canonical term.
- See [`glossary.md`](glossary.md) for definitions.
