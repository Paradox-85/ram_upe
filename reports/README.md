# `reports/` — audience-facing deliverables

Reports are **how information is presented to a specific audience**. A report is never
canonical knowledge, and it can never silently create it.

## Sub-directories

| Directory | Audience | Examples |
|---|---|---|
| `reports/working/` | internal draft | status report, working notes |
| `reports/architecture-committee/` | Architecture Committee | decision packages, architecture papers |
| `reports/published/` | distributed beyond the team | issued assessments, historical briefs |

## Rules

1. **A report references, it does not define.** Every factual claim should trace to a canonical
   KB entity or to a named analysis. Link them.
2. **A report cannot create knowledge.** If a report concludes something new, promote that
   conclusion separately into `knowledge-base/{requirements,problems,capabilities,architecture/decisions}/`
   and then reference it.
3. **One authoritative representation.** A requirement may appear in an atomic KB record, a
   view and a committee paper — only the KB record is canonical. The others render or cite it.
4. **Name with an ISO date**: `reports/architecture-committee/2026-10-09-transport-upe-coverage.md`.
5. **Never copy canonical text as the source of truth.** If it drifts, the KB wins.

## Provenance header

Reports are plain Markdown, but should state their inputs and audience so a reader can verify:

```markdown
> **Audience:** Architecture Committee · **Date:** 2026-10-09 · **Status:** working
> **Inputs:** knowledge-base/views/requirements-coverage.md · analysis/reviewed/transport/…
```

## Historical reports

Two audience-facing legacy reports were moved here from the frozen legacy corpus
(`reports/published/demo-script-2026-05-26.md`, `reports/published/stakeholder-brief-2026-05-26.md`).
They are historical artifacts — their original bytes are preserved, and they are **not**
current statements about UPE.
