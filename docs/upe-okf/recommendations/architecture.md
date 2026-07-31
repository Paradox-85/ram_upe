---
type: Recommendation
title: Layer UPE by information responsibility
description: Recommended separation of knowledge, configuration, operations, integration, and user experience.
tags: [upe, architecture, recommendation, interoperability]
generated:
  by: agent:github-copilot
  at: 2026-08-01T00:00:00Z
status: draft
stale_after: 2026-11-01
sources:
  - id: initial-prompt
    resource: ../../../main.md
    title: UPE initial prompt
  - id: process
    resource: ../../../../knowledge-base/raw-input/event-driven work management system.md
    title: Event-driven work management raw input
  - id: startup
    resource: ../../../../knowledge-base/raw-input/project-startup.excalidraw
    title: Project startup model
---

# Layer UPE by information responsibility

## Recommendation

Use five logical layers. Products can span layers during a pilot, but ownership and contracts should not be collapsed.

### 1. Knowledge layer

Store curated process descriptions, standards, definitions, decisions, playbooks, service descriptions, lessons, and agent guidance as [OKF concepts](../index.md). Use normal links to form the knowledge graph and OKF trust fields to expose provenance and freshness.

### 2. Desired-state configuration layer

Use version-controlled YAML or JSON for project metadata, platform selection, folder and layer structures, role mappings, templates, and policy parameters. Validate changes in CI and produce a dry-run plan before provisioning.

This layer describes intended state. It does not record every live operational transition.

### 3. Operational domain layer

Services own dynamic project state: deliveries, workflow instances, requested actions, approvals, access grants, events, and reconciliation. Start narrowly. Microsoft Lists can serve as UI and state holder in an initial pilot while backend logic validates behavior.[^process]

As complexity grows, commands should pass through APIs and Lists should become a controlled interaction or projection surface.

### 4. Integration and adapter layer

Adapters translate canonical UPE contracts to CDE, authoring-tool, M365, GIS, and enterprise-system APIs. They isolate licensing constraints, API peculiarities, retries, rate limits, and vendor-specific permission models.

Every critical adapter needs a tested data-exit path and declared fallback when an API is unavailable.

### 5. Experience layer

Use Teams and familiar engineering tools as context-sensitive entry points. Users should see only relevant project state, checks, requests, blockers, and approvals. Avoid requiring engineers to navigate a generic platform portal for routine production work.

## Cross-cutting controls

- Entra-based authentication and least-privilege authorization.
- Correlation identifiers and audit evidence across commands and events.
- OpenTelemetry-compatible observability and project-level cost attribution.
- Human approval for consequential engineering, access, and publishing decisions.
- Versioned schemas, API contracts, event contracts, and compatibility policy.
- Named product ownership, support tier, lifecycle budget, and retirement criteria.

## Architectural decisions to make first

1. Define the minimum canonical entities and IDs.
2. Declare authority for configuration, workflow, access, information containers, and knowledge.
3. Agree the UPE and enterprise-architecture boundary.
4. Select two pilots and define measurable exit criteria.
5. Define project extension and exception rules.

Delivery should follow the [low-hanging fruits](low-hanging-fruits.md) and [parallel workstreams](../workstreams/index.md).

[^process]: The raw process material recommends a progressive model in which Lists can initially hold state while backend services own validation and behavior.