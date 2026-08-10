---
description: Scout → Deep Forensic Audit pipeline for especially complex codebases
argument-hint: "<audit target: directory or codebase description>"
---

# Deep Review (Forensic Audit) Cycle

You are orchestrating a **Scout → Context → Deep Forensic Audit** pipeline: an INDEPENDENT EXTERNAL FORENSIC AUDIT for especially complex cases. This is NOT a plan-to-implement cycle and NOT a work cycle. The audit is READ-ONLY: no code is changed, no worker is spawned, no fixes are executed.

The ONLY deliverable is the forensic audit report at `.pi/audit/<SESSION_SLUG>/report.md`: complete, self-sufficient, evidence-backed, giving the user everything needed to plan and execute fixes later — without re-running the analysis. The `deep-reviewer` role (its agent contract in `agent-roles/deep-reviewer.md`) IS the audit methodology — do NOT copy its checklist, completeness rules, finding format, or report schema into this prompt.

---
## PHASE 0 — SETUP

1. `bash("pwd")`.
2. Generate `SESSION_SLUG = YYYYMMDD-HHMMSS-<two-word-slug>`.
3. Before the first write, set `REPORT_PATH=.pi/audit/<SESSION_SLUG>/report.md` and `CONTEXT_PATH=.pi/audit/<SESSION_SLUG>/evidence/context.md`; inside a git repo verify each exact path with `git check-ignore -q "$REPORT_PATH"` and `git check-ignore -q "$CONTEXT_PATH"`. If either is not ignored, STOP and ask the user to add an appropriate `.gitignore` rule. Tracked files elsewhere under `.pi/` are allowed. Before spawning each scout in Phase 1, likewise determine and verify that scout's exact `.pi/audit/<SESSION_SLUG>/evidence/<topic>.md` target before it writes. Never modify `.gitignore` yourself.
4. Preserve the user's audit request verbatim as `AUDIT_TARGET`. It is immutable: no agent may silently replace the target with a different meta-task.

## PHASE 1 — PARALLEL RESEARCH (background scouts)

Decompose `AUDIT_TARGET` into **2–4 independent investigation questions** across the audit's forensic dimensions (adapt to the target): entry points & critical paths; dead / hidden / duplicate / misconnected code; configuration & decision systems; data layer & migrations; tests vs. production; dependencies & build provenance; security & robustness; docs vs. reality.

Before creating the audit directory or spawning any scout, assign every question a `<topic>` and exact evidence target `.pi/audit/<SESSION_SLUG>/evidence/<topic>.md`; verify every such target with `git check-ignore -q`, then run `bash("mkdir -p .pi/audit/<SESSION_SLUG>/evidence")`.

For each question, spawn a background `scout`; the evidence path is part of the scout's contract:

```text
Agent({
  subagent_type: "scout",
  prompt: "<specific research question with exact grep/find targets>\n\nSave your findings to: .pi/audit/<SESSION_SLUG>/evidence/<topic>.md",
  description: "<5-word label>",
  run_in_background: true
})
```

Rules:
- Questions must be independent — no scout depends on another's output.
- Scouts are read-only except for saving their own evidence file.
- Wait for ALL scouts: `get_subagent_result({ agent_id: "...", wait: true })`.

### Failure handling
- A scout errors / returns empty / produced no evidence artifact → retry ONCE with a fresh `scout` (same question, same evidence path). If both attempts fail, record the dimension:

```text
UNEXAMINED DIMENSIONS:
- <dimension>: scout failed on both attempts
```

Pass this list to the deep-reviewer (PHASE 3): it MUST reflect every such dimension in its report under §13.2 Scope and Evidence / §13.12 Open Questions and Evidence Gaps of its role contract — "nothing silently skipped" is part of the audit contract.
- Do not retry merely because findings are unfavorable. One retry attempt per primary failure.

## PHASE 2 — CONTEXT AGGREGATION

After all scouts complete:

1. Read all files from `.pi/audit/<SESSION_SLUG>/evidence/*.md`.
2. Synthesize them into ONE merged context file — do NOT concatenate raw outputs; preserve file:line evidence, external URLs/provenance, constraints, and unresolved gaps:

```text
.pi/audit/<SESSION_SLUG>/evidence/context.md
```

```markdown
# Context: <SESSION_SLUG>
Generated: <ISO datetime>
Task: <AUDIT_TARGET>

## Research Findings

### <Topic 1>
<content from scout 1>

### <Topic 2>
...
```

## PHASE 3 — DEEP FORENSIC AUDIT (foreground deep-reviewer)

Spawn a **foreground** `deep-reviewer` with the full context. Its agent contract IS the methodology — do NOT copy it here:

```text
Agent({
  subagent_type: "deep-reviewer",
  prompt: "ORIGINAL GOAL (audit scope):\n<AUDIT_TARGET>\n\nCONTEXT (research findings):\n<full content of .pi/audit/<SESSION_SLUG>/evidence/context.md>\n\nUNEXAMINED DIMENSIONS (if any — from scout failures):\n<list, or \"(none)\">\n\nExecution context: <current directory or target directory being audited>\n\nApply your complete deep technical reviewer contract without omission. The report is the ONLY deliverable. Every UNEXAMINED DIMENSION above MUST be reflected in your report under §13.2 Scope and Evidence / §13.12 Open Questions and Evidence Gaps — nothing silently skipped.\n\nThis is a READ-ONLY audit. Do NOT apply any fixes or modifications to the audited code.\n\nSave your audit report to: .pi/audit/<SESSION_SLUG>/report.md",
  description: "Deep forensic audit"
})
```

### Failure handling
- `deep-reviewer` errors / returns empty / produces no report artifact → retry ONCE with a fresh `deep-reviewer` and the SAME prompt. One retry attempt per primary failure.
- If both attempts fail → STOP: there is no audit to present. Ask the user to choose "direct" (the orchestrator writes the report itself from the gathered context and evidence), "retry", or "abort".

## PHASE 4 — FINAL REPORT / STOP

1. Display the full contents of `.pi/audit/<SESSION_SLUG>/report.md`.
2. State:

```text
═══════════════════════════════════════════════════════
🔍  DEEP AUDIT COMPLETE
═══════════════════════════════════════════════════════

The audit is READ-ONLY — no code was changed. The report is the basis for fixes.

📁 Artifact saved:
  - Audit: .pi/audit/<SESSION_SLUG>/report.md
  - Evidence/context: .pi/audit/<SESSION_SLUG>/evidence/

To act on it:
  1. Run /spec to freeze fix requirements, then /harness to execute them
  2. Or fix manually from the audit
```

3. Stop. Do NOT spawn any worker. Do NOT apply any changes.

---

AUDIT: $@
