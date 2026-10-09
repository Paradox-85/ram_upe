# `labs/` — experiments and prototypes

Runnable experiments and prototypes live **outside** the canonical KB. A lab asserts nothing
canonical: the KB holds the **distilled conclusion**, not the prototype.

```text
labs/<slug>/manifest.md              the lab, its inputs and its result
        ↓ evaluates
knowledge-base/architecture/...      what the lab informs
        ↓ produces
knowledge-base/evidence/...          the canonical conclusion / evidence record
```

## Start a lab

1. Pick a short `<slug>`.
2. Copy [`_template/manifest.md`](_template/manifest.md) to `labs/<slug>/manifest.md`.
3. Fill it in and keep it current while the lab runs.
4. When it concludes, **promote the finding** into the KB through the normal review gate — the
   manifest links to that record; it never replaces it.

## Manifest fields (contract)

| Field | Meaning |
|---|---|
| `upstream_intent` | `hypothesis` \| `requirement` \| `capability` \| `option` \| `ADR` — what the lab is testing |
| `lab_status` | `idea` \| `planned` \| `active` \| `concluded` \| `archived` |
| `upstream_entities` | the KB entities this lab evaluates (requirements, capabilities, architecture, ADRs) |
| `evidence_links` | inputs, results and any KB evidence records produced |
| run command / environment | how to reproduce the run |
| outputs | expected and actual artifacts |
| `decision_influence` | which decision/concept the result informed |
| `canonical_evidence_created` | the KB record that carries the accepted conclusion (or `none`) |
| retention | how long the lab and its data are kept |

## Rules

- Do **not** claim a lab was run without evidence.
- A lab README or manifest is **never** a second KB: no canonical statements belong here.
- Promotional path: `lab → validated reusable implementation → tools/`. Promotion to `tools/`
  requires reuse intent, an owner, a documented contract and proportionate validation.
- Throwaway probes stay in `labs/` (or in branch history) — they do not need production-grade
  engineering.

Contract owner: `@chief-architect`. Operating model:
[`../knowledge-base/governance/operating-model.md`](../knowledge-base/governance/operating-model.md).
