---
type: Analytical Model
title: UPE ontology-lite analytical source model
description: Typed graph containing the detailed principles, contradictions, opportunities, workstreams, risks, standards, technologies, outcomes, and relationships.
resource: ../../upe-strategic-assessment.okf.yaml
tags: [upe, ontology-lite, graph, source-model]
generated:
  by: agent:github-copilot
  at: 2026-07-31T00:00:00Z
status: draft
stale_after: 2026-11-01
sources:
  - id: initial-prompt
    resource: ../../../main.md
    title: UPE initial prompt
  - id: raw-input
    resource: ../../../../knowledge-base/raw-input
    title: UPE raw input corpus
---

# UPE ontology-lite analytical source model

The retained [YAML graph](../../upe-strategic-assessment.okf.yaml) is the detailed analytical model used to derive this OKF bundle. It contains:

- controlled element and relationship vocabularies;
- stable identifiers;
- seven evaluation principles;
- nine contradictions or design tensions;
- eight ranked opportunities;
- eight workstreams and their dependencies;
- a detailed risk register;
- standards and replaceable technology recommendations;
- measurable outcomes;
- graph-integrity and governance rules.

It is intentionally labeled `ontology-lite`, not Open Knowledge Format. OKF organizes curated knowledge as linked Markdown concepts; the YAML model provides stronger typed-edge semantics and machine validation. They are complementary rather than competing representations.

The organized interpretation is available from the [bundle index](../index.md), while the most important recommendations are in [architecture](../recommendations/architecture.md) and [low-hanging fruits](../recommendations/low-hanging-fruits.md).