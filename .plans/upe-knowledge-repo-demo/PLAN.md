# UPE Knowledge Repository Demo

План реализации репозитория знаний UPE и демонстрационного примера для проверки LLM-Native Product Design Framework на модуле Project Initialization / Provisioning.

## Context
- В текущем проекте есть исходные материалы, но пока нет целевого knowledge-base репозитория, `master.md` и fork-файла `project-intialization-module.md` / `project-initialization-module.md`.
- Основной framework описан в `prompts/LLM-Native Product Design Framework.md`: data-first, docs-as-data, дизайн через LLM-диалог, master как single source of truth, модульные forks, review/merge, Mermaid-диаграммы, ADR, session logs.
- UPE уже описан как комплексная модульная платформа в `docs/UPE_Executive_Summary_v1.md` и `docs/UPE_Functional_Blocks_v1.md` с 14 functional domains и 175+ capabilities.
- Приоритетный demo-модуль подтверждается материалами: `Project Initialization & Provisioning` — must-have foundation, Phase 1 MVP, “start projects correctly, every time”. Детали есть в `docs/UPE_Functional_Blocks_v1.md`, Section 1.1.
- Дополнительный контекст: `docs/brainstorming.md` задаёт модульную архитектуру и suggested Microsoft/Azure stack; `src/loop/loop.md` содержит workstreams WS 3.1–3.5, включая Unified Project Data Model, AI-accelerated knowledge gathering, Unified Project Initialization and Provisioning, Project data extraction, Open interoperability layer.
- Framework полезен, но его нужно дополнить для enterprise product design: добавить machine-readable metadata, stable IDs, explicit merge gates, decision log, traceability matrix, quality checks, artifact taxonomy, demo сценарий и разделение master/fork/prototype snapshot.

## Plan:
1. Создать целевую структуру knowledge-base внутри текущего проекта, например `knowledge-base/`, не заменяя текущие исходные материалы. Структура должна быть понятной для демонстрации коллегам:
   - `knowledge-base/master.md` — главный вход и интеграционная картина UPE.
   - `knowledge-base/00_index.md` — индекс всех knowledge artifacts.
   - `knowledge-base/00_principles.md` — улучшенный framework/rules of work.
   - `knowledge-base/00_glossary.md` — канонические термины UPE.
   - `knowledge-base/00_changelog.md` — глобальный журнал изменений.
   - `knowledge-base/architecture/` — overview, interfaces, decisions.
   - `knowledge-base/modules/m01_project_initialization/` — approved/current module slice.
   - `knowledge-base/backlog/forks/project-intialization-module.md` — демонстрационный fork с сохранением пользовательского написания `intialization`; внутри указать canonical spelling `project-initialization`.
   - `knowledge-base/sessions/` — примеры LLM session logs.
   - `knowledge-base/reports/` — производные snapshots/stakeholder brief.
   - `knowledge-base/prototypes/` — prompt/spec для генерации demo-прототипа.
2. Зафиксировать улучшенную версию framework в `knowledge-base/00_principles.md`. Добавить к исходному DDDM следующие обязательные элементы:
   - YAML front matter для каждого файла.
   - Stable IDs для требований, сущностей, workflow steps, interfaces, ADR (`REQ-M01-001`, `ENT-Project`, `WF-M01-Initialize-010`, `IF-M01-CRM-001`, `ADR-0001`).
   - Lifecycle statuses: `idea`, `draft`, `in-review`, `approved`, `superseded`, `deprecated`.
   - Merge gates: completeness, traceability, interface impact, data model impact, architecture owner approval, stakeholder demo readiness.
   - Definition of Ready / Definition of Done для fork → review → master.
   - Правило “master contains approved knowledge; forks contain working hypotheses”.
   - Правило “reports are generated snapshots and must not become source of truth”.
3. Сформировать `knowledge-base/master.md` как демонстрационный master-файл для архитектуры UPE. Он должен быть self-contained и включать:
   - Vision: UPE = Unified Project Execution / enterprise digital backbone.
   - Scope и non-goals: не заменяет CDE/authoring tools, а координирует проектный execution layer.
   - 14 functional domains из `docs/UPE_Executive_Summary_v1.md` в компактной таблице.
   - Layered architecture Mermaid diagram: Collaboration UX, Process Orchestration, Intelligence/Data/Knowledge, Integration/API Hub, CDE/Authoring Tools, Enterprise Systems, Governance cross-cutting.
   - Module registry с минимум m01–m14, где m01 имеет status `approved-demo` или `in-review-demo`.
   - Phase 1 focus: Project Initialization, core data model, user/access, progress tracking, Teams/SharePoint integration.
   - Architecture decisions summary и ссылки на ADR.
   - Traceability to source docs (`docs/...`, `src/loop/loop.md`).
4. Создать `knowledge-base/architecture/arch_overview.md` на основе `master.md`, но более технически сфокусированный:
   - UPE не CDE и не DMS; CDE остаётся project system of record, UPE — coordination/intelligence layer.
   - Buy commodity layers, build differentiating layers: AI-ready engineering decomposition, knowledge graph, decision intelligence, unified collaboration UX.
   - Mermaid component diagram и краткое описание основных integration points.
5. Создать `knowledge-base/architecture/module_interfaces.md` с контрактами первого уровня для m01. Минимальный набор интерфейсов:
   - CRM/Opportunity → Project seed data.
   - HR/Azure AD/Workday → Users, org units, skills.
   - ERP/Maconomy → project codes/cost context.
   - Teams/SharePoint/Planner → collaboration spaces and boards.
   - CDE/ACC/ProjectWise → workspace provisioning.
   - Standards/Template Library → project template selection.
   - UPE Knowledge Graph → project context, similarity, reusable standards.
6. Создать минимум один ADR в `knowledge-base/architecture/decisions/ADR-0001-docs-as-data.md`, фиксирующий решение использовать Markdown+Mermaid+Git-style workflow как source of truth для product design. Указать consequences, alternatives rejected, review date.
7. Создать approved/current module slice в `knowledge-base/modules/m01_project_initialization/`:
   - `index.md`: purpose, owner, scope, dependencies, current status.
   - `requirements.md`: business, functional, non-functional requirements с IDs; использовать Section 1.1 из `docs/UPE_Functional_Blocks_v1.md`.
   - `data_model.md`: canonical entities (`Project`, `ProjectTemplate`, `ProjectType`, `Discipline`, `Role`, `User`, `ProjectMembership`, `CDEWorkspace`, `CollaborationSpace`, `ProvisioningJob`, `ProvisioningTask`, `Standard`, `ReferenceDataSet`) и Mermaid ERD.
   - `workflows.md`: state machine и flowchart для project initialization from request to active project.
   - `api_spec.md`: входы/выходы модуля, events, error states.
   - `backlog.md`: MVP tasks, review tasks, demo tasks.
8. Создать demo fork `knowledge-base/backlog/forks/project-intialization-module.md`. Это должен быть один удобный для сессии файл, показывающий, как модульный owner работает в fork до merge. Структура:
   - Front matter: `fork_of: knowledge-base/master.md`, `target_module: m01_project_initialization`, `status: draft`, `merge_target: knowledge-base/modules/m01_project_initialization/`.
   - Fork hypothesis: what is being tested.
   - Proposed changes to master/module.
   - Requirements delta с IDs.
   - Data model delta.
   - Workflow proposal with Mermaid.
   - Interface impact table.
   - Open questions for review.
   - Merge checklist.
   - Review decision log placeholder.
9. Создать `knowledge-base/sessions/2026-05-26_m01_project_initialization_llm_session.md` как демонстрационный лог LLM-сессии:
   - Prompt/context.
   - Decisions proposed by LLM.
   - Human review notes.
   - Output artifacts changed/created.
   - Follow-up tasks.
10. Создать `knowledge-base/prototypes/sprint-01_project_initialization/prototype_prompt.md`, который можно передать v0.dev/Replit/Claude для быстрой генерации UI/MVP. Он должен ссылаться на `master.md` и m01 artifacts и описывать demo screens: Project Creation Wizard, Template Selection, Provisioning Status, Project Dashboard, Access/Team setup.
11. Создать `knowledge-base/reports/stakeholder_brief_2026-05-26.md` как производный snapshot для коллег:
   - 1-page narrative: why this framework matters.
   - What is master vs fork.
   - Demo flow for review session.
   - Decisions requested from colleagues.
12. Обновить/создать `knowledge-base/00_index.md` так, чтобы не было orphan files. Каждая созданная MD-страница должна быть перечислена с назначением, owner/status и ссылкой.
13. Проверить консистентность ссылок и терминологии вручную: `Unified Project Execution`, `Project Initialization`, `CDE`, `knowledge graph`, `master`, `fork`, `merge`, `ADR`. Отдельно отметить, что имя файла `project-intialization-module.md` содержит typo только для соответствия постановке задачи; canonical name — `project-initialization`.
14. Подготовить короткий demo script в `knowledge-base/reports/stakeholder_brief_2026-05-26.md` или отдельном `knowledge-base/demo_script.md`:
   - 3 минуты: проблема традиционных ТЗ.
   - 5 минут: master.md как живой product architecture.
   - 7 минут: fork для m01 и review/merge модель.
   - 5 минут: prototype prompt как производный output.
   - 5 минут: обсуждение governance и adoption.
15. После реализации выполнить read-only sanity check: найти все `.md`, убедиться, что ключевые файлы существуют, ссылки относительные, Mermaid blocks присутствуют, front matter присутствует у knowledge-base файлов.

## Risks / Open Questions
- В постановке упомянуты `master.md` и `project-intialization-module.md`, но в репозитории их сейчас нет; план предполагает их создание.
- Нужно решить, является ли `knowledge-base/` финальной папкой или демо-папкой. Для сессии лучше явно назвать её knowledge-base и оставить текущие `docs/`, `src/`, `prompts/` как source inputs.
- Нужно согласовать spelling: пользователь указал `project-intialization-module.md`; лучше создать именно этот файл для demo compatibility, но внутри использовать canonical `project-initialization`.
- Framework не должен превращаться в тяжёлую бюрократию. Важно сохранить minimal viable governance: IDs, statuses, traceability, review gates — без избыточных шаблонов.
- Реализация не должна менять исходные документы в `docs/`, `src/`, `prompts/`; они служат источниками/референсами.
