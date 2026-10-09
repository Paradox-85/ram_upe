# UPE Repository Agent Rules

## Language
Always respond in English.

## Repository Mission
This repository is the central governed, OKF-based Knowledge Base and architecture system of record for the Unified Project Execution environment (UPE).

It separates **four artifact classes with different lifecycles**: received evidence (`sources/`), non-canonical analysis (`analysis/`), the **single canonical KB** (`knowledge-base/`), and audience deliverables (`reports/`). Plus `labs/` (experiments), `tools/` (maintained utilities) and `.pi/` (agent process state).

## Navigation Authority
**README → AGENTS → `knowledge-base/index.md` → `knowledge-base/governance/` → `knowledge-base/architecture/master.md` → `knowledge-base/architecture/context-map.md` → `sources/`**

`knowledge-base/governance/operating-model.md` is the authority on how human and AI workflows interact; `knowledge-base/governance/usage-guide.md` is the contributor contract; `knowledge-base/governance/metadata-profile.md` is the single metadata authority.

## Where Things Belong
| Content | Location |
|---|---|
| received source payload | `sources/<topic>/` (immutable, one file per revision) |
| human-authored analysis | `analysis/human/<topic>/` |
| durable AI-generated analysis | `analysis/ai/<topic>/` |
| consolidated reviewed analysis | `analysis/reviewed/<topic>/` |
| **canonical knowledge** | `knowledge-base/` |
| source-reference metadata | `knowledge-base/evidence/` |
| generated human-facing views | `knowledge-base/views/` |
| audience deliverable | `reports/{working,architecture-committee,published}/` |
| experiment / prototype | `labs/` |
| maintained reusable utility | `tools/` |
| agent execution state | `.pi/` |

`.pi/` is **not** the AI knowledge layer. Agent plans, research, checkpoints and reviews belong there; durable analysis that a human may review belongs in `analysis/ai/`.

## The Invariant
> Humans and AI may create different analyses of the same evidence, but UPE has only one governed knowledge model. Analysis becomes canonical knowledge only through an explicit human review and promotion process.

Therefore:
- There is **one** canonical KB. Never create a Human KB, an AI KB, or a "machine truth" beside a "human truth".
- `sources/`, `analysis/`, `reports/`, `labs/` and `.pi/` may never introduce a fact absent from the KB.
- Never treat analysis — human or AI — as accepted truth.
- A report or view cannot create canonical knowledge; promote the conclusion separately.

## Authority Order
1. Approved KB concepts and decisions are authoritative.
2. Other KB concepts represent knowledge only at their declared maturity and governance status.
3. `reports/` and `knowledge-base/views/` are derived representations — they never override their KB inputs.
4. `sources/` supports knowledge but is not itself approved architecture.
5. Generated indexes, reports, diagrams, summaries and analyses never override their KB inputs.

## KB-First Rule
- Update the KB before changing derived documentation.
- Do not introduce facts, requirements, decisions, or architecture only in `reports/`, `analysis/` or `views/`.
- Do not treat placement, a version suffix, or a filename such as `_final` as evidence of approval.
- Do not promote current content to approved status without explicit evidence.

## Source Handling
- New sources are placed under `sources/<topic>/` as immutable payloads; never edit a payload — supersede it with a new dated revision.
- Register sources with a `source-reference` record in `knowledge-base/evidence/` (location, revision, hash, origin).
- Distinguish source claims, extracted statements, interpretations, requirements, and conclusions.
- Never silently alter, summarize away, or reconcile conflicting raw sources.
- `knowledge-base/raw-input/` was the legacy ingestion mechanism and **no longer exists** (migrated 2026-10-09). Do not recreate it or any second sources location.

## Metadata Discipline
- Preserve required OKF metadata and stable concept identifiers.
- Do not invent source evidence, verification, approval, owners, dates, maturity, or status.
- Keep knowledge maturity separate from governance or decision status.
- Preserve provenance, freshness, supersession, and relationship metadata where applicable.
- Use only the relation vocabulary in `governance/metadata-profile.md` §6. Do not invent new ID schemes (`upe.id` only for `M01`–`M14`, `ADR-*`).

## Structural Discipline
- Follow the established repository tree and read the nearest applicable `AGENTS.md`.
- Read the relevant directory index before changing governed knowledge.
- Do not create new root-level folders without explicit user approval.
- Avoid duplicate parallel files such as `_new`, `_latest`, and `_final`, and duplicate collection READMEs.
- Update affected links and indexes with every approved structural change.
- Preserve superseded knowledge and its relationships rather than overwriting history.
- Do not assume `src/` contains software or that current reports are derived artifacts; inspect first.


## Publication Surfaces (Azure DevOps)
- **Repos** holds the authoritative artifacts; **Wiki** publishes `main:/knowledge-base` as the code wiki
  *UPE Knowledge Hub* for human browsing and search; **Boards** owns planning; **Pipelines** enforce
  validation.
- The wiki is a **publication and navigation surface over the existing repository**. It does not alter the
  operating model and it never becomes an independent source of truth. Canonical knowledge remains in
  `knowledge-base/`.
- Never restructure the repository for the wiki, and never write canonical knowledge only in the wiki.
- Pages under `knowledge-base/` are wiki pages: page titles come from file names (no spaces, no
  `README.md` for collections), and folder order is defined by committed `.order` files.
- Links to content outside `knowledge-base/` must be absolute repository URLs; in-KB links stay relative.
  Managed by `tools/wiki/make_links_wiki_safe.py` — do not hand-edit those URLs.
- Run `python tools/kb-validate/run_all.py` (includes `check_wiki.py`) before merging anything that
  changes a wiki page, an `.order` file or a cross-boundary link.
- Generated views under `knowledge-base/views/` are never hand-edited; curated entry pages
  (`index.md`, `product-overview.md`, `contributing.md`) are hand-written and must stay traceable.
## Approval Boundaries
Explicit user approval is required before:
- changing the root structure or creating root-level directories;
- changing the KB ontology, taxonomy, module boundaries, or OKF extension model (including new concept types or stable-ID schemes);
- changing maturity or status vocabularies, transitions, or approval semantics;
- bulk-moving, renaming, deleting, or archiving content;
- changing approved decisions or promoting content to approved;
- modifying derived-document eligibility or synthesis rules;
- changing branch strategy, merge policy, CODEOWNERS, or CI approval gates;
- resolving material contradictions by assumption.

AI must never autonomously approve requirements or architecture, mark an ADR accepted, change approved domain boundaries, or promote analysis into canonical knowledge.

## Agent Change Sequence
1. Locate relevant KB concepts and indexes.
2. Inspect source provenance and supporting evidence (`sources/`, `evidence/`).
3. Check maturity, status, freshness, verification, and approval.
4. Identify affected relationships, derived artifacts, and contradictions.
5. Make the smallest coherent KB-first change.
6. Validate metadata, identifiers, links, and source references.
7. Regenerate affected indexes and reproducible views.
8. Re-synthesize affected documents only when eligibility and approval rules permit it.
9. Report assumptions, unresolved contradictions, and approvals still required.

## Validation
- Use only commands verified against repository or current OKF tooling.
- Run `python tools/kb-validate/run_all.py` (frontmatter, links, provenance). Add `--lint` for markdownlint.
- Prefer reproducible Python-based validation compatible with the repository environment.
- Generated views must be reproducible and must not contain independently maintained authority.
- Validation success does not itself grant governance approval.

## Final Report
Every change report must identify:
- files and concepts changed;
- maturity or status transitions;
- sources used and provenance checked;
- relationships and links updated;
- indexes or documents regenerated;
- validation performed and its result;
- unresolved questions, contradictions, and approvals still required.

## Audit Safety
Agents may create research, context, inventory, design, and planning artifacts under `.pi/` (which is gitignored) and may update this file only when explicitly authorized. Do not perform migration, bulk restructuring, or application-source changes without a separately approved implementation plan. Never write into `.pi/` artifacts that are expected to be ignored without verifying `git check-ignore` for each intended path first.
