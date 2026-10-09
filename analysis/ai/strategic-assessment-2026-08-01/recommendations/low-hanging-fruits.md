---
type: Prioritized Roadmap
title: UPE low-hanging fruits
description: Ordered increments that create reusable foundations and test UPE in real project work.
tags: [upe, roadmap, pilots, quick-wins]
generated:
  by: agent:github-copilot
  at: 2026-08-01T00:00:00Z
status: draft
stale_after: 2026-11-01
sources:
  - id: interviews
    resource: ../../../../knowledge-base/raw-input/interviews-summary.md
    title: UPE interviews summary
  - id: process-format
    resource: ../../../../knowledge-base/raw-input/business-process-capture-format.md
    title: Business process capture format
---

# UPE low-hanging fruits

## 1. Minimum vocabulary and schemas

Publish versioned definitions for Project, Organization, ProjectRole, WorkPackage, Delivery, Dependency, Process, Checklist, InformationContainer, Platform, and Outcome. Include stable ID rules, examples, validation, and project extension conventions.

**Exit criterion:** two pilot teams exchange and validate the same sample project without interpretation meetings.

## 2. Golden-path sample project

Create a realistic reference project containing delivery plans, roles, checks, naming, information states, folder conventions, and platform mappings. It should show the expected result rather than only explaining the procedure.

**Exit criterion:** a new project team can understand expected setup and delivery from the example alone.

## 3. Clone-and-override project repository

Represent desired project state in a template repository. Let a project select templates and override explicit parameters. Validate changes automatically and generate a human-reviewable provisioning plan.

**Exit criterion:** one pilot produces an approved setup plan without re-keying the same information into multiple tools.

## 4. One onboarding and offboarding path

Automate request, PM approval, project-role assignment, access to Teams and one project platform, evidence logging, expiry, and removal.

**Exit criterion:** median lead time falls and every access grant records approver, role, scope, and expiry.

## 5. One delivery workflow

Choose one high-frequency delivery type and one discipline pair. Implement self-check, cross-check, approval request, dependency visibility, and Teams feedback. Keep transition rules outside Lists even if Lists holds state in the pilot.

**Exit criterion:** users complete the process without bypassing rules and rejected transitions provide actionable feedback.

## 6. One property and validation path

Define a minimal process property set carrying delivery ID, state snapshot, and validation timestamp. Map it through one authoring tool and IFC export, then validate applicable requirements with IDS.

**Exit criterion:** repeated manual property population is removed and stale model snapshots are detectable.

## 7. Two-CDE information register

Map metadata exports from two CDEs to common WIP, Shared, Published, and Archived states. Link each record to its authoritative source rather than copying all files.

**Exit criterion:** portfolio reporting resolves every record to the correct CDE and reports metadata completeness.

## 8. Curated knowledge retrieval pilot

Use one bounded handbook or process corpus. Add owners, access labels, sources, verification, freshness dates, evaluation questions, and usage telemetry before introducing broader agents.

**Exit criterion:** the pilot meets an agreed grounded-answer threshold without unauthorized disclosure.

These increments are owned and sequenced through the [parallel workstreams](../workstreams/index.md). Their measures are retained in the [analytical source model](../references/analytical-source-model.md).