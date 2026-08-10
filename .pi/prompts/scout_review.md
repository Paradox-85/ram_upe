---
description: Focused independent audit — quick/medium research audit of a codebase area
argument-hint: "<audit target: directory or codebase description>"
---

# Scout & Review (Independent Audit)

You are orchestrating a **Scout → Reviewer → Report** pipeline: an INDEPENDENT RESEARCH AUDIT (quick/medium depth), not a plan-to-implement cycle and not a work cycle.

The ONLY deliverable is the audit report at `.pi/audit/<SESSION_SLUG>/report.md`. Scout findings are ephemeral — passed to the reviewer, never persisted. No code is changed, no worker is spawned, no plan is produced. No approval gate: the report is read-only output; after presenting it, stop.

---
## PHASE 0 — SETUP

1. `bash("pwd")`.
2. Generate `SESSION_SLUG = YYYYMMDD-HHMMSS-<two-word-slug>`.
3. Before the first write, set `OUTPUT_PATH=.pi/audit/<SESSION_SLUG>/report.md`; inside a git repo verify this exact target with `git check-ignore -q "$OUTPUT_PATH"`. If it is not ignored, STOP and ask the user to add an appropriate `.gitignore` rule. Tracked files elsewhere under `.pi/` are allowed. Never modify `.gitignore` yourself.
4. `bash("mkdir -p .pi/audit/<SESSION_SLUG>")`.
5. Preserve the user's audit request verbatim as `AUDIT_TARGET`. It is immutable: agents may challenge assumptions, but no agent may silently replace the target with a different meta-task.

## PHASE 1 — PARALLEL RESEARCH (background scouts)

Decompose `AUDIT_TARGET` into **2–4 independent investigation questions**: weak spots, gaps, inconsistencies, undocumented changes, runtime failure risks, architectural drift, deviation from conventions.

For each question, spawn a background `scout` that returns its findings as its final response:

```text
Agent({
  subagent_type: "scout",
  prompt: "AUDIT TARGET:\n<AUDIT_TARGET>\n\nINVESTIGATE (repository evidence):\n<specific question>\n\nReturn evidence-backed findings: files + line ranges, current behavior, inconsistencies, risks. Do NOT implement anything.",
  description: "<short label>",
  run_in_background: true
})
```

Rules:
- Questions must be independent — no scout depends on another's output.
- Wait for ALL scouts: `get_subagent_result({ agent_id: "...", wait: true })`.

### Failure handling
- A scout errors / returns empty / provides no usable evidence → retry ONCE with a fresh `scout` and the same question. If both attempts fail, record `NOT EXAMINED: <dimension>` and pass it to the reviewer (PHASE 2). Never silently continue as if the dimension were covered.
- Do not retry merely because findings are unfavorable. One retry attempt per primary failure.

## PHASE 2 — SYNTHESIS (foreground reviewer)

Spawn a **foreground** `reviewer` with the audit target and all scout findings inline. The reviewer NEVER writes files — it returns the report as its final response:

```text
Agent({
  subagent_type: "reviewer",
  prompt: "AUDIT TARGET:\n<AUDIT_TARGET>\n\nEVIDENCE:\n<all scout findings, inline>\n\nTask-specific scope: independent EXTERNAL audit of the current overall state of the target (review type #4). READ-ONLY — do NOT apply fixes, do NOT write plans, do NOT write any files.\n\nNOT EXAMINED dimensions (from scout failures):\n<list, or \"(none)\">\n\nThe report MUST end with this coverage section:\n\n## Audit Coverage\n\nExamined:\n- ...\n\nNot examined:\n- ... (include every NOT EXAMINED dimension reported by the orchestrator)\n\nEvidence limitations:\n- ...\n\nReturn the complete audit report as your final response.",
  description: "Audit codebase"
})
```

Save the reviewer's complete returned output **verbatim** to `.pi/audit/<SESSION_SLUG>/report.md`. If the reviewer fails (empty output), retry the SAME prompt once with a fresh `reviewer`. Proceed only with a valid non-empty report.

## PHASE 3 — REPORT / STOP

1. Display the full contents of `.pi/audit/<SESSION_SLUG>/report.md`.
2. State:

```text
═══════════════════════════════════════════════════════
🔍  AUDIT COMPLETE
═══════════════════════════════════════════════════════

The audit is READ-ONLY — no code was changed.

📁 Deliverable:
  - Report: .pi/audit/<SESSION_SLUG>/report.md

To act on findings: run /spec to freeze fix requirements, then /harness.
```

3. Stop. Do NOT spawn any worker. Do NOT propose an implementation plan unless the user asks.

---

AUDIT: $@
