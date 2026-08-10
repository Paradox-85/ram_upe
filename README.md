# ram_upe — Ramboll Unified Project Execution

**The living, queryable knowledge base and architecture system of record for UPE.** This is not application source code — it is the canonical design manifest: architecture, DDD concepts, requirements, governance, and the raw evidence from which they are built, for Ramboll's enterprise digital backbone.

---

## What This Repository Is

`ram_upe` is the **single source of truth** for UPE (**U**nified **P**roject **E**xecution). It is structured as one OKF (Open Knowledge Framework) knowledge bundle with a DDD (Domain-Driven Design) organization:

- **`knowledge-base/`** — the canonical bundle: DDD concept collections, governance, architecture, decisions, and the immutable raw evidence layer.
- **`knowledge-base/raw-input/`** — every legacy artifact preserved verbatim (history kept via `git mv`), never edited.
- Everything newly written is **draft** (or `idea`); nothing is promoted to `approved` in this cycle.

> **Current state:** all canonical content is `draft`/`candidate`. The raw corpus under `knowledge-base/raw-input/` is evidence, not authority.

## KB-First Navigation

Newcomers (humans and agents) follow this path:

1. **This README** — orientation and entry points.
2. **[`AGENTS.md`](AGENTS.md)** — operating rules; agents must read it before changing knowledge.
3. **[`knowledge-base/index.md`](knowledge-base/index.md)** — progressive-disclosure index of the KB bundle (domains, capabilities, problems, use-cases, events, solution-candidates, architecture, governance, labs).
4. **[`knowledge-base/governance/principles.md`](knowledge-base/governance/principles.md)** — KB-first rules, raw immutability, draft-only scope, metadata contract.
5. **[`knowledge-base/architecture/master.md`](knowledge-base/architecture/master.md)** — draft integration architecture view over the DDD concepts and decisions.
6. **[`knowledge-base/architecture/context-map.md`](knowledge-base/architecture/context-map.md)** — draft context map; M01–M14 are candidate functional domains, not bounded contexts.
7. **[`knowledge-base/raw-input/`](knowledge-base/raw-input/)** — the immutable raw corpus behind every concept.

## Reading Order (Detailed)

| Step | Where | What you get |
|---|---|---|
| 1 | [`knowledge-base/index.md`](knowledge-base/index.md) | Bundle map, endpoints, status |
| 2 | [`knowledge-base/governance/glossary.md`](knowledge-base/governance/glossary.md) | Ubiquitous language (DDD + UPE terms) |
| 3 | [`knowledge-base/governance/metadata-profile.md`](knowledge-base/governance/metadata-profile.md) | Metadata contract, lifecycle, typed relations |
| 4 | [`knowledge-base/domains/`](knowledge-base/domains/) | 14 candidate functional domains M01–M14 |
| 5 | [`knowledge-base/capabilities/`](knowledge-base/capabilities/) | 100+ source-backed capabilities |
| 6 | [`knowledge-base/architecture/master.md`](knowledge-base/architecture/master.md) | Integration architecture view |
| 7 | [`knowledge-base/architecture/decisions/`](knowledge-base/architecture/decisions/) | ADR catalog + template + historic ADR-0001 |

## UPE in One Line

UPE (**U**nified **P**roject **E**xecution) is Ramboll's enterprise digital backbone — a coordination and intelligence layer that orchestrates project delivery across the full lifecycle: a stable core (chassis) with modular, configurable variations (the *Parameterized Constructor*).

### What UPE IS
- **Coordination & Intelligence Layer** — sits above CDEs and authoring tools
- **Process Orchestration** — automates project workflows across systems (CRM, ERP, HR, CDE)
- **Knowledge Platform** — captures, organizes, and leverages organizational intelligence
- **Integration Hub** — connects enterprise systems through defined interface contracts
- **Decision Support** — AI-powered insights for project delivery

### What UPE is NOT
- Does NOT replace CDE (ACC, ProjectWise) — CDE remains the project system of record
- Does NOT replace DMS/authoring tools (Revit, Bentley, AVEVA)
- Does NOT replace ERP/CRM — integrates with them, never substitutes
- Does NOT replace document stores — it is a coordination and intelligence surface

## Knowledge Base Layers

| Layer | Purpose | Status |
|---|---|---|
| `knowledge-base/raw-input/**` | Immutable raw evidence (legacy docs, src, prompts, transcripts) | n/a — evidence, never edited |
| `knowledge-base/{domains,capabilities,problems,use-cases,events,solution-candidates}/` | Extracted DDD concepts with raw provenance | `draft`/`idea` |
| `knowledge-base/governance/` | Principles, glossary, metadata contract, aliases | `draft` |
| `knowledge-base/architecture/` | Master view, context map, ADR catalog | `draft` |
| `knowledge-base/labs/` | R&D lab contract + manifest template | `draft` framework (empty) |

## How the Pieces Connect

```
raw-input/ (immutable evidence: legacy knowledge-base, docs, src, prompts)
        │  sourced-by
        ▼
DDD concept collections: domains -> capabilities -> problems -> use-cases -> events -> solution-candidates
        │  linked-by
        ▼
governance/ (principles, glossary, metadata) + architecture/ (master view, context map, decisions)
        │  informed-by
        ▼
labs/ (R&D ideas, future experiments)
```

The cycle: **raw evidence** is extracted into **DDD concepts** (source-backed, draft), which are consumed by **governance and architecture** views; **labs** captures open R&D questions. Canonical current content is draft; raw is the evidence trail.

## Current UPE Scope

| Aspect | Detail |
|---|---|
| **Domains** | 14 functional-domain candidates (M01–M14) |
| **Capabilities** | 100+ source-backed, captured in `knowledge-base/capabilities/` |
| **Architecture** | Draft integration view + candidate context map (see `knowledge-base/architecture/`) |
| **Status** | All new KB content is `draft`/`idea`; no promotions in this cycle |

## Deployment Guides

Legacy deployment guides are preserved verbatim under the raw corpus:
- [`knowledge-base/raw-input/docs/pi-beginner-deployment-guide.md`](knowledge-base/raw-input/docs/pi-beginner-deployment-guide.md) — install and configure the Pi coding agent
- [`knowledge-base/raw-input/docs/deployment-knowledge-base.md`](knowledge-base/raw-input/docs/deployment-knowledge-base.md) — deploy an empty KB instance

## Open Questions

Open questions are tracked inside concept bodies under `## Open questions` and in the architecture master view. Current topics include data centralization vs. federation, AI approach, knowledge representation, vendor stack depth, and funding model.

## Repository Provenance

- **Azure DevOps:** `https://dev.azure.com/ramboll-bim/_git/UPE` (primary)
- **GitHub mirror:** `https://github.com/Paradox-85/ram_upe` (public mirror via CI/CD)
- **Azure pipeline:** automatically mirrors `main` to GitHub
- **Originally forked** from Azure DevOps to GitHub for public collaboration
