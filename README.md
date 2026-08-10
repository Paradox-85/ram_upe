# ram_upe — Ramboll Unified Project Execution

**The living, queryable product design system for UPE.** This is not application source code — it is the canonical design manifest: architecture, requirements, methodology, and knowledge base for Ramboll's enterprise digital backbone.

---

## What This Repository Is

`ram_upe` is the **single source of truth** for the UPE (Unified Project Execution) product design. Every architecture decision, functional requirement, entity model, interface contract, and governance rule lives here as structured Markdown under Git version control.

The repository implements **DDDM** (Dialogue-Driven Design Method) — an LLM-native methodology where:

- Markdown + Mermaid + Git replace Word, Visio, and Confluence
- LLM sessions are primary design instruments
- Every artifact has a stable ID, YAML front matter, and a defined lifecycle
- All changes go through a fork → review → merge cycle with 6 explicit gates

> **See the full methodology reference:** [`docs/knowledge-base-reference.md`](docs/knowledge-base-reference.md)

---

## Core Concept: UPE as a Parameterized Constructor

UPE is Ramboll's **enterprise digital backbone** — a coordination and intelligence layer that orchestrates project delivery across the entire lifecycle. Think of it as a **car platform**: a stable core chassis with modular, configurable variations that produce thousands of unique, high-quality projects from standardized building blocks.

### What UPE IS
- **Coordination & Intelligence Layer** — sits above CDEs and authoring tools
- **Process Orchestration** — automates project workflows across systems (CRM, ERP, HR, CDE)
- **Knowledge Platform** — captures, organizes, and leverages organizational intelligence
- **Integration Hub** — connects enterprise systems through defined interface contracts
- **Decision Support** — AI-powered insights for project delivery

### What UPE is NOT
- ❌ Does NOT replace CDE (ACC, ProjectWise) — CDE remains the project system of record
- ❌ Does NOT replace DMS/authoring tools (Revit, Bentley, AVEVA)
- ❌ Does NOT replace ERP/CRM — integrates with them, never substitutes
- ❌ Does NOT replace document stores — it's a coordination and intelligence surface

---

## Repository Map

| Directory | Purpose |
|---|---|
| [`knowledge-base/`](knowledge-base/) | **Canonical DDDM vault.** Master, architecture, principles, glossary, index, changelog, module specs, ADRs, reports, raw input. All structured Markdown with YAML front matter. |
| [`docs/`](docs/) | **Human-readable documentation.** Executive summary, functional blocks, brainstorming, deployment guides, KB reference. Not DDDM-governed — free-form Markdown for project context. |
| [`src/`](src/) | **Raw source materials.** Vendor research (AVEVA, Autodesk, Hexagon), meeting transcripts (MoMs), Loop workstreams, architect chat logs. These feed the KB but are not themselves canonical artifacts. |
| [`prompts/`](prompts/) | **Methodology prompts.** The founding DDDM framework prompt that defines how LLMs should design within this repo. |
| [`.plans/`](.plans/) | **Pi agent planning history.** Registered plans with JSON manifest. Tracks what planning work has been done. |
| [`.pi/`](.pi/) | **Pi agent runtime artifacts.** Context files, research output, implementation plans, review logs. Transient working files. |
| [`azure-pipelines.yml`](azure-pipelines.yml) | **CI/CD.** Azure DevOps pipeline that mirrors the repo to GitHub. |

---

## How the Pieces Connect

```
┌──────────────────────────────────────────────────────────────────┐
│  Source Materials (raw input)                                    │
│  docs/   src/   prompts/   knowledge-base/raw-input/             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────────┐ │
│  │Exec Summ │  │Vendors   │  │DDDM      │  │Interviews,       │ │
│  │Func Blks │  │MoMs      │  │Framework │  │ISO 19650,        │ │
│  │Brainstorm│  │Loop WS   │  │Prompt    │  │Capabilities...   │ │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────────┬─────────┘ │
└───────┼──────────────┼─────────────┼─────────────────┼───────────┘
        │              │             │                 │
        ▼              ▼             ▼                 ▼
┌──────────────────────────────────────────────────────────────────┐
│  Knowledge Base (canonical artifacts)                            │
│  knowledge-base/                                                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────────┐ │
│  │master.md │  │00_prin-  │  │architec- │  │modules/          │ │
│  │(vision,  │  │ciples.md │  │ture/     │  │m01_*/            │ │
│  │14 domains│  │(DDDM     │  │(overview,│  │(reqs, data model,│ │
│  │7 layers) │  │rules)    │  │ADR-0001) │  │workflows, APIs)  │ │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────────┬─────────┘ │
└───────┼──────────────┼─────────────┼─────────────────┼───────────┘
        │              │             │                 │
        ▼              ▼             ▼                 ▼
┌──────────────────────────────────────────────────────────────────┐
│  Outputs (derived, never edited directly)                        │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────────┐ │
│  │Reports   │  │Prototypes│  │Demo      │  │Stakeholder       │ │
│  │           │  │           │  │Scripts   │  │Briefs            │ │
│  └──────────┘  └──────────┘  └──────────┘  └──────────────────┘ │
└──────────────────────────────────────────────────────────────────┘
```

The cycle: **source materials** are ingested and synthesized into **canonical KB artifacts** through LLM design sessions. **Reports, demos, and briefs** are rendered from those artifacts on demand.

---

## Start Here: Reading Order

For a new contributor or agent, follow this path:

1. **This README** (you are here) — understand the repo at a glance
2. **[`knowledge-base/master.md`](knowledge-base/master.md)** — vision, 14 domains, 7-layer architecture, Phase 1 scope
3. **[`knowledge-base/00_principles.md`](knowledge-base/00_principles.md)** — DDDM methodology, ID scheme, lifecycle, merge gates, governance
4. **[`knowledge-base/00_glossary.md`](knowledge-base/00_glossary.md)** — canonical terminology
5. **[`knowledge-base/00_index.md`](knowledge-base/00_index.md)** — complete file inventory
6. **[`docs/knowledge-base-reference.md`](docs/knowledge-base-reference.md)** — detailed reference for all DDDM rules
7. **Deployment guides** (only if setting up tooling):
   - [`docs/deployment-pi-coding-agent.md`](docs/deployment-pi-coding-agent.md) — install and configure the Pi coding agent
   - [`docs/deployment-knowledge-base.md`](docs/deployment-knowledge-base.md) — deploy an empty KB instance in another repo
8. **[`knowledge-base/architecture/arch_overview.md`](knowledge-base/architecture/arch_overview.md)** — 7-layer architecture deep-dive
9. **[`knowledge-base/architecture/decisions/ADR-0001-docs-as-data.md`](knowledge-base/architecture/decisions/ADR-0001-docs-as-data.md)** — why we chose Markdown+Mermaid+Git

If working on M01, also read:
- `feature/m01-project-initialization` branch (module artifacts, prototype prompt, session logs)

---

## How to Use This Repo

### For Human Contributors

1. **Read before editing.** Follow the reading order above. Understand DDDM before touching `knowledge-base/`.
2. **Never edit `knowledge-base/` directly on `main`.** Create a feature branch, design there, submit a PR.
3. **Follow the fork → review → merge cycle.** All 6 Merge Gates must pass before merging.
4. **Update the index.** After merging, update `knowledge-base/00_index.md` and `knowledge-base/00_changelog.md`.
5. **Reports are derived.** Never edit `knowledge-base/reports/` as source — regenerate from master artifacts.
6. **Use Mermaid for all diagrams.** No manual diagram authoring.
7. **No orphan files.** Every new file must be listed in `00_index.md`.
8. **Every LLM session produces a commit.** No session without output to the repo.

### For Pi Agents

1. **Load context:** Read `00_index.md` → `00_principles.md` → `master.md` → relevant module/architecture files.
2. **Search:** Use grep on front matter fields (`id:`, `type:`, `status:`, `tags:`) for metadata queries. Use full-text grep for content queries.
3. **Validate:** Before writing, verify YAML front matter (8 fields), stable ID format, no orphan creation.
4. **Never edit master directly.** All changes go through forks.
5. **No auto-mining of chat history.** Ingestion is explicit-only.
6. **Provenance markers:** Use `^[inferred]` and `^[ambiguous]` for unconfirmed information.

---

## DDDM Workflow in Practice

```
Fork → Design → Self-Check → Submit PR → 6 Gates → Merge → Update Index
```

1. Create branch: `feature/m{NN}-{description}`
2. LLM sessions produce commits with new/modified KB files
3. Validate: front matter, stable IDs, no orphans
4. Open PR, tag `@chief-architect`
5. All 6 Merge Gates pass → merge to `main`
6. Update `00_index.md` and `00_changelog.md`

> Full details: [`docs/knowledge-base-reference.md`](docs/knowledge-base-reference.md)

---

## Current UPE Scope

| Aspect | Detail |
|---|---|
| **Domains** | 14 functional domains (M01–M14), 175+ capabilities |
| **Architecture** | 7 layers + cross-cutting governance |
| **Phase 1** (Months 1–6) | M01, M02, M03, M07, M10, M13 — 4–6 FTE |
| **Active design** | M01 on `feature/m01-project-initialization` (`in-review-demo`) |
| **Tech stack** | Microsoft 365 E5 + Azure + Autodesk APIs |

---

## Deployment Guides

Two deployment guides are available for setting up the tooling around this repo:

| Guide | When to Use |
|---|---|
| [`docs/deployment-pi-coding-agent.md`](docs/deployment-pi-coding-agent.md) | Install and configure the Pi coding agent with profiles, packages, skills, prompts, MCP, LSP, and subagents |
| [`docs/deployment-knowledge-base.md`](docs/deployment-knowledge-base.md) | Deploy an empty Karpathy-pattern Obsidian Wiki KB instance in another repository |

---

## Important Source Materials

| Source | What It Contains |
|---|---|
| [`docs/UPE_Executive_Summary_v1.md`](docs/UPE_Executive_Summary_v1.md) | 14 domains, phases, metrics |
| [`docs/UPE_Functional_Blocks_v1.md`](docs/UPE_Functional_Blocks_v1.md) | 175+ capabilities across all domains |
| [`docs/brainstorming.md`](docs/brainstorming.md) | Module architecture, M365 stack |
| [`src/loop/loop.md`](src/loop/loop.md) | Workstreams WS 3.1–3.5, Copilot sparring session |
| [`src/chat/`](src/chat/) | Architect chat — concept evolution |
| [`src/moms/`](src/moms/) | Meeting transcripts (Project Launch Series) |
| [`src/vendors/`](src/vendors/) | AVEVA, Autodesk, Hexagon research (21 files) |
| [`prompts/LLM-Native Product Design Framework.md`](prompts/LLM-Native%20Product%20Design%20Framework.md) | Founding DDDM methodology prompt |
| [`knowledge-base/raw-input/`](knowledge-base/raw-input/) | ISO 19650, capabilities, interviews, vision |

---

## Current Branching Status

| Branch | Contents | Status |
|---|---|---|
| `main` | Canonical artifacts (approved + draft). 10 KB files + 12 raw input files. | ✅ Stable |
| `feature/m01-project-initialization` | M01 module design: requirements, data model, workflows, API spec, backlog, prototype prompt, session log. | 🔄 `in-review-demo` |

All other modules (M02–M14) are `idea` — defined in `master.md` but not yet designed.

---

## Open Questions

These are tracked in `knowledge-base/master.md`:

1. **Data Centralization vs. Federation** — single data lake or distributed with views?
2. **AI Approach** — enterprise AI platform (custom) or vendor AI + vibe coding?
3. **Knowledge Representation** — RDF/semantic web or simpler taxonomy?
4. **Vendor Stack depth** — commit deeply to Microsoft+Autodesk or keep options open?
5. **Funding model** — product team budget vs. project budgets?

---

## Repository Provenance

- **Azure DevOps:** `https://dev.azure.com/ramboll-bim/_git/UPE` (primary)
- **GitHub mirror:** `https://github.com/Paradox-85/ram_upe` (public mirror via CI/CD)
- **Azure pipeline:** automatically mirrors `main` to GitHub
- **Originally forked** from Azure DevOps to GitHub for public collaboration
