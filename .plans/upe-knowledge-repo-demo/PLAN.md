# UPE Knowledge Repository Demo

Implementation plan for the UPE knowledge base repository and a demonstration example for validating the LLM-Native Product Design Framework on the Project Initialization / Provisioning module.

## Context
- The current project has source materials but no target knowledge-base repository, `master.md`, or fork file `project-intialization-module.md` / `project-initialization-module.md` yet.
- The main framework is described in `prompts/LLM-Native Product Design Framework.md`: data-first, docs-as-data, design through LLM dialogue, master as single source of truth, modular forks, review/merge, Mermaid diagrams, ADR, session logs.
- UPE is already described as a complex modular platform in `docs/UPE_Executive_Summary_v1.md` and `docs/UPE_Functional_Blocks_v1.md` with 14 functional domains and 175+ capabilities.
- The priority demo module is confirmed by the materials: `Project Initialization & Provisioning` — must-have foundation, Phase 1 MVP, "start projects correctly, every time". Details are in `docs/UPE_Functional_Blocks_v1.md`, Section 1.1.
- Additional context: `docs/brainstorming.md` defines the modular architecture and suggested Microsoft/Azure stack; `src/loop/loop.md` contains workstreams WS 3.1–3.5, including Unified Project Data Model, AI-accelerated knowledge gathering, Unified Project Initialization and Provisioning, Project data extraction, Open interoperability layer.
- The framework is useful but needs to be extended for enterprise product design: add machine-readable metadata, stable IDs, explicit merge gates, decision log, traceability matrix, quality checks, artifact taxonomy, demo scenario and separation of master/fork/prototype snapshot.

## Plan:
1. Create the target `knowledge-base/` structure inside the current project, without replacing the current source materials. The structure must be clear enough to demonstrate to colleagues:
   - `knowledge-base/master.md` — main entry and integration picture of UPE.
   - `knowledge-base/00_index.md` — index of all knowledge artifacts.
   - `knowledge-base/00_principles.md` — improved framework/rules of work.
   - `knowledge-base/00_glossary.md` — canonical UPE terms.
   - `knowledge-base/00_changelog.md` — global change log.
   - `knowledge-base/architecture/` — overview, interfaces, decisions.
   - `knowledge-base/modules/m01_project_initialization/` — approved/current module slice.
   - `knowledge-base/backlog/forks/project-intialization-module.md` — demo fork preserving the user’s spelling `intialization`; canonical spelling `project-initialization` noted inside.
   - `knowledge-base/sessions/` — example LLM session logs.
   - `knowledge-base/reports/` — derived snapshots/stakeholder brief.
   - `knowledge-base/prototypes/` — prompt/spec for generating a demo prototype.
2. Record the improved version of the framework in `knowledge-base/00_principles.md`. Add to the original DDDM the following mandatory elements:
   - YAML front matter for each file.
   - Stable IDs for requirements, entities, workflow steps, interfaces, ADR (`REQ-M01-001`, `ENT-Project`, `WF-M01-Initialize-010`, `IF-M01-CRM-001`, `ADR-0001`).
   - Lifecycle statuses: `idea`, `draft`, `in-review`, `approved`, `superseded`, `deprecated`.
   - Merge gates: completeness, traceability, interface impact, data model impact, architecture owner approval, stakeholder demo readiness.
   - Definition of Ready / Definition of Done for fork → review → master.
   - Rule: “master contains approved knowledge; forks contain working hypotheses”.
   - Rule: “reports are generated snapshots and must not become source of truth”.
3. Build `knowledge-base/master.md` as a demo master file for UPE architecture. It must be self-contained and include:
   - Vision: UPE = Unified Project Execution / enterprise digital backbone.
   - Scope and non-goals: does not replace CDE/authoring tools, coordinates the project execution layer.
   - 14 functional domains from `docs/UPE_Executive_Summary_v1.md` in a compact table.
   - Layered architecture Mermaid diagram: Collaboration UX, Process Orchestration, Intelligence/Data/Knowledge, Integration/API Hub, CDE/Authoring Tools, Enterprise Systems, Governance cross-cutting.
   - Module registry with at least m01–m14 where m01 has status `approved-demo` or `in-review-demo`.
   - Phase 1 focus: Project Initialization, core data model, user/access, progress tracking, Teams/SharePoint integration.
   - Architecture decisions summary and links to ADR.
   - Traceability to source docs (`docs/...`, `src/loop/loop.md`).
4. Create `knowledge-base/architecture/arch_overview.md` based on `master.md`, but more technically focused:
   - UPE is not a CDE and not a DMS; CDE remains the project system of record, UPE is the coordination/intelligence layer.
   - Buy commodity layers, build differentiating layers: AI-ready engineering decomposition, knowledge graph, decision intelligence, unified collaboration UX.
   - Mermaid component diagram and brief description of main integration points.
5. Create `knowledge-base/architecture/module_interfaces.md` with first-level contracts for m01. Minimum set of interfaces:
   - CRM/Opportunity → Project seed data.
   - HR/Azure AD/Workday → Users, org units, skills.
   - ERP/Maconomy → project codes/cost context.
   - Teams/SharePoint/Planner → collaboration spaces and boards.
   - CDE/ACC/ProjectWise → workspace provisioning.
   - Standards/Template Library → project template selection.
   - UPE Knowledge Graph → project context, similarity, reusable standards.
6. Create at least one ADR in `knowledge-base/architecture/decisions/ADR-0001-docs-as-data.md`, recording the decision to use Markdown+Mermaid+Git-style workflow as source of truth for product design. State consequences, alternatives rejected, review date.
7. Create an approved/current module slice in `knowledge-base/modules/m01_project_initialization/`:
   - `index.md`: purpose, owner, scope, dependencies, current status.
   - `requirements.md`: business, functional, non-functional requirements with IDs; use Section 1.1 from `docs/UPE_Functional_Blocks_v1.md`.
   - `data_model.md`: canonical entities (`Project`, `ProjectTemplate`, `ProjectType`, `Discipline`, `Role`, `User`, `ProjectMembership`, `CDEWorkspace`, `CollaborationSpace`, `ProvisioningJob`, `ProvisioningTask`, `Standard`, `ReferenceDataSet`) and Mermaid ERD.
   - `workflows.md`: state machine and flowchart for project initialization from request to active project.
   - `api_spec.md`: module inputs/outputs, events, error states.
   - `backlog.md`: MVP tasks, review tasks, demo tasks.
8. Create demo fork `knowledge-base/backlog/forks/project-intialization-module.md`. This should be a single convenient session file showing how a module owner works in a fork before merge. Structure:
   - Front matter: `fork_of: knowledge-base/master.md`, `target_module: m01_project_initialization`, `status: draft`, `merge_target: knowledge-base/modules/m01_project_initialization/`.
   - Fork hypothesis: what is being tested.
   - Proposed changes to master/module.
   - Requirements delta with IDs.
   - Data model delta.
   - Workflow proposal with Mermaid.
   - Interface impact table.
   - Open questions for review.
   - Merge checklist.
   - Review decision log placeholder.
9. Create `knowledge-base/sessions/2026-05-26_m01_project_initialization_llm_session.md` as a demo LLM session log:
   - Prompt/context.
   - Decisions proposed by LLM.
   - Human review notes.
   - Output artifacts changed/created.
   - Follow-up tasks.
10. Create `knowledge-base/prototypes/sprint-01_project_initialization/prototype_prompt.md`, which can be passed to v0.dev/Replit/Claude for quick UI/MVP generation. It must reference `master.md` and m01 artifacts and describe demo screens: Project Creation Wizard, Template Selection, Provisioning Status, Project Dashboard, Access/Team setup.
11. Create `knowledge-base/reports/stakeholder_brief_2026-05-26.md` as a derived snapshot for colleagues:
   - 1-page narrative: why this framework matters.
   - What is master vs fork.
   - Demo flow for review session.
   - Decisions requested from colleagues.
12. Update/create `knowledge-base/00_index.md` so there are no orphan files. Every created MD page must be listed with its purpose, owner/status and a link.
13. Manually check consistency of links and terminology: `Unified Project Execution`, `Project Initialization`, `CDE`, `knowledge graph`, `master`, `fork`, `merge`, `ADR`. Note separately that the filename `project-intialization-module.md` contains a typo only to match the task specification; canonical name is `project-initialization`.
14. Prepare a short demo script in `knowledge-base/reports/stakeholder_brief_2026-05-26.md` or a separate `knowledge-base/demo_script.md`:
   - 3 minutes: the problem with traditional specifications.
   - 5 minutes: master.md as a living product architecture.
   - 7 minutes: fork for m01 and the review/merge model.
   - 5 minutes: prototype prompt as a derived output.
   - 5 minutes: governance and adoption discussion.
15. After implementation, perform a read-only sanity check: find all `.md` files, verify that key files exist, links are relative, Mermaid blocks are present, front matter is present in knowledge-base files.

## Risks / Open Questions
- The task mentions `master.md` and `project-intialization-module.md`, but they do not currently exist in the repository; the plan assumes they will be created.
- It needs to be decided whether `knowledge-base/` is the final folder or a demo folder. For the session it is better to explicitly name it knowledge-base and leave the current `docs/`, `src/`, `prompts/` as source inputs.
- Spelling needs to be agreed: the user specified `project-intialization-module.md`; it is better to create exactly this file for demo compatibility, but use canonical `project-initialization` inside.
- The framework must not turn into heavy bureaucracy. It is important to maintain minimal viable governance: IDs, statuses, traceability, review gates — without excessive templates.
- Implementation must not modify source documents in `docs/`, `src/`, `prompts/`; they serve as sources/references.
