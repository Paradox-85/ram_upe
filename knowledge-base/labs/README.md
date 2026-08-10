---
type: lab
title: Labs — R&D Framework
description: Empty framework for research and development labs in the Unified Project Execution KB. This is a contract, not an experiment inventory.
tags: [labs, rnd, framework, upe, draft]
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

# Labs (R&D Framework)

**Empty framework.** This is a contract for future experiments, not an inventory of completed labs.

## Purpose
Provide a consistent place and schema for recording research/development ideas and experiments in a structured, reviewable way.

## How to add a lab
1. Choose a short `<slug>` for the lab.
2. Copy the manifest template [`_template/manifest.md`](_template/manifest.md) to `labs/<slug>/manifest.md`.
3. Fill in `upstream_intent`, `lab_status`, `evidence_links`, run command/environment, outputs, decision influence, and retention.

## Manifest fields (contract)
- `upstream_intent`: `hypothesis` | `requirement` | `capability` | `option` | `ADR`
- `lab_status`: `idea` | `planned` | `active` | `concluded` | `archived`
- `evidence_links`: supporting raw/KB links
- run command / environment
- outputs
- decision influence
- retention

## Rules
- Do **not** claim a lab was run without evidence.
- Do **not** promote experimental code to `../tools/` in this cycle.
- All lab records are `draft`/`idea`; no approvals here.
