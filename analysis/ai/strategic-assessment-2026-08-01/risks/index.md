---
type: Risk Register
title: UPE principal risks
description: Strategic, architectural, operational, security, adoption, and cost risks for UPE.
tags: [upe, risk, governance, controls]
generated:
  by: agent:github-copilot
  at: 2026-08-01T00:00:00Z
status: draft
stale_after: 2026-10-01
sources:
  - id: risks
    resource: ../../../../knowledge-base/raw-input/risks.md
    title: UPE raw risk model
  - id: interviews
    resource: ../../../../knowledge-base/raw-input/interviews-summary.md
    title: UPE interviews summary
---

# UPE principal risks

| Risk | Early indicator | Primary mitigation | Owning workstream |
|---|---|---|---|
| Enterprise-architecture misalignment | Competing canonical models or duplicated shared platforms | Agree domain boundaries and integration contracts before platform commitments | Operating model |
| Monolith and platform overreach | Pilots wait for a central platform or unrelated releases move together | Fund capability products independently and share only versioned contracts | Operating model |
| Vendor lock-in | Critical data cannot be exported without licenses or reconstruction | Require canonical exports, adapter boundaries, exit tests, and contractual data rights | CDE interoperability |
| Schema overdesign | Vocabulary debate delays pilots and fields remain unused | Model only concepts required by two pilots; evolve compatibly | Operating model |
| Poor data quality | IDs, owners, revisions, or approvals are repeatedly repaired manually | Validate at capture, assign owners, and expose quality measures | CDE interoperability |
| Stale duplicated state | Git, Lists, CDEs, dashboards, and models disagree | Declare field authority, timestamp projections, and reconcile differences | Delivery digital thread |
| Event loops and races | Duplicate approvals, repeated messages, or non-deterministic state | Use idempotency, correlation, optimistic concurrency, retries, and dead-letter handling | Delivery digital thread |
| Permission leakage | Access lacks scope or expiry, or retrieval returns unauthorized content | Least privilege, project roles, recertification, evidence, and permission-trimmed retrieval | Identity and access |
| Citizen-development sprawl | Unowned flows, unsupported connectors, and personal production automations | Golden paths, environment tiers, DLP, inventory, telemetry, and expiry | Production toolbox |
| API and licensing constraints | A workflow assumes unavailable APIs or premium connectors | Run capability spikes, design fallback paths, and test representative contracts | Startup and provisioning |
| Agent fragmentation | Duplicate agents use inconsistent tools, prompts, and sources | Registry, reusable skills, evaluation gates, owners, versions, and retirement rules | Knowledge and AI |
| AI trust failure | Agents answer from stale, unverified, or inaccessible knowledge | OKF provenance and freshness plus runtime access controls and evaluations | Knowledge and AI |
| Low adoption | Teams retain shadow spreadsheets and bypass checks | Co-design in active projects and remove controls that add no measured value | Adoption and value |
| Unclear ownership | Nobody owns incidents, schemas, adapters, or post-pilot funding | Product owners, service tiers, lifecycle budgets, and retirement criteria | Adoption and value |
| Cost growth | Usage cannot be attributed and idle services persist | Project tags, quotas, budgets, unit-cost measures, and idle-resource review | Production toolbox |
| Standards become shelfware | Standards remain documents and exceptions are invisible | Publish schemas, examples, validators, conformance reports, and exception records | Operating model |

## Risk-management recommendation

Treat risks as product backlog inputs, not a parallel compliance document. Every [workstream](../workstreams/index.md) should review its warning indicators during pilot governance. Critical risks require explicit acceptance before scale.

OKF concepts should use `generated`, `verified`, `status`, `stale_after`, and `sources` so agents and people can distinguish draft synthesis from reviewed organizational knowledge. These signals support trust decisions but do not replace authorization or engineering approval.