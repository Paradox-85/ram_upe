---
description: Execute an approved task, review the result, and request a human decision
argument-hint: "<plan path or inline task>"
---

# Work and Review Cycle

Orchestrate a **Human Approval → Worker → Reviewer → Human Decision** workflow. All prompts, artifacts, and user-facing output must be in English, even when the task is supplied in another language. Use only project-local GitHub Copilot agents. There are no fallback agents.

## Phase 0 — Resolve the Task

1. If `$@` points to a `.pi/plan/*.md` file, read it as the approved execution plan.
2. Otherwise treat `$@` as an inline task.
3. Derive `SESSION_SLUG` from the plan filename or generate `YYYY-MM-DD-<short-lowercase-hyphenated-task>`.
4. Use:
   - implementation summary: `.pi/implementation/<SESSION_SLUG>-impl.md`;
   - review: `.pi/review/<SESSION_SLUG>-review.md`.
5. Record the current branch, commit, and `git status --short` before execution. Do not absorb unrelated pre-existing changes into the task.

## Phase 1 — Execution Approval Gate

Display the complete plan or inline task, the worker model from `.pi/agents/worker.md`, the intended execution context, and the expected files to change.

Ask the user to choose:
- `go` — authorize implementation;
- `abort` — cancel.

Stop until the user explicitly chooses `go`. This gate authorizes the worker's task-scoped file writes and validation commands, but not destructive operations or unrelated changes.

## Phase 2 — Worker Execution

Launch a foreground `worker` agent with:
- the full plan or task;
- repository state and relevant context;
- explicit scope boundaries;
- the required implementation-summary path;
- this mandatory instruction:

> For every targeted edit to an existing file, read it first and use hash-based `replace`. Use `write` only for new files or justified complete rewrites. Immediately re-read every written or replaced file and verify the change. If verification fails, stop. Do not modify unrelated files.

After completion, verify:
- `.pi/implementation/<SESSION_SLUG>-impl.md` exists;
- `git status --short` matches the reported changed files;
- the worker executed the validation it claims.

If the worker fails, returns no useful result, or leaves an uncertain partial state, stop. Show the actual repository state and offer:
1. `retry` — retry the worker once with clarified context;
2. `direct` — authorize the orchestrator to complete the same approved scope;
3. `abort` — stop without claiming success.

## Phase 3 — Independent Review

Launch a foreground `reviewer` with:
- original plan or task;
- implementation summary;
- actual diff and changed-file list;
- execution context;
- review output path `.pi/review/<SESSION_SLUG>-review.md`.

Require a read-only review against requirements, repository conventions, correctness, regressions, tests, documentation, and scope. The reviewer must cite exact paths and lines.

If review fails or no artifact is produced, stop and offer `retry`, `direct`, or `abort`.

## Phase 4 — Human Review Gate

Display the complete review, implementation artifact path, review path, changed files, and validation results. Ask the user to choose:

1. `accept` — accept the implementation;
2. `revise: <instructions>` — run another approval-gated worker iteration;
3. `replan` — return to `/scout_planner`;
4. `abort` — stop.

Do not commit or push unless the user explicitly requested commit and push as part of the approved task. Before committing, stage only task-owned files, show the staged diff summary, and avoid unrelated pre-existing changes.

TASK: $@
