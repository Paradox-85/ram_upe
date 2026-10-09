# `analysis/` — non-canonical analysis

Everything here is **non-canonical**. Analysis is what a human or an AI *concluded* from
sources. It never becomes truth by being written down; it becomes truth only through the
promotion gate into `knowledge-base/`.

> Humans and AI may produce **different analyses of the same evidence**. That is expected and
> allowed. Neither may change canonical knowledge on its own.

## Sub-directories

| Directory | Who / what | Notes |
|---|---|---|
| `analysis/human/` | Analysis authored by people | Group by topic: `analysis/human/transport/…` |
| `analysis/ai/` | **Durable** machine-derived analysis useful to UPE participants | Group by topic: `analysis/ai/transport/…`. Agent *execution* state belongs in `.pi/`, not here. |
| `analysis/reviewed/` | Consolidated analysis that has passed review and is ready for promotion | Staging area for the Architecture Committee gate |

### `analysis/ai/` vs `.pi/`

This distinction is load-bearing:

| | `.pi/` | `analysis/ai/` |
|---|---|---|
| Purpose | agent execution state (plans, scratch research, checkpoints) | durable project analysis a human may review later |
| Lifetime | disposable, gitignored | committed, reviewable, citable |
| Example | "how should I refactor this repo?" | "Transport ↔ UPE requirement coverage" |
| Canonical? | no | no |

## Artifact metadata contract (lightweight — do not over-engineer)

```yaml
---
type: analysis
title: Transport vs UPE Coverage Analysis
analysis:
  method: human          # human | ai | hybrid
  agent: <tool/model>    # only when method is ai or hybrid
status: working          # see lifecycle below
sources:                 # required: the evidence this analysis used
  - sources/transport/2026-10-09-rtr-production-improvement-opportunity-space.xlsx
related:                 # optional: KB entities this analysis touches
  - knowledge-base/requirements/req-transport-...md
  - knowledge-base/problems/cde-interoperability-and-manual-syncing.md
created: 2026-10-09
updated: 2026-10-09
promoted:                # filled in only when a conclusion entered the KB
  - knowledge-base/requirements/req-transport-....
---
```

Minimum useful fields: `type`, `title`, `analysis.method`, `status`, `sources`,
`related`, `created`/`updated`, and eventually `promoted`.

## Lifecycle (analysis only — do **not** reuse the canonical KB lifecycle)

```text
working  →  review-ready  →  reviewed  →  superseded
```

| Status | Meaning |
|---|---|
| `working` | in progress; not ready for anyone to rely on |
| `review-ready` | author believes it is complete; waiting for review |
| `reviewed` | a reviewer has examined it; conclusions may be promoted |
| `superseded` | replaced by a newer analysis; keep for history, never delete |

Canonical governance (`idea → draft → in-review → approved → superseded → deprecated`) is a
**separate** vocabulary and is not used here. Analysis is never `approved`.

## Provenance rules (§22) — every durable analysis must answer

1. Which **sources** were used? (`sources:`)
2. Was it **human, AI or hybrid**? (`analysis.method`)
3. Is it **reviewed**? (`status`)
4. Which **KB concepts** does it relate to? (`related:`)
5. Did it result in a **promoted knowledge change**? (`promoted:`)

## Promotion gate

```text
SOURCE
  ↓
ANALYSIS                     analysis/{human,ai}/<topic>/
  ↓
CANDIDATE FINDING            a specific claim, not a whole document
  ↓
HUMAN REVIEW                 Architecture Committee / owner / ADR review
  ↓
ACCEPT / MODIFY / REJECT
  ↓
CANONICAL KB                 knowledge-base/{requirements,problems,capabilities,architecture/decisions,...}/
```

Promotion is per **finding**, not per document: a 30-page analysis may yield three accepted
requirements and twenty rejected observations. The accepted ones get their own KB records with
`sources:` and a `derived-from` relation pointing at the analysis.

**Never allowed:** `analysis → canonical KB` without the human gate. AI may parse, classify,
index, compare, propose, map and draft. AI must not approve requirements or architecture, mark
ADRs accepted, or change approved domain boundaries.

Full rules: [`knowledge-base/governance/operating-model.md`](../knowledge-base/governance/operating-model.md).
