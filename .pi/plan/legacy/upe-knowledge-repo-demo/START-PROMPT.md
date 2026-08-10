# Handoff Prompt: Implement UPE Knowledge Repository Demo

You are implementing a demo knowledge-base repository for UPE (Unified Project Execution) inside the current project at `C:/Development/upe/UPE`.

## Critical Constraints
- You are now in implementation mode unless otherwise specified by the harness.
- Do not delete or rewrite existing source materials in `docs/`, `src/`, or `prompts/`.
- Build the demo as new Markdown content under `knowledge-base/`.
- Use Markdown as data/source of truth, Mermaid for diagrams, YAML front matter for metadata.
- Mark each completed plan step in your response with `[DONE:n]` where `n` is the step number.
- The user explicitly mentioned `project-intialization-module.md` with a typo. Create that exact file under `knowledge-base/backlog/forks/` for compatibility, but document canonical spelling as `project-initialization` inside the file.

## Existing Codebase / Source Context
Read these files first:
1. `prompts/LLM-Native Product Design Framework.md`
   - Defines the proposed LLM-native product design framework: Docs-as-Data, Design-by-Dialogue, master branch/source of truth, module forks, review/merge, Mermaid diagrams, ADRs, session logs.
2. `docs/UPE_Executive_Summary_v1.md`
   - Defines UPE vision and 14 functional domains.
   - Identifies high-priority foundation: Project Initialization & Provisioning, Basic Data Model, User Access Management, Progress Tracking, Onboarding/Offboarding.
   - Includes phases, success metrics, risks and open questions.
3. `docs/UPE_Functional_Blocks_v1.md`
   - Detailed capability pool. Use Section 1.1 “Project Initialization & Provisioning” as primary source for module m01.
   - Contains 14 sections and cross-cutting concerns.
4. `docs/brainstorming.md`
   - Defines UPE as a collection of modules; suggested stack: Teams/SharePoint, Power BI, Power Automate, Planner, Azure; integrations: CRM, Maconomy, CDE, design tools, BIM/GIS.
5. `src/loop/loop.md`
   - Contains workstreams: WS 3.1 Unified Project Data Model, WS 3.2 AI accelerated Knowledge gathering, WS 3.3 Unified Project Initialization and Provisioning, WS 3.4 Project data extraction, WS 3.5 Open interoperability layer.
6. Optional context: `src/chat/UPE Platform Architects Chat.md` and `src/moms/*` for discussion points around prototypes, project initialization, data backbone, CDE/DMS boundaries.

## Framework Enhancements to Apply
The framework is valuable but incomplete for enterprise product design. Add these enhancements throughout the knowledge-base:
- Stable IDs for requirements, entities, workflows, interfaces, ADRs:
  - Requirements: `REQ-M01-001`
  - Entities: `ENT-Project`
  - Workflow steps: `WF-M01-010`
  - Interfaces: `IF-M01-CRM-001`
  - Decisions: `ADR-0001`
- Status lifecycle: `idea`, `draft`, `in-review`, `approved`, `superseded`, `deprecated`.
- Merge gates: completeness, traceability, interface impact, data model impact, architect approval, stakeholder demo readiness.
- Master vs fork rule: master contains approved/current knowledge; forks contain working hypotheses and deltas.
- Reports are generated snapshots; reports must not become source of truth.
- No orphan files: every file should be linked from `knowledge-base/00_index.md`.

## Plan to Execute

1. Create target `knowledge-base/` structure with these paths:
   - `knowledge-base/master.md`
   - `knowledge-base/00_index.md`
   - `knowledge-base/00_principles.md`
   - `knowledge-base/00_glossary.md`
   - `knowledge-base/00_changelog.md`
   - `knowledge-base/architecture/arch_overview.md`
   - `knowledge-base/architecture/module_interfaces.md`
   - `knowledge-base/architecture/decisions/ADR-0001-docs-as-data.md`
   - `knowledge-base/modules/m01_project_initialization/index.md`
   - `knowledge-base/modules/m01_project_initialization/requirements.md`
   - `knowledge-base/modules/m01_project_initialization/data_model.md`
   - `knowledge-base/modules/m01_project_initialization/workflows.md`
   - `knowledge-base/modules/m01_project_initialization/api_spec.md`
   - `knowledge-base/modules/m01_project_initialization/backlog.md`
   - `knowledge-base/backlog/forks/project-intialization-module.md`
   - `knowledge-base/sessions/2026-05-26_m01_project_initialization_llm_session.md`
   - `knowledge-base/prototypes/sprint-01_project_initialization/prototype_prompt.md`
   - `knowledge-base/reports/stakeholder_brief_2026-05-26.md`
   - optionally `knowledge-base/demo_script.md` if the stakeholder brief becomes too long.

2. Implement `knowledge-base/00_principles.md` as the improved framework/rules of work. Include:
   - Philosophy: Docs-as-Data, Design-by-Dialogue, Data First.
   - Required front matter template.
   - Artifact types and folder rules.
   - Stable ID scheme.
   - Fork/review/merge lifecycle.
   - Definition of Ready and Definition of Done.
   - Review gates.
   - Mermaid-only diagram rule.
   - Reports-as-derived-output rule.

3. Implement `knowledge-base/master.md` as the main demo master file. It must be self-contained and include:
   - YAML front matter.
   - Vision: UPE = Unified Project Execution; enterprise digital backbone.
   - Scope and non-goals: UPE does not replace CDE/DMS/authoring tools; it coordinates project execution and intelligence above them.
   - Compact table of 14 functional domains from `docs/UPE_Executive_Summary_v1.md`.
   - Mermaid architecture diagram with layers:
     - Collaboration UX / Portal / dashboards
     - Process automation & orchestration
     - AI, data quality, knowledge graph
     - Integration/API hub
     - CDE and authoring tools
     - Enterprise systems (CRM/ERP/HR/Finance)
     - Cross-cutting governance/security
   - Module registry for m01–m14, with m01 Project Initialization status as `in-review-demo` or `approved-demo`.
   - Phase 1 focus.
   - Current decisions and open questions.
   - Links to key source docs.

4. Implement `knowledge-base/architecture/arch_overview.md`:
   - Explain CDE is necessary but not the enterprise brain.
   - Explain UPE as coordination/intelligence layer.
   - Include hybrid build-vs-buy principle: buy commodity layers, build differentiating layers.
   - Include Mermaid component or flow diagram.

5. Implement `knowledge-base/architecture/module_interfaces.md` with first-level interface contracts for m01:
   - `IF-M01-CRM-001` CRM/Opportunity to Project seed data.
   - `IF-M01-HR-001` HR/Azure AD/Workday to users/org/skills.
   - `IF-M01-ERP-001` ERP/Maconomy to project codes/cost context.
   - `IF-M01-M365-001` Teams/SharePoint/Planner provisioning.
   - `IF-M01-CDE-001` ACC/ProjectWise workspace provisioning.
   - `IF-M01-TEMPLATE-001` Standards/Template Library template selection.
   - `IF-M01-KG-001` UPE Knowledge Graph context/reuse.
   For each contract include purpose, producer, consumer, key payload fields, trigger, output, failure modes.

6. Implement `knowledge-base/architecture/decisions/ADR-0001-docs-as-data.md`:
   - Decision: Use Markdown + Mermaid + Git-style workflow as source of truth for product design.
   - Status: accepted for demo.
   - Context, decision, consequences, alternatives rejected, review date.

7. Implement module m01 files under `knowledge-base/modules/m01_project_initialization/`:
   - `index.md`: purpose, scope, dependencies, owner placeholder, status, links to other module files.
   - `requirements.md`: derive from `docs/UPE_Functional_Blocks_v1.md` Section 1.1. Include business, functional, non-functional requirements with IDs. Cover project creation interface, template deployment, tool/service configuration, data model instantiation.
   - `data_model.md`: define entities and attributes. Include Mermaid ERD with at least `Project`, `ProjectTemplate`, `ProjectType`, `Discipline`, `Role`, `User`, `ProjectMembership`, `CDEWorkspace`, `CollaborationSpace`, `ProvisioningJob`, `ProvisioningTask`, `Standard`, `ReferenceDataSet`.
   - `workflows.md`: include state machine and flowchart from request to active project. Include failure/retry path.
   - `api_spec.md`: describe inputs/outputs, events, error states, external dependencies.
   - `backlog.md`: MVP tasks, review tasks, demo tasks.

8. Implement fork demo file `knowledge-base/backlog/forks/project-intialization-module.md`:
   - YAML front matter with `fork_of: ../../master.md`, `target_module: m01_project_initialization`, `status: draft`, `merge_target: ../../modules/m01_project_initialization/`.
   - State clearly: filename intentionally preserves typo from initial task; canonical spelling is `project-initialization`.
   - Include fork hypothesis, proposed master/module changes, requirements delta, data model delta, workflow proposal Mermaid, interface impact table, open questions, merge checklist, review decision log placeholder.
   - This file should be suitable to show colleagues as “how a module owner works in a fork before review/merge”.

9. Implement demo LLM session log `knowledge-base/sessions/2026-05-26_m01_project_initialization_llm_session.md`:
   - Prompt/context summary.
   - LLM-proposed decisions.
   - Human review notes placeholders.
   - Output artifacts changed/created.
   - Follow-up tasks.

10. Implement prototype prompt `knowledge-base/prototypes/sprint-01_project_initialization/prototype_prompt.md`:
   - It should be usable as a prompt for v0.dev/Replit/Claude.
   - Describe screens: Project Creation Wizard, Template Selection, Provisioning Status, Project Dashboard, Access/Team setup.
   - Include data objects and UX assumptions.
   - Emphasize it is generated from master/module knowledge, not manually maintained source of truth.

11. Implement stakeholder brief `knowledge-base/reports/stakeholder_brief_2026-05-26.md`:
   - 1-page style narrative.
   - Explain why the framework matters vs traditional specs.
   - Explain master vs fork.
   - Include demo flow for the session.
   - Include decisions requested from colleagues.
   - Mark it as a derived snapshot, not source of truth.

12. Implement `knowledge-base/00_index.md` linking every created file. Include columns: path, artifact type, status, owner placeholder, purpose.

13. Implement `knowledge-base/00_glossary.md` and `knowledge-base/00_changelog.md`:
   - Glossary should define UPE, CDE, DMS, master, fork, merge, ADR, module, interface contract, knowledge graph, project initialization.
   - Changelog should list initial demo repository creation with date 2026-05-26.

14. Optional but recommended: create `knowledge-base/demo_script.md` if the stakeholder brief is not enough. Include timing:
   - 3 min: problem with traditional specs.
   - 5 min: master.md as living product architecture.
   - 7 min: m01 fork and review/merge.
   - 5 min: prototype prompt as generated output.
   - 5 min: governance/adoption discussion.

15. Perform sanity checks:
   - Use file search to confirm all expected Markdown files exist.
   - Read key files to ensure front matter exists.
   - Search for `mermaid` blocks in master/module workflow/data model files.
   - Ensure all files under `knowledge-base/` are listed in `00_index.md`.
   - Ensure relative links are coherent.

## Expected Final Response
After implementing, respond concisely in Russian with:
- Summary of created repository/demo.
- Key files created.
- Any assumptions or deviations.
- `[DONE:n]` tags for completed steps.
