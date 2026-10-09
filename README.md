# ram_upe — Ramboll Unified Project Execution

The **governed knowledge base and architecture system of record** for UPE. This is not
application source code: it is the canonical design manifest — architecture, DDD concepts,
requirements, decisions, and the evidence they are derived from — for Ramboll's enterprise
digital backbone.

> **Current state:** everything under `knowledge-base/` is `draft`/`candidate`. Nothing is
> `approved` yet. Evidence under `sources/` is not knowledge.

## Where do I put things?

| I have… | Put it in |
|---|---|
| a document I just received (spreadsheet, PDF, transcript, vendor material) | **`sources/<topic>/`** — one immutable file per revision |
| my own assessment or analysis | **`analysis/human/<topic>/`** |
| durable AI-generated business/project analysis | **`analysis/ai/<topic>/`** |
| agent scratch work, plans, research state | **`.pi/`** |
| an Architecture Committee paper or status report | **`reports/architecture-committee/`** or `reports/working/` |
| an experiment or prototype | **`labs/`** |
| a reusable maintained utility | **`tools/`** |
| accepted, reviewed, reusable knowledge | **`knowledge-base/`** |
| a decision | **`knowledge-base/architecture/decisions/`** |

## Where do I find things?

| I want… | Go to |
|---|---|
| the entry point to the KB | [`knowledge-base/index.md`](knowledge-base/index.md) |
| the rules and vocabulary | [`knowledge-base/governance/principles.md`](knowledge-base/governance/principles.md) · [`glossary.md`](knowledge-base/governance/glossary.md) |
| how this repository operates (human + AI) | [`knowledge-base/governance/operating-model.md`](knowledge-base/governance/operating-model.md) |
| to contribute (authoring, intake, validation) | [`knowledge-base/governance/usage-guide.md`](knowledge-base/governance/usage-guide.md) |
| current UPE architecture | [`knowledge-base/architecture/master.md`](knowledge-base/architecture/master.md) |
| a readable overview without opening hundreds of files | [`knowledge-base/views/`](knowledge-base/views/) |
| requirements and traceability | [`knowledge-base/requirements/`](knowledge-base/requirements/) |
| original evidence | [`sources/`](sources/README.md) |
| agent operating rules | [`AGENTS.md`](AGENTS.md) |

## How the pieces connect

```text
sources/                 what we received (evidence, never canonical)
    ↓
analysis/{human,ai}/     what we concluded (non-canonical, both equally)
    ↓
HUMAN REVIEW + PROMOTION GATE
    ↓
knowledge-base/          the ONE canonical model
    ↓
views/ · reports/        how we show it (non-authoritative projections)
labs/ · tools/           experiments and maintained utilities
.pi/                     agent process state
```

**The invariant:** humans and AI may create different analyses of the same evidence, but UPE has
only one governed knowledge model. Analysis becomes canonical knowledge only through an explicit
human review and promotion process. There is no Human KB and no AI KB.

## Structure

```text
sources/            received evidence payload, by topic
analysis/           non-canonical analysis: human/ · ai/ · reviewed/
knowledge-base/     canonical KB (OKF + DDD): governance, requirements, domains,
                    capabilities, problems, use-cases, events, solution-candidates,
                    architecture, evidence, views
reports/            audience deliverables: working/ · architecture-committee/ · published/
labs/               experiments and prototypes
tools/              maintained utilities (kb-validate)
.pi/                agent execution state — not a knowledge layer
```

## Validation

```bash
python tools/kb-validate/run_all.py          # frontmatter + links + provenance
python tools/kb-validate/run_all.py --lint   # + markdownlint
```

## UPE in one line

UPE (**U**nified **P**roject **E**xecution) is Ramboll's enterprise digital backbone — a
coordination and intelligence layer that orchestrates project delivery across the full lifecycle:
a stable core (chassis) with modular, configurable variations.

- **Is:** coordination & intelligence layer, process orchestration, knowledge platform,
  integration hub, decision support.
- **Is not:** a replacement for the CDE (ACC, ProjectWise), for DMS/authoring tools (Revit,
  Bentley, AVEVA), for ERP/CRM, or for document stores — it integrates with them.

## Repository provenance

- **Azure DevOps:** `https://dev.azure.com/ramboll-bim/_git/UPE` (primary)
- **GitHub mirror:** `https://github.com/Paradox-85/ram_upe` (public mirror, pushed by CI on `main`)
- Note: because the mirror is public, `sources/` — including vendor documentation — is published publicly.

## Open questions

Tracked inside concept bodies under `## Open questions` and in
[`knowledge-base/governance/principles.md`](knowledge-base/governance/principles.md). Current topics
include data centralization vs. federation, AI approach, knowledge representation, vendor stack
depth, funding model, and whether new concept types (requirements, source references) need formal
stable IDs.
