# `tools/kb-views` — human-surface generator

Generates the readable views in `knowledge-base/views/` from canonical KB metadata.

```bash
python tools/kb-views/generate.py
```

Run it after **any** change to canonical knowledge — and before a review or committee paper —
so the views do not drift from the records they render.

## Contract

| View | Rendered from |
|---|---|
| `architecture-overview.md` | `architecture/**` records, the decision catalog, the 14 candidate domains |
| `capability-map.md` | the 520 capability records grouped by `upe.functional_block` → candidate domain |
| `requirements-coverage.md` | the `requirements/**` records and the capability links in their `## Traceability` section |
| `gba-overview.md` | GBA folders under `sources/`, their source records, their analysis folders, and citing requirements |
| `vendor-overview.md` | `sources/vendors/*/` plus KB records whose title/description mentions the vendor |
| `architecture-committee.md` | decisions, the ADR catalog, the roadmap view, `analysis/reviewed/`, the reports index, and the Boards link from the config |
| `roadmap.md` | domain `## Priority` values, requirement kinds, pending decisions |
| `open-decisions.md` | decision records plus `## Open questions` sections of non-atomic records |
| `reports.md` | `reports/{working,architecture-committee,published}/` |
| `sources-and-evidence.md` | the `sources/` tree with counts, plus the `source-reference` records |

Every view carries a **generated / non-authoritative** banner and the generation date. A view must
never be hand-edited: if a view is wrong, fix the record it renders and regenerate.

## Notes

- Reads frontmatter only, except the requirements view, which also reads each requirement's
  `## Traceability` section to resolve realising-capability links.
- Links copied out of record bodies are flattened to plain labels, because a relative link that is
  valid inside a record is not valid inside `views/`.
- Capability records do not (yet) carry `supports` relations to their domains, so the grouping uses
  the `upe.functional_block` field. Adding those relations is a semantic change that needs review.
- No dependencies beyond PyYAML.
