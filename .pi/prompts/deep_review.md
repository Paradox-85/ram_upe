---
description: Run a maximum-depth forensic audit of an especially complex target
argument-hint: "<audit target>"
---

# Deep Forensic Review Cycle

Orchestrate a **Parallel Scouting → Context → Deep Forensic Audit → Human Decision** workflow. The only deliverable is a complete audit report; no fixes are applied. All prompts, artifacts, and user-facing output must be in English, even when the target is supplied in another language. Use only project-local GitHub Copilot agents. There are no fallback agents.

## Phase 0 — Setup

1. Record repository root, branch, commit, working-tree state, date, and available environment.
2. Generate `SESSION_SLUG` as `YYYY-MM-DD-<short-lowercase-hyphenated-audit-target>`.
3. Use:
   - research: `.pi/research/<SESSION_SLUG>-deep-audit-<topic>.md`;
   - context: `.pi/context/<SESSION_SLUG>-deep-audit-context.md`;
   - final report: `.pi/review/<SESSION_SLUG>-deep-audit.md`.
4. Do not modify audited code, configuration, data, or infrastructure.

## Phase 1 — Parallel Forensic Scouting

Decompose the audit into two to four independent high-value investigations. Cover the most relevant of:
- real production entry points, critical use cases, and call/data paths;
- dead, hidden, duplicate, legacy, shadow, disconnected, or misleading code;
- configuration precedence, registries, routing decisions, overrides, and fallbacks;
- schema, migrations, transactions, indexes, and data integrity;
- tests versus production orchestration and mock-to-runtime differences;
- security boundaries, reliability, performance, observability, and operations;
- dependencies, CI/CD, build reproducibility, artifacts, and supply-chain provenance;
- documentation, architecture claims, and version-history drift.

Launch all independent `scout` agents in one message with `run_in_background: true`. Each scout must save a unique artifact, cite exact paths and lines, distinguish fact from inference, and search for evidence that falsifies its hypotheses.

Do not duplicate scout work. If a critical investigation fails, retry once only when transient failure is plausible; otherwise stop or mark the evidence gap explicitly.

## Phase 2 — Context Aggregation

Merge all research into `.pi/context/<SESSION_SLUG>-deep-audit-context.md`. Include:

# Deep Audit Context: <SESSION_SLUG>

## Original Goal and Scope
## Repository and Environment Baseline
## Intended System
## Actual Entry Points and Architecture
## Critical Use-Case Traces
## Research Findings by Topic
## Contradictory Evidence
## Commands and Runtime Evidence
## Evidence Gaps and Exclusions

Do not silently reconcile contradictions or omit uncertainty.

## Phase 3 — Deep Forensic Audit

Launch a foreground `deep-reviewer` with:
- original audit goal and explicit priorities;
- complete aggregated context;
- exact repository and environment baseline;
- final report path `.pi/review/<SESSION_SLUG>-deep-audit.md`.

Require the agent to apply every section of its system definition, including:
- independent evidence verification;
- reconstruction of intended and actual behavior;
- system, dependency, data-flow, configuration, and trust-boundary mapping;
- safe reproduction and end-to-end tracing where possible;
- every mandatory review dimension;
- cross-layer verification;
- adversarial falsification questions;
- complete finding classification and evidence;
- use-case traceability and code relevance inventory;
- root-cause synthesis, remediation roadmap, strengths, and evidence gaps;
- final reviewer declaration.

Report-completeness requirements:
- The report is self-contained and is the only deliverable.
- Every material claim has inline evidence: file and line, symbol, call chain, configuration key, command, test, trace, or artifact.
- Every material finding explains expected behavior, actual behavior, root cause, impact, why it may appear correct, correction direction, and objective verification.
- Every unexamined dimension, component, or use case is named with a reason.
- Static inference is clearly separated from reproduced behavior.
- No code changes, fixes, or worker execution are allowed.
- Depth and completeness take precedence over brevity.

If the deep reviewer fails or no report exists, stop. Show the actual artifact state and offer `retry`, `direct`, or `abort`.

## Phase 4 — Human Decision Gate

Display the complete report and artifact paths, then ask the user to choose:
1. `accept` — acknowledge the audit;
2. `plan: <scope>` — derive a separate remediation plan without executing it;
3. `re-audit: <instructions>` — run additional scouts and repeat the audit;
4. `abort` — stop.

Do not spawn a worker or apply any remediation in this workflow.

AUDIT: $@
