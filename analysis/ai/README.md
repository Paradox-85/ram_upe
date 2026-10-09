# `analysis/ai/` — durable machine-derived analysis

Output produced by AI agents that is **worth keeping for humans to review later**. Grouped by
topic, not by tool:

```text
analysis/ai/transport/      requirement extraction, UPE coverage, gap analysis
analysis/ai/autodesk/       vendor capability mapping
analysis/ai/requirements/   clustering, deduplication, candidate requirements
```

## What belongs here

Extracted candidate requirements · inferred problems · capability mappings · entity extraction ·
clustering · document indexing summaries · semantic comparison · gap analysis · proposed
relationships.

## What does **not** belong here

| Not here | Goes to |
|---|---|
| Agent plans, scratch research, checkpoints, review notes | `.pi/` (gitignored, disposable) |
| Editorial rules, prompts, agent role definitions | `.pi/` or `knowledge-base/governance/` |
| Anything a reviewer has accepted as canonical | `knowledge-base/` (after the gate) |

## Rules

1. **Candidate knowledge only.** Nothing here is authoritative, no matter how confident the
   output looks, and no matter which model produced it.
2. **Never write to `knowledge-base/` from an analysis run.** A human promotes a *finding*; the
   agent may not create, edit or approve canonical records autonomously.
3. **Declare the method and the tool**: `analysis.method: ai` (or `hybrid`) plus `analysis.agent`.
4. **Record the sources** actually used — an extraction with no source list cannot be reviewed.
5. **Ingested legacy material is marked as such.** `strategic-assessment-2026-08-01/` was
   produced by `agent:github-copilot` before this operating model existed and is preserved
   verbatim as historical AI analysis. It was previously mis-filed as raw evidence (audit
   finding F8). Do not treat it as a source.

Frontmatter contract and promotion gate: [`../README.md`](../README.md).
