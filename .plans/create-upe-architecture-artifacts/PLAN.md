# Create UPE Architecture Artifacts

This plan creates or refreshes the requested UPE knowledge-base artifacts and updates the index and changelog so the repository remains complete and ready to commit.

## Context

Key findings from read-only analysis:

- The repository root is `C:/Development/upe/UPE` with the UPE knowledge base under `knowledge-base/`.
- The DDDM framework source is `prompts/LLM-Native Product Design Framework.md` and defines Docs-as-Data / Design-by-Dialogue, Git-style master/fork/merge governance, Mermaid diagrams, and Markdown as source of truth.
- `knowledge-base/00_principles.md` is approved and defines required YAML front matter fields: `id`, `type`, `status`, `owner`, `version`, `last_updated`, `parent`, `tags`. The user request says each created file must have the standard header fields `id`, `type`, `status`, `owner`, `version`, `last_updated`, `tags`; to remain consistent with the actual approved standard, include `parent` as well.
- Approved files listed by the user must not be modified except `00_index.md` and `00_changelog.md`, which the task explicitly requires updating.
- `knowledge-base/master.md` is approved and defines UPE as Unified Project Execution: a coordination/intelligence layer, not a CDE/DMS/authoring tool replacement. It also contains a 14-module registry, including M01 and future M02-M05 owners/statuses.
- `knowledge-base/00_glossary.md` is approved and defines the canonical terms to use: Unified Project Execution, CDE, DMS, master, fork, merge, ADR, knowledge graph, interface contract, GBA, idempotency, etc.
- M01 data model and requirement files exist and should be treated as canonical references:
  - `knowledge-base/modules/m01_project_initialization/data_model.md` defines entities including `ENT-Project`, `ENT-ProjectTemplate`, `ENT-ProvisioningJob`, `ENT-ProvisioningTask`, plus Project attributes such as `project_id`, `name`, `project_code`, `client_name`, `client_id`, `gbu`, `location`, `opportunity_id`; ProjectTemplate attributes include `template_id`, `name`, `description`, `project_class`, `folder_structure`, `tool_configuration`, `standards_set`, `default_roles`, `default_channels`.
  - `knowledge-base/modules/m01_project_initialization/requirements.md` defines valid M01 requirement IDs including `REQ-M01-010` through `REQ-M01-017` for the wizard, `REQ-M01-020` through `REQ-M01-027` for template/provisioning, `REQ-M01-050` through `REQ-M01-054` for provisioning status/recovery, and `REQ-M01-060` through `REQ-M01-067` for non-functional/security requirements.
- `src/loop/loop.md` contains the Copilot sparing session. Relevant architecture context appears around the `Copilot sparing session` section and includes layer references such as Authoring Tools / CDE / integration / orchestration / AI-data / enterprise systems / collaboration and build-vs-buy options.
- Some target files currently exist, but they do not exactly satisfy the user's requested content/statuses:
  - `knowledge-base/architecture/arch_overview.md` exists but uses a different component diagram and references a 9-layer source; it should be refreshed to explicitly show the requested 7-layer stack from Authoring Tools to Collaboration UX.
  - `knowledge-base/architecture/module_interfaces.md` exists but should be refreshed to include all requested fields for each interface, including `direction`, `owner`, `status`, ERP retry + idempotency, M365 channel templates, Template Library `estimated_setup_duration`, and KG status deferred to Sprint 2.
  - `knowledge-base/architecture/decisions/ADR-0001-docs-as-data.md` exists but should be aligned to the exact requested ADR title/status/context/decision/alternatives/review date of `2026-08-26`.
  - `knowledge-base/reports/stakeholder_brief_2026-05-26.md` exists but status is `approved`; the request requires `draft (pending review)` and exactly three decisions requested from colleagues.
  - `knowledge-base/prototypes/sprint-01_project_initialization/prototype_prompt.md` exists but should be reshaped to exactly five requested demo screens and emphasize it is a design validation prototype, not production code.
- `knowledge-base/00_index.md` currently already lists these files, but the metadata/statuses will need to be corrected after file refreshes. The statistics section should also be checked/updated if statuses or counts change.
- `knowledge-base/00_changelog.md` currently has an initial 1.0.0 entry that already mentions the files. Add a new session entry for the requested artifact creation/refresh rather than rewriting the approved history.

## Plan:

1. Create or overwrite `knowledge-base/architecture/arch_overview.md` with a complete Markdown artifact using YAML front matter: `id: arch-overview`, `type: architecture`, `status: draft` or `in-review`, `owner: "@chief-architect"`, `version: 1.0`, `last_updated: 2026-05-26`, `parent: master.md`, and relevant tags.
   - Include UPE positioning as a coordination/intelligence layer and explicitly state it is not a CDE or DMS.
   - Include a hybrid build-vs-buy section: buy commodity layers (CDE, iPaaS, data lake infrastructure), build differentiating layers (engineering AI decomposition, knowledge graph, cross-platform decision intelligence, unified collaboration UX).
   - Add a Mermaid component diagram with the exact requested 7-layer stack: Authoring Tools → CDE → Integration/iPaaS → Orchestration → Enterprise Data/AI → Enterprise Systems → Collaboration UX. Show Azure foundation and standards/governance as cross-cutting if useful.
   - Add architectural principles: vendor independence, open standards (`IFC`, `bSDD`, `W3C`), Microsoft Azure as cloud foundation.
   - Add relative references to `../../src/loop/loop.md` if referencing from `knowledge-base/architecture/` would be invalid; instead from this file use `../../src/loop/loop.md` only if Markdown links are expected to resolve from the file location, and use `../master.md` for `knowledge-base/master.md`. Avoid absolute URLs for internal files.

2. Create or overwrite `knowledge-base/architecture/module_interfaces.md` with a complete M01 interface contract artifact.
   - Use YAML front matter with `id: module-interfaces`, `type: architecture`, `status: draft` or `in-review`, `owner: "@chief-architect"`, `version: 1.0`, `last_updated: 2026-05-26`, `parent: master.md`, and tags.
   - Add a short scope statement that M01 is the demo module and all payload shapes are simplified and aligned to `../modules/m01_project_initialization/data_model.md`.
   - Add an interface registry table with stable IDs exactly as requested:
     1. `IF-M01-CRM-001`: CRM/Opportunity → Project seed data
     2. `IF-M01-HR-001`: Azure AD/Workday → Users, org hierarchy, skills
     3. `IF-M01-ERP-001`: ERP/Maconomy → Project codes, cost context
     4. `IF-M01-M365-001`: Teams/SharePoint/Planner → Collaboration spaces
     5. `IF-M01-CDE-001`: ACC/ProjectWise → CDE workspace provisioning
     6. `IF-M01-TEMPLATE-001`: Template Library → Project template selection
     7. `IF-M01-KG-001`: Knowledge Graph → Similar projects, reusable standards, with status deferred to Sprint 2.
   - For each interface include: direction, trigger, simplified JSON payload shape, error handling, owner, and status.
   - For `IF-M01-ERP-001`, explicitly include retry and idempotency handling, e.g. `idempotency_key` derived from `project_id`/`opportunity_id`, safe retry up to 3 attempts, duplicate response treated as success if mapped project code matches.
   - For `IF-M01-M365-001`, include channel templates using `default_channels` from `ENT-ProjectTemplate` terminology.
   - For `IF-M01-TEMPLATE-001`, add `estimated_setup_duration` to the payload but do not imply it exists in the approved `ENT-ProjectTemplate` model unless presented as an interface/display field from the Template Library. Avoid inventing a new entity ID.
   - For `IF-M01-KG-001`, make it non-blocking and mark `status: deferred to Sprint 2`.
   - Add a Mermaid sequence diagram showing the full provisioning flow across CRM, Template Library, KG, ERP/Maconomy, Azure AD/Workday, Teams/SharePoint/Planner, ACC/ProjectWise, and M01/UPE Wizard/Provisioning Orchestrator.

3. Create or overwrite `knowledge-base/architecture/decisions/ADR-0001-docs-as-data.md` with the requested ADR content.
   - Use YAML front matter: `id: ADR-0001`, `type: decision`, `status: accepted`, `owner: "@chief-architect"`, `version: 1.0`, `last_updated: 2026-05-26`, `parent: ../arch_overview.md` or `../../master.md`, tags including `ADR`, `docs-as-data`, `markdown`, `mermaid`, `git`.
   - Use title: `# ADR-0001: Adopt Markdown + Mermaid + Git-style workflow as the single source of truth for UPE product design`.
   - Use `## Status` with `Accepted`.
   - Context must state traditional specs, Visio diagrams, and Word documents lose context, diverge from reality, and cannot be queried or versioned effectively.
   - Decision must state all design knowledge lives as structured MD files in Git; diagrams generated from Mermaid inside MD; reports are rendered snapshots, never source of truth.
   - Include positive and negative consequences.
   - Include alternatives rejected exactly: Confluence wiki, SharePoint pages, traditional TOGAF artifacts, Enterprise Architect (Sparx).
   - Use review date `2026-08-26`.
   - Reference `../../../prompts/LLM-Native Product Design Framework.md` if linking from `knowledge-base/architecture/decisions/`.

4. Create or overwrite `knowledge-base/reports/stakeholder_brief_2026-05-26.md`.
   - Use YAML front matter: `id: stakeholder-brief-2026-05-26`, `type: report`, `status: draft`, `owner: "@chief-architect"`, `version: 0.1`, `last_updated: 2026-05-26`, `parent: ../master.md`, tags.
   - Include the required derived snapshot warning from `00_principles.md`.
   - Make the audience architects and module owners who will attend the demo session.
   - Keep it as a one-page narrative explaining why DDDM matters for Unified Project Execution.
   - Explain master, fork, and prototype in plain language without jargon.
   - Describe what will be shown in the demo session and link relatively to `../demo_script.md`.
   - Include exactly the three requested colleague decisions:
     1. Adopt this framework as the working method for UPE design?
     2. Assign module owners for M02–M05?
     3. Agree on branching convention and review cadence?
   - Avoid extra unrelated requested decisions from the existing file.

5. Create or overwrite `knowledge-base/prototypes/sprint-01_project_initialization/prototype_prompt.md`.
   - Use YAML front matter: `id: prototype-sprint01-m01`, `type: prototype`, `status: draft`, `owner: "@module-owner-m01"`, `version: 0.1`, `last_updated: 2026-05-26`, `parent: ../../modules/m01_project_initialization/index.md`, tags.
   - Make the body a self-contained prompt ready to paste into v0.dev, Replit, or Claude.
   - Reference the canonical data model with a relative path: `../../modules/m01_project_initialization/data_model.md`.
   - Use only fields/entities aligned with the canonical data model; include a note that `estimated_setup_duration` is a UI/prototype field from Template Library interface, not a canonical M01 entity attribute unless later approved.
   - Describe exactly five demo screens:
     1. Project Creation Wizard (step 1: project type + template selection)
     2. Project Metadata Form (step 2: name, client, disciplines, GBA, location)
     3. Team & Access Setup (step 3: add members, assign roles)
     4. Provisioning Status Dashboard (real-time status per system: ERP, M365, CDE)
     5. Project Landing Page (post-initialization: summary, quick actions, notifications)
   - Include tech stack hint: React + TailwindCSS or shadcn/ui; mock data acceptable.
   - Explicitly state this is a design validation prototype, not production code.
   - Avoid adding unrelated admin screens that were not requested.

6. Update `knowledge-base/00_index.md`.
   - Ensure entries for all created/refreshed files exist and match final status/type/owner/purpose:
     - `architecture/arch_overview.md`
     - `architecture/module_interfaces.md`
     - `architecture/decisions/ADR-0001-docs-as-data.md`
     - `reports/stakeholder_brief_2026-05-26.md`
     - `prototypes/sprint-01_project_initialization/prototype_prompt.md`
   - Keep all existing approved files listed; do not remove M01, fork, session, or demo script entries.
   - Reconcile the statistics section to reflect actual counts/statuses after the refresh if necessary.
   - Consider `type` values in front matter: `architecture` and `prototype` are already present in existing files, although not listed in the strict type examples in `00_principles.md`; retain project-consistent usage unless the implementor elects to use broader allowed values. Do not change approved principles.

7. Update `knowledge-base/00_changelog.md`.
   - Add a new top entry for this session dated `2026-05-26`, e.g. `## [1.0.1] — 2026-05-26`.
   - Record creation/refresh of the five artifacts, index update, and that M01 interfaces/prototype/report were aligned to the user-requested demo package.
   - Do not rewrite or remove the existing `1.0.0` initial repository creation entry.

8. Perform validation before final response.
   - Confirm every target file starts with YAML front matter and contains all required fields.
   - Confirm every architecture/process file contains at least one Mermaid diagram: `arch_overview.md`, `module_interfaces.md`, and ADR if considered architecture/process should include a Mermaid diagram to satisfy the user's broad quality rule. To be safe, add a small Mermaid flowchart to the ADR showing `Markdown source -> Mermaid render -> Reports snapshot`.
   - Confirm internal links are relative paths and plausible from each file's location.
   - Confirm no new `REQ-*` or `ENT-*` IDs are invented beyond the existing M01 files. Refer to existing entities by name, and only use existing requirement IDs if needed.
   - Confirm `IF-M01-*` stable IDs match exactly the requested list.
   - Confirm terminology matches `00_glossary.md`: use `Unified Project Execution`, `CDE`, `knowledge graph`, `master`, `fork`, `merge`, `ADR`.

## Risks / Open Questions

- The user described the five artifacts as missing, but the local repository already contains files at those paths. The implementation should treat this as a refresh/overwrite to match the requested content precisely, not as a reason to skip them.
- The task says not to modify approved files, but also explicitly requires updating `00_index.md` and `00_changelog.md`, which are approved. This plan assumes the explicit task permission overrides the general non-modification rule for those two files only.
- The approved YAML type vocabulary in `00_principles.md` does not list `architecture` or `prototype`, but existing repository files already use those values. The implementor should preserve consistent existing practice unless a repository-wide standards update is separately approved.
- The requested `estimated_setup_duration` field is not currently in `ENT-ProjectTemplate`; include it only in the Template Library interface/prototype display context unless the user separately approves a data model change.
