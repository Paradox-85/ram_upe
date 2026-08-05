---
description: Scout, synthesize, and obtain approval for an implementation plan
argument-hint: "<goal description>"
---

# Scout and Plan Cycle

Orchestrate a **Scout → Context → Plan → Human Approval** workflow for the goal below. All prompts, artifacts, and user-facing output must be in English, even when the goal is supplied in another language. Use only project-local agents, all of which run through GitHub Copilot. There are no fallback agents.

## Phase 0 — Setup

1. Determine the repository root and current branch.
2. Generate `SESSION_SLUG` as `YYYY-MM-DD-<short-lowercase-hyphenated-goal>`. Add a distinguishing topic suffix when parallel work could collide.
3. Use these artifact paths:
   - research: `.pi/research/<SESSION_SLUG>-<topic>.md`;
   - merged context: `.pi/context/<SESSION_SLUG>-context.md`;
   - plan: `.pi/plans/<SESSION_SLUG>-plan.md`.
4. Do not modify application source code in this workflow.

## Phase 1 — Parallel Scouting

Decompose the goal into two to four independent codebase questions. Launch all independent `scout` agents in one message with `run_in_background: true`.

Each scout prompt must include:
- the exact question and why it matters;
- likely paths, symbols, and search terms;
- read-only constraints for source files;
- its unique `.pi/research/` output path;
- a requirement for exact file and line citations.

Continue with unrelated orchestration work while scouts run. When notified, collect every result. Do not duplicate their searches yourself.

If a scout fails or returns no useful artifact, report that gap. Retry that scout once only when the failure appears transient; otherwise continue only if the missing angle is non-critical.

## Phase 2 — Context Aggregation

Read all scout artifacts and write a merged context document containing:

# Context: <SESSION_SLUG>

## Goal
## Repository State
## Research Findings
## Relevant Files and Symbols
## Architecture and Data Flow
## Constraints and Decisions
## Risks and Open Questions
## Validation Paths

Preserve citations and contradictions. Do not silently resolve ambiguous product or architecture decisions.

## Phase 3 — Planning

Launch a foreground `planner` agent with the complete merged context and original goal. Require it to save the plan to `.pi/plans/<SESSION_SLUG>-plan.md`.

The plan must contain concrete tasks, exact files, dependencies, acceptance criteria, validation commands, risks, and unresolved decisions. If the planner fails or produces no artifact, stop and offer `retry`, `direct`, or `abort`; do not invent that the planning phase succeeded.

## Phase 4 — Human Approval Gate

Display the complete plan and artifact paths, then stop and ask the user to choose:

1. `approved` or `proceed` — lock the plan as written;
2. `revise: <instructions>` — revise the plan without executing it;
3. `abort` — stop.

Do not spawn a worker and do not modify source code before explicit approval.

After approval, confirm the final plan path and recommend running `/work_and_review <plan-path>`.

GOAL: $@
