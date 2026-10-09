---
type: view
title: Open Decisions
description: "Decisions and open questions currently needing human input."
tags: [view, generated, open-decisions, draft]
sources: []
generated: 2026-10-09T00:00:00Z
verified: false
status: draft
stale_after: 2027-10-09
upe:
  lifecycle: draft
  owner: "@chief-architect"
  relations:
    - type: supports
      target: index
---

# Open Decisions

> **Generated / non-authoritative projection of canonical KB entities.**
> Regenerate: `python tools/kb-views/generate.py`. Do not hand-edit; the records win.

## Decisions awaiting a human decision

| Decision | Title | Status | Lifecycle |
|---|---|---|---|
| [`adr-0001-history`](../architecture/decisions/adr-0001-history.md) | ADR-0001 — Docs-as-Data (History) | draft | draft |
| [`index`](../architecture/decisions/index.md) | Architecture Decision Catalog | draft | draft |

## Open questions recorded on canonical records

### [ADR-0001 — Docs-as-Data (History)](../architecture/decisions/adr-0001-history.md)
- None.

### [ADR Template](../architecture/decisions/adr-template.md)
- ...

### [Master Architecture Integration View](../architecture/master.md)
- Bounded-context boundaries for M01–M14 are unproven (see `context-map.md`).
- This view is candidate; do not treat any layer assignment as approved.

### [M01 — Project Lifecycle & Environment Management](../domains/m01-project-lifecycle-environment-management.md)
- Bounded-context boundary for M01 is unproven.
- Not promoted to `approved`; remains `draft`.

### [M02 — User & Access Management](../domains/m02-user-access-management.md)
- Bounded-context boundary for M02 is unproven.
- Not promoted to `approved`; remains `draft`.

### [M03 — Project Planning & Delivery Management](../domains/m03-project-planning-delivery-management.md)
- Bounded-context boundary for M03 is unproven.
- Not promoted to `approved`; remains `draft`.

### [M04 — Data Quality & Validation](../domains/m04-data-quality-validation.md)
- Bounded-context boundary for M04 is unproven.
- Not promoted to `approved`; remains `draft`.

### [M05 — Information Governance & Knowledge Management](../domains/m05-information-governance-knowledge-management.md)
- Bounded-context boundary for M05 is unproven.
- Not promoted to `approved`; remains `draft`.

### [M06 — AI Integration & Intelligence Capabilities](../domains/m06-ai-integration-intelligence-capabilities.md)
- Bounded-context boundary for M06 is unproven.
- Not promoted to `approved`; remains `draft`.

### [M07 — System Integration & Interoperability](../domains/m07-system-integration-interoperability.md)
- Bounded-context boundary for M07 is unproven.
- Not promoted to `approved`; remains `draft`.

### [M08 — Embedded Process Automation & Workflow](../domains/m08-embedded-process-automation-workflow.md)
- Bounded-context boundary for M08 is unproven.
- Not promoted to `approved`; remains `draft`.

### [M09 — User Experience & Interface Design](../domains/m09-user-experience-interface-design.md)
- Bounded-context boundary for M09 is unproven.
- Not promoted to `approved`; remains `draft`.

### [M10 — Foundational Requirements & Technical Enablement](../domains/m10-foundational-requirements-technical-enablement.md)
- Bounded-context boundary for M10 is unproven.
- Not promoted to `approved`; remains `draft`.

### [M11 — Platform Governance & Roadmap Management](../domains/m11-platform-governance-roadmap-management.md)
- Bounded-context boundary for M11 is unproven.
- Not promoted to `approved`; remains `draft`.

### [M12 — Monitoring, Diagnostics & Operational Support](../domains/m12-monitoring-diagnostics-operational-support.md)
- Bounded-context boundary for M12 is unproven.
- Not promoted to `approved`; remains `draft`.

### [M13 — Technology Enablement & Build vs. Buy](../domains/m13-technology-enablement-build-buy.md)
- Bounded-context boundary for M13 is unproven.
- Not promoted to `approved`; remains `draft`.

### [M14 — Special Capability Domains (BIM/GIS, Time, Contracts)](../domains/m14-special-capability-domains.md)
- Bounded-context boundary for M14 is unproven.
- Not promoted to `approved`; remains `draft`.

### [Approval requested](../events/approval-requested.md)
- Approval SLA and routing rules not exhaustively captured.

### [Automated action executed in response to an event](../events/automated-action-executed.md)
- Audit-trail granularity for automated actions is open.

### [Data change detected in a project system](../events/data-change-detected.md)
- Event-rule vocabulary and cascade depth not fully specified.

### [Delivery blocked by dependency](../events/delivery-blocked-by-dependency.md)
- Which notifications are surfaced vs. suppressed (fatigue) is open.

### [Delivery state transitioned](../events/delivery-state-transitioned.md)
- Full state machine (states/transitions) not yet standardized.

### [Governance — Principles](../governance/principles.md)
- **Stable IDs for new concept types.** The UPE refactoring brief proposed `SRC-*` source-reference numbers (and requirement numbers by implication). That conflicts with §6, so path-as-ID is used instead. Introducing a formal `SRC-*`/`REQ-*` scheme is an ontology change and requires explicit approval.
- **Master Architecture scope.** `architecture/master.md` is designated the primary human-readable integration view over governed architecture state; whether additional component/contract records become canonical in this cycle is unresolved.
- **Domain boundary status.** M01–M14 remain candidate functional domains; none is a proven bounded context.

### [CDE interoperability and manual cross-platform syncing](../problems/cde-interoperability-and-manual-syncing.md)
- Distributed-CDE guidance specifics need further validation.

### [Governance and approval process friction](../problems/governance-and-approval-process-friction.md)
- Approval SLAs and JV access specifics are not exhaustively enumerated.

### [Manual property-set and IFC conversion work](../problems/manual-property-set-ifc-conversion-work.md)
- Specific tool versions and conversion-rule requirements are not exhaustively captured.

### [Misalignment with Ramboll's enterprise architecture](../problems/misalignment-with-ramboll-enterprise-architecture.md)
- Exact enterprise-architecture boundary is unspecified in the source; treat as a candidate problem to validate.

### [Monolith architecture risk](../problems/monolith-architecture-risk.md)
- Considered a candidate design risk; modularity direction referenced in brainstorming module concept.

### [Data quality rules are enforced across pipeline stages](../requirements/req-data-quality-rules-enforced-across-pipeline-stages.md)
- No architecture component or decision is assigned to this requirement yet; promotion to

### [Improvement opportunities are assessed against existing practices and initiatives](../requirements/req-improvement-opportunities-assessed-against-existing-practices.md)
- No architecture component or decision is assigned to this requirement yet; promotion to

### [Information management complies with ISO 19650](../requirements/req-iso-19650-information-management-compliance.md)
- No architecture component or decision is assigned to this requirement yet; promotion to

### [Member onboarding and offboarding are automated](../requirements/req-member-onboarding-and-offboarding-automated.md)
- No architecture component or decision is assigned to this requirement yet; promotion to

### [The platform operates at multi-project scale](../requirements/req-multi-project-scale-and-performance.md)
- No architecture component or decision is assigned to this requirement yet; promotion to

### [Organisational knowledge is captured once and reused](../requirements/req-organisational-knowledge-captured-and-reusable.md)
- No architecture component or decision is assigned to this requirement yet; promotion to

### [Project data is archived and dispositioned at closeout](../requirements/req-project-data-archived-and-dispositioned-at-closeout.md)
- No architecture component or decision is assigned to this requirement yet; promotion to

### [New projects are initialized from a class-based template](../requirements/req-project-initialized-from-class-template.md)
- No architecture component or decision is assigned to this requirement yet; promotion to

### [Access is role-based and scoped to project membership](../requirements/req-role-based-access-scoped-to-project-membership.md)
- No architecture component or decision is assigned to this requirement yet; promotion to

### [UPE does not displace the CDE or authoring tools](../requirements/req-upe-does-not-displace-cde-or-authoring-tools.md)
- No architecture component or decision is assigned to this requirement yet; promotion to

### [Vendor-specific differences are abstracted behind the integration layer](../requirements/req-vendor-specific-differences-abstracted-behind-integration.md)
- No architecture component or decision is assigned to this requirement yet; promotion to

### [Authoring-tool add-in with process-aware UI](../solution-candidates/authoring-tool-addin-process-ui.md)
- Add-in build/toolchain per authoring tool is not specified.

### [Backend-controlled workflow engine](../solution-candidates/backend-controlled-workflow-engine.md)
- Exact state machine and rules require further specification.

### [Microsoft 365-centric technology stack](../solution-candidates/microsoft-365-centric-stack.md)
- Vendor depth (Microsoft + Autodesk) weighting is open.

### [SharePoint Lists as a state and projection layer](../solution-candidates/sharepoint-lists-as-state-projection-layer.md)
- Read-only vs controlled-edit balance depends on UX maturity phase.

### [Automate member onboarding and access provisioning](../use-cases/automate-member-onboarding-access-provisioning.md)
- Onboarding SLAs and approval routing not fully specified.

### [Initialize a project from a class-based template](../use-cases/initialize-project-from-class-template.md)
- Exact template-selection rules per class are not fully specified.

### [Raise an approval request from an authoring tool add-in](../use-cases/raise-approval-request-from-addin.md)
- Approval routing and reviewer-queue rules not exhaustively specified.

### [Track a delivery through its workflow lifecycle](../use-cases/track-delivery-through-workflow-lifecycle.md)
- Checklist variant rules per delivery type not fully enumerated.

### [View consolidated multi-project task and status view](../use-cases/view-consolidated-multiproject-status.md)
- Planner vs. unified-task-list trade-off is open.


---

_Generated 2026-10-09 from 582 canonical records._
