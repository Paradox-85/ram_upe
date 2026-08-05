# UPE OKF Knowledge Base Repository Options Analysis: Comparative Evaluation of Alternatives A, B, and C

**Document ID:** `.pi/review/2026-08-05-upe-okf-repository-options-analysis.md`  
**Date:** 2026-08-05  
**Status:** Architecture Discussion Report — explanatory analysis for architect review. It is not a plan, not an implementation decision, and not a migration authorization.
**Analyzed Local Commit/Branch:** Primary workspace `main` at commit `44efc15d27d0989bf587ff77fde73ac161fa1d02`; separately inspected feature branch `feature/m01-project-initialization` at commit `cf3cbb4`. Research artifacts were produced on ephemeral `pi-agent-*` branches and materialized under `.pi/`; those research commits are not part of `main`.  
**Upstream OKF Baseline:** Open Knowledge Format (OKF) v0.2 at commit `930b65fc3f5619d5d0591f88c72ebae8b848d60d` (GoogleCloudPlatform/knowledge-catalog, inspected upstream state dated 2026-08-04).  
**Scope:** Architectural evaluation of physical directory layouts, metadata schemas, governance models, cross-cutting knowledge links, human/AI ergonomics, and validation mechanics across three candidate implementations for the Unified Project Execution environment (UPE) Knowledge Base.  
**Decision Statement:** This report compares three target implementation options (Alternative A: Concept-Type-Oriented Unified Graph; Alternative B: Domain-Oriented Coordinated Bundles; Alternative C: Shared Core plus Module Subtrees and Generated Views) and establishes a conditional recommendation for human governance review. It does not execute repository restructuring, modify canonical files, or authorize branch migration.

---

## 1. Title, Status, Analyzed Local Commit/Branch, Upstream OKF Commit, Scope, and Decision Statement

This document explains, with examples, how three repository organization alternatives relate to the Open Knowledge Format (OKF) v0.2 and to the actual UPE repository. It is an architecture discussion report for review with colleagues; it is not a plan and does not authorize migration.

- **Title:** UPE OKF Knowledge Base Repository Options Analysis: Comparative Evaluation of Alternatives A, B, and C
- **Document Path:** `.pi/review/2026-08-05-upe-okf-repository-options-analysis.md`
- **Status:** Architecture Discussion Report — explanatory analysis for architect review; not a plan or migration authorization.
- **Analyzed Local Commit / Branch:** Primary workspace `main` at `44efc15d27d0989bf587ff77fde73ac161fa1d02`; feature branch `feature/m01-project-initialization` at `cf3cbb4`. Ephemeral research commits are not on `main`.
- **Upstream OKF Baseline Commit:** Open Knowledge Format (OKF) v0.2 specification and reference implementation at commit `930b65fc3f5619d5d0591f88c72ebae8b848d60d` (`GoogleCloudPlatform/knowledge-catalog`, inspected state dated 2026-08-04).
- **Scope:** Complete architectural evaluation of physical directory structures, metadata schemas, governance frameworks, cross-cutting knowledge handling, human and AI ergonomics, and validation mechanics for the UPE Knowledge Base across 14 functional domains and 175+ capabilities.
- **Purpose:** Compare three candidate physical organizations for a future UPE OKF Knowledge Base, explain their concepts with examples, and give a conditional recommendation for architect discussion. It does not execute restructuring, modify canonical source files, or authorize branch migration.

---

## 2. Executive Summary

This report evaluates physical repository layouts and knowledge architecture models for the Unified Project Execution environment (UPE) Knowledge Base under the Open Knowledge Format (OKF) v0.2 specification. The repository currently exhibits a hybrid authority problem: files declaring KB governance coexist with primary-looking documents in `docs/`, unregistered source material in `src/`, operational plans in `.plans/`, and structured M01 content isolated on a feature branch. Current authority labels are evidence to audit, not automatic proof of governance approval.

To resolve these structural tensions and establish a scalable, AI-ready, and enterprise-governed knowledge system, three architectural alternatives are evaluated in detail:

1. **Alternative A (Concept-Type-Oriented Unified Graph):** A proposed single OKF bundle organized primarily by concept type (`requirements/`, `capabilities/`, `entities/`, `workflows/`, `decisions/`, `interfaces/`). Domain and module affiliations are graph relationships and metadata.
2. **Alternative B (Domain-Oriented Organization):** A proposed domain-first tree using neutral business/knowledge domain slugs such as `domains/project-lifecycle/`. The report evaluates both single-bundle domain subtrees and true coordinated bundles; the latter are not natively federated by OKF v0.2.
3. **Alternative C (Shared Core + Module Subtrees + Generated Views):** A proposed single-bundle hybrid where `core/` owns shared enterprise concepts, `modules/m01-project-initialization/` and other module subtrees own solution-specific concepts, and reproducible non-authoritative `views/` provide domain/type/status navigation.

### Synthesis of Scout Contradictions & Conditional Recommendation

Prior research produced contradictory recommendations: the upstream OKF scout favored Alternative A for its native alignment with graph queries and OKF single-bundle ergonomics, while the local repository scout favored Alternative B (progressing to Alternative C) due to alignment with team mental models and the existing M01 feature branch.

The contradiction is not fully resolvable without governance decisions: Alternative A optimizes machine-oriented typed navigation; Alternative B optimizes domain ownership; Alternative C attempts to balance module ownership and cross-cutting generated views. The audit must validate which ownership model matches UPE operations.

**Conditional Recommendation:** Evaluate **Alternative C (Shared Core + Module Subtrees + Generated Views)** as the leading candidate, implemented as a **single proposed OKF bundle** and combined with Alternative A's typed metadata and generated concept views. This recommendation is not approved and depends on stable module ownership, an agreed shared-versus-module placement rule, and reliable validation/view generation.
- **Canonical Storage:** `core/` owns shared enterprise concepts; `modules/<module>/` owns module-specific concepts. Modules and functional domains remain separate many-to-many concepts.
- **Cross-Cutting Views:** `views/` aggregates capability, domain, module, status, maturity, and traceability navigation reproducibly; generated views are non-authoritative.
- **Traceability Contract:** Future approved KB concepts and decisions are authoritative. `docs/` may contain generated or manually synthesized approved derived representations only when they record KB revision, knowledge references, approval evidence, freshness, supersession, manual-edit policy, and drift controls. Current documents remain provisional until evaluated.

Implementation must proceed through explicit, approval-gated phases. Migration execution remains blocked pending Chief Architect review and approval of the decision framework in Section 17.

---

## 3. Current UPE Repository & Authority Baseline

Read-only verification of `main` at `44efc15` identifies 96 tracked files. An earlier scout reported 81; this discrepancy is retained as a research-quality warning and the formal inventory must separate tracked, untracked, branch-only, binary, and generated artifacts. The feature branch `feature/m01-project-initialization` was inspected separately.

```
UPE Repository Baseline (Commit 44efc15 / Branch feature/m01-project-initialization)
├── .plans/                                [UNGOVERNED OPERATIONAL PLANS]
│   └── create-upe-architecture-artifacts/
│       ├── PLAN.md                        (lines 1–123)
│       └── START-PROMPT.md                (lines 1–370)
├── docs/                                  [COMPETING HUMAN AUTHORITY / DERIVED]
│   ├── UPE_Executive_Summary_v1.md        (368 lines; primary vision & 14 domains)
│   ├── UPE_Functional_Blocks_v1.md        (1,007 lines; 175+ capability outline)
│   ├── upe-strategic-assessment.okf.yaml  (920 lines; proposed OKF assessment manifest)
│   └── upe-okf/                           (9 tracked files; draft/generated assessment set)
│       ├── index.md                       (65 lines; draft assessment index)
│       └── log.md                         (18 lines; assessment revision log)
├── knowledge-base/                        [DECLARED CANONICAL KNOWLEDGE BASE]
│   ├── 00_index.md                        (89 lines; declared KB inventory)
│   ├── 00_principles.md                   (187 lines; declared DDDM/metadata rules)
│   ├── 00_glossary.md                     (62 lines; declared terminology)
│   ├── master.md                          (199 lines; 14 functional-domain definitions)
│   ├── architecture/
│   │   ├── arch_overview.md               (7-layer architecture stack)
│   │   ├── module_interfaces.md           (M01 interface contracts)
│   │   └── decisions/
│   │       └── ADR-0001-docs-as-data.md   (records a Docs-as-Data decision claim; approval evidence to verify)
│   ├── raw-input/                         (11 files; captured business inputs)
│   └── modules/m01_project_initialization/[FEATURE BRANCH ONLY: cf3cbb4]
│       ├── index.md                       (module overview)
│       ├── requirements.md                (25+ requirements with stable IDs)
│       ├── data_model.md                  (13 entities & ERD)
│       └── workflows.md                   (provisioning state machine)
├── prompts/                               [DEVELOPMENT TEMPLATES]
│   └── LLM-Native Product Design Framework.md
└── src/                                   [UNINDEXED RAW SOURCES]
    ├── moms/                              (3 text + 3 VTT launch meeting transcripts)
    └── vendors/                           (20 vendor technical evaluations)
```

### Critical Baseline Findings & Authority Inversions

1. **Authority tension:** Primary-looking specifications (`docs/UPE_Executive_Summary_v1.md` and `docs/UPE_Functional_Blocks_v1.md`) reside in `docs/`, while `knowledge-base/master.md:190-199` lists them as source documents. `knowledge-base/00_principles.md` declares KB authority, but current statuses and approval claims must be checked against actual governance evidence before being accepted.
2. **Feature Branch Isolation:** Complete, structured module specifications exist only for Module M01 on branch `feature/m01-project-initialization` (`knowledge-base/modules/m01_project_initialization/`). On `main`, these paths are replaced by stub markers (`knowledge-base/00_index.md:lines 30–35`).
3. **Unindexed Sources:** 26 raw material files in `src/moms/` and `src/vendors/` lack OKF frontmatter, stable IDs, and registration in `knowledge-base/00_index.md`.
4. **Operational Leakage:** Active execution plans in `.plans/` run outside knowledge base governance, lacking lifecycle metadata, versioning, and status checks.

---

## 4. Terminology & Conceptual Model

To eliminate ambiguity across human stakeholders, AI agents, and automated tools, canonical definitions are established below. Every concept includes a concrete UPE example and explicit qualification distinguishing illustrative examples from verified repository facts.

```
                                  UPE KNOWLEDGE CONCEPTUAL MODEL
                                  
 [ Source Record / Material ] ──(yields)──► [ Source Statement / Claim ]
            │                                         │
            │ (justifies)                             │ (formalizes into)
            ▼                                         ▼
   [ Business Need ] ────────(drives)────────► [ Requirement ] ──(maps to)──► [ Functional Domain ]
            │                                         │                              │
            │ (addressed by)                          │ (implemented by)             │ (groups)
            ▼                                         ▼                              ▼
    [ Capability ] ───────────────────────► [ Module / System ] ◄─────────── [ Process / Workflow ]
            │                                         │
            │ (evaluated in)                          │ (defines)
            ▼                                         ▼
   [ Architecture Option ] ──(decided via)──► [ Decision / ADR ] ──(produces)──► [ Implementation Item ]
                                                      │                                  │
                                                      │ (validated by)                   │ (produces)
                                                      ▼                                  ▼
                                            [ Validation Record ] ◄─────── [ Approved Document ]
```

### Canonical Definitions

1. **Knowledge Object / Concept:** An addressable unit of KB knowledge serialized as Markdown plus OKF-compatible frontmatter. Stable UPE IDs are proposed where path-derived OKF identity alone is insufficient for link stability. *Verified example:* feature-branch `REQ-M01-001` requires at least 50% reduction in average project-initialization time (`feature/m01-project-initialization:knowledge-base/modules/m01_project_initialization/requirements.md:22`).
2. **Source:** A person, meeting, document, system, dataset, or event from which knowledge originates. *Illustrative target ID:* `SRC-MOM-2026-05-26` for the raw file whose literal legacy filename uses “Unified Production Environment”; that filename is not the governed UPE name.
3. **Source Record:** Metadata that registers the original source, provenance, date, location, repository copy, access constraints, checksum, freshness, and extraction state. A raw binary or transcript may be linked rather than rewritten.
4. **Source Statement / Claim:** An atomic assertion extracted from a source before interpretation. *Illustrative example:* `CLM-001: Project setup requires several disconnected manual steps`; this must not be promoted to a verified fact until linked to an exact source passage.
5. **Finding:** An analytical conclusion derived from one or more claims. *Illustrative example:* `FND-001: fragmented provisioning creates avoidable setup delay`. Findings must retain source links and inference status.
6. **Business Need:** A stakeholder outcome or problem expressed without prescribing a solution. *Illustrative example:* reduce project initialization effort while preserving controls.
7. **Requirement:** A testable statement the solution must satisfy. *Verified example:* feature-branch `REQ-M01-005` requires project managers to configure standard projects without IT involvement (`feature/m01-project-initialization:knowledge-base/modules/m01_project_initialization/requirements.md:26`).
8. **Capability:** A stable statement of what UPE must be able to do, independent of a specific implementation. *Illustrative example:* `CAP-PROVISION-WORKSPACE`; the final ID and wording require capability-catalog audit.
9. **Functional Domain:** A problem-oriented business or knowledge area grouping related needs, capabilities, policies, and vocabulary. Current `knowledge-base/master.md:42-59` describes 14 functional domains; their boundaries and names must be preserved as source evidence pending review.
10. **Module:** A bounded solution, ownership, or implementation component that realizes capabilities and exposes contracts. M01 feature-branch content is verified evidence of a module-oriented pattern, but a one-to-one mapping between all 14 domains and M01–M14 modules is unresolved.
11. **System:** An enterprise application or platform with which UPE interacts, such as CRM, ERP, identity, or CDE platforms. Current interface documentation supplies integration evidence (`knowledge-base/architecture/module_interfaces.md`).
12. **Process / Workflow:** An ordered sequence of human and automated steps with states and transitions. The M01 feature branch contains a provisioning workflow, but IDs such as `WKF-M01-01` in this report are illustrative proposals, not current facts.
13. **Use Case / User Journey:** An end-to-end scenario describing how a stakeholder achieves an outcome. *Illustrative example:* a project manager initiates a new project and receives provisioned workspaces.
14. **Data Entity:** A governed information object with attributes, relationships, ownership, and lifecycle. *Verified evidence:* the M01 feature-branch data model contains 13 entities; any proposed stable entity ID requires design approval.
15. **Interface / Event:** A synchronous or asynchronous contract between modules or systems. *Verified evidence:* `knowledge-base/architecture/module_interfaces.md:24-34` documents an Opportunity-to-Project seed-data interface; event IDs and names in target examples are proposals.
16. **Architecture View:** A stakeholder-specific representation of architecture, such as integration, data, security, or deployment. The current seven-layer architecture evidence is in `knowledge-base/architecture/arch_overview.md`; generated diagrams must not become independent authority.
17. **Architecture Option:** A candidate way to satisfy requirements before a decision. *Illustrative example:* direct API orchestration versus event-driven provisioning.
18. **Decision / ADR:** A record of context, evaluated options, decision, authority, and consequences. `knowledge-base/architecture/decisions/ADR-0001-docs-as-data.md` records a current decision claim; its approval evidence must be verified rather than inferred from path or status alone.
19. **Standard / Policy:** A mandatory rule or constraint issued by an authorized body. *Illustrative example:* an approved authentication policy; no policy should be invented from common practice.
20. **Assumption / Hypothesis / Discussion / Open Question / Risk:** Distinct uncertainty objects that must not be collapsed into decisions. Illustrative IDs may be used in target design, but current strategic-assessment risks must be cited by their actual identifiers and passages.
21. **Prototype / Experiment:** A bounded artifact used to test feasibility or an option. *Verified evidence:* the feature branch contains prototype material with current ID `prototype-sprint01-m01`; its target classification remains proposed.
22. **Implementation Item:** A task, backlog item, change, or PR implementing a requirement or decision. Existing M01 backlog entries use their current table identifiers; `TSK-*` identifiers shown in target examples are illustrative.
23. **Validation Record / Evidence:** A test result, review record, benchmark, or sign-off showing whether requirements and decisions are satisfied. *Illustrative target ID:* `VAL-M01-001`.
24. **Release:** A governed version or baseline of selected modules, capabilities, knowledge, and evidence. Release composition is unresolved; no current release is promoted by this report.
25. **Derived Document:** An approved representation synthesized from eligible KB knowledge, either generated or manually synthesized under a documented traceability and drift contract. It never overrides the KB. Current reports are provisional until lineage and approval are verified.
26. **Generated View / Index:** A deterministic, reproducible projection built from canonical metadata and links. *Illustrative proposal:* `views/capability-matrix.md`. Generated views are non-authoritative and must carry a non-editable/generated marker.
27. **OKF Bundle:** A directory tree containing OKF Markdown concepts. In OKF v0.2, `index.md` and `log.md` are reserved deterministic artifacts when present, not mandatory files for every bundle. Treating the future UPE KB as one bundle is a proposal; the current `knowledge-base/` is not proven to be a conformant OKF bundle.
28. **Provenance:** Evidence connecting a concept to source records, authorship/origin, extraction, verification, and Git history. Proposed UPE source links must use actual registered source identifiers.
29. **Trust / Verification:** Metadata recording who or what verified a claim, when, and by what method. Example values are proposals until supported by actual review evidence; agents must never invent verifiers or dates.
30. **Freshness:** Metadata and policy indicating when knowledge was checked and when it becomes stale. `docs/upe-okf/index.md:10` currently contains `stale_after: 2026-11-01`; this is file-specific evidence, not a KB-wide policy.
31. **Maturity:** The degree of knowledge development, separate from governance status. Candidate levels require definition, entry/exit criteria, ownership, transition authority, and approval before use.
32. **Governance Status:** The formal review/decision state. Existing `status` values are source assertions and do not by themselves prove approval. The controlled vocabulary and transitions remain approval-pending.
33. **Supersession:** Explicit lineage connecting a replacement concept to the concept it supersedes while preserving history. `supersedes` and `superseded_by` are proposed UPE fields unless upstream OKF semantics are shown to cover the need.
34. **Approval Eligibility:** A proposed rule determining whether a concept may contribute to approved documents, considering maturity, governance status, provenance, verification, freshness, contradictions, supersession, and decision authority. Exact thresholds require human approval.

---

## 5. Rigorous Breakdown: Domain vs. Module

A critical finding from repository analysis is the conflation of **Domain** and **Module** boundaries across baseline files.

```
                      DOMAIN vs. MODULE RELATIONSHIP IN UPE
                      
   PROBLEM SPACE (Domains)                         SOLUTION SPACE (Modules)
+---------------------------+                   +---------------------------+
| Domain 01: Project        |──(implemented by)►| Module M01: Project       |
| Lifecycle Management      |                   | Initialization Service    |
+---------------------------+                   +---------------------------+
| Domain 02: User & Access  |──(implemented by)►| Module M02: User Access   |
| Management                |                   | Management Service        |
+---------------------------+                   +---------------------------+
| Domain 07: System         |                   | Module M07: iPaaS         |
| Integration Hub           |─┐               ┌►| Integration Gateway       |
+---------------------------+ │               │ +---------------------------+
                              │   MANY-TO-MANY│
                              ├───────────────┼─► Module M10: Technical
                              │               │   Foundations Engine
                              │               │ +---------------------------+
                              └───────────────┴─► Module M13: Tech
                                                  Enablement Services
```

### Definitions & Structural Separation

- **Domain (Problem Space):** An abstract business function, organizational area, or problem context. Domains define *what* business capabilities exist and *why* they are needed. They are stable, enduring, and rarely change unless the enterprise business model shifts.  
  *Baseline Citation:* `docs/UPE_Executive_Summary_v1.md:lines 85–120` defines 14 functional domains.
- **Module (Solution Space):** A bounded software package, service, repository folder, or deployment unit owned by an engineering team. Modules define *how* capabilities are built, maintained, and delivered. Modules may evolve, split, merge, or be replaced without altering the underlying business domain.  
  *Baseline Citation:* `knowledge-base/master.md:lines 120–135` lists modules M01 through M14.

### Local Scout Finding: Unresolved Terminology & Conflation

The current repository conflates domain and module terminology:
1. `knowledge-base/master.md:lines 40–60` lists "14 Functional Domains" using codes `M01` through `M14`.
2. `knowledge-base/master.md:lines 120–135` presents a "Module Registry" mapping codes `M01`–`M14` 1:1 to those same 14 names.
3. `docs/UPE_Functional_Blocks_v1.md:lines 10–50` refers to "14 Functional Blocks" as structural headings, introducing a third term ("Functional Block") without defining its relationship to domains or modules.

*Finding Statement:* The repository currently assumes a rigid 1:1 mapping between domains and modules. In enterprise engineering architecture, this assumption fails when cross-cutting capabilities arise (e.g., Domain 07: System Integration requires capabilities implemented across Module M01, Module M07, Module M10, and Module M13). Unless UPE explicitly decides otherwise, the knowledge base architecture must support a **many-to-many relationship** where a module can fulfill capabilities across multiple domains, and a domain's capabilities can span multiple modules.

---

## 6. Upstream OKF v0.2 Verified Semantics vs. UPE Extensions

Analysis of the upstream OKF reference repository (`GoogleCloudPlatform/knowledge-catalog` at commit `930b65fc3f5619d5d0591f88c72ebae8b848d60d`) establishes the exact semantics of OKF v0.2.

```
+-----------------------------------------------------------------------------------+
|                            OKF v0.2 FILE STRUCTURE                                |
|                                                                                   |
|  ---                                                                              |
|  type: requirement                       ◄── ONLY REQUIRED KEY IN UPSTREAM OKF       |
|  # UPE Custom Extensions (Permissive)                                             |
|  id: REQ-M01-001                                                                  |
|  governance_status: approved                                                      |
|  maturity_level: pilot                                                            |
|  sources: [{ id: SRC-01, resource: ... }]                                         |
|  ---                                                                              |
|                                                                                   |
|  # Markdown Document Body                                                         |
|  Path-derived ID: folder/subfolder/filename (without .md)                         |
|  Single-bundle catalog: index.md                                                  |
|  Revision audit log: log.md                                                        |
+-----------------------------------------------------------------------------------+
```

### Verified Upstream OKF v0.2 Semantics

1. **Required Keys:** Upstream reference validation requires only non-empty `type` (`REQUIRED_FRONTMATTER_KEYS = ("type",)` at [`okf/src/reference_agent/bundle/document.py#L13`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/930b65fc3f5619d5d0591f88c72ebae8b848d60d/okf/src/reference_agent/bundle/document.py#L13)). Other fields are optional for minimum OKF conformance.
2. **Path-Derived Identifiers:** OKF identifies a concept by its path relative to the bundle root without `.md`; UPE stable semantic IDs are an additional proposal for move resilience.
3. **Reserved Index & Log Files:** `index.md` and `log.md` have reserved deterministic semantics when present and may be generated by the reference workflow; they are not mandatory files in every conforming bundle.
4. **Permissive Validation:** Conforming consumers tolerate unknown types, keys, and unresolved links. UPE therefore needs a separate, approval-gated governance schema for stricter enterprise checks.
5. **Single-Bundle Focus:** OKF v0.2 specifies bundle-local behavior and does not define multi-bundle federation, a global registry, or cross-bundle consistency. Alternative B multi-bundle mode would require UPE-specific coordination tooling.

### Qualification of Enterprise Governance Sufficiency

Minimum OKF v0.2 conformance is not sufficient by itself for UPE governance because it does not require UPE-specific ownership, approval, traceability, transition, or document-eligibility rules. This is not a defect in OKF; those enterprise semantics are intentionally left to adopters. Requirements such as ISO 19650 alignment or discipline classification must be demonstrated and approved rather than assumed.

### Proposed UPE Extensions Requiring Approval

The following example illustrates candidate fields to evaluate. None is mandatory or approved yet. Each field must be retained only if it supports retrieval, trust, provenance, lifecycle, validation, synthesis, or impact analysis and if existing OKF semantics do not already cover the need.

```yaml
# Illustrative proposal — not current approved metadata
type: requirement                 # upstream OKF-required key
id: REQ-EXAMPLE-001               # proposed stable semantic ID
title: "Provision an approved project workspace"
domains: [project-lifecycle]       # proposed relationship to problem space
modules: [m01-project-initialization]  # proposed relationship to solution owner
maturity: formulated              # proposed knowledge-development dimension
status: under-review              # proposed governance dimension
sources:                           # use OKF-native provenance semantics where sufficient
  - id: SRC-EXAMPLE-001
    resource: "sources/example.md"
verified: []                       # no verifier may be invented
stale_after: "<policy-derived-date>"
supersedes: []                     # proposed only if required beyond links
```

---

## 7. Alternative A — Concept-Type-Oriented Unified Graph

Alternative A organizes the physical repository strictly by **capability concept type**. Domain and module affiliations are detached from physical folder paths and stored entirely as YAML frontmatter attributes.

### Target Directory Layout (Alternative A)

```
knowledge-base/                              [SINGLE OKF BUNDLE ROOT]
├── index.md                                 [OKF Master Catalog Manifest]
├── log.md                                   [OKF Global Revision Log]
├── sources/                                 [Source Records & Claims]
│   ├── SRC-MOM-2026-05-26.md
│   └── SRC-VND-AVEVA-01.md
├── needs/                                   [Business Needs]
│   └── BND-001-fast-project-startup.md
├── requirements/                            [Functional & System Requirements]
│   ├── REQ-M01-001-acc-provisioning.md
│   └── REQ-M02-001-role-assignment.md
├── capabilities/                            [175+ Functional Capabilities]
│   └── CAP-M01-01-cde-workspace.md
├── entities/                                [Domain Data Entities]
│   └── ENT-Project.md
├── workflows/                               [Process State Machines]
│   └── WKF-M01-01-provisioning-flow.md
├── interfaces/                              [OpenAPI Specs & Event Contracts]
│   └── IF-M01-CRM-001.md
├── decisions/                               [Architecture Decision Records]
│   └── ADR-0001-docs-as-data.md
├── validation/                              [Validation Records & Evidence]
│   └── VAL-M01-001-webhook-test.md
└── views/                                   [Generated Non-Authoritative Views]
    ├── domain-01-lifecycle-view.md
    └── module-m01-summary-view.md
```

### Illustrative Miniature OKF Example (Alternative A)

> **Proposal, not a current UPE requirement or approval record.** IDs, values, paths, verifiers, dates, and service levels below exist only to demonstrate structure.

**Proposed File Path:** `kb/requirements/REQ-EXAMPLE-001-workspace-provisioning.md`
```markdown
---
type: requirement
id: REQ-EXAMPLE-001
title: "Provision an approved project workspace"
domains: [project-lifecycle]
modules: [m01-project-initialization]
maturity: formulated
status: draft
sources:
  - id: SRC-EXAMPLE-001
    resource: "sources/SRC-EXAMPLE-001.md"
verified: []
stale_after: "<policy-derived-date>"
related:
  - "capabilities/CAP-EXAMPLE-001.md"
  - "entities/ENT-EXAMPLE-PROJECT.md"
---

# REQ-EXAMPLE-001: Provision an Approved Project Workspace

## Statement
Upon receipt of an approved project initialization event from CRM, the UPE platform shall automatically invoke the Autodesk Construction Cloud (ACC) API to create a project folder structure matching the enterprise standard template within 60 seconds.

## Validation Criteria
- Verification via automated Postman test suite `VAL-M01-001`.
- Project folder template ID matches the assigned engineering business unit.
```

### Current UPE File Migration Mapping (Alternative A)

| Current Baseline File | Proposed Target Location (Alternative A) | Migration Action |
|---|---|---|
| `knowledge-base/00_principles.md` | `knowledge-base/decisions/ADR-0000-principles.md` | Convert to typed decision artifact |
| `docs/UPE_Executive_Summary_v1.md` | `knowledge-base/needs/BND-000-executive-vision.md` | Split vision into atomic business needs |
| `docs/UPE_Functional_Blocks_v1.md` | `knowledge-base/capabilities/CAP-M01-01...CAP-M14-99.md` | Decompose 175+ outline items into individual capability files |
| `feature/m01.../requirements.md` | `knowledge-base/requirements/REQ-M01-001...REQ-M01-025.md` | Extract 25 requirements into typed requirement files |
| `feature/m01.../data_model.md` | `knowledge-base/entities/ENT-Project.md` (and 12 others) | Split ERD into individual entity concept files |
| `src/moms/Launch_Series_1.txt` | `knowledge-base/sources/SRC-MOM-2026-05-26.md` | Wrap raw text with source frontmatter |

### Architectural Evaluation (Alternative A)

- **Ownership Model:** Cross-cutting "Type Stewards" own directory mechanics (e.g., Requirement Lead owns `requirements/`), but domain owners must constantly filter files by metadata attributes (`domain: domain-01`).
- **Human Navigation Ergonomics:** Poor for domain engineers. A developer working on Module M01 must navigate across 8 separate directories (`requirements/`, `entities/`, `workflows/`, `decisions/`, `interfaces/`) to inspect M01 specifications.
- **AI Retrieval Ergonomics:** Excellent for structured graph compilation and query execution ("Return all entities linked to REQ-M01-001"). AI agents easily parse homogeneous folders.
- **Review & Branch Behavior:** High pull request collision risk. PRs modifying Module M01 impact root directories shared by all 14 domains, leading to Git merge conflicts in `requirements/index.md`.
- **Validation Mechanics:** Highly straightforward. A single JSON Schema validator applies uniformly to all files inside `requirements/`.
- **Strengths:** Native single-bundle OKF alignment; uniform validation schemas per directory; powerful AI graph querying.
- **Weaknesses:** Destroys team domain boundaries; severe file fragmentation (thousands of small files); high Git merge friction; unintuitive human navigation.
- **Failure Modes:** Domain teams lose track of module boundaries; orphaned concepts accumulate when metadata tags are misconfigured.
- **Prerequisites:** Automated graph query tooling; strict CI metadata linters.
- **When to Choose:** Choose if UPE is authored primarily by AI agents via programmatic APIs and human engineers interact exclusively through rendered web portals.

---

## 8. Alternative B — Domain-Oriented Coordinated Bundles

Alternative B organizes concepts by **functional domain**, understood as a stable business/knowledge problem space rather than a module code. The 14 current domain definitions provide candidate evidence, but their ownership and boundaries must be validated before creating physical subtrees.

```text
Alternative B proposed modes
SINGLE-BUNDLE DOMAIN HIERARCHY                 TRUE MULTI-BUNDLE FEDERATION
kb/                                             kb-catalog/
├── sources/                                    ├── catalog.yaml  # custom UPE registry
├── core/                                       ├── project-lifecycle-bundle/
└── domains/                                    └── information-management-bundle/
    ├── project-lifecycle/
    └── information-management/
```

### Single-Bundle Domain Subtrees vs. True Multi-Bundle Federation

Alternative B must be evaluated under two distinct physical modes:
1. **Single-Bundle Domain Hierarchy:** One proposed bundle contains domain subtrees such as `domains/project-lifecycle/`. This is compatible with OKF's directory-neutral model; optional generated `index.md`/`log.md` artifacts may support navigation and history.
2. **True Multi-Bundle Federation:** Each domain is a separate OKF bundle. Upstream OKF v0.2 does not define federation, cross-bundle identity, or consistency, so UPE would need a custom registry, dependency/version policy, and federation validator. This mode has materially higher governance risk.

### Target Directory Layout (Alternative B — Single-Bundle Mode)

```
kb/                                         [PROPOSED SINGLE OKF BUNDLE]
├── sources/                                [registered raw and external sources]
├── core/                                   [shared principles, vocabulary, standards]
├── domains/
│   ├── project-lifecycle/                  [problem-space ownership]
│   │   ├── requirements/
│   │   ├── capabilities/
│   │   ├── processes/
│   │   ├── architecture/
│   │   └── decisions/
│   └── information-management/
├── governance/
└── views/                                  [generated cross-domain projections]
```

### Illustrative Miniature OKF Example (Alternative B)

> **Proposal:** a requirement owned by the Project Lifecycle domain; it may be implemented by several modules.

**Proposed File Path:** `kb/domains/project-lifecycle/requirements/REQ-EXAMPLE-001.md`

```markdown
---
type: requirement
id: REQ-EXAMPLE-001
title: "Provision an approved project workspace"
primary_domain: project-lifecycle
related_domains: [information-management, enterprise-integration]
implemented_by: [m01-project-initialization, cde-integration, identity-access]
maturity: formulated
status: draft
sources: [{ id: SRC-EXAMPLE-001, resource: "../../sources/SRC-EXAMPLE-001.md" }]
verified: []
---

# Illustrative requirement
The approved solution shall provision the required project workspace and roles according to governed templates.
```

### Architectural Evaluation (Alternative B)

- **Ownership Model:** A domain owner governs concepts whose primary business meaning belongs to that domain; module owners remain linked implementers, not owners of the domain folder by default.
- **Human Navigation:** Strong for stakeholders who think in business problem spaces, provided every cross-domain concept has one primary domain and generated backlinks.
- **AI Retrieval:** Good for domain-scoped questions; cross-domain retrieval requires stable IDs, explicit relationships, and generated graph indexes.
- **Review & Branch Behavior:** Domain-focused PRs are coherent, but shared concepts and cross-domain changes may touch several subtrees. Branch isolation is not guaranteed by the layout alone.
- **Validation Mechanics:** Requires multi-file parsing since requirements and entities are often grouped into catalog markdown files (`requirements.md`).
- **Strengths:** Excellent organizational fit; mirrors engineering team structure; isolates Git PRs; highly intuitive human navigation.
- **Weaknesses:** Cross-cutting knowledge (e.g., shared data entities used by M01, M03, and M07) suffers from duplication or weak linkage; true federation is unsupported by OKF v0.2.
- **Failure Modes:** Domain silos form; duplicate entity definitions emerge in multiple domain folders without central detection.
- **Prerequisites:** Cross-domain reference linting; central entity registry.
- **When to Choose:** Choose if domain teams operate independently with minimal shared data models and human readability is the highest priority.

---

## 9. Alternative C — Shared Core + Module Subtrees + Generated Views

Alternative C combines module-oriented physical ownership with concept-type and domain visibility. Canonical shared enterprise concepts live in `core/`; canonical solution-specific concepts live in `modules/<module>/`; automated validation generates non-authoritative, reproducible `views/` for domains, concept types, status, maturity, sources, and traceability.

```
Alternative C Data & Authority Architecture

CANONICAL AUTHORING LAYER (Source of Truth)          DERIVED PUBLISHING LAYER (Non-Authoritative)
[ modules/m01-.../requirements/*.md ] ─┐             ┌──► [ views/concept-types/requirements.md ]
[ modules/m01-.../capabilities/*.md ] ├─(generator)─┼──► [ views/domains/project-lifecycle.md ]
[ core/requirements/*.md ] ──────────┘             └──► [ views/traceability/source-to-doc.md ]
```

### Target Directory Layout (Alternative C)

```
kb/                                         [PROPOSED SINGLE OKF BUNDLE]
├── sources/                                [source records + preserved materials]
├── core/                                   [shared enterprise concepts]
│   ├── vision/
│   ├── principles/
│   ├── stakeholders/
│   ├── requirements/
│   ├── standards/
│   ├── data/
│   └── decisions/
├── modules/                                [solution/ownership components, not domains]
│   ├── m01-project-initialization/
│   │   ├── module.md
│   │   ├── requirements/
│   │   ├── capabilities/
│   │   ├── processes/
│   │   ├── data/
│   │   ├── interfaces/
│   │   ├── decisions/
│   │   ├── implementation/
│   │   └── validation/
│   └── <other-approved-module>/
├── governance/                             [schemas, vocabularies, transition rules]
└── views/                                  [generated, reproducible, non-authoritative]
    ├── domains/
    ├── concept-types/
    ├── status/
    ├── maturity/
    └── traceability/
```

### Illustrative OKF Example (Alternative C)

> **Proposal:** canonical module-owned knowledge remains OKF Markdown with frontmatter; generated views project the same metadata without becoming authority.

**Proposed Concept Path:** `kb/modules/m01-project-initialization/requirements/REQ-EXAMPLE-001.md`

```markdown
---
type: requirement
id: REQ-EXAMPLE-001
title: "Provision an approved project workspace"
modules: [m01-project-initialization]
domains: [project-lifecycle, information-management]
implements_capabilities: [CAP-EXAMPLE-001]
maturity: formulated
status: draft
sources: [{ id: SRC-EXAMPLE-001, resource: "../../../sources/SRC-EXAMPLE-001.md" }]
verified: []
---

# Illustrative module-owned requirement
The solution shall provision a governed project workspace using an approved template.
```

**Proposed Generated View Path:** `kb/views/domains/project-lifecycle.md`

```markdown
<!-- GENERATED, NON-AUTHORITATIVE — DO NOT EDIT -->
<!-- Inputs: core/**/*.md and modules/**/*.md; generator/version recorded at build time -->

# Project Lifecycle Domain View

| Concept | Type | Owning module | Status |
|---|---|---|---|
| REQ-EXAMPLE-001 | requirement | m01-project-initialization | draft |
```

### View Drift Prevention & Traceability Contract

To prevent human editors from accidentally modifying generated files, Alternative C enforces strict drift prevention:
1. **Reproducibility check:** CI or local validation regenerates views in check mode and compares deterministic output. The exact command does not exist yet and must be designed, implemented, and verified before becoming a gate.
2. **Generated banners:** Every generated view records generator version, input revision/hash, generation time, and a non-editable/non-authoritative marker.
3. **Docs contract:** Approved documents may be generated or manually synthesized, but both must record KB revision, knowledge references, approval evidence, generation/synthesis method, manual-edit policy, freshness, supersession, and drift checks. No “100% auditability” claim is valid until tooling and process evidence demonstrate it.

---

## 10. End-to-End Concrete Business Scenario: Project Approval Workflow

To evaluate Alternatives A, B, and C under identical conditions, the following enterprise scenario is mapped across all three options:

> **Illustrative scenario, not a verified current requirement:** a governed project-approval event triggers creation of a project record, workspace provisioning, role assignment, integration actions, a recorded architecture decision, validation, and eventual synthesis of an approved startup document. All IDs and paths below are proposals.

```
                           END-TO-END TRACEABILITY FLOW
                           
  [ Source ] → [ Source Statement ] → [ Business Need ] → [ REQ-EXAMPLE-001 ]
                                                        │
                                                        ▼
  [ ADR-EXAMPLE-001 ] ← [ CAP-EXAMPLE-001 ] ← [ Domain + Module links ]
            │                                                   │
            ▼                                                   ▼
  [ Implementation Item ] ──► [ Validation Evidence ] ──► [ Approved Document ]
```

### End-to-End Tracing Table Across Alternatives A, B, and C

| Concept / Artifact | Alternative A (Concept-Type Physical Path) | Alternative B (Domain Physical Path) | Alternative C (Shared Core + Generated Views Path) |
|---|---|---|---|
| **Source Record** | `sources/SRC-EXAMPLE-001.md` | `sources/SRC-EXAMPLE-001.md` | `sources/SRC-EXAMPLE-001.md` |
| **Source Statement** | `source-statements/CLM-EXAMPLE-001.md` | `domains/project-lifecycle/source-statements/CLM-EXAMPLE-001.md` | `core/source-statements/CLM-EXAMPLE-001.md` |
| **Business Need** | `business-needs/NEED-EXAMPLE-001.md` | `domains/project-lifecycle/business-needs/NEED-EXAMPLE-001.md` | `core/business-needs/NEED-EXAMPLE-001.md` |
| **Requirement** | `requirements/REQ-EXAMPLE-001.md` | `domains/project-lifecycle/requirements/REQ-EXAMPLE-001.md` | `modules/m01-project-initialization/requirements/REQ-EXAMPLE-001.md` |
| **Capability** | `capabilities/CAP-EXAMPLE-001.md` | `domains/project-lifecycle/capabilities/CAP-EXAMPLE-001.md` | `modules/m01-project-initialization/capabilities/CAP-EXAMPLE-001.md` |
| **Data Entity** | `data-entities/ENT-EXAMPLE-001.md` | `domains/information-management/data/ENT-EXAMPLE-001.md` | `core/data/ENT-EXAMPLE-001.md` if shared, otherwise module-owned |
| **Interface/Event** | `interfaces/IF-EXAMPLE-001.md` | `domains/enterprise-integration/interfaces/IF-EXAMPLE-001.md` | `modules/m01-project-initialization/interfaces/IF-EXAMPLE-001.md` |
| **ADR / Decision** | `decisions/ADR-EXAMPLE-001.md` | `domains/project-lifecycle/decisions/ADR-EXAMPLE-001.md` | `core/decisions/ADR-EXAMPLE-001.md` if cross-module, otherwise module-owned |
| **Implementation Item** | `implementation/ITEM-EXAMPLE-001.md` | `domains/project-lifecycle/implementation/ITEM-EXAMPLE-001.md` | `modules/m01-project-initialization/implementation/ITEM-EXAMPLE-001.md` |
| **Validation Evidence** | `validation/VAL-EXAMPLE-001.md` | `domains/project-lifecycle/validation/VAL-EXAMPLE-001.md` | `modules/m01-project-initialization/validation/VAL-EXAMPLE-001.md` |
| **Approved Document** | `docs/project-startup.md` derived from typed concepts | `docs/project-startup.md` derived from domain concepts | `docs/project-startup.md` derived from core/module concepts; generated domain view is not the approved document by itself |

---

## 11. Mapping Representative Current UPE Artifacts

To demonstrate migration mechanics, representative current UPE repository files are mapped into proposed target locations across Alternatives A, B, and C. Every target path is explicitly marked as **proposed**.

| Baseline UPE File | Proposed Target Path (Alternative A) | Proposed Target Path (Alternative B) | Proposed Target Path (Alternative C) |
|---|---|---|---|
| `knowledge-base/00_index.md` | generated `kb/views/concept-types/index.md` plus governance record | generated `kb/views/domains/index.md` | generated `kb/views/index.md` |
| `knowledge-base/00_principles.md` | split into `kb/principles/` and decision records | `kb/core/principles/` | `kb/core/principles/` |
| `knowledge-base/master.md` | split into typed concepts and generated master view | split into domain concepts under `kb/domains/` | shared concepts in `kb/core/`; module concepts in `kb/modules/`; generated domain view |
| `knowledge-base/architecture/arch_overview.md` | `kb/architecture-views/` plus linked decisions | shared/domain architecture views | `kb/core/architecture/` or module architecture according to ownership |
| `knowledge-base/architecture/module_interfaces.md` | atomic concepts under `kb/interfaces/` | interfaces assigned to primary domains with cross-domain links | module-owned interfaces under `kb/modules/<module>/interfaces/`; generated interface view |
| `knowledge-base/raw-input/UPE-vision.md` | register as source under `kb/sources/`; extract typed vision concepts separately | same source registration, with domain links | same source registration; shared vision concepts under `kb/core/vision/` |
| `docs/UPE_Executive_Summary_v1.md` | provisional source/historical artifact until KB lineage and approval are established | same | same; future approved replacement may be generated or manually synthesized from eligible KB concepts |
| `docs/UPE_Functional_Blocks_v1.md` | source candidate plus extracted capability concepts under `kb/capabilities/` | source candidate plus capabilities assigned to primary domains | source candidate plus shared/module-owned capabilities and generated capability view |
| `src/moms/**` | preserve/register under `kb/sources/internal/meetings/` | same | same |
| `src/vendors/**` | preserve/register under `kb/sources/external/vendors/` | same | same |
| feature-branch M01 `requirements.md` | extract reviewed atomic requirement concepts under `kb/requirements/` | assign reviewed concepts to primary business domains | place shared requirements in `kb/core/requirements/` and module-specific requirements in `kb/modules/m01-project-initialization/requirements/` |
| feature-branch M01 `data_model.md` | extract reviewed entities under `kb/data-entities/` | place concepts in the owning information domain and link users | place shared entities in `kb/core/data/`; module-private entities in `kb/modules/m01-project-initialization/data/` |
| `.plans/**` and `.pi/**` | operational artifacts remain outside KB authority unless a reviewed knowledge concept is extracted | same | same |
| reusable prompts | classify as tooling or implementation knowledge; do not treat prompt text as architecture authority | same | same |

---

## 12. Trade-off Analysis & Evaluation Matrix

To provide a decision-ready comparison, Alternatives A, B, and C are evaluated across 13 core dimensions on a 5-point scale (🔴 Poor, 🟡 Fair, 🟢 Good, 🔵 Very High / Excellent).

| Dimension / Criteria | Alternative A (Concept-Type Graph) | Alternative B (Domain Bundles) | Alternative C (Shared Core + Gen Views) |
|---|---|---|---|
| **1. OKF v0.2 compatibility** | Strong single-bundle fit; organization is a UPE convention | Strong in single-bundle domain-tree mode; federation is custom | Strong single-bundle fit if canonical concepts remain OKF Markdown |
| **2. Fit with current UPE evidence** | Requires substantial reclassification | Aligns with current domain narrative but not automatically with M01 module layout | Reuses M01 module pattern and shared governance, but needs placement rules and generators |
| **3. Human navigation** | Predictable by concept type; module context is distributed | Strong for domain stakeholders | Strong for module teams; domain/type navigation depends on generated views |
| **4. AI retrieval and graph analysis** | Strong homogeneous collections | Requires explicit cross-domain relationships | Strong if metadata is consistent and generated graph views are validated |
| **5. Ownership** | Concept stewards or central knowledge team | Domain owners | Shared-core stewards plus module owners |
| **6. Duplication risk** | Lower for globally shared concept types | Higher unless primary-domain ownership is enforced | Moderate-to-low if shared-versus-module placement is governed |
| **7. Cross-cutting knowledge** | Natural through typed links | Harder; domain silos are a primary risk | Natural through shared core, relationships, and generated views |
| **8. Branch/review behavior** | Type folders may attract concurrent edits | Domain PRs are coherent, but shared changes cross boundaries | Module PRs are coherent; shared-core changes require broader review |
| **9. Generated-view dependency** | Useful but not essential for type navigation | Useful for cross-domain views | Essential for domain/type/status navigation; drift tooling is a prerequisite |
| **10. Validation complexity** | Type-specific schemas plus relationship checks | Domain completeness plus cross-domain consistency | Type schemas, placement rules, cross-module links, and view reproducibility |
| **11. Link stability** | Path moves remain risky without stable UPE IDs/aliases | Domain reassignment can move paths | Module reassignment can move paths; shared IDs and supersession remain necessary |
| **12. Migration reversibility** | Many file splits increase mapping complexity | Domain grouping can be staged, but ownership mistakes are costly | Can be staged module by module if shared concepts are identified first |
| **13. Scale across 14 domains / 175+ capabilities** | Scales through many atomic files and generated module/domain views | Scales only with strong cross-domain governance | Promising balance, but unproven until generator and placement prototype succeed |

---

## 13. Decision Framework & Scenario-Based Choice Rules

To guide Chief Architect approval, this decision framework outlines explicit questions and scenario-based selection rules.

```
                            DECISION TREE FLOWCHART
                            
  Is automated CI view compiler tooling available & supported?
          │
          ├── NO ──► Do domain teams prioritize PR isolation & human folder navigation?
          │               │
          │               ├── YES ──► SELECT ALTERNATIVE B (Single-Bundle Mode)
          │               └── NO  ──► SELECT ALTERNATIVE A (Concept-Type Graph)
          │
          └── YES ──► Do you require automated drift prevention & 175+ capability matrices?
                          │
                          └── YES ──► SELECT ALTERNATIVE C (HYBRID CONDITIONAL RECOMMENDATION)
```

### Scenario-Based Selection Rules

1. **Choose A when** concept-type stewardship and machine retrieval are primary, teams accept distributed module context, and generated module/domain views can restore human context.
2. **Choose B when** domain ownership is stable, most concepts have one clear primary domain, and the organization can govern cross-domain references without duplication. Prefer one bundle with domain subtrees unless federation requirements justify custom tooling.
3. **Choose C when** module ownership is the main delivery model, shared enterprise concepts can be separated consistently, and UPE is willing to build and govern reproducible domain/type/status views. C is not automatically superior; it depends on module-boundary stability and generator validation.

---

## 14. Evidence-Based Conditional Recommendation

Prior research artifacts exhibited an explicit recommendation divergence:
- **Upstream Scout (`820da71`):** Recommended Alternative A due to native single-bundle OKF path alignment, uniform folder validation schemas, and clean AI graph compilation.
- **Local Scout (`49495fa`):** Recommended Alternative B (progressing to C) due to alignment with the current `feature/m01-project-initialization` branch, team mental models, and reduced Git PR collision.

### Resolution of Contradiction & Hybrid Conditional Recommendation

The scout divergence reflects different optimization goals rather than an error: upstream OKF evidence favors A's simple single-bundle typed organization; local repository evidence favors B's domain narrative and the M01 module pattern; C combines module ownership with generated graph views. The available evidence does not by itself authorize a final choice.

This report recommends **evaluating Alternative C as the leading prototype**, not adopting it immediately: one proposed OKF bundle, `core/` for shared enterprise concepts, `modules/` for module-owned concepts, and Alternative A-style typed metadata plus generated views. Alternative B remains viable if domain ownership proves stronger than module ownership.

```text
PROPOSED C + A-TYPED-VIEWS CANDIDATE
kb/
├── sources/
├── core/                          # shared concepts
├── modules/                       # bounded solution ownership
│   └── m01-project-initialization/
│       ├── requirements/*.md      # OKF Markdown concepts
│       ├── capabilities/*.md
│       ├── data/*.md
│       └── interfaces/*.md
├── governance/
└── views/                         # generated, non-authoritative
    ├── domains/
    ├── concept-types/
    └── traceability/
```

### Conditions for Final Selection

1. **Generator prototype:** demonstrate deterministic views from OKF Markdown frontmatter and links, with drift detection and machine-readable diagnostics.
2. **Bundle decision:** confirm whether one bundle satisfies ownership and scale needs; select multi-bundle federation only with an approved custom registry/version/validation design.
3. **Authority contract:** approve the KB eligibility model and allow `docs/` to contain generated or manually synthesized approved representations under traceability and drift controls.
4. **Boundary decision:** validate module boundaries, domain boundaries, and many-to-many mapping using M01 plus at least one cross-cutting capability before broad migration.

---

## 15. Phased Implementation Illustration

To visualize target state progression without claiming calendar duration estimates or executing unauthorized file moves, the phased evolution of the repository structure is illustrated below.

```text
PHASE 1 — APPROVED DESIGN BASELINE (NO BULK MOVE)
current repository + completed inventory + authority map + approved metadata/placement rules

PHASE 2 — SMALL PILOT BUNDLE ON A DEDICATED BRANCH
kb/
├── sources/
├── core/
├── modules/
│   └── m01-project-initialization/
│       ├── requirements/*.md
│       ├── capabilities/*.md
│       └── interfaces/*.md
├── governance/
└── views/                         # generated from pilot concepts

PHASE 3 — REVIEWED EXPANSION
kb/
├── sources/                       # registered current sources
├── core/                          # approved shared concepts
├── modules/                       # only approved module boundaries
├── governance/                    # validators and transition rules
└── views/                         # reproducible domain/type/status/traceability views

docs/                              # approved derived representations only
tools/                             # only if validation/generation tooling is approved
```

---

## 16. Risks, Unresolved Decisions, Approval Gates & Validation Evidence

### Risk Matrix

| Risk ID | Risk Description | Severity | Mitigation Strategy |
|---|---|---|---|
| `RSK-OPT-01` | **View drift:** generated projections diverge from canonical concepts. | High | Design deterministic generation, input hashes, non-editable markers, and check-mode comparison before enabling CI gates. |
| `RSK-OPT-02` | **Schema over-engineering:** too many fields reduce maintainability. | Medium | Justify every field by retrieval, trust, provenance, lifecycle, validation, synthesis, or impact analysis; apply fields by concept type. |
| `RSK-OPT-03` | **Federation complexity:** multiple bundles create unresolved identity and version coordination. | High | Prefer a single-bundle pilot; require a custom federation design and prototype before selecting multi-bundle B. |
| `RSK-OPT-04` | **Remote/branch divergence:** the selected baseline omits relevant content or is overwritten by synchronization. | High | Confirm remote ownership and synchronization behavior before baseline selection; do not prescribe merge or pipeline changes in this report. |

### Unresolved Architectural Decisions

1. **Canonical format:** OKF knowledge concepts should be Markdown with frontmatter. Non-Markdown schemas or binaries may be linked implementation/source assets, not replacements for canonical OKF concept documents.
2. **Shared versus module-owned concepts:** define a placement test for requirements, entities, standards, decisions, and interfaces used by multiple modules.
3. **Domain/module mapping:** determine whether current functional domains and proposed modules are many-to-many, and assign accountable owners without reusing module codes as domain identity by assumption.
4. **Bundle topology:** decide between one bundle and coordinated bundles only after testing scale, ownership, cross-linking, and validation implications.
5. **Derived-document policy:** decide which documents may be manually synthesized, which must be generated, and how both remain traceable and drift-controlled.

### Approval Gates Before Any Implementation

- [ ] Approve the selected baseline and branch/remote scope.
- [ ] Approve domain and module definitions, ownership, and mapping.
- [ ] Approve the OKF extension model, controlled vocabularies, and transition rules.
- [ ] Approve the selected physical alternative or pilot variant.
- [ ] Approve source-registration, docs-eligibility, validation, and rollback contracts.
- [ ] Approve any later merge, tag, branch-policy, CI, bulk move, archive, deletion, or promotion action separately. This report authorizes none of them.

---

## 17. Final Decision Record Template for Human Approver

```markdown
# UPE Knowledge Base Target Architecture — Formal Decision Record

**Decision Record ID:** `ADR-2026-08-05-KB-TARGET-ARCHITECTURE`  
**Date:** [YYYY-MM-DD]  
**Approver:** Chief Architect / Technical Steering Committee  

---

## 1. Selected Architecture Alternative
- [ ] **Alternative A:** Concept-Type-Oriented Unified Graph
- [ ] **Alternative B:** Domain-Oriented Coordinated Bundles (Single-Bundle Mode)
- [ ] **Alternative C (leading prototype candidate):** Shared Core + Module Subtrees + Generated Views

---

## 2. Decision Approval & Authorization
I confirm that I have reviewed the architecture discussion report `.pi/review/2026-08-05-upe-okf-repository-options-analysis.md`.

**Action Approved:**
- [ ] **DIRECTION ACCEPTED:** Record the preferred architecture direction and commission a separate approval-gated pilot/migration plan.
- [ ] **CONDITIONAL DIRECTION:** Accept only after named open decisions and evidence gaps are resolved.
- [ ] **REJECTED / REVISED:** Require additional analysis or alternative proposal.

**Sign-off Signature:** ____________________________________  
**Date:** ________________________  
**Notes / Mandatory Guidance:**
```

---

## 18. Sources & Citation Index

1. **Upstream OKF v0.2 Repository & Specification:**  
   Google Cloud Platform Knowledge Catalog at immutable commit `930b65fc3f5619d5d0591f88c72ebae8b848d60d` (inspected upstream state dated 2026-08-04).  
   - Specification: [`okf/SPEC.md`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/930b65fc3f5619d5d0591f88c72ebae8b848d60d/okf/SPEC.md) (1,003 lines in inspected revision).  
   - Overview: [`okf/README.md`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/930b65fc3f5619d5d0591f88c72ebae8b848d60d/okf/README.md) (220 lines in inspected revision).  
   - Required-key implementation evidence: [`okf/src/reference_agent/bundle/document.py#L13`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/930b65fc3f5619d5d0591f88c72ebae8b848d60d/okf/src/reference_agent/bundle/document.py#L13).
2. **Local Research Artifacts:**  
   - `.pi/research/2026-08-05-okf-repository-options-local-fit.md` — materialized from ephemeral agent branch `pi-agent-d9b3bfea-3763-4df` (commit `49495fa`); not on `main`.
   - `.pi/research/2026-08-05-okf-repository-options-upstream-fit.md` — materialized from ephemeral agent branch `pi-agent-7336f21d-0e5d-4ad` (commit `820da71`); not on `main`.
   - `.pi/context/2026-08-05-upe-structural-audit-okf-architecture-context.md` — materialized from ephemeral agent branch (commit `395e6bb`); not on `main`.
   - `.pi/research/2026-08-05-upe-structural-audit-okf-architecture-repository-inventory.md` — materialized from ephemeral agent branch (commit `2531666`); not on `main`.
   - `.pi/research/2026-08-05-upe-structural-audit-okf-architecture-okf-spec.md` — materialized from ephemeral agent branch (commit `9e6e3b1`); not on `main`.
   - `.pi/research/2026-08-05-upe-structural-audit-okf-architecture-authority-traceability.md` — materialized from ephemeral agent branch (commit `50a156d`); not on `main`.
   - `.pi/research/2026-08-05-upe-structural-audit-okf-architecture-branches-history.md` — materialized from ephemeral agent branch (commit `6fe8421`); not on `main`.
3. **Canonical Baseline Repository Files (Commit `44efc15` & Branch `feature/m01-project-initialization` `cf3cbb4`):**  
   - `knowledge-base/00_index.md` (89 lines in inspected revision).
   - `knowledge-base/00_principles.md` (187 lines in inspected revision).
   - `knowledge-base/00_glossary.md` (62 lines in inspected revision).
   - `knowledge-base/master.md` (199 lines in inspected revision).
   - `knowledge-base/architecture/arch_overview.md`.
   - `knowledge-base/architecture/module_interfaces.md`.
   - `knowledge-base/architecture/decisions/ADR-0001-docs-as-data.md`.
   - `feature/m01-project-initialization:knowledge-base/modules/m01_project_initialization/requirements.md`.
   - `feature/m01-project-initialization:knowledge-base/modules/m01_project_initialization/data_model.md`.
   - `feature/m01-project-initialization:knowledge-base/modules/m01_project_initialization/workflows.md`.
   - `docs/UPE_Executive_Summary_v1.md` (368 lines in inspected revision).
   - `docs/UPE_Functional_Blocks_v1.md` (1,007 lines in inspected revision).
   - `docs/upe-strategic-assessment.okf.yaml` (920 lines in inspected revision).
   - `docs/upe-okf/index.md` (65 lines in inspected revision; `stale_after: 2026-11-01` at line 10).
   - `src/moms/Unified Production Environment (UPE)_ Project Launch Series.txt` — legacy raw filename; governed platform name is Unified Project Execution environment.
   - `.plans/create-upe-architecture-artifacts/PLAN.md` — operational plan outside KB governance.

---
*End of Report — Target Repository Options Analysis for UPE OKF Knowledge Base.*
