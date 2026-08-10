---
type: governance
title: Knowledge Base Usage Guide
description: "Practical guide for humans and agents: how to navigate, read, author, validate, and evolve the Unified Project Execution knowledge bundle (OKF + DDD organization)."
tags: [governance, usage, guide, okf, ddd, navigation, authoring, validation]
sources:
  - raw-input/knowledge-base/raw-input/DDD.md
  - raw-input/knowledge-base/00_principles.md
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
---

# Knowledge Base Usage Guide

> Attribution: structure/conventions adopted from `GoogleCloudPlatform/knowledge-catalog/okf` (SPEC v0.2, Apache-2.0); no upstream content copied. DDD organization per `knowledge-base/raw-input/DDD.md` (architect-approved). All current content is **draft/candidate** — nothing in this bundle is `approved` yet.

## 1. What this bundle is

`knowledge-base/` is the **single source of truth** for UPE knowledge, organized as one OKF v0.2 bundle with a DDD-inspired classification:

- **OKF answers** *how knowledge is represented, identified, linked and exchanged*: Markdown + YAML frontmatter, path-as-ID, bundle-relative links, `index.md`/`log.md`, provenance/trust/freshness fields.
- **DDD answers** *how the problem domain is partitioned*: the chain `Domains → Capabilities → Problems → Use Cases → Events → Solution Candidates → Reusable Modules` (per `raw-input/knowledge-base/raw-input/DDD.md`).

Two golden rules:

1. **KB-first** — knowledge is captured once here and referenced from everywhere else. No other directory (docs, labs, `.pi`) may introduce an architectural fact absent from the KB.
2. **Raw is immutable** — `raw-input/**` is historical evidence. Never edit raw files, even to fix links or the legacy product name.

## 2. Directory structure

```
knowledge-base/
├── index.md                         # entry point: progressive disclosure (start here)
├── log.md                           # change log (newest first, ISO-date groups)
├── governance/                      # rules and vocabulary — read before authoring
│   ├── principles.md                # operating principles (KB-first, raw immutability, draft-only)
│   ├── glossary.md                  # ubiquitous language
│   ├── metadata-profile.md          # THE metadata contract (fields, types, lifecycle, relations)
│   └── terminology-aliases.md       # legacy/ambiguous spellings → canonical terms
├── architecture/                    # master architecture view (draft integration view)
│   ├── master.md                    # integration view over concepts + decisions + raw sources
│   ├── context-map.md               # DDD context-map framework; M01–M14 = candidates only
│   └── decisions/                   # ADR catalog + template + historical ADR-0001 record
├── domains/                         # 14 candidate functional domains M01–M14 (not bounded contexts)
├── capabilities/                    # 500+ source-backed capability records (one statement each)
├── problems/                        # pain points and gaps surfaced in evidence
├── use-cases/                       # source-backed use cases, linked to capabilities/events
├── events/                          # business events (automation/workflow context)
├── solution-candidates/             # solution/module candidates with traceability
├── labs/                            # R&D laboratory: manifests + experiments (framework only)
│   └── _template/manifest.md        # lab manifest template (copy this for a new lab)
└── raw-input/                       # IMMUTABLE historical evidence (73 files, path-preserved)
```

## 3. Frontmatter contract (summary; full contract in `governance/metadata-profile.md`)

Every active KB file (everything except `raw-input/**`) **must** start with YAML frontmatter:

```yaml
---
type: capability                # type from the dictionary (see below)
title: Short Title
description: One-paragraph description of the concept.
tags: [keyword1, keyword2]
sources:                        # bundle-relative raw evidence backing this record
  - raw-input/docs/UPE_Functional_Blocks_v1.md
generated: 2026-08-10T09:00:00Z
verified: false
status: draft                   # OKF projection: draft | stable | deprecated
stale_after: 2027-08-10
upe:
  id: M01                       # ONLY when an existing DDDM stable ID applies (M01–M14, ADR-*)
  lifecycle: draft              # authoritative DDDM sequence: idea → draft → in-review → approved → superseded → deprecated
  owner: "@module-owner-m01"
  relations:                    # minimal typed vocabulary, {type, target}
    - type: supports
      target: capabilities/enable-decision-making-and-innovation
---
```

**Type dictionary:** `domain`, `subdomain`, `capability`, `problem`, `use-case`, `event`, `solution-candidate`, `module` (DDD concepts) + `governance`, `architecture`, `decision`, `lab`, `navigation`, `log` (structural records).

**Typed relations (allowed vocabulary — do not invent new types):** `supports`, `derived-from`, `evaluates`, `evidenced-by`, `refutes`, `decided-by`, `supersedes`, `derived-document-of`. Target is a bundle-relative path (without `.md`) or a stable ID. DDD context-map edge types are **not** in use yet.

**Statuses:** new content uses `status: draft` and `upe.lifecycle: idea|draft`. **Never assign `approved` or `in-review`** in this phase — promotion is a gated human decision.

## 4. Navigation (humans)

1. **Start at `knowledge-base/index.md`** — progressive disclosure to every collection, governance, architecture, labs and raw corpus.
2. **Read `governance/principles.md` + `governance/glossary.md`** before doing anything — they define the vocabulary and the rules.
3. **For the current architecture:** `architecture/master.md` → `architecture/context-map.md` → `architecture/decisions/`.
4. **For a business area:** pick a `domains/m0X-*.md`, follow its links to capabilities/problems/use-cases/events/solution-candidates.
5. **For evidence:** every concept lists `sources:` — open the raw files under `raw-input/` to check provenance.
6. **Search:** `grep -ri "<term>" knowledge-base --include="*.md"` or use the glossary aliases.

## 5. Authoring workflow (agents and humans)

To add or update knowledge:

1. **Find the right concept** — use `index.md` and the glossary; prefer linking to an existing concept over creating a near-duplicate.
2. **Create one file per concept** under the matching collection (e.g. a new capability → `capabilities/<slug>.md`). One normalized source statement per record.
3. **Fill the frontmatter** per §3; set `status: draft`, `upe.lifecycle: draft` (or `idea`), `sources` pointing to the raw evidence.
4. **Link with bundle-relative paths** (path without `.md`): `[text](../capabilities/validate-models)`. Prefer links over duplicating content.
5. **Preserve contradictions** — if sources disagree, record both claims with separate `sources` and note them under `## Open questions` in the body. Never silently reconcile.
6. **Never edit `raw-input/**`** — evidence stays verbatim; fix problems by editing the active concept instead.
7. **Update `index.md` and `log.md`** with every change (new file → add to index; any change → append a log entry, newest first, ISO-date group).
8. **Validate** (see §7) before committing.

## 6. R&D laboratory (labs/)

- `labs/` hosts experiments and prototypes. A lab is **not** a knowledge document: it may assert nothing canonical. Canonical conclusions/evidence go to the KB (as `evidence` records in a later cycle); a lab README never becomes a second KB.
- **Start a lab:** copy `labs/_template/manifest.md` to `labs/<slug>/manifest.md` and fill:
  - `upstream_intent` — any legitimate source: hypothesis, requirement/constraint, capability, architecture option/feature, ADR/decision (an ADR is **not** mandatory before an experiment);
  - `lab_status` — `active | successful | rejected | superseded | abandoned`;
  - `evidence_links` — where results/evidence live (prefer KB evidence records);
  - run command/environment, outputs, decision influence, retention/deletability.
- **Promotion to `tools/`** (reusable maintained code) requires: reuse intent, an owner, a documented interface, proportionate tests, and a decision/evidence basis. Throwaway probes stay in `labs/` or branch history.

## 7. Common commands (validation & maintenance)

Run from the repository root (git-bash on Windows; quote paths with spaces/parentheses/`+`):

```bash
# --- Repository / migration integrity ---
git status --porcelain=v1                                   # clean worktree check
git diff --summary --find-renames                           # moves detected as renames (no delete+add)

# --- Markdown lint (KB + README; raw excluded — it is immutable evidence) ---
npx markdownlint-cli2 --config .pi/temp/markdownlint.json \
  "knowledge-base/**/*.md" "!knowledge-base/raw-input/**" "README.md"

# --- Internal links (every non-raw KB link must resolve) ---
python .pi/temp/check_links.py

# --- Frontmatter contract (type required, upe.id unique, no approved, allowed statuses) ---
python .pi/temp/check_frontmatter.py

# --- Product-name hygiene (no "Unified Production Environment" outside raw/annotated exceptions) ---
git grep -n 'Unified Production Environment' -- ':!knowledge-base/raw-input'

# --- README ghost-path check ---
git grep -nE 'modules/|backlog/|sessions/|prototypes/' README.md

# --- Legacy `.plans` reference check (should be empty in active files) ---
git grep -nE '(^|[^[:alnum:]_])\.plans/' -- . ':!knowledge-base/raw-input/**' ':!.pi/plan/legacy/**'
```

**Optional external tooling** (for the future CI spec — do not install permanently in this phase):
- `okflint` (PyPI `okflint`, mattdav/okflint): `okflint audit`, `okflint validate --manifest okf-base.yaml`, `okflint index` — manifest-driven OKF conformance (rule codes F001/F002/R001/R002; v0.1/v0.2 core rules identical).
- `markdown-link-check`: add `"replacementPatterns": [{"pattern": "^/", "replacement": "{{BASEURL}}/"}]` for root-relative links.
- `okfcli/okf` (Go) and `playcode/okf-lint` (cross-links + staleness) as alternatives.

## 8. Architecture decisions (ADR)

- Decisions are recorded in `architecture/decisions/` as `ADR-{NNNN}` records using `decisions/adr-template.md` (sections: Context, Options, Decision, Consequences, Evidence, Status, Open questions).
- Historical `ADR-0001` (docs-as-data) lives in raw (`raw-input/knowledge-base/architecture/decisions/ADR-0001-docs-as-data.md`) and is referenced from `decisions/adr-0001-history.md` via `derived-from`.
- Decision lifecycle: `idea/hypothesis → research/option → ADR draft → lab evidence → review → accepted/rejected → master architecture & docs update`.

## 9. Agent operating rules (summary)

1. **Read before writing:** `AGENTS.md` → `knowledge-base/index.md` → `governance/principles.md` + `governance/glossary.md` → `architecture/master.md`/`context-map.md` → the relevant concept.
2. **Temporary work goes to `.pi/`** (research, context, plans, reviews) — never into the KB.
3. **Promote only distilled facts/evidence** into KB concepts, with `sources:` and `draft` status; never copy whole reports into the KB.
4. **Never fabricate** sources, verification, or approval; never set `approved`.
5. **Before merging a change:** all §7 checks pass; `index.md`/`log.md` updated; affected architecture views/decisions updated; raw untouched.
6. **Obsolete knowledge:** mark `upe.lifecycle: superseded|deprecated` (gated) or record the replacement relation — never delete evidence.

## 10. Pre-merge checklist (humans)

- [ ] Frontmatter complete and conforming (§3); `type` present; `upe.id` unique if set
- [ ] `sources:` link to real raw evidence; body links resolve (bundle-relative)
- [ ] `status: draft`, `upe.lifecycle: idea|draft`; no `approved`
- [ ] Contradictions preserved with attribution + `## Open questions` where needed
- [ ] `index.md` updated; `log.md` entry added
- [ ] markdownlint / check_links / check_frontmatter pass (§7)
- [ ] No `.pi/**` artifacts staged in the commit (except the frozen `.pi/plan/legacy/**` exception)
- [ ] Raw files untouched

## 11. Troubleshooting

| Symptom | Cause / fix |
|---|---|
| `markdownlint` errors in raw files | Raw is intentionally excluded (`!knowledge-base/raw-input/**`); never edit raw to satisfy a linter |
| `check_links.py` reports a broken link | Link target moved with the bundle; update the active concept link (raw links are exempt) |
| `check_frontmatter.py` reports duplicate `upe.id` | Two records reuse a DDDM ID; only one may carry it — link the other with `derived-from`/`supports` instead |
| `.plans` grep hits | Annotated historical mentions only (raw, `.pi/plan/legacy/**`, `.pi/review/**`); active files must be clean |
| Windows quoting | Always double-quote paths with spaces/`+`/parentheses in git-bash; use `--` before paths in `git mv`/`git rm` |
| Where to ask | `governance/glossary.md` for vocabulary; `architecture/decisions/` for decisions; `labs/` for experiments; raw for evidence |
