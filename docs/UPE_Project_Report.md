# UPE (Unified Project Execution) — Project Report

**Repository:** [github.com/Paradox-85/ram_upe](https://github.com/Paradox-85/ram_upe)
**Prepared by:** Principal Architect Assistant
**Status:** Draft / Discovery & Early Architecture Phase

---

## 1. Executive Summary

**UPE (Unified Project Execution)** is Ramboll's initiative to build a cohesive platform ecosystem that orchestrates project delivery across its entire portfolio — spanning project lifecycle management, intelligent process automation, knowledge management, and enterprise system integration. The ambition is to move engineering and project teams away from fragmented, tool-by-tool workflows toward a coherent, connected environment where project setup, data quality, collaboration, and AI-assisted work happen on a shared foundation.

The project originated from cross-GBA (Global Business Area) discussions recognizing that:
- Project initialization is inconsistent and manual across the organization.
- Engineering and enterprise data live in silos (CDEs, DMS, ERP, CRM) with no unified data backbone.
- Knowledge captured during projects is frequently lost at closeout.
- AI adoption is happening bottom-up (ungoverned "vibe coding") and top-down (vendor AI features) without a coordinating framework.

UPE is not being built as a single monolithic application. It is conceived as a **modular ecosystem** — a set of loosely coupled capability domains, each addressing a recurring organizational need, integrated through APIs and a shared data model, and built pragmatically on top of existing enterprise technology (Microsoft 365, Autodesk, AVEVA) rather than reinventing core infrastructure.

---

## 2. Goals and Objectives

### 2.1 Strategic Goals
- **Consistency:** Standardize how projects are initialized, staffed, and closed across all GBAs.
- **Data integrity:** Establish a canonical, queryable data model for project context (projects, disciplines, roles, standards) as a single source of truth.
- **Knowledge retention:** Prevent institutional knowledge loss at project closeout; make organizational knowledge AI-queryable.
- **Interoperability:** Avoid vendor lock-in through vendor-agnostic abstraction layers and open standards (Open BIM, IFC, bSDD, W3C).
- **Intelligent automation:** Embed AI-assisted validation, rules-checking, and domain-specific agents directly into engineers' existing tools (Revit, ACC, etc.) rather than requiring context switches.

### 2.2 Measurable Objectives (from the Executive Summary)
| Category | Target |
|---|---|
| Project initialization time | −50% |
| Time to onboard a team member | < 1 day |
| Data quality score | 95%+ |
| On-time delivery improvement | +20% |
| New projects using UPE | 90%+ adoption |
| Monthly active users | 80%+ |
| Cost of rework/errors | −30% |
| Project margin improvement | +15% |

### 2.3 Non-Goals / Explicit Scope Boundaries
- UPE is **not** a replacement for a Common Data Environment (CDE) or Document Management System (DMS) — it is a coordination and intelligence layer that sits above/across them.
- UPE is **not** limited to "production" — it explicitly broadens to cover the full project lifecycle, including time reporting, contracting, billing, and HR-adjacent processes (hence the renaming from "Unified *Production* Environment" to "Unified *Project* Execution").

---

## 3. Scope: 14 Functional Domains

UPE's functional scope was mapped into **14 capability domains** comprising **175+ discrete functional capabilities**, extracted from stakeholder interviews, brainstorming sessions, and architect chat logs:

| # | Domain | Focus |
|---|--------|-------|
| 1 | Project Lifecycle & Environment Management | Automated project setup, operation, closure |
| 2 | User & Access Management | Identity, roles, permissions across systems |
| 3 | Project Planning & Delivery Management | WBS, schedule, progress visibility, risk detection |
| 4 | Data Quality & Validation | Classification, validation rules, master data |
| 5 | Information Governance & Knowledge Management | AI-powered knowledge extraction, ontologies, best practices |
| 6 | AI Integration & Intelligence Capabilities | Rules engines, domain agents, vibe coding support |
| 7 | System Integration & Interoperability | APIs to CRM/ERP/M365/Autodesk, vendor-agnostic layers |
| 8 | Embedded Process Automation & Workflow | Rules baked into tools, not spreadsheets |
| 9 | User Experience & Interface Design | Unified portal, multi-project dashboards |
| 10 | Foundational Requirements & Technical Enablement | Canonical data model, cloud architecture, security |
| 11 | Platform Governance & Roadmap Management | Feature prioritization, GBA requirements aggregation |
| 12 | Monitoring, Diagnostics & Operational Support | SLA tracking, usage analytics, incident management |
| 13 | Technology Enablement & Build vs. Buy | Microsoft/Autodesk stack leverage, connector development |
| 14 | Special Capability Domains | BIM/GIS integration, time reporting, compliance |

### Priority Tiers
- **High priority (must-have foundation):** Project initialization & provisioning, basic data model, user access management, progress tracking, onboarding/offboarding.
- **Medium priority (core value delivery):** Data quality & validation, knowledge capture, CRM/ERP integration, process embedding, unified access interface.
- **Strategic priority (differentiation):** AI-powered rules & compliance, domain-specific agents, master data management, knowledge graph/ontology, governance automation.

---

## 4. How UPE Is Proposed to Be Implemented

### 4.1 Architectural Philosophy
UPE is designed as a **collection of modules**. From a user's perspective, a module is a logical grouping of features (e.g., "Project Initialization"). From an implementer's perspective, a module is composed of concrete artifacts:
- Templates / configuration files
- Approval workflows
- Dashboards
- Backend automation scripts
- Databases
- Web applications

This modular decomposition allows different GBAs and teams to contribute independently while maintaining architectural coherence through a shared data backbone and API layer.

### 4.2 Technology Strategy — Build vs. Buy
The guiding principle is **pragmatic reuse over reinvention**:
- **Leverage existing enterprise licensing:** Microsoft 365 E5 (Teams, SharePoint, Power BI, Power Automate, Planner, Azure) as the collaboration and orchestration backbone.
- **Integrate rather than replace:** Deep API integration with Autodesk (Revit, ACC, Forma) for design-tool-embedded workflows, and with AVEVA products where engineering information management is required.
- **Build only where differentiation is needed:** Custom development is reserved for the canonical data model, cross-vendor abstraction layers, AI agents, and connectors — not for commodity capabilities already covered by CDE/ERP/CRM vendors.

### 4.3 Key Architectural Decisions Under Discussion
1. **Data centralization vs. federation** — single data lake vs. distributed sources with unified views.
2. **Vendor commitment** — deep integration with Microsoft + Autodesk vs. preserving vendor optionality.
3. **API strategy** — a single unified UPE API vs. direct use of vendor-native APIs.
4. **AI approach** — enterprise AI platform with custom models vs. vendor AI features + grassroots "vibe coding."
5. **Knowledge representation** — RDF/semantic web/knowledge graph vs. simpler taxonomy-based approaches.

A recurring theme in architect discussions is the tension between **DMS-centric vendor positioning** (vendors pitching document management systems as the "knowledge vault" and AI data layer) and Ramboll's actual need for a **system of record for structured project and engineering data** — distinct from unstructured document storage.

### 4.4 Data & Information Management Workstream
This was identified as the **most immature and most urgent** workstream. Key developments:
- A new **Data Management Chapter** has been proposed, sitting alongside the existing DD&P (Digital Delivery & Production) chapter, to unify engineering and enterprise data strategy rather than treating them separately — a deliberate choice given the AI era's need for unified data access.
- An in-house **Enterprise Data Warehouse (EDW)** effort is underway (SQL-based) to consolidate reference data and master books, since Ramboll lacks a product equivalent to AVEVA AIM/NET. This effort includes exporting to **IFC** and validating against **bSDD (buildingSMART Data Dictionary)** — testing IFC as a data container independent of 3D geometry.
- This work was catalyzed by a real, time-boxed operational driver: a client-driven **final handover and full IT/master-reference-book audit** (the Shell/Jackdaw context referenced in team discussions), which forced rapid consolidation of scattered engineering data into a structured, validated format.

### 4.5 AI Enablement Strategy
A dual-track approach is planned:
- **Top-down:** Enable and integrate vendor-native AI (Tier 1/2 vendors — Autodesk, AVEVA, etc.) rather than building competing general-purpose AI.
- **Bottom-up:** Support and channel grassroots "vibe coding" (AI-assisted rapid development using tools like GitHub Copilot, Claude, Replit) that is already happening organically across projects — by providing a shared tech-stack recommendation, a solutions registry, and reusable patterns, rather than trying to suppress it.
- Domain-specific AI agents are prioritized for high-value, narrow tasks: 3D model querying (via Revit/ACC APIs), AI-powered rules checkers, and unpacking AI-unfriendly data from PDFs/closed containers into structured, LLM-consumable formats.

### 4.6 Prototyping Approach
The architecture team explicitly adopted a **prototype-first discussion method**: rather than debating abstract requirements, the team builds visible UI mockups/prototypes (using Claude for UI mockups, Replit for full-stack prototypes) to anchor conversations about user experience and align stakeholder understanding — a practice benchmarked against how peer firms (Mott MacDonald, Arup) approached their own unified platform efforts.

### 4.7 Design Methodology — DDDM (Dialogue-Driven Design Method)
To make product design itself LLM-native and auditable, the project adopted a **Markdown + Mermaid + Git-based workflow** as the single source of truth for design knowledge (formalized in ADR-0001), replacing traditional Word/Visio specifications. Core principles:
- `main` branch contains only **approved, reviewed artifacts**.
- Module development happens on **feature branches**, with LLM design sessions logged for full traceability.
- **Pull Requests** serve as the digital architecture review gate — module owners submit a PR with a review checklist and explicit architecture decision points; nothing merges to `main` without passing review.
- Derived artifacts (stakeholder briefs, UI prototype prompts, demo scripts) are generated *from* the approved knowledge base, not authored independently — ensuring they stay synchronized with the source of truth.

---

## 5. Implementation Phasing

| Phase | Timeframe | Objective | Key Deliverables | Effort |
|---|---|---|---|---|
| **Phase 1 — Foundation** | Months 1–6 | Establish core project context & basic automation | Project initialization MVP, basic data model, onboarding/offboarding, progress dashboard, RBAC, Teams/SharePoint integration | 4–6 FTE |
| **Phase 2 — Intelligence & Quality** | Months 6–12 | Embed quality and enable learning | Data validation & classification, knowledge capture framework, basic AI rules engine, unified access abstraction layer, reference data management | 6–8 FTE |
| **Phase 3 — Scale & Optimization** | Months 12+ | Extend to all GBAs, drive adoption | Domain-specific AI agents per GBA, advanced knowledge graph, portfolio governance, multi-project resource management, compliance automation | 8–10 FTE |

**Module M01 (Project Initialization & Provisioning)** was selected as the first fully worked demonstration module, used to validate the DDDM methodology end-to-end (requirements → data model → workflows → API spec → prototype → architecture review via PR).

---

## 6. Repository Structure

The `ram_upe` GitHub repository serves as the living knowledge base and demo environment for UPE's architecture and design methodology.

### 6.1 Root Structure (branch `main`)

```
ram_upe/
├── .plans/                        Structured project plans (e.g. upe-knowledge-repo-demo/PLAN.md, START-PROMPT.md)
├── .excalidraw-copilot/            Excalidraw diagram authoring support
├── azure-pipelines.yml             CI/CD pipeline definition
├── logo.svg
├── docs/                           Source strategy & discovery documents
├── prompts/                        Reusable LLM prompt library (design framework)
├── src/                            Working source materials (chat logs, vendor research)
└── knowledge-base/                 DDDM-governed architecture & module knowledge base
```

### 6.2 `docs/` — Strategic Source Material
| File | Purpose |
|---|---|
| `UPE_Executive_Summary_v1.md` | Vision, 14 domains, phasing, KPIs, critical success factors |
| `UPE_Functional_Blocks_v1.md` / `.pdf` | Full 175+ capability inventory across 14 domains |
| `brainstorming.md` | Early capability mind-map, tech stack rationale, "the how" |
| `upe-strategic-assessment.okf.yaml` | Structured strategic assessment (OKF format) |
| `upe-okf/` | Supporting OKF-format artifacts |
| `pi-beginner-deployment-guide.md/.docx` | Deployment guide (PI-related infrastructure) |
| `prompt.md` | Source prompt material |
| `UPE-AI-architecture.excalidraw` | Visual AI architecture diagram (editable) |

### 6.3 `src/` — Working Materials
| Folder | Purpose |
|---|---|
| `src/loop/` | Iterative working notes (e.g. Copilot "sparing session" — layered architecture exploration) |
| `src/chat/` | Architect chat transcripts (raw discussion capturing real-time decisions) |
| `src/moms/` | Meeting minutes |
| `src/vendors/` | Vendor research — AVEVA, Autodesk, Hexagon, including validation rules and product deep-dives |

### 6.4 `prompts/` — Reusable Design Prompts
| File | Purpose |
|---|---|
| `LLM-Native Product Design Framework.md` | The foundational prompt defining the DDDM methodology used to drive the knowledge-base build-out |

### 6.5 `knowledge-base/` — Governed Architecture & Module Knowledge (DDDM-managed)

This is the actively governed part of the repository, structured to enforce the principle that **`main` holds only approved artifacts**, while module development occurs on feature branches.

**On `main` (approved baseline):**
```
knowledge-base/
├── master.md                       Living architecture map: vision, 14 domains, module registry, ADRs
├── 00_index.md                     Complete inventory of all artifacts (no orphans)
├── 00_principles.md                DDDM methodology, YAML standard, ID scheme, merge gates
├── 00_glossary.md                  Canonical terminology
├── 00_changelog.md                 Global change history
├── demo_script.md                  Stakeholder demo script
├── architecture/
│   ├── arch_overview.md            7-layer stack, build-vs-buy strategy, Azure/open standards
│   ├── module_interfaces.md        Interface contracts (CRM, HR, ERP, M365, CDE, Template, KG)
│   └── decisions/
│       └── ADR-0001-docs-as-data.md   Decision to adopt Markdown+Mermaid+Git as source of truth
└── reports/
    └── stakeholder_brief_*.md      Derived, point-in-time stakeholder briefs
```

**On feature branches (e.g. `feature/m01-project-initialization`, merged via reviewed Pull Requests):**
```
knowledge-base/
├── modules/m01_project_initialization/
│   ├── index.md                    Module purpose, scope, dependencies
│   ├── requirements.md             25+ requirements with stable IDs (REQ-M01-*)
│   ├── data_model.md               13 entities, Mermaid ERD
│   ├── workflows.md                State machine, failure/retry flows
│   ├── api_spec.md                 REST endpoints, events, error codes
│   └── backlog.md                  MVP tasks, definition of done
├── backlog/forks/
│   └── project-*-module.md         Design brief: hypothesis, requirements delta, merge checklist
├── sessions/
│   └── *_llm_session.md            Logged LLM design sessions for traceability
└── prototypes/
    └── sprint-01_*/prototype_prompt.md   Self-contained UI generation prompt (v0.dev/Claude/Replit)
```

**Governance flow:** idea → feature branch (LLM-assisted design) → Pull Request (architecture review checklist + explicit decision points) → merge to `main` → `master.md` and `00_index.md` updated → `00_changelog.md` entry recorded.

---

## 7. Key Risks and Open Questions

| Area | Open Question |
|---|---|
| Data model | How to establish a unified data model while supporting discipline-specific variation? |
| Scope boundary | What is the relationship between UPE, DMS, and PLM — and is a dedicated DMS even needed? |
| Governance | Who owns data quality and stewardship per domain (DAMA-DMBOK stewardship roles)? |
| Funding | How is ongoing platform evolution funded — central product budget vs. project budgets? |
| GBA autonomy | How to balance central standards with GBA-specific process variation? |
| AI governance | How to reconcile ungoverned bottom-up AI adoption with enterprise AI risk management (NIST AI RMF)? |

---

## 8. Standards and Frameworks Referenced

- **Architecture methodology:** TOGAF
- **Data management:** DAMA-DMBOK
- **Data warehouse design:** Kimball Dimensional Modeling, Data Vault 2.0
- **BIM / open data standards:** IFC, bSDD (buildingSMART Data Dictionary), BCF, IDS, ISO 19650, ISO 15926/CFIHOS
- **Integration standards:** Open BIM, W3C, OASIS
- **Project management:** PMI PMBOK, Agile/Scrum
- **AI governance:** NIST AI RMF

---

## 9. Critical Success Factors

1. Executive sponsorship treating UPE as a business priority, not an IT side project.
2. Clear data governance under a DAMA-DMBOK-aligned framework with named data stewards.
3. Iterative, outcome-focused delivery starting from highest-value use cases (Phase 1 MVP).
4. Deep vendor partnership with Microsoft and Autodesk to avoid reinventing commodity capability.
5. Structured change management — training, communication, and adoption incentives.
6. Continuous capture of lessons learned, enabled by the DDDM session-logging discipline.
7. Deliberate avoidance of over-engineering — MVP first, capability added iteratively.
