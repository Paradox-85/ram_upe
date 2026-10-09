---
type: view
title: Requirements Coverage
description: "Requirement to capability and evidence traceability across the requirements collection."
tags: [view, generated, requirements-coverage, draft]
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

# Requirements Coverage

> **Generated / non-authoritative projection of canonical KB entities.**
> Regenerate: `python tools/kb-views/generate.py`. Do not hand-edit; the records win.

| Requirement | Kind | Status | Evidence | Realising capabilities |
|---|---|---|---|---|
| [Data quality rules are enforced across pipeline stages](../requirements/req-data-quality-rules-enforced-across-pipeline-stages.md) | functional | draft | `UPE_Functional_Blocks_v1.md` | [ability-to-apply-quality-checks-at-pipeline-stages](../capabilities/ability-to-apply-quality-checks-at-pipeline-stages.md), [ability-to-embed-validation-in-design-tools-revit-etc](../capabilities/ability-to-embed-validation-in-design-tools-revit-etc.md), [ability-to-apply-machine-learning-models-to-detect-anomalies](../capabilities/ability-to-apply-machine-learning-models-to-detect-anomalies.md) |
| [Improvement opportunities are assessed against existing practices and initiatives](../requirements/req-improvement-opportunities-assessed-against-existing-practices.md) | stakeholder | draft | `rtr-production-improvement-opportunity-space.xlsx` | — |
| [Information management complies with ISO 19650](../requirements/req-iso-19650-information-management-compliance.md) | constraint | draft | `iso-19650.md` | — |
| [Member onboarding and offboarding are automated](../requirements/req-member-onboarding-and-offboarding-automated.md) | functional | draft | `UPE_Functional_Blocks_v1.md` | [ability-to-add-users-to-project-team](../capabilities/ability-to-add-users-to-project-team.md), [ability-to-log-offboarding-date-and-reason](../capabilities/ability-to-log-offboarding-date-and-reason.md), [ability-to-assign-initial-project-stakeholdersroles](../capabilities/ability-to-assign-initial-project-stakeholdersroles.md) |
| [The platform operates at multi-project scale](../requirements/req-multi-project-scale-and-performance.md) | non-functional | draft | `UPE_Functional_Blocks_v1.md` | [ability-to-aggregate-tasks-across-all-projects](../capabilities/ability-to-aggregate-tasks-across-all-projects.md), [ability-to-aggregate-data-from-multiple-projects](../capabilities/ability-to-aggregate-data-from-multiple-projects.md), [ability-to-provide-consolidated-view-like-ms-planner](../capabilities/ability-to-provide-consolidated-view-like-ms-planner.md) |
| [Organisational knowledge is captured once and reused](../requirements/req-organisational-knowledge-captured-and-reusable.md) | business | draft | `UPE_Functional_Blocks_v1.md` | [ability-to-maintain-scalable-knowledge-capture-not-manual-10-hour-pr](../capabilities/ability-to-maintain-scalable-knowledge-capture-not-manual-10-hour-pr.md), [ability-to-make-reference-data-available-for-project-reuse](../capabilities/ability-to-make-reference-data-available-for-project-reuse.md), [ability-to-apply-reference-data-to-new-projects](../capabilities/ability-to-apply-reference-data-to-new-projects.md) |
| [Project data is archived and dispositioned at closeout](../requirements/req-project-data-archived-and-dispositioned-at-closeout.md) | functional | draft | `UPE_Functional_Blocks_v1.md` | [ability-to-archive-project-data-at-project-completion](../capabilities/ability-to-archive-project-data-at-project-completion.md), [ability-to-mark-project-as-closedarchived](../capabilities/ability-to-mark-project-as-closedarchived.md), [ability-to-compressoptimize-archived-data](../capabilities/ability-to-compressoptimize-archived-data.md), [ability-to-maintain-audit-trail-for-archived-content](../capabilities/ability-to-maintain-audit-trail-for-archived-content.md) |
| [New projects are initialized from a class-based template](../requirements/req-project-initialized-from-class-template.md) | functional | draft | `UPE_Functional_Blocks_v1.md` | [ability-to-select-project-type-from-portfoliotaxonomy](../capabilities/ability-to-select-project-type-from-portfoliotaxonomy.md), [ability-to-apply-templates-to-new-projects](../capabilities/ability-to-apply-templates-to-new-projects.md) |
| [Access is role-based and scoped to project membership](../requirements/req-role-based-access-scoped-to-project-membership.md) | functional | draft | `UPE_Functional_Blocks_v1.md` | [ability-to-assign-user-roles-within-project-context](../capabilities/ability-to-assign-user-roles-within-project-context.md), [ability-to-establish-role-based-access-control-rbac](../capabilities/ability-to-establish-role-based-access-control-rbac.md), [ability-to-provision-access-control-rules-for-folderspermissions](../capabilities/ability-to-provision-access-control-rules-for-folderspermissions.md), [ability-to-apply-discipline-specific-tool-access-rules](../capabilities/ability-to-apply-discipline-specific-tool-access-rules.md) |
| [UPE does not displace the CDE or authoring tools](../requirements/req-upe-does-not-displace-cde-or-authoring-tools.md) | constraint | draft | `UPE_Functional_Blocks_v1.md`, `UPE_Executive_Summary_v1.md` | — |
| [Vendor-specific differences are abstracted behind the integration layer](../requirements/req-vendor-specific-differences-abstracted-behind-integration.md) | non-functional | draft | `UPE_Functional_Blocks_v1.md` | [ability-to-abstract-vendor-specific-differences](../capabilities/ability-to-abstract-vendor-specific-differences.md), [ability-to-add-new-vendors-without-breaking-existing-integrations](../capabilities/ability-to-add-new-vendors-without-breaking-existing-integrations.md) |

Traceability chain: `Source → Problem → Requirement → Capability → Architecture → Decision → Lab/Implementation → Evidence`.


---

_Generated 2026-10-09 from 582 canonical records._
