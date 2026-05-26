---
id: index
type: index
status: approved
owner: "@scrum-master"
version: 1.0
last_updated: 2026-05-26
parent: master.md
tags: [index, registry, inventory]
---

# UPE Knowledge Base — Master Index

Every file in the `knowledge-base/` repository is listed here. No orphan files.

---

## Root Files

| Path | Artifact Type | Status | Owner | Purpose |
|---|---|---|---|---|
| `master.md` | Master | `approved` | @chief-architect | Main integration document: vision, domains, architecture, module registry |
| `00_index.md` | Index | `approved` | @scrum-master | This file — complete inventory of all artifacts |
| `00_principles.md` | Framework | `approved` | @chief-architect | DDDM methodology, YAML standard, ID scheme, lifecycle, merge gates |
| `00_glossary.md` | Glossary | `approved` | @chief-architect | Canonical terminology and abbreviations |
| `00_changelog.md` | Changelog | `approved` | @scrum-master | Global change log for the knowledge base |

---

## Architecture

| Path | Artifact Type | Status | Owner | Purpose |
|---|---|---|---|---|
| `architecture/arch_overview.md` | Architecture | `approved` | @chief-architect | Architecture overview, UPE positioning, build-vs-buy, component diagram |
| `architecture/module_interfaces.md` | Interface Contracts | `in-review-demo` | @chief-architect | 7 interface contracts for M01 (CRM, HR, ERP, M365, CDE, Template, KG) |
| `architecture/decisions/ADR-0001-docs-as-data.md` | Decision (ADR) | `accepted` | @chief-architect | ADR-0001: Use Markdown+Mermaid+Git as source of truth |

---

## Module M01 — Project Initialization & Provisioning

| Path | Artifact Type | Status | Owner | Purpose |
|---|---|---|---|---|
| `modules/m01_project_initialization/index.md` | Module | `in-review-demo` | @module-owner-m01 | Module overview, scope, dependencies, metrics |
| `modules/m01_project_initialization/requirements.md` | Requirements | `in-review-demo` | @module-owner-m01 | 25+ business/functional/non-functional requirements with stable IDs |
| `modules/m01_project_initialization/data_model.md` | Data Model | `in-review-demo` | @module-owner-m01 | 13 entities with Mermaid ERD and attribute tables |
| `modules/m01_project_initialization/workflows.md` | Workflow | `in-review-demo` | @module-owner-m01 | State machine, flowchart, step details, failure/recovery flow |
| `modules/m01_project_initialization/api_spec.md` | API Spec | `in-review-demo` | @module-owner-m01 | REST endpoints, events, error codes, external dependencies |
| `modules/m01_project_initialization/backlog.md` | Backlog | `in-review-demo` | @module-owner-m01 | MVP tasks, review tasks, demo tasks, definition of done |

---

## Backlog & Forks

| Path | Artifact Type | Status | Owner | Purpose |
|---|---|---|---|---|
| `backlog/forks/project-intialization-module.md` | Fork | `draft` | @module-owner-m01 | Working fork for M01 — hypotheses, deltas, open questions, merge checklist |

> **Note:** Filename preserves the original typo (`intialization`) from task specification. Canonical spelling: `project-initialization`.

---

## Sessions

| Path | Artifact Type | Status | Owner | Purpose |
|---|---|---|---|---|
| `sessions/2026-05-26_m01_project_initialization_llm_session.md` | Session Log | `approved` | @module-owner-m01 | LLM session log: prompt, decisions, review notes, artifacts, follow-ups |

---

## Prototypes

| Path | Artifact Type | Status | Owner | Purpose |
|---|---|---|---|---|
| `prototypes/sprint-01_project_initialization/prototype_prompt.md` | Prototype Prompt | `draft` | @module-owner-m01 | UI prototype prompt for v0.dev/Replit/Claude — 5 screens described |

---

## Reports & Demo

| Path | Artifact Type | Status | Owner | Purpose |
|---|---|---|---|---|
| `reports/stakeholder_brief_2026-05-26.md` | Report (Derived) | `approved` | @chief-architect | 1-page stakeholder brief — why DDDM, master vs fork, decisions requested |
| `demo_script.md` | Demo Script (Derived) | `approved` | @chief-architect | 25-minute demo script with timing and talking points |

---

## Statistics

| Metric | Count |
|---|---|
| Total files | 19 |
| Architecture files | 3 |
| Module files (M01) | 6 |
| Fork files | 1 |
| Session logs | 1 |
| Prototype prompts | 1 |
| Reports | 1 |
| Demo scripts | 1 |
| Root files (index, principles, glossary, changelog, master) | 5 |
| Files with `approved` status | 8 |
| Files with `in-review-demo` status | 6 |
| Files with `accepted` status | 1 |
| Files with `draft` status | 2 |
