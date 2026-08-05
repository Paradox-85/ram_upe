---
description: Gather, synthesize, and approve a durable session handoff document
argument-hint: "[session slug or scope description]"
---

# Session Handoff Cycle

Orchestrate a **Gather → Synthesize → Human Approval** workflow that creates one durable handoff document. All prompts, artifacts, and user-facing output must be in English, even when the scope is supplied in another language. Use only project-local GitHub Copilot agents. There are no fallback agents.

## Phase 0 — Setup

1. Determine repository root, branch, commit, and current date.
2. If `$@` contains an existing artifact path or slug, reuse its slug. Otherwise generate `YYYY-MM-DD-<short-lowercase-hyphenated-scope>`.
3. Target: `.pi/context/<SESSION_SLUG>-handoff.md`.
4. Do not modify application source files.

## Phase 1 — Gather Sources of Truth

Using read-only inspection, collect:
- matching artifacts from `.pi/plans/`, `.pi/implementation/`, `.pi/review/`, `.pi/research/`, and `.pi/context/`;
- `git status --short`, recent log entries, diff summary, and changed-file list;
- original goal and explicit success criteria;
- implemented changes and validation results;
- decisions, rejected alternatives, assumptions, limitations, and open questions.

Keep gathered facts separate from interpretation.

## Phase 2 — Synthesis

Launch a foreground `context-builder` with the gathered material. Require exactly this structure and save it to `.pi/context/<SESSION_SLUG>-handoff.md`:

# Handoff: <SESSION_SLUG>

## 1. Session Metadata
Slug, timestamps, repository version, branch, purpose, and recorded model/tool context.

## 2. Goal
Concrete intended outcome and success statement.

## 3. Summary
What was actually completed.

## 4. Files Touched
Created and modified paths with reasons.

## 5. Key Decisions
What was chosen, why, and by whom when known.

## 6. Rejected Alternatives
Options not chosen and why.

## 7. Dependencies
Upstream, downstream, deployment, and cross-session dependencies.

## 8. Open Questions
Unresolved decisions or required external input.

## 9. Known Limitations and Technical Debt
Discovered or introduced constraints and assumptions.

## 10. Failure Modes
Known ways the solution can fail and relevant safeguards.

## 11. Validation Evidence
Commands, results, runtime evidence, and unavailable checks.

## 12. Cross-References
Related plans, research, implementation summaries, reviews, and prior handoffs.

## 13. Next Steps
Ordered, actionable continuation steps.

## 14. Notes
Other durable context and revision information.

Every heading must appear; use `None identified` when empty. If synthesis fails or no artifact is created, stop and offer `retry`, `direct`, or `abort`.

## Phase 3 — Human Approval Gate

Display the complete handoff and ask the user to choose:
1. `approved` or `proceed` — accept it;
2. `revise: <instructions>` — regenerate specified sections;
3. paste replacement content — overwrite only after explicit confirmation;
4. `abort` — cancel.

Do not proceed beyond this gate without an explicit decision.

SESSION: $@
