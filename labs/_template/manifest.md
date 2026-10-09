---
type: lab
title: Lab Manifest Template (template)
description: Template for a research/development lab manifest. Copy to labs/<slug>/manifest.md and fill in. A lab is not a knowledge document.
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

# Lab Manifest — \<slug\>

> **Template.** One lab per manifest. Do **not** claim a lab was run without evidence.
> A lab asserts nothing canonical; the accepted conclusion is promoted into the KB separately.

## upstream_intent

One of: `hypothesis` | `requirement` | `capability` | `option` | `ADR`

- <the specific hypothesis, requirement, capability, option or ADR being tested>

## upstream_entities

- <KB entities this lab evaluates, e.g. `knowledge-base/requirements/req-….md`,
  `knowledge-base/architecture/….md`, `knowledge-base/architecture/decisions/adr-….md`>

## lab_status

`idea` | `planned` | `active` | `concluded` | `archived` (default `idea`)

## evidence_links

- <inputs backing the intent — evidence payloads under `sources/` or KB records>

## Run command / environment

- <command> / <environment, versions>

## Outputs

- <expected and actual artifacts>

## Result

- <what was observed; state plainly if inconclusive>

## Decision influence

- <which requirement/architecture/decision this lab could inform>

## Canonical evidence created

- <the KB record carrying the accepted conclusion, or `none`>

## Retention

- <how long to keep the lab record and its data>
