# `reports/architecture-committee/` — committee deliverables

Architecture Committee papers and decision packages. Audience-facing, **never canonical**.

Name files `<iso-date>-<topic>.md`, e.g. `2026-10-21-transport-upe-coverage.md`.

## Rules

1. **Trace every claim.** Each factual statement points to a canonical KB record or a named
   analysis under `analysis/reviewed/`. A committee cannot decide on unsourced assertions.
2. **A report cannot create knowledge.** If the committee reaches a conclusion, promote it
   separately into `knowledge-base/{requirements,problems,capabilities,architecture/decisions}/`
   and let the report reference the resulting records.
3. **State the ask explicitly.** Every paper names the decisions requested of the committee, so the
   outcome is recorded as an ADR or a `status: reviewed` analysis finding rather than a discussion.
4. **Include the provenance header** described in [`../README.md`](../README.md): audience, date,
   status, inputs.

The KB's own copy of "what is decided" stays in `knowledge-base/architecture/decisions/`; this
directory holds how it was presented.
