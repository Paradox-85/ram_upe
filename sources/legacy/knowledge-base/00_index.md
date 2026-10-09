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
| `architecture/arch_overview.md` | Architecture | `draft` | @chief-architect | 7-layer architecture overview, UPE positioning, hybrid build-vs-buy, Azure/open-standards principles |
| `architecture/module_interfaces.md` | Interface Contracts | `draft` | @chief-architect | 7 interface contracts for M01 (CRM, HR, ERP, M365, CDE, Template, KG) with provisioning sequence |
| `architecture/decisions/ADR-0001-docs-as-data.md` | Decision (ADR) | `accepted` | @chief-architect | ADR-0001: Adopt Markdown+Mermaid+Git-style workflow as single source of truth |

---

## Module M01 — Project Initialization & Provisioning

> ⚠️ M01 artifacts are under active development on branch
> `feature/m01-project-initialization`.
> They will appear in this index after
> [PR #1](https://github.com/Paradox-85/ram_upe/pull/1) is approved and merged.

---

## Prototypes

| Branch | Path | Status | Note |
|--------|------|--------|------|
| `feature/m01-project-initialization` | `prototypes/sprint-01_project_initialization/prototype_prompt.md` | `in-progress` | Moved from main. Enters main after PR #1 merge. |

---

## Reports & Demo

| Path | Artifact Type | Status | Owner | Purpose |
|---|---|---|---|---|
| `reports/stakeholder_brief_2026-05-26.md` | Report (Derived) | `draft` | @chief-architect | 1-page stakeholder brief — why DDDM for UPE, 3 colleague decisions requested |
| `demo_script.md` | Demo Script (Derived) | `approved` | @chief-architect | 25-minute demo script with timing and talking points |

---

## Statistics

| Metric | Count |
|---|---|
| Total files | 10 |
| Architecture files | 3 |
| Module files (M01) | 0 |
| Fork files | 0 |
| Session logs | 0 |
| Prototype prompts | 0 |
| Reports | 1 |
| Demo scripts | 1 |
| Root files (index, principles, glossary, changelog, master) | 5 |
| Files on feature branch (pending PR #1 review) | 9 |
| Files with `approved` status | 6 |
| Files with `in-review-demo` status | 0 |
| Files with `accepted` status | 1 |
| Files with `draft` status | 3 |

## Active Feature Branches

| Branch | Module | Status | PR |
|--------|--------|--------|----|
| `feature/m01-project-initialization` | M01 Project Initialization | `in-review-demo` | [Open PR →] |
