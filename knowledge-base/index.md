---
type: navigation
title: UPE Knowledge Hub
description: "Home page of the UPE Knowledge Hub: the human entry point to the governed UPE knowledge base, published as an Azure DevOps code wiki."
tags: [index, navigation, wiki, home, upe]
sources: []
generated: 2026-08-10T07:48:05Z
verified: false
status: draft
stale_after: 2027-08-10
upe:
  lifecycle: draft
  owner: "@chief-architect"
  relations:
    - type: supports
      target: governance/operating-model
    - type: supports
      target: contributing
---

# UPE Knowledge Hub

The governed knowledge base for the **Unified Project Execution** environment. Everything here is
`draft`/`candidate` unless a record says otherwise — nothing is `approved` yet.

> **This wiki is a reading surface over the repository.** It is not a second source of truth.
> Canonical knowledge lives in `knowledge-base/`; the wiki only makes it accessible.

## Start here

| # | Section | Page |
|---|---|---|
| 1 | **Product overview** — what UPE is and is not | [Product Overview](product-overview.md) |
| 2 | **Architecture** — current state, context map, decisions | [Architecture Overview](views/architecture-overview.md) · [master view](architecture/master.md) · [ADRs](architecture/decisions/) |
| 3 | **Requirements** — business, functional, non-functional, constraints, stakeholder | [Requirements Coverage](views/requirements-coverage.md) · [collection](requirements/) |
| 4 | **Capabilities** — the 520 atomic ability records, grouped | [Capability Map](views/capability-map.md) |
| 5 | **GBA needs & coverage** — Transport and other GBAs | [GBA Needs & Coverage](views/gba-overview.md) |
| 6 | **Architecture Committee** — backlog, decisions, review queue | [Architecture Committee](views/architecture-committee.md) |
| 7 | **Vendors & technology** — vendor material held as evidence | [Vendors & Technology](views/vendor-overview.md) |
| 8 | **Reports** — committee papers, status, published briefs | [Reports](views/reports.md) |
| 9 | **Sources & evidence** — the original material behind everything | [Sources & Evidence](views/sources-and-evidence.md) |
| 10 | **How to contribute** — where to put a document or an analysis | [How to Contribute](contributing.md) |

Other entry points: [Open Decisions](views/open-decisions.md) ·
[Roadmap projection](views/roadmap.md) · [Governance](governance/) · [Change log](log.md)

## What is canonical and what is not

| Layer | Where | Status |
|---|---|---|
| Canonical knowledge | `knowledge-base/` (this wiki) | the only governed model — `draft` until reviewed |
| Source evidence | [sources/](https://dev.azure.com/ramboll-bim/_git/UPE?path=/sources&version=GBmain) | evidence, **never** knowledge |
| Analysis (human, AI) | [analysis/](https://dev.azure.com/ramboll-bim/_git/UPE?path=/analysis&version=GBmain) | **non-canonical** working output |
| Reports | [reports/](https://dev.azure.com/ramboll-bim/_git/UPE?path=/reports&version=GBmain) | audience-facing, never canonical |
| Labs / tools | [labs/](https://dev.azure.com/ramboll-bim/_git/UPE?path=/labs&version=GBmain) · [tools/](https://dev.azure.com/ramboll-bim/_git/UPE?path=/tools&version=GBmain) | experiments and utilities |

> **Analysis artifacts are non-canonical working outputs.** Canonical project knowledge is maintained
> under the UPE Knowledge Base.

New knowledge enters through one gate only:

```text
Sources → Analysis (human or AI) → Review → PROMOTION GATE → knowledge-base/
```

Nobody — human or AI — edits canonical knowledge directly; a finding is promoted by a human decision
after review. See [How to Contribute](contributing.md) and the
[operating model](governance/operating-model.md).
