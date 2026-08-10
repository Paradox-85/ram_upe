## Purpose
This PR contains the complete design for Module M01 — Project Initialization & Provisioning.
It is submitted for Architecture Review per the DDDM framework.

## What's included
- `modules/m01_project_initialization/` — full module slice (requirements, data model,
  workflows, api spec, backlog)
- `backlog/forks/project-intialization-module.md` — design brief, hypotheses,
  requirements delta, interface impact
- `sessions/2026-05-26_m01_...` — LLM session log

## Review Checklist
- [ ] Requirements reviewed and IDs stable (REQ-M01-001...)
- [ ] Data model reviewed by Chief Architect (13 entities confirmed)
- [ ] Interface contracts validated in `architecture/module_interfaces.md`
- [ ] Workflows cover failure/retry paths
- [ ] Mermaid diagrams render correctly in GitHub
- [ ] No orphan files — 00_index.md updated
- [ ] 00_changelog.md updated
- [ ] master.md Module Registry updated (M01 status → `approved`)

## Architecture Decisions Required
1. Parallel vs sequential provisioning (ERP + M365 + CDE)?
2. Knowledge Graph interface (IF-M01-KG-001) in MVP scope or defer to Sprint 2?
3. ProjectWise support in MVP or Sprint 2?

## References
- Design brief: `knowledge-base/backlog/forks/project-intialization-module.md`
- LLM session: `knowledge-base/sessions/2026-05-26_m01_project_initialization_llm_session.md`
- Framework: `knowledge-base/00_principles.md`
