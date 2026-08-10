---
type: use-case
title: Initialize a project from a class-based template
description: An authorized user creates a new project by selecting a project class/category so that the environment, tools, templates, and access are provisioned automatically.
tags: [use-case, project-initialization, provisioning, draft]
sources:
  - raw-input/docs/UPE_Functional_Blocks_v1.md
generated: 2026-08-10T07:48:05Z
verified: false
status: draft
stale_after: 2027-08-10
upe:
  lifecycle: idea
  owner: "@chief-architect"
  relations:
    - type: derived-from
      target: raw-input/docs/UPE_Functional_Blocks_v1.md
    - type: supports
      target: domains/m01-project-lifecycle-environment-management
    - type: supports
      target: capabilities/ability-to-select-project-type-from-portfoliotaxonomy
---

# Initialize a project from a class-based template

## Use case
> An authorized user selects a project type from the portfolio/taxonomy and defines its class/category; the platform auto-selects and deploys project templates so the project is provisioned from inception to an operational state.

## Primary actor
Project administrator / authorized user.

## Supporting capabilities
- Ability to select project type from portfolio/taxonomy
- Ability to auto-select and deploy project templates based on class

## Source
Functional block **1.1 Project Initialization & Provisioning** in [`raw-input/docs/UPE_Functional_Blocks_v1.md`](../raw-input/docs/UPE_Functional_Blocks_v1.md).

## Open questions
- Exact template-selection rules per class are not fully specified.
