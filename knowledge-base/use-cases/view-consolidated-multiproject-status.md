---
type: use-case
title: View consolidated multi-project task and status view
description: A user across several projects gets a consolidated view (Planner-style) of tasks and project status to track workload and issues.
tags: [use-case, multi-project, dashboard, observability, draft]
sources:
  - raw-input/docs/UPE_Functional_Blocks_v1.md
  - raw-input/docs/brainstorming.md
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
      target: capabilities/ability-to-aggregate-tasks-across-all-projects
    - type: supports
      target: domains/m09-user-experience-interface-design
---

# View consolidated multi-project task and status view

## Use case
> Most people in Ramboll work on several projects at the same time. They need a consolidated task/status view (like MS Planner) that aggregates tasks across all projects, filters by project/priority/deadline, and shows project health to surface issues.

## Primary actor
Project member working across multiple projects.

## Supporting capability
- Ability to aggregate tasks across all projects
- Ability to provide consolidated view (like MS Planner)

## Source
Functional block **9.3 Multi-Project & Multi-Context Support** in [`raw-input/docs/UPE_Functional_Blocks_v1.md`](../raw-input/docs/UPE_Functional_Blocks_v1.md) and project-scoped user-friendliness in `raw-input/docs/brainstorming.md`.

## Open questions
- Planner vs. unified-task-list trade-off is open.
