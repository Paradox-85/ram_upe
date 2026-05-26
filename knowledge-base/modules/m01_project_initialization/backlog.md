---
id: m01-backlog
type: backlog
status: in-review-demo
owner: "@module-owner-m01"
version: 1.0
last_updated: 2026-05-26
parent: modules/m01_project_initialization/index.md
tags: [m01, backlog, mvp, tasks]
---

# M01 Backlog — Project Initialization

## MVP Tasks (Sprint 1)

| # | Task | Type | Priority | Status | Requirements |
|---|---|---|---|---|---|
| T-M01-001 | Implement Project Creation Wizard UI (React) | Dev | 🔴 Must | `idea` | REQ-M01-010 to REQ-M01-017 |
| T-M01-002 | Implement Project Seed ingestion from CRM webhook | Dev | 🔴 Must | `idea` | REQ-M01-004, IF-M01-CRM-001 |
| T-M01-003 | Implement Template Library API and selection logic | Dev | 🔴 Must | `idea` | REQ-M01-020, REQ-M01-021, IF-M01-TEMPLATE-001 |
| T-M01-004 | Implement ERP integration (Maconomy project code) | Dev | 🔴 Must | `idea` | IF-M01-ERP-001 |
| T-M01-005 | Implement Azure AD user search for team assembly | Dev | 🔴 Must | `idea` | IF-M01-HR-001, REQ-M01-015 |
| T-M01-006 | Implement M365 provisioning (Teams + SharePoint + Planner) | Dev | 🔴 Must | `idea` | IF-M01-M365-001 |
| T-M01-007 | Implement CDE workspace provisioning (ACC) | Dev | 🔴 Must | `idea` | IF-M01-CDE-001 |
| T-M01-008 | Implement Data Model instantiation service | Dev | 🔴 Must | `idea` | REQ-M01-040 to REQ-M01-044 |
| T-M01-009 | Implement Provisioning Orchestrator with retry logic | Dev | 🔴 Must | `idea` | REQ-M01-050 to REQ-M01-054 |
| T-M01-010 | Implement Provisioning Status dashboard | Dev | 🔴 Must | `idea` | REQ-M01-050 |
| T-M01-011 | Implement audit logging for all provisioning actions | Dev | 🔴 Must | `idea` | REQ-M01-044, REQ-M01-063 |
| T-M01-012 | Implement role-based access control for project creation | Dev | 🔴 Must | `idea` | REQ-M01-067 |

---

## MVP Tasks (Sprint 2)

| # | Task | Type | Priority | Status | Requirements |
|---|---|---|---|---|---|
| T-M01-013 | Knowledge Graph integration for similar projects | Dev | 🟡 Should | `idea` | IF-M01-KG-001, REQ-M01-016 |
| T-M01-014 | Standards and reference data seeding | Dev | 🟡 Should | `idea` | REQ-M01-035, REQ-M01-042 |
| T-M01-015 | Save/resume project creation draft | Dev | 🟡 Should | `idea` | REQ-M01-017 |
| T-M01-016 | Project scope and boundary definition | Dev | 🟡 Should | `idea` | REQ-M01-014 |
| T-M01-017 | Discipline-specific tool configuration (Revit templates) | Dev | 🟡 Should | `idea` | REQ-M01-024 |
| T-M01-018 | Approval workflow configuration | Dev | 🟡 Should | `idea` | REQ-M01-031 |
| T-M01-019 | ProjectWise CDE integration (alternative stack) | Dev | 🟢 Could | `idea` | IF-M01-CDE-001 |

---

## Review Tasks

| # | Task | Assignee | Status |
|---|---|---|---|
| R-M01-001 | Review requirements completeness against Section 1.1 | @module-owner-m01 | `draft` |
| R-M01-002 | Review data model with Chief Architect | @chief-architect | `draft` |
| R-M01-003 | Review interface contracts with integration team | @integration-lead | `draft` |
| R-M01-004 | Review workflow for edge cases (partial failures, retries) | @module-owner-m01 | `draft` |
| R-M01-005 | Review non-functional requirements feasibility | @tech-lead | `draft` |

---

## Demo Tasks

| # | Task | Assignee | Status |
|---|---|---|---|
| D-M01-001 | Generate UI prototype from prototype_prompt.md | @module-owner-m01 | `idea` |
| D-M01-002 | Prepare demo data (sample opportunity, templates, users) | @module-owner-m01 | `idea` |
| D-M01-003 | Create demo script for stakeholder session | @chief-architect | `idea` |
| D-M01-004 | Conduct dry-run of demo | @team | `idea` |

---

## Definition of Done for MVP

- [ ] All Must requirements (REQ-M01-010 to REQ-M01-067) implemented
- [ ] All interface contracts (IF-M01-*) operational with at least one external system
- [ ] Provisioning workflow completes end-to-end for standard template
- [ ] Error recovery handles all documented failure modes
- [ ] Audit logging operational
- [ ] RBAC enforced
- [ ] Performance targets met (30 min setup, 2s UI response)
