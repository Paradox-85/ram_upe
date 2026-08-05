---
description: Scout and synthesize an independent repository audit for human review
argument-hint: "<audit target>"
---

# Scout and Review Cycle

Orchestrate a **Scout → Context → Independent Audit → Human Decision** workflow. This is read-only analysis, not implementation planning. All prompts, artifacts, and user-facing output must be in English, even when the audit target is supplied in another language. Use only project-local GitHub Copilot agents. There are no fallback agents.

## Phase 0 — Setup

1. Determine repository root, branch, commit, and working-tree state.
2. Generate `SESSION_SLUG` as `YYYY-MM-DD-<short-lowercase-hyphenated-audit-target>`.
3. Use:
   - research: `.pi/research/<SESSION_SLUG>-audit-<topic>.md`;
   - context: `.pi/context/<SESSION_SLUG>-audit-context.md`;
   - audit: `.pi/review/<SESSION_SLUG>-audit.md`.
4. Do not modify application code, configuration, or data.

## Phase 1 — Parallel Investigation

Decompose the target into two to four independent questions, such as:
- production entry points and critical paths;
- weak, dead, hidden, duplicate, or disconnected code;
- configuration precedence, routing, decisions, and fallbacks;
- data integrity and migrations;
- tests versus production behavior;
- dependencies and build provenance;
- security, reliability, performance, or documentation drift.

Launch all independent `scout` agents in one message with `run_in_background: true`. Each scout must save a unique research artifact and cite exact files and lines. Do not duplicate scout work in the orchestrator.

If a critical scout fails, retry it once when the failure appears transient. Otherwise stop or explicitly record the missing evidence.

## Phase 2 — Context Aggregation

Merge all research into `.pi/context/<SESSION_SLUG>-audit-context.md` with:

# Audit Context: <SESSION_SLUG>

## Audit Goal and Scope
## Repository Baseline
## Research Findings
## Critical Paths
## Contradictions and Risks
## Evidence Gaps

Preserve contradictory evidence and uncertainty.

## Phase 3 — Audit Synthesis

Launch a foreground `reviewer` with the original target, complete context, repository baseline, and audit path. Require the reviewer to perform its repository-health review mode and independently verify material scout claims.

The report must include:
- verdict and scope limitations;
- evidence-backed strengths;
- prioritized findings with severity and confidence;
- exact file and line citations;
- runtime or validation evidence where available;
- concrete remediation directions without applying changes;
- open questions and evidence gaps.

If the reviewer fails or produces no artifact, stop and offer `retry`, `direct`, or `abort`.

## Phase 4 — Human Decision Gate

Display the complete audit and artifact paths, then ask the user to choose:
1. `accept` — acknowledge the audit;
2. `plan: <scope>` — create a remediation plan in a separate, approval-gated workflow;
3. `re-audit: <instructions>` — run additional investigation;
4. `abort` — stop.

Do not spawn a worker or apply fixes in this workflow.

AUDIT: $@
