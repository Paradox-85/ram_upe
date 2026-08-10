# UPE Repository Agent Rules

## Language
Always respond in English.

## Repository Mission
This repository is the central governed, OKF-based Knowledge Base and architecture system of record for the Unified Project Execution environment (UPE).

The repository is currently under structural audit. Existing paths remain current facts; any target structure described in audit or planning artifacts is a proposal until explicitly approved and migrated.

## Current and Proposed Locations
- Navigation authority: **README → AGENTS → `knowledge-base/index.md` → `knowledge-base/governance/` → `knowledge-base/architecture/master.md` → `knowledge-base/architecture/context-map.md` → `knowledge-base/raw-input/`**.
- The canonical KB lives under `knowledge-base/` (OKF + DDD collections). Do not assume a `kb/` tree exists.
- Legacy `docs/`, `src/`, `prompts/` content is preserved verbatim under `knowledge-base/raw-input/` as immutable evidence (raw, not authority).
- Store agent research, context, and plans under `.pi/`; these are operational artifacts, not architectural authority.
- Proposed migrations, taxonomies, and directory contracts belong in audit or plan artifacts until approved.

## Authority Order
1. Approved KB concepts and decisions are authoritative.
2. Other KB concepts represent knowledge only at their declared maturity and governance status.
3. `docs/` contains approved derived representations once approval and traceability are established.
4. Raw sources support knowledge but are not themselves approved architecture.
5. Generated indexes, reports, diagrams, and summaries never override their KB inputs.

## KB-First Rule
- Update the KB before changing derived documentation.
- Do not introduce facts, requirements, decisions, or architecture only in `docs/`.
- Do not treat placement in `docs/`, a version suffix, or a filename such as `_final` as evidence of approval.
- Do not promote current content to approved status without explicit evidence.

## Source Handling
- Raw project sources belong in the defined source area inside the KB once that location is approved.
- Register provenance and preserve the original source meaning.
- Distinguish source claims, extracted statements, interpretations, requirements, and conclusions.
- Never silently alter, summarize away, or reconcile conflicting raw sources.
- Register binary sources with an adjacent or linked source record when the approved model requires it.

## Metadata Discipline
- Preserve required OKF metadata and stable concept identifiers.
- Do not invent source evidence, verification, approval, owners, dates, maturity, or status.
- Keep knowledge maturity separate from governance or decision status.
- Preserve provenance, freshness, supersession, and relationship metadata where applicable.

## Structural Discipline
- Follow the established repository tree and read the nearest applicable `AGENTS.md`.
- Read the relevant directory index before changing governed knowledge.
- Do not create new root-level folders without explicit user approval.
- Avoid duplicate parallel files such as `_new`, `_latest`, and `_final`.
- Update affected links and indexes with every approved structural change.
- Preserve superseded knowledge and its relationships rather than overwriting history.
- Do not assume `src/` contains software or that current reports are derived artifacts; inspect first.

## Approval Boundaries
Explicit user approval is required before:
- changing the root structure or creating root-level directories;
- changing the KB ontology, taxonomy, module boundaries, or OKF extension model;
- changing maturity or status vocabularies, transitions, or approval semantics;
- bulk-moving, renaming, deleting, or archiving content;
- changing approved decisions or promoting content to approved;
- modifying derived-document eligibility or synthesis rules;
- changing branch strategy, merge policy, CODEOWNERS, or CI approval gates;
- resolving material contradictions by assumption.

## Agent Change Sequence
1. Locate relevant KB concepts and indexes.
2. Inspect source provenance and supporting evidence.
3. Check maturity, status, freshness, verification, and approval.
4. Identify affected relationships, derived artifacts, and contradictions.
5. Make the smallest coherent KB-first change.
6. Validate metadata, identifiers, links, and source references.
7. Regenerate affected indexes and reproducible views.
8. Re-synthesize affected documents only when eligibility and approval rules permit it.
9. Report assumptions, unresolved contradictions, and approvals still required.

## Validation
- Use only commands verified against repository or current OKF tooling.
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
During the current audit, agents may create research, context, inventory, design, and planning artifacts under `.pi/` and may update this file when explicitly authorized. Do not perform migration, bulk restructuring, or application-source changes without a separately approved implementation plan.
