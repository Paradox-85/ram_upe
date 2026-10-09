# `sources/` — received evidence payload

This is the **only** intake location for material the team receives. A file here is
**evidence**, never knowledge. Its presence in Git does not make its content canonical.

> Legacy material previously held under `knowledge-base/raw-input/` was classified and moved
> here in the 2026-10-09 refactoring. There is exactly one sources location.

## Where do I place a document I just received?

Here. Pick the business topic:

| Topic | Directory |
|---|---|
| Transport GBA | `sources/transport/` |
| Other GBAs (Buildings, Energy, Water, Architecture & Landscape) | `sources/<gba>/` |
| Vendor material (AVEVA, Autodesk, Hexagon, …) | `sources/vendors/<vendor>/` |
| Meetings, workshops, transcripts, recordings | `sources/meetings/` |
| Ramboll-internal source documents and initiatives | `sources/ramboll/` |
| External standards and specifications (ISO, IFC, …) | `sources/standards/` |
| Historical material kept as evidence only | `sources/legacy/` |

## Rules

1. **Payload is immutable.** Once added, a source file is not edited — not even to fix links
   or rename a product. Supersede it with a new dated copy instead.
2. **One file per received revision.** Never overwrite; put the revision in the name:
   `<iso-date>-<slug>.<ext>` (e.g. `2026-10-09-rtr-production-improvement-opportunity-space.xlsx`).
3. **Register it in the KB.** Add a `source-reference` record under
   `knowledge-base/evidence/` with a stable `SRC-*` id, the location, revision and sha256.
   Concepts then cite the source; the physical location can change without breaking provenance.
4. **Do not derive here.** Extracted summaries, mappings, comparisons and conclusions belong in
   `analysis/` (non-canonical) and reach the KB only through the promotion gate.

## How a source becomes knowledge

```text
sources/<topic>/<payload>            you put it here
        |
        v
analysis/{human,ai}/<topic>/...      someone analyses it (non-canonical, provenance recorded)
        |
        v
analysis/reviewed/<topic>/...        consolidated, review-ready
        |
        v
knowledge-base/{requirements,problems,capabilities,...}/   human promotion gate
```

Full rules: [`knowledge-base/governance/operating-model.md`](../knowledge-base/governance/operating-model.md).

## Source record vs source payload

Do not confuse the two. A **source record** (`knowledge-base/evidence/src-*.md`,
`type: source-reference`) is canonical *metadata about* a source. The **payload** is the
received file. See `knowledge-base/evidence/README.md`.
