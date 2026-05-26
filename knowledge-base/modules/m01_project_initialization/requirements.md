---
id: m01-requirements
type: requirements
status: in-review-demo
owner: "@module-owner-m01"
version: 1.0
last_updated: 2026-05-26
parent: modules/m01_project_initialization/index.md
tags: [m01, requirements, business, functional, non-functional]
---

# M01 Requirements — Project Initialization & Provisioning

> **Source:** Derived from `docs/UPE_Functional_Blocks_v1.md`, Section 1.1

---

## Business Requirements

| ID | Requirement | Priority | Rationale |
|---|---|---|---|
| REQ-M01-001 | The system shall reduce average project initialization time by at least 50% compared to manual setup | Must | Core business value of M01 |
| REQ-M01-002 | The system shall ensure 100% of projects follow approved templates and standards | Must | Consistency and compliance |
| REQ-M01-003 | The system shall provide a single interface for project creation across all project types | Must | Eliminate fragmented workflows |
| REQ-M01-004 | The system shall capture project context from CRM opportunities automatically | Should | Reduce manual data entry |
| REQ-M01-005 | The system shall enable PMs to configure projects without IT involvement for standard cases | Must | Self-service, scalability |
| REQ-M01-006 | The system shall support multi-discipline project configurations | Must | Cross-discipline projects are the norm |

---

## Functional Requirements

### Project Creation Interface

| ID | Requirement | Priority |
|---|---|---|
| REQ-M01-010 | The system shall provide a web-based project creation wizard | Must |
| REQ-M01-011 | The system shall allow selection of project type from portfolio taxonomy | Must |
| REQ-M01-012 | The system shall allow definition of project class/category driving template selection | Must |
| REQ-M01-013 | The system shall capture basic project metadata (name, code, location, client, disciplines) | Must |
| REQ-M01-014 | The system shall allow definition of project scope and boundaries | Should |
| REQ-M01-015 | The system shall allow assignment of initial project stakeholders and roles | Must |
| REQ-M01-016 | The system shall display similar past projects from the knowledge graph | Could |
| REQ-M01-017 | The system shall support saving and resuming project creation drafts | Should |

### Automated Template Deployment

| ID | Requirement | Priority |
|---|---|---|
| REQ-M01-020 | The system shall auto-select project templates based on project class and type | Must |
| REQ-M01-021 | The system shall initialize folder structure in SharePoint and file repositories | Must |
| REQ-M01-022 | The system shall provision access control rules per template | Must |
| REQ-M01-023 | The system shall configure CDE workspace structure per template | Must |
| REQ-M01-024 | The system shall deploy discipline-specific tool configurations (Revit templates, etc.) | Should |
| REQ-M01-025 | The system shall configure team collaboration spaces (Teams channels, SharePoint lists) | Must |
| REQ-M01-026 | The system shall auto-generate task boards (Planner) from template | Should |
| REQ-M01-027 | The system shall allow override of template defaults before provisioning | Must |

### Tool & Service Configuration

| ID | Requirement | Priority |
|---|---|---|
| REQ-M01-030 | The system shall provision project tools based on template configuration | Must |
| REQ-M01-031 | The system shall configure approval workflows for project artifacts | Should |
| REQ-M01-032 | The system shall establish project-level governance rules per template | Should |
| REQ-M01-033 | The system shall link external tools and services via APIs (ACC, Revit, etc.) | Must |
| REQ-M01-034 | The system shall configure project standards and discipline-specific settings | Should |
| REQ-M01-035 | The system shall seed project with reference data and best practices | Could |

### Data Model Instantiation

| ID | Requirement | Priority |
|---|---|---|
| REQ-M01-040 | The system shall create a project entity in the UPE data model | Must |
| REQ-M01-041 | The system shall initialize project context (disciplines, roles, geographical areas) | Must |
| REQ-M01-042 | The system shall associate standards and guidelines with the project | Must |
| REQ-M01-043 | The system shall establish baseline master data for the project | Must |
| REQ-M01-044 | The system shall create audit trail for all provisioning actions | Must |

### Provisioning Status & Recovery

| ID | Requirement | Priority |
|---|---|---|
| REQ-M01-050 | The system shall display real-time provisioning status for each step | Must |
| REQ-M01-051 | The system shall automatically retry failed provisioning steps (up to 3 times) | Must |
| REQ-M01-052 | The system shall allow manual retry of individual provisioning steps | Must |
| REQ-M01-053 | The system shall notify PM and support team on provisioning failures | Must |
| REQ-M01-054 | The system shall support partial provisioning states (some tools ready, others pending) | Should |

---

## Non-Functional Requirements

| ID | Requirement | Metric |
|---|---|---|
| REQ-M01-060 | The project creation wizard shall complete standard setup in under 30 minutes | 30 min max for standard template |
| REQ-M01-061 | The system shall be available 99.5% during business hours | 99.5% uptime |
| REQ-M01-062 | The wizard UI shall respond within 2 seconds for any step | 2s max response |
| REQ-M01-063 | All provisioning actions shall be logged with timestamp and actor | 100% audit coverage |
| REQ-M01-064 | The system shall support concurrent creation of 20+ projects | 20 concurrent |
| REQ-M01-065 | Project data shall be encrypted at rest and in transit | AES-256, TLS 1.2+ |
| REQ-M01-066 | The system shall integrate with Azure AD for authentication | SSO required |
| REQ-M01-067 | Access to project creation shall be role-restricted (PM+ roles only) | RBAC enforced |

---

## Traceability

| Source | Section | Mapped Requirements |
|---|---|---|
| `docs/UPE_Functional_Blocks_v1.md` §1.1 | Project Creation Interface | REQ-M01-010 to REQ-M01-017 |
| `docs/UPE_Functional_Blocks_v1.md` §1.1 | Automated Template Deployment | REQ-M01-020 to REQ-M01-027 |
| `docs/UPE_Functional_Blocks_v1.md` §1.1 | Tool & Service Configuration | REQ-M01-030 to REQ-M01-035 |
| `docs/UPE_Functional_Blocks_v1.md` §1.1 | Data Model Instantiation | REQ-M01-040 to REQ-M01-044 |
| `src/loop/loop.md` WS 3.3 | Unified Project Initialization | REQ-M01-001 to REQ-M01-006 |
