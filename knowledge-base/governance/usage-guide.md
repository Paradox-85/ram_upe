---
type: governance
title: Knowledge Base Usage Guide
description: "Practical guide for humans and agents: bundle basis/version, repository artifact classes, structure, frontmatter contract, authoring, source intake, analysis and promotion workflow, validation, ADR and lab workflows, agent rules."
tags: [governance, usage, guide, okf, ddd, navigation, authoring, validation, operating-model]
sources:
  - ../sources/ramboll/DDD.md
  - ../sources/legacy/knowledge-base/00_principles.md
generated: 2026-08-10T09:10:00Z
verified: false
status: draft
stale_after: 2027-08-10
upe:
  lifecycle: draft
  owner: "@chief-architect"
  relations:
    - type: derived-from
      target: governance/metadata-profile
    - type: supports
      target: index
    - type: supports
      target: governance/operating-model
---

# Knowledge Base Usage Guide

> Attribution: structure/conventions adopted from `GoogleCloudPlatform/knowledge-catalog/okf` (SPEC v0.2, Apache-2.0); no upstream content copied. DDD organization per `sources/ramboll/DDD.md` (architect-approved). All current content is **draft/candidate** — nothing in this bundle is `approved` yet.

## 1. What this bundle is

`knowledge-base/` is the **single source of truth** for UPE knowledge, organized as one OKF v0.2 bundle with a DDD-inspired classification:

- **OKF answers** *how knowledge is represented, identified, linked and exchanged*: Markdown + YAML frontmatter, path-as-ID, bundle-relative links, `index.md`/`log.md`, provenance/trust/freshness fields.
- **DDD answers** *how the problem domain is partitioned*: the chain `Domains → Capabilities → Problems → Use Cases → Events → Solution Candidates → Reusable Modules` (per `sources/ramboll/DDD.md`).

Three golden rules:

1. **KB-first** — knowledge is captured once here and referenced from everywhere else. No other directory (`sources/`, `analysis/`, `reports/`, `labs/`, `.pi/`) may introduce an architectural fact absent from the KB.
2. **Evidence is immutable** — `sources/**` is received evidence. Never edit a payload, even to fix links or the legacy product name.
3. **Nothing becomes knowledge by itself** — human and AI analysis are equally non-canonical until a human promotion gate accepts a finding. See [`operating-model.md`](operating-model.md).

### 1.1 Basis, version and provenance

The bundle was **redeployed from scratch** (harness `20260810-074805-upe-harmonization`, 2026-08-10) on these foundations, and **re-based onto the hybrid operating model** (refactoring `20261009-104047-upe-refactor`, 2026-10-09):

| Foundation | Detail |
|---|---|
| **Upstream format repo** | `GoogleCloudPlatform/knowledge-catalog` → `okf/SPEC.md` — **Open Knowledge Format v0.2** (Apache-2.0). Only structure/conventions adopted; **no upstream content copied** (attribution in `log.md`). Conformance: 3 rules (parseable frontmatter, non-empty `type`, reserved filenames); consumers tolerate broken links/unknown types/missing fields. |
| **DDD input** | `sources/ramboll/DDD.md` — architect-approved (2026-08-10): the chain `Domains → Capabilities → Problems → Use Cases → Events → Solution Candidates → Reusable Modules` + 5 focus concepts. |
| **Legacy DDDM corpus** | Old `knowledge-base/` (00_*.md, master.md, architecture) → source of stable IDs (`M01–M14`, `ADR-0001`), the authoritative lifecycle (`idea→draft→in-review→approved→superseded→deprecated`), 14 functional domains, 520 capabilities — preserved verbatim under `sources/legacy/knowledge-base/`. |
| **Evidence corpus** | Immutable payloads under `sources/**` (transported 2026-10-09 from `knowledge-base/raw-input/`, byte-preserved, path-mapped) backing every concept via `sources:`. |
| **Governance** | Draft-only scope, no promotion without explicit user approval, `governance/metadata-profile.md` as the single metadata authority, `governance/operating-model.md` as the operating model. |

## 2. Repository structure

The repository separates **four artifact classes with different lifecycles**. Only one of them is canonical.

```
/
├── README.md                         # human entry point: where do I put things
├── AGENTS.md                         # agent operating rules
├── azure-pipelines.yml               # CI mirror to GitHub
│
├── sources/                          # CLASS A — received evidence (NEVER canonical)
│   ├── README.md                     # intake contract
│   ├── transport/                    # Transport GBA material
│   ├── vendors/{autodesk,aveva,hexagon}/
│   ├── meetings/                     # transcripts, workshops
│   ├── ramboll/                      # Ramboll-internal source documents
│   ├── standards/                    # external standards (e.g. ISO 19650)
│   └── legacy/                       # historical docs + legacy DDDM corpus
│
├── analysis/                         # CLASS B — non-canonical analysis
│   ├── README.md                     # metadata + lifecycle + promotion contract
│   ├── human/<topic>/                # manual analysis
│   ├── ai/<topic>/                   # durable AI analysis
│   └── reviewed/<topic>/             # consolidated, review-ready
│
├── knowledge-base/                   # CLASS C — THE canonical KB
│   ├── index.md log.md
│   ├── governance/                   # principles, glossary, metadata, operating model, this guide
│   ├── requirements/                 # first-class traceability layer
│   ├── domains/                      # 14 candidate functional domains M01–M14
│   ├── capabilities/                 # 520 source-backed capability records
│   ├── problems/ use-cases/ events/ solution-candidates/
│   ├── architecture/
│   │   ├── master.md                 # primary human-readable integration view
│   │   ├── context-map.md            # M01–M14 = candidates only
│   │   └── decisions/                # ADR catalog + template + ADR-0001 history
│   ├── evidence/                     # source-reference records (metadata about sources)
│   └── views/                        # GENERATED human surface (non-authoritative)
│
├── reports/                          # CLASS D — audience deliverables (never canonical)
│   ├── README.md
│   ├── working/  architecture-committee/  published/
│
├── labs/                             # executable experiments (not knowledge)
│   ├── README.md  _template/manifest.md
│
├── tools/                            # maintained reusable utilities
│   └── kb-validate/                  # the validation gate
│
└── .pi/                              # agent execution state — NOT a knowledge layer
```

**Where do I put…?** — the short answer:

| Artefact | Location |
|---|---|
| a document I just received | `sources/<topic>/` |
| my own assessment | `analysis/human/<topic>/` |
| durable AI analysis | `analysis/ai/<topic>/` |
| agent scratch/research | `.pi/` |
| accepted reusable knowledge | `knowledge-base/` |
| an Architecture Committee paper | `reports/architecture-committee/` |
| a prototype | `labs/` |
| a reusable utility | `tools/` |

## 3. Frontmatter contract (summary; full contract in `governance/metadata-profile.md`)

Every active KB file (`knowledge-base/**`, excluding the legacy corpus) **must** start with YAML frontmatter:

```yaml
---
type: capability                # type from the dictionary (see below)
title: Short Title
description: One-paragraph description of the concept.
tags: [keyword1, keyword2]
sources:                        # evidence backing this record
  - ../sources/ramboll/upe-foundations.md
generated: 2026-10-09T09:00:00Z
verified: false
status: draft                   # OKF projection: draft | stable | deprecated
stale_after: 2027-10-09
upe:
  id: M01                       # ONLY when an existing DDDM stable ID applies (M01–M14, ADR-*)
  lifecycle: draft              # idea → draft → in-review → approved → superseded → deprecated
  owner: "@module-owner-m01"
  relations:                    # minimal typed vocabulary, {type, target}
    - type: supports
      target: domains/m01-project-lifecycle-environment-management
---
```

**Type dictionary:** `domain`, `subdomain`, `capability`, `problem`, `use-case`, `event`, `solution-candidate`, `module`, `requirement` (DDD concepts) + `governance`, `architecture`, `decision`, `lab`, `navigation`, `log`, `view`, `source-reference` (structural records).

**Typed relations (allowed vocabulary — do not invent new types):** `supports`, `derived-from`, `evaluates`, `evidenced-by`, `refutes`, `decided-by`, `supersedes`, `derived-document-of`. Target is a bundle-relative path (without `.md`), a KB record path, or `../sources/...` for evidence. DDD context-map edge types are **not** in use yet.

**Statuses:** new content uses `status: draft` and `upe.lifecycle: idea|draft`. **Never assign `approved` or `in-review`** in this phase — promotion is a gated human decision.

**Analysis artifacts** follow a different, lighter contract and a different lifecycle (`working → review-ready → reviewed → superseded`) — see [`../../analysis/README.md`](https://dev.azure.com/ramboll-bim/_git/UPE?path=/analysis/README.md&version=GBmain). Never apply the canonical lifecycle to analysis, and never apply the analysis lifecycle to the KB.

## 4. Navigation (humans)

1. **Start at `README.md`** — the where-to-put map, then `knowledge-base/index.md` for the bundle map.
2. **Read `governance/principles.md` + `governance/glossary.md`** before doing anything — they define the vocabulary and rules.
3. **Operating model:** `governance/operating-model.md` — the four artifact classes, the two surfaces, the promotion gate.
4. **For the current architecture:** `architecture/master.md` → `architecture/context-map.md` → `architecture/decisions/`.
5. **For a business area:** pick a `domains/m0X-*.md`, follow its links to capabilities/problems/use-cases/events/solution-candidates.
6. **For a readable overview instead of atomic files:** `views/` (generated, non-authoritative).
7. **For evidence:** every concept lists `sources:` — open the payload under `sources/`, or the `evidence/` record describing it.
8. **Search:** `grep -ri "<term>" knowledge-base --include="*.md"` or use the glossary aliases.

## 5. Authoring workflow (agents and humans)

To add or update canonical knowledge:

1. **Find the right concept** — use `index.md` and the glossary; prefer linking to an existing concept over creating a near-duplicate.
2. **Create one file per concept** under the matching collection (e.g. a new requirement → `requirements/<slug>.md`). One normalized source statement per record.
3. **Fill the frontmatter** per §3; set `status: draft`, `upe.lifecycle: draft` (or `idea`), and `sources:` pointing at the evidence in `sources/`.
4. **Link with paths that resolve** (path-as-ID; use the `.md` suffix in Markdown links so validators resolve them): `[text](../capabilities/enable-decision-making-and-innovation.md)`. Prefer links over duplicating content.
5. **Preserve contradictions** — if sources disagree, record both claims with separate `sources` and note them under `## Open questions`. Never silently reconcile.
6. **Never edit `sources/**`** — evidence stays verbatim; fix problems by editing the active concept instead.
7. **Update `index.md` and `log.md`** with every change (new file → add to index; any change → append a log entry, newest first, ISO-date group).
8. **Validate** (§7) before committing.

### 5.1 Adding a new source document

1. Place the payload under `sources/<topic>/` using `<iso-date>-<slug>.<ext>`. Never overwrite an existing revision.
2. Add a `source-reference` record in `knowledge-base/evidence/` recording location, revision, hash and origin.
3. Reference it from concepts (and from analyses) via `sources:`.
4. Ask: *is this a source, or is it actually my analysis of a source?* If the file contains conclusions, it belongs in `analysis/`, not `sources/`.

### 5.2 Promoting analysis into the KB

Analysis — human or AI — becomes canonical only through the gate:

```text
SOURCE → ANALYSIS → CANDIDATE FINDING → HUMAN REVIEW → ACCEPT/MODIFY/REJECT → CANONICAL KB
```

Promotion is **per finding**. Create the KB record separately (it gets its own `sources:` and a `derived-from` relation to the analysis), then record the outcome in the analysis artifact's `promoted:` field. Agents must not perform this step on their own.

## 6. R&D laboratory (`labs/`)

- `labs/` hosts experiments and prototypes and lives **outside** the KB. A lab asserts nothing canonical; canonical conclusions go to the KB as records backed by evidence.
- **Start a lab:** copy `../labs/_template/manifest.md` to `labs/<slug>/manifest.md` and fill in:
  - `upstream_intent` — hypothesis, requirement/constraint, capability, architecture option or ADR (an ADR is **not** mandatory before an experiment);
  - `lab_status` — `idea | planned | active | concluded | archived`;
  - `evidence_links` — where results live (prefer KB evidence records);
  - run command/environment, outputs, decision influence, retention.
- **Promotion to `tools/`** (reusable maintained code) requires: reuse intent, an owner, a documented interface, a contract and proportionate validation. Throwaway probes stay in `labs/`.

## 7. Common commands (validation & maintenance)

Run from the repository root (git-bash on Windows; quote paths with spaces/parentheses/`+`):

```bash
# --- Knowledge-base validation gate (all three gates) ---
python tools/kb-validate/run_all.py
python tools/kb-validate/run_all.py --lint          # + markdownlint (needs npx)

# --- Individual gates ---
python tools/kb-validate/check_frontmatter.py       # type/status/lifecycle/upe.id contract
python tools/kb-validate/check_links.py             # every local Markdown link resolves
python tools/kb-validate/check_sources.py           # every sources:/relations target resolves

# --- Repository integrity ---
git status --porcelain=v1                           # clean worktree check
git diff --summary --find-renames                   # moves detected as renames (no delete+add)

# --- Hygiene greps ---
git grep -n 'Unified Production Environment' -- ':!sources'     # product-name hygiene
git grep -nE 'modules/|backlog/|sessions/' README.md AGENTS.md  # ghost-path check
git grep -nE '(^|[^[:alnum:]_])\.plans/' -- . ':!sources/**' ':!.pi/**'
```

`check_sources.py` exists because provenance paths were previously unchecked — a dangling
`sources:` entry could survive indefinitely. See `tools/kb-validate/README.md`.

**Optional external tooling** (not required, do not install permanently):
- `okflint` (PyPI `okflint`, mattdav/okflint): `okflint audit`, `okflint validate --manifest okf-base.yaml`.
- `markdown-link-check` — add `"replacementPatterns": [{"pattern": "^/", "replacement": "{{BASEURL}}/"}]` for root-relative links.

## 8. Injection & sourcing conventions

### 8.1 Where things go

| Input | Destination | What we get |
|---|---|---|
| New source payload (file) | `sources/<topic>/<iso-date>-<slug>.<ext>` (bytes unchanged, never overwritten) | immutable evidence + registered provenance |
| Source registration | `knowledge-base/evidence/src-<topic>-<slug>.md` | canonical metadata about the source (location, revision, hash) |
| New canonical concept | `knowledge-base/<collection>/<slug>.md` (allowed: `requirements`, `domains`, `capabilities`, `problems`, `use-cases`, `events`, `solution-candidates`, `architecture/decisions`) | draft OKF+`upe:` record with required sections |
| Analysis (human or AI) | `analysis/{human,ai}/<topic>/<iso-date>-<slug>.md` | non-canonical, provenance-recorded work product |
| Reviewed analysis | `analysis/reviewed/<topic>/…` | promotion staging |
| Audience deliverable | `reports/{working,architecture-committee,published}/<iso-date>-<slug>.md` | presentation layer, never canonical |
| Generated human surface | `knowledge-base/views/<name>.md` via `tools/kb-views/generate.py` | non-authoritative projection |

Rules: a source payload is never transformed on intake; nothing under `analysis/`, `reports/`, `sources/` or `labs/` is canonical; **no auto-approval, no auto-index/log** — `index.md`/`log.md` stay human-maintained (§5 step 7).

### 8.2 Planned custom Pi skills

Inject/query skills (`kb-inject`, `kb-query`) were designed in plan
`20260810-095945-kb-access-plan.md` and are **not yet implemented**. Until they land, use the
manual workflow of §5, the intake rules of §8.1, and grep triage of §4.

## 9. Architecture decisions (ADR)

- Decisions are recorded in `architecture/decisions/` as `ADR-{NNNN}` records using `decisions/adr-template.md` (sections: Context, Options, Decision, Consequences, Evidence, Status, Open questions).
- Historical `ADR-0001` (docs-as-data) lives in the evidence corpus and is referenced from `decisions/adr-0001-history.md` via `derived-from`.
- Decision lifecycle: `idea/hypothesis → research/option → ADR draft → lab evidence → review → accepted/rejected → master architecture & docs update`.
- **Only humans accept an ADR.** AI may draft one.

## 10. Agent operating rules (summary)

1. **Read before writing:** `AGENTS.md` → `README.md` → `knowledge-base/index.md` → `governance/principles.md` + `governance/glossary.md` → `governance/operating-model.md` → the relevant concept.
2. **Search the canonical KB first**; search `sources/` when you need the original evidence.
3. **Durable AI business/project analysis goes to `analysis/ai/<topic>/`**; agent execution state goes to `.pi/`. These are different things.
4. **Never treat analysis as accepted truth.** Promote only distilled findings, with `sources:` and `draft` status; never copy a whole report into the KB.
5. **Never fabricate** sources, verification or approval; never set `approved`; never accept an ADR; never change approved domain boundaries.
6. **Propose promotion with provenance** rather than performing it; the human gate decides.
7. **Update views after canonical knowledge changes**, and `index.md`/`log.md` with every change.
8. **Preserve DDD/OKF semantics and stable IDs** — no new ID schemes.
9. **Before merging:** all §7 gates pass, `index.md`/`log.md` updated, affected architecture views/decisions updated, `sources/` untouched.
10. **Obsolete knowledge:** mark `upe.lifecycle: superseded|deprecated` (gated) or record the replacement relation — never delete evidence.

## 11. Pre-merge checklist

- [ ] Frontmatter complete and conforming (§3); `type` present; `upe.id` unique if set
- [ ] `sources:` resolve (payload in `sources/` or an `evidence/` record); body links resolve
- [ ] `status: draft`, `upe.lifecycle: idea|draft`; no `approved`
- [ ] Contradictions preserved with attribution + `## Open questions` where needed
- [ ] `index.md` updated; `log.md` entry added
- [ ] `python tools/kb-validate/run_all.py` passes (frontmatter, links, provenance)
- [ ] No `.pi/**` artifacts staged in the commit (except the frozen `.pi/plan/legacy/**` exception)
- [ ] No analysis, report or view treated as canonical; evidence payloads untouched
- [ ] Not a duplicate: no `_new`/`_final`/`_latest` sibling

## 12. Troubleshooting

| Symptom | Cause / fix |
|---|---|
| `markdownlint` errors in evidence payloads | Evidence is excluded from the gate; never edit a source to satisfy a linter |
| `check_links.py` reports a broken link | The target moved; update the active concept's link. Evidence paths are exempt only inside `sources/` |
| `check_sources.py` reports `UNRESOLVED_SOURCE` | A `sources:` entry points at a path that no longer exists — fix the record, or add the missing `evidence/` record |
| `check_sources.py` reports `UNRESOLVED_RELATION` | A `upe.relations` target does not resolve; use a bundle-relative concept path or `../sources/...` |
| `check_frontmatter.py` reports duplicate `upe.id` | Two records reuse a DDDM ID; only one may carry it — link the other with `derived-from`/`supports` |
| Windows quoting | Always double-quote paths with spaces/`+`/parentheses in git-bash; use `--` before paths in `git mv`/`git rm` |
| "Where does my analysis go?" | If a human wrote it → `analysis/human/<topic>/`; if an agent produced durable output → `analysis/ai/<topic>/`; if it is agent scratch → `.pi/` |
| "Can I edit this source file?" | No. Add a new dated revision and register it |
| Where to ask | `governance/glossary.md` for vocabulary; `governance/operating-model.md` for workflow; `architecture/decisions/` for decisions; `labs/` for experiments; `sources/` for evidence |
