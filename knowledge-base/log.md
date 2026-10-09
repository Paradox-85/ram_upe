---
type: log
title: Knowledge Base Change Log
description: Change log for the Unified Project Execution knowledge bundle, recording migration and creation batches and OKF attribution.
tags: [log, changelog, okf, upe]
status: draft
stale_after: 2027-08-10
upe:
  lifecycle: draft
  owner: "@chief-architect"
  relations: []
---

# Change Log

> **Attribution:** structure/conventions adopted from [`GoogleCloudPlatform/knowledge-catalog/okf`](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) (SPEC v0.2) under **Apache-2.0**. No upstream content was copied. Only structure and conventions are adopted.

Record of batches as the bundle was deployed (harness `20260810-074805-upe-harmonization`). **Status:** draft; log entries track mutations in creation order.

## 2026-10-09 — Azure DevOps code wiki (human publication surface)

1. **Wiki published over the KB.** `main:/knowledge-base` is published as the code wiki *UPE Knowledge
   Hub*. It is a reading surface only: no second knowledge base, no change to the operating model.
2. **Home page recalibrated.** `index.md` is now the wiki home with ten sections (product, architecture,
   requirements, capabilities, GBA, committee, vendors, reports, sources, contribute) and an explicit
   statement of what is canonical and what is not.
3. **Ten human-surface views** in `views/`: the existing architecture overview, capability map,
   requirements coverage and open decisions, plus new GBA overview, vendor overview, Architecture
   Committee hub, roadmap projection, reports index and sources-and-evidence index.
4. **Three curated entry pages** at the KB root: `product-overview.md`, `contributing.md`, and the
   recalibrated `index.md`. Curated pages are hand-written; everything in `views/` is generated.
5. **Collection guide pages renamed** for wiki titles: `requirements/README.md` →
   `requirements-guide.md`, `evidence/README.md` → `evidence-guide.md`, `views/README.md` →
   `views-guide.md`. Azure DevOps derives page titles from file names.
6. **Navigation ordering.** Six `.order` files (`knowledge-base/` and five subfolders) define the
   published sequence; a code wiki does not order pages without them.
7. **Cross-boundary links made wiki-safe.** 577 body links that escaped the published folder became
   absolute repository URLs; frontmatter provenance paths stay repo-relative. Reversible via
   `tools/wiki/make_links_wiki_safe.py --revert`.
8. **New gate.** `tools/kb-validate/check_wiki.py` validates out-of-KB links and their targets,
   `.order` integrity, page-name constraints and the presence of the entry pages; it is part of
   `run_all.py`.
9. **Single link source.** All repository/wiki URLs live in `tools/wiki/wiki.config.json`; setup steps
   and optional REST automation in `tools/wiki/`.
10. **Operating model and agent rules extended** with the publication-surface rules (operating model §9,
    `AGENTS.md` → Publication Surfaces).

## 2026-10-09 — hybrid human/AI operating model (refactoring `20261009-104047-upe-refactor`)

1. **Four artifact classes separated.** `sources/` (received evidence), `analysis/{human,ai,reviewed}/`
   (non-canonical), `knowledge-base/` (the only canonical model), `reports/{working,architecture-committee,published}/`
   (audience deliverables); plus `labs/` (experiments), `tools/` (maintained utilities) and `.pi/` (agent
   process state, explicitly not a knowledge layer).
2. **Evidence corpus relocated.** All 73 legacy artifacts under `knowledge-base/raw-input/**` were
   classified and moved with `git mv` (bytes unchanged): 54 SOURCE, 11 AI-analysis, 7 legacy
   architecture, 2 reports, and one legacy decision record. `knowledge-base/raw-input/` no longer exists —
   there is exactly one sources location.
3. **Reclassified material.** `upe-okf/**` + `upe-strategic-assessment.okf.yaml` were AI-generated
   (`agent:github-copilot`) and moved out of evidence into `analysis/ai/strategic-assessment-2026-08-01/`;
   the two audience-facing legacy reports moved to `reports/published/`; labs moved out of the KB to `labs/`.
4. **Provenance paths rewritten.** 2 272 references across 571 files updated to the new locations,
   including one previously dangling `sources:` entry in `governance/principles.md`.
5. **Governance extended.** Added `governance/operating-model.md` (invariant, artifact classes, two
   consumption surfaces, promotion gate, provenance rules, human gates). `principles.md` gained an
   evidence-immutability and an operating-model principle plus an `## Open questions` section; the
   metadata profile gained the `requirement`, `source-reference` and `view` types, the `analysis`
   lifecycle and the `requirement:`/`source:` extensions.
6. **New canonical collections.** `requirements/` (first-class traceability layer),
   `evidence/` (source-reference records), `views/` (generated human surface).
7. **Validation made reproducible.** `tools/kb-validate/` now holds the frontmatter and link gates plus a
   new `check_sources.py` provenance gate and `run_all.py`. Previously these scripts lived in the
   gitignored `.pi/temp/`, so a fresh clone could not run any documented check.
8. **Navigation rewritten.** Root `README.md` is now the where-to-put map; `AGENTS.md` states the agent
   operating rules; `governance/usage-guide.md` documents the new structure, intake, promotion and gates.

See also: `governance/operating-model.md`, `sources/README.md`, `analysis/README.md`, `reports/README.md`.

## 2026-08-10 — bundle deployment
1. **Raw migration.** Moved 73 tracked artifacts (legacy `knowledge-base/**`, `docs/**`, `src/**`, `prompts/**`) into `raw-input/` via `git mv` (path-preserving), after removing the byte-identical duplicate `docs/deployment-pi-coding-agent.md`. Legacy plan store moved to existing track under `.pi/plan/legacy/`. Root `docs/`, `src/`, `prompts/` removed; `nul` confirmed absent.
2. **OKF shell + governance.** Created `index.md`, `log.md`, `governance/{principles,glossary,metadata-profile,terminology-aliases}.md` (all `draft`).
3. **Domains.** Created 14 candidate functional-domain records M01–M14 (`type: domain`, `upe.id M01…M14`, draft).
4. **Capabilities.** Extracted 100+ source-backed capability records from raw functional-block/eference sources.
5. **Concepts.** Created source-backed `problems/`, `use-cases/`, `events/`, `solution-candidates/` records (≥3 each).
6. **Architecture.** Created draft `architecture/master.md`, `architecture/context-map.md`, and `architecture/decisions/{index.md,adr-template.md,adr-0001-history.md}`.
7. **Labs.** Created empty `../labs/README.md` framework + manifest template.
8. **Navigation.** Rewrote root `README.md` (KB-first); aligned `AGENTS.md` navigation wording; updated `index.md`/`log.md` per batch.
9. **Usage guide.** Added `governance/usage-guide.md` (draft): navigation, frontmatter contract, authoring workflow, lab usage, common validation commands (markdownlint / check_links / check_frontmatter / okflint pointers), agent operating rules, pre-merge checklist, troubleshooting. Linked from `index.md`.
10. **Usage guide v2.** Expanded `governance/usage-guide.md`: basis/version section (OKF v0.2, upstream repo, DDD.md, legacy DDDM, raw corpus), directory-tree detail (usage-guide listed), new §8 "Injection & query via custom Pi skills (planned)" — kb-inject/kb-query subcommands, injection map (raw-input / concepts / checkpoint), approved-decisions predicate, implementation principles (PyYAML, OKF v0.2 field alignment); sections renumbered to 12.

## Conventions
- OKF path-as-ID; bundle-relative links; `upe.id` only for existing DDDM stable IDs.
- New content only `status: draft`, `upe.lifecycle: idea|draft`; no `approved`.
- Raw never edited; validators exclude `raw-input/**`.
