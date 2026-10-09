# `analysis/human/` — manual analysis

Where you put **your own** assessment of source material.

```bash
# one directory per topic, one file per analysis
analysis/human/transport/2026-10-09-transport-upe-coverage.md
analysis/human/autodesk/2026-10-09-autodesk-gap-assessment.md
```

Use the frontmatter contract in [`../README.md`](../README.md) (`analysis.method: human`).

Rules that matter here:

- **You do not get a privileged path.** Human analysis must go through the same review and
  promotion gate as AI analysis — being written by a person does not make it canonical.
- **Cite your sources** in `sources:`; without evidence the analysis cannot be promoted.
- **Record disagreement, don't resolve it silently.** If your conclusion differs from an AI
  analysis or from a source, say so and cite both. Contradictions are preserved in the KB.
- **Link related KB entities** in `related:` so reviewers can see what would change.
- **Keep it non-canonical in tone.** Write "we conclude / we propose", not "UPE requires".

When the analysis is complete, set `status: review-ready` and hand it to review
(see `../README.md` → Promotion gate).
