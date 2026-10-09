---
type: source-reference
title: RTR production improvement opportunity space (Transport GBA)
description: "Transport GBA workbook consolidating Workshop 1 problems, Workshop 2 problem clusters, existing local practices, ongoing Ramboll initiatives, and the mappings between them, with a review log and controlled vocabularies."
tags: [source-reference, transport, gba, opportunity-space, draft]
sources:
  - ../../sources/transport/rtr-production-improvement-opportunity-space.xlsx
generated: 2026-10-09T10:40:47Z
verified: false
status: draft
stale_after: 2027-10-09
upe:
  lifecycle: draft
  owner: "@chief-architect"
  relations: []
source:
  source_type: spreadsheet
  location: sources/transport/rtr-production-improvement-opportunity-space.xlsx
  revision: "as received; single revision on file"
  hash: sha256:e31cecc7d97a00a3350a4e046039731357a325907bc94ef8977ab06b79c9f63b
  received: 2026-10-09
  origin: Transport GBA (via the project mailbox; sender not recorded in the workbook)
---

# RTR production improvement opportunity space (Transport GBA)

## What this source is

An 18-sheet analysis workbook. Its sheets fall into four kinds, which matters for how it may be used:

| Kind | Sheets |
|---|---|
| Meta / governance | `Read Me`, `Controlled Values`, `Review Log`, `Exceptions` |
| Derived analysis | `WS2_ProblemClusters`, `Q3_Top problems`, `Candidate Problems`, `Existing Practices`, `Initiatives`, `VIEW_WS1_Related work` |
| Mapping tables | `Problem Mappings`, `Practice Mappings`, `Initiative Mappings`, `Clusters`, `Cluster Assignments` |
| Working/draft | `TMP_PracticeProblemProposals`, `TMP_ProblemSpaceAnalysis`, `WS2_Clusters_COPY` |

External identifiers used inside it (`WS1-Pnnn`, `Cnn`, `ESP-Snnn`, `PI-RTR-nnn`) are the source's own
vocabulary. They are **not** DDDM ids and must never be written into `upe.id` (see
[`../governance/principles.md`](../governance/principles.md) §6).

## Provenance and handling

- Received 2026-10-09 and placed under `sources/transport/` in the evidence intake of the hybrid
  operating-model refactoring. Payload bytes are unchanged and must not be edited.
- It previously sat in the legacy `knowledge-base/raw-input/docs/` corpus, where it was mistakenly
  filed as legacy material (audit finding F2).
- **Open question (unresolved):** the workbook mixes *received* material (workshop problem
  statements, captured practices, initiatives) with *derived* material produced by the Transport
  analysis itself (clusters, candidate problems, mappings). Only the received part is evidence.
  If the derived sheets are this team's analysis product, they should be split out into
  `analysis/human/transport/` and this record should be narrowed to the received original only.

## Concepts derived from it

None yet. No canonical requirement, problem or capability record cites this source at the time of
writing; the Transport analysis pipeline is the first intended consumer:

```text
sources/transport/rtr-production-improvement-opportunity-space.xlsx   (this payload)
        ↓ analysis
analysis/ai/transport/…     analysis/human/transport/…
        ↓ review + promotion gate
knowledge-base/{requirements,problems,capabilities}/…
```
