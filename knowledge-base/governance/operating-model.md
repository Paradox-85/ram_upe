---
type: governance
title: Knowledge Operating Model — Hybrid Human + AI
description: "How the UPE knowledge system operates: one governed canonical KB, four artifact classes, two consumption surfaces, the human promotion gate, and the provenance rules that keep analysis separate from canonical knowledge."
tags: [governance, operating-model, human-in-the-loop, ai, promotion, provenance, okf, ddd]
sources:
  - ../governance/usage-guide.md
generated: 2026-10-09T10:40:47Z
verified: false
status: draft
stale_after: 2027-10-09
upe:
  lifecycle: draft
  owner: "@chief-architect"
  relations:
    - type: supports
      target: index
    - type: derived-from
      target: governance/principles
---

# Knowledge Operating Model — Hybrid Human + AI

## The invariant

> **Humans and AI may create different analyses of the same evidence, but UPE has only one
> governed knowledge model. Analysis becomes canonical knowledge only through an explicit
> review and promotion process.**

And the division of responsibility:

> **OKF** defines the representation and traceability of canonical knowledge. **DDD** defines its
> semantic and domain boundaries. **Human governance** determines what becomes authoritative.
> **AI** accelerates ingestion, extraction, analysis and navigation.

There is no Human KB and no AI KB. There is no separate machine truth and no separate human
truth. There is one canonical KB with two *workflows* feeding it through one *gate*.

```text
                         SOURCES
                            |
                 +----------+----------+
                 |                     |
                 v                     v
          HUMAN ANALYSIS          AI ANALYSIS          both NON-canonical
                 |                     |
                 +----------+----------+
                            |
                     HUMAN REVIEW
                            |
                     PROMOTION GATE
                            |
                            v
                   CANONICAL UPE KB
                            |
              +-------------+-------------+
              |             |             |
              v             v             v
         ARCHITECTURE     VIEWS        DECISIONS
              |                           |
              v                           v
       R&D / PROTOTYPES -----------> EVIDENCE
```

## 1. Four artifact classes

Different lifecycles must not be mixed. Each class has exactly one home:

| Class | Question it answers | Where | Canonical? |
|---|---|---|---|
| **A. Sources** | What did we receive? | `sources/` | no — evidence |
| **B. Analysis** | What did we conclude from it? | `analysis/{human,ai,reviewed}/` | no |
| **C. Canonical knowledge** | What has UPE reviewed and accepted? | `knowledge-base/` | **yes** |
| **D. Reports** | How do we present it to an audience? | `reports/{working,architecture-committee,published}/` | no |

Two supporting classes:

| Class | Where | Notes |
|---|---|---|
| **Labs** | `labs/` | executable experiments; the KB holds only the distilled conclusion |
| **Tools** | `tools/` | maintained reusable utilities (e.g. `tools/kb-validate`) |
| **Agent process** | `.pi/` | agent execution state — explicitly **not** the AI knowledge layer |

### Sources vs Knowledge Base

`sources/` = original evidence payload. `knowledge-base/` = governed knowledge derived from
evidence. The physical presence of a file in Git does not make its content canonical.
A **source record** (see `evidence/`) is canonical metadata about a payload; the payload is not
knowledge.

## 2. Two consumption surfaces, one KB

| | Machine surface | Human surface |
|---|---|---|
| Optimised for | agents, automation, semantic search | engineers, Product Owner, Architecture Committee |
| Consists of | atomic concepts, metadata, ids, relations, provenance, indexes | curated/generated views, maps, matrices, architecture descriptions, reports, decision summaries |
| Lives in | `knowledge-base/<collection>/` | `knowledge-base/views/`, `reports/`, `architecture/` |

Both read the **same** canonical KB. Canonical information is never duplicated to implement the
human surface: a view renders records, it does not restate them as truth.

The atomic collections stay. They are **not** replaced by human mega-documents.

## 3. Workflows

### Human-driven

```text
sources/transport/<payload>
      ↓  human analysis
analysis/human/transport/<date>-<slug>.md          analysis.method: human
      ↓  Architecture Committee review
reports/architecture-committee/<date>-<slug>.md
      ↓  accepted conclusions only
knowledge-base/requirements/ · problems/ · capabilities/ · architecture/
```

### AI-driven

```text
sources/transport/<payload>
      ↓  extraction / mapping / gap analysis
analysis/ai/transport/<date>-<slug>.md             analysis.method: ai
      ↓  human review (same gate as human analysis)
analysis/reviewed/transport/<date>-<slug>.md       analysis.status: reviewed
      ↓  promotion
knowledge-base/…
```

Human analysis gets **no privileged path**: it passes the same review and promotion gate.
AI output is **candidate knowledge only**.

`.pi/` vs `analysis/ai/`: agent execution and research state goes to `.pi/` (disposable,
gitignored); durable machine analysis a human will review goes to `analysis/ai/`.

## 4. The promotion gate

```text
SOURCE → ANALYSIS → CANDIDATE FINDING → HUMAN REVIEW → ACCEPT / MODIFY / REJECT → CANONICAL KB
```

Promotion is **per finding**, not per document. The mechanism is deliberately lightweight and
uses what already exists:

- frontmatter status on the analysis artifact (`working → review-ready → reviewed → superseded`);
- pull requests and review;
- Architecture Committee review;
- ADR approval for architectural decisions;
- an explicit named reviewer/owner in `upe.owner`.

When a finding is accepted, the **KB record is created separately** with its own `sources:` and a
`derived-from` relation to the analysis, and the analysis records the outcome in `promoted:`.

### Lifecycles are not shared

| Layer | Vocabulary |
|---|---|
| Canonical KB | `idea → draft → in-review → approved → superseded → deprecated` |
| Analysis | `working → review-ready → reviewed → superseded` |

Analysis is never `approved`. The canonical lifecycle is not reused for analysis artifacts.

## 5. Human gates — what AI may and may not do

AI **may**: parse, classify, index, compare, propose, identify duplicates, suggest relations,
draft requirements, draft ADRs, generate views.

AI **must not** autonomously:

- approve requirements or architecture;
- mark an ADR accepted;
- change approved domain boundaries;
- promote uncertain analysis into canonical knowledge.

Those are human decisions. Where existing UPE/DDDM approval rules already cover a case, they are
reused — no parallel governance system is created.

## 6. Provenance rules

Every durable analysis answers: which **sources** were used; **human, AI or hybrid**; is it
**reviewed**; which **KB concepts** it relates to; did it result in a **promoted** change.

Every canonical KB record answers: **where did this come from** (`sources:`); **which evidence
supports it**; **what decision or review made it canonical**.

Enforced mechanically by `tools/kb-validate/check_sources.py` — a dangling provenance path fails
the gate.

## 7. Repository navigation (short form)

| I want to… | Go to |
|---|---|
| place a received document | `sources/<topic>/` |
| put my own assessment | `analysis/human/<topic>/` |
| store durable AI business analysis | `analysis/ai/<topic>/` |
| park agent scratch work | `.pi/` |
| find accepted reusable knowledge | `knowledge-base/` |
| find current architecture | `knowledge-base/architecture/` |
| browse the KB without opening hundreds of files | `knowledge-base/views/` |
| write an Architecture Committee deliverable | `reports/architecture-committee/` |
| run an experiment or prototype | `labs/` |
| find maintained reusable code | `tools/` |

## 8. What must not happen

- Two knowledge bases, or a "machine truth" beside a "human truth".
- A report, view or analysis introducing a canonical fact that the KB does not hold.
- Reusing the canonical lifecycle for non-canonical artifacts.
- Replacing atomic concepts with hand-maintained mega-documents.
- `analysis → KB` without a human gate.
- Treating a source's presence in Git as approval of its content.

## 9. Publication surfaces (Azure DevOps)

The repository is the system of record; Azure DevOps provides reading, planning and execution
surfaces over it. None of them is a second source of truth.

| Surface | Role | Authority |
|---|---|---|
| **Repos** | the repository itself — canonical artifacts under version control | authoritative |
| **Wiki** (code wiki *UPE Knowledge Hub*, from `main:/knowledge-base`) | human browsing, search and navigation over the canonical KB | publication only — renders the KB, never defines it |
| **Boards** | backlog, epics, features, stories, architecture tasks | authoritative for planning, not for knowledge |
| **Pipelines** | automated validation (`tools/kb-validate`) | enforcement, not authority |

Rules:

- The wiki publishes `main:/knowledge-base` and does not alter the operating model. It never becomes an
  independent source of truth.
- **Canonical knowledge remains in `knowledge-base/`; the wiki makes that knowledge accessible to humans.**
- A wiki page cannot create knowledge: anything a page concludes is promoted through the gate like any
  other finding.
- Do not restructure the repository to make the wiki prettier. Wiki usability comes from indexes, views,
  ordering and links, not from flattening the atomic structure.
- Out-of-KB links on wiki-published pages are absolute repository URLs (an Azure DevOps platform
  constraint); in-KB links stay relative. Managed by `tools/wiki/make_links_wiki_safe.py`, validated by
  `tools/kb-validate/check_wiki.py`.
- Where planning already lives (Azure Boards), link to it instead of duplicating a backlog in Markdown.

Setup and implementation: [`../../tools/wiki/README.md`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/tools/wiki/README.md&version=GBmain).

Related: [`principles.md`](principles.md) · [`metadata-profile.md`](metadata-profile.md) ·
[`usage-guide.md`](usage-guide.md) · [`../../analysis/README.md`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/analysis/README.md&version=GBmain) ·
[`../../sources/README.md`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/sources/README.md&version=GBmain) · [`../../reports/README.md`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/reports/README.md&version=GBmain)
