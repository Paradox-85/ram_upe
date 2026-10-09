---
type: Workstream Portfolio
title: UPE parallel workstreams
description: Capability-oriented delivery streams connected through a minimum shared operating-model contract.
tags: [upe, workstreams, delivery, ownership]
generated:
  by: agent:github-copilot
  at: 2026-08-01T00:00:00Z
status: draft
stale_after: 2026-11-01
sources:
  - id: foundations
    resource: ../../../../knowledge-base/raw-input/upe-foundations.md
    title: UPE foundations
  - id: interviews
    resource: ../../../../knowledge-base/raw-input/interviews-summary.md
    title: UPE interviews summary
---

# UPE parallel workstreams

## Shared foundation

### 1. Operating model, vocabulary, and architecture governance

Own capability boundaries, IDs, vocabularies, schemas, extension rules, architectural decisions, and alignment with enterprise architecture.

**First deliverable:** minimum UPE contract v0.1 and a lightweight decision forum.

This stream enables all others. It should remain small and must not become a central delivery bottleneck.

## Parallel capability streams

### 2. Project startup and platform provisioning

Turn approved desired state into auditable setup plans and platform-specific actions.

**First deliverable:** clone-and-override project repository with a dry-run provisioning report.

### 3. Delivery planning, workflows, and digital thread

Own work packages, deliveries, dependencies, checklists, transitions, approvals, events, and artifact identifiers.

**First deliverable:** one end-to-end delivery workflow using Lists as the initial UI/state surface and backend-owned rules.

### 4. Identity and project access

Own project roles, approvals, platform mappings, joiner-mover-leaver events, expiry, recertification, and evidence.

**First deliverable:** one role-based onboarding and offboarding path spanning Teams and one project platform.

### 5. CDE interoperability and information management

Own authoritative-source declarations, common information-register metadata, lifecycle-state mappings, requirements traceability, and exchange validation.

**First deliverable:** two-CDE metadata mapping and information-health view.

### 6. Production toolbox and citizen-development golden paths

Own approved templates, APIs, MCP servers, automation patterns, environments, observability, support tiers, and cost guardrails.

**First deliverable:** three supported solution patterns with ownership and production-readiness checks.

### 7. Knowledge governance and AI enablement

Own knowledge-source curation, permission-aware retrieval, agent and skill registries, evaluation, provenance, usage, and cost monitoring.

**Dependencies:** operating-model contract, project-access controls, and toolbox guardrails.

**First deliverable:** one bounded retrieval pilot with evaluation and retirement criteria.

### 8. Adoption and portfolio value

Own pilot selection, baselines, user support, feedback, outcome reporting, funding decisions, and retirement.

**First deliverable:** pilot scorecard, adoption plan, baseline, and quarterly portfolio review.

## Coordination model

- Streams share contracts, not a common release train.
- Startup, delivery workflow, identity, CDE interoperability, toolbox, and adoption can proceed in parallel after the minimum contract exists.
- AI production use waits for identity and toolbox controls, but experiments can run earlier in bounded sandboxes.
- Each stream needs a product owner, support model, lifecycle budget, and measurable outcome before production rollout.
- Scale decisions use evidence from the [low-hanging-fruit pilots](../recommendations/low-hanging-fruits.md), not architectural completeness.

Each stream must actively own relevant items in the [risk register](../risks/index.md).