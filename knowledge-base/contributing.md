---
type: navigation
title: How to Contribute
description: "Where to put a document, an analysis or a report — and why nobody creates canonical knowledge directly. Written for business contributors, not developers."
tags: [navigation, contributing, workflow, wiki, upe]
sources: []
generated: 2026-10-09T12:00:00Z
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
      target: governance/operating-model
---

# How to Contribute

**You do not need Git, and you do not need to understand this repository's internals.** Everything
below can be done from the repository web interface (upload a file, open a pull request).

The single rule to remember:

> **Nothing becomes knowledge by being written down.** A document you add is *evidence*; an analysis
> you write is *opinion* until a reviewer promotes a specific finding.

## Where do I put things?

| I have… | Put it in | What it is |
|---|---|---|
| a document someone sent me (spreadsheet, PDF, meeting notes, vendor material) | [`sources/`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/sources&version=GBmain) — pick the topic folder, e.g. `sources/transport/` | **evidence** — never knowledge |
| my own assessment, comparison or gap analysis | [`analysis/human/`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/analysis/human&version=GBmain)`<topic>/` | **non-canonical** analysis |
| a durable AI-generated analysis worth keeping | [`analysis/ai/`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/analysis/ai&version=GBmain)`<topic>/` | **non-canonical** analysis |
| a status update, working note or committee paper | [`reports/working/`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/reports/working&version=GBmain) or [`reports/architecture-committee/`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/reports/architecture-committee&version=GBmain) | **report** — presentation, never knowledge |
| an experiment or prototype | [`labs/`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/labs&version=GBmain) | throwaway R&D |
| a reusable script or utility | [`tools/`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/tools&version=GBmain) | maintained utility |

### Concrete steps for a new document

1. Open the topic folder under `sources/` (create it if the topic is new, e.g. `sources/buildings/`).
2. Upload the file, named `<iso-date>-<short-title>.<ext>` — for example
   `2026-10-21-transport-workshop-notes.xlsx`.
3. Never overwrite an existing file: a new revision is a **new file**.
4. Tell a knowledge owner (currently `@chief-architect`) so a source record and any resulting analysis
   can be registered. Nothing is expected of you beyond supplying the document and saying where it came from.

### Concrete steps for your own analysis

1. Create or open `analysis/human/<topic>/`.
2. Name the file `<iso-date>-<short-title>.md`.
3. Start it with these fields (the rest is free-form prose):

```yaml
---
type: analysis
title: Transport vs UPE coverage
analysis:
  method: human
status: working
sources:
  - sources/transport/2026-10-21-transport-workshop-notes.xlsx
related: []
created: 2026-10-21
---
```

4. Write your conclusions. Cite the sources you used, and state explicitly where you disagree with an
   existing analysis or a source — disagreements are preserved, not smoothed over.
5. When you are finished, set `status: review-ready`.

Do the same for AI output, with `analysis.method: ai` (and the tool name if you know it). **AI output is
not more trustworthy than a person's**: both are candidate material, reviewed the same way.

## How something becomes canonical

```text
Source / Analysis
        ↓
     Review              your finding is examined, not your document
        ↓
  PROMOTION GATE         a human accepts, modifies or rejects it
        ↓
  knowledge-base/        the accepted finding becomes a record — with its own sources
```

Promotion is **per finding**, not per document: a 30-page analysis may yield three accepted
requirements and twenty rejected observations, and the rejections are recorded too.

## What you cannot do (and why)

- **You cannot create or edit canonical knowledge directly.** Records under
  `knowledge-base/requirements/`, `problems/`, `capabilities/`, `architecture/` are created by the
  promotion process, so that every canonical claim has a reviewer and a source behind it.
- **Nobody edits `sources/`.** Evidence is frozen; a correction is a new dated revision.
- **A report cannot create knowledge.** If a committee paper concludes something new, the conclusion is
  promoted separately and the report then links to it.

## Deeper reading

- [Operating model](governance/operating-model.md) — the four artifact classes, the two surfaces, the gate.
- [Usage guide](governance/usage-guide.md) — the full contributor contract: metadata, authoring, validation.
- [Principles](governance/principles.md) — KB-first, evidence immutability, draft-only scope.
- [Requirements collection](requirements/) · [Evidence collection](evidence/) — templates and rules.
