---
type: lab
title: Lab Manifest Template (template)
description: Template for a research/development lab manifest in the Unified Project Execution KB. Copy to labs/<slug>/manifest.md and fill in.
tags: [labs, template, manifest, rnd, draft]
sources: []
generated: 2026-08-10T07:48:05Z
verified: false
status: draft
stale_after: 2027-08-10
upe:
  lifecycle: idea
  owner: "@chief-architect"
  relations: []
---

# Lab Manifest — <slug>

> **Template.** One lab per manifest. Do **not** claim a lab was run without evidence.

## upstream_intent
One of: `hypothesis` | `requirement` | `capability` | `option` | `ADR`

## lab_status
`idea` | `planned` | `active` | `concluded` | `archived` (default `idea`)

## evidence_links
- <bundle-relative raw/KB links backing the intent>

## Run command / environment
- <command> / <environment, versions>

## Outputs
- <expected/actual artifacts>

## Decision influence
- <which concept/ADR/decision this lab could inform>

## Retention
- <how long to keep the lab record>
