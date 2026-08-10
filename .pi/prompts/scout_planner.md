---
description: Scout → Research → Context → Plan pipeline for planning tasks
argument-hint: "<goal description>"
---

# Scout & Planner Cycle

You are orchestrating a **Research → Context → Plan** pipeline.

The purpose is to investigate the user's task, consolidate the evidence into ONE context file, and produce an implementation plan.

This is READ-ONLY planning:

* Do NOT modify production code.
* Do NOT spawn a worker.
* Do NOT implement the plan.
* Do NOT reinterpret the user's request into a different task.
* Stop after presenting the plan.

Final persisted artifacts:

```text
.pi/context/<SESSION_SLUG>-context.md
.pi/plan/<SESSION_SLUG>-plan.md
```

Individual scout/researcher outputs are ephemeral — do NOT persist them unless the user explicitly asked for raw research artifacts.

---

## PHASE 0 — SETUP

1. Determine the working directory with `bash("pwd")`.
2. Generate:
   ```text
   SESSION_SLUG = YYYYMMDD-HHMMSS-<two-word-slug>
   ```
3. Apply the `.pi` artifact safety policy: if the working directory is inside a git repository, verify that the intended targets are ignored by git (the check does not apply otherwise):
   ```text
   .pi/context/<SESSION_SLUG>-context.md
   .pi/plan/<SESSION_SLUG>-plan.md
   ```
   If they are not ignored, STOP before the first write and ask the user to correct `.gitignore`. Never modify `.gitignore` automatically.
4. Create only:
   ```bash
   bash("mkdir -p .pi/context .pi/plan")
   ```
5. Preserve the user's complete request verbatim as `ORIGINAL_GOAL`. It is immutable throughout this workflow: research may challenge assumptions, but no agent may silently replace the task with a different meta-task. Example: `"research X"` must NOT become `"design a workflow that could research X later"`.

---

## PHASE 1 — PARALLEL RESEARCH

Decompose `ORIGINAL_GOAL` into **2–4 independent investigation questions**. Classify each question by its evidence source:

| Evidence source | Agent |
|-----------------|-------|
| repository / local code, schemas, config, tests | `scout` |
| external / current / web: Internet, GitHub, vendor docs, standards, current package behavior | `researcher` |

Use `researcher` whenever the user explicitly requests Internet/GitHub/vendor/current research. For mixed tasks, run both in parallel.

Spawn the agents in background and wait for ALL of them before proceeding:

```text
Agent({
  subagent_type: "scout",
  prompt: "ORIGINAL GOAL:\n<ORIGINAL_GOAL>\n\nINVESTIGATE (repository evidence):\n<specific question>\n\nReturn implementation-relevant evidence: files + line ranges, current behavior, reusable mechanisms, constraints, gaps. Do NOT implement anything.",
  description: "<short label>",
  run_in_background: true
})
```

```text
Agent({
  subagent_type: "researcher",
  prompt: "ORIGINAL GOAL:\n<ORIGINAL_GOAL>\n\nRESEARCH (external/current evidence):\n<specific question>\n\nPerform ACTUAL web research and report sources/provenance. Do not rely on model memory. Do NOT implement anything.",
  description: "<short label>",
  run_in_background: true
})
```

Give each agent one clear, scoped question — the role definition controls the methodology. Do not paste research methodology into the prompt.

Collect results with `get_subagent_result({ agent_id: "...", wait: true })`.

### Failure handling

* `scout` errors / returns empty / provides no usable evidence → retry ONCE with a fresh `scout` and the same question. If both attempts fail, record `NOT EXAMINED: <dimension>` in the context.
* For every mandatory `researcher` investigation, classify the completed result before aggregating it:
  1. A result is usable only when it is non-empty and, when live external research is mandatory, contains actual web/search evidence with source provenance.
  2. Treat as an **operational failure**: an `Agent` or `get_subagent_result` error; a malformed or invalid tool call (including `Failed to parse tool call arguments as JSON`); empty/whitespace output; `No output.`; or no actual web/search evidence where live research was mandatory.
  3. On the first operational failure, invoke a **fresh** `researcher` with the identical research question and prompt. Do not resume the failed agent.
  4. If that fresh retry also fails operationally, attempt ONE final fresh `researcher` with the identical research question and prompt.
  5. Only if every permitted attempt fails operationally, record `EXTERNAL RESEARCH NOT COMPLETED: <dimension>` and stop with `BLOCKED: mandatory external research was not completed`.
* Do not retry merely because a research finding is unfavorable or incomplete in substance. Never replace failed mandatory live research with model memory.
* `planner` fails at infrastructure/model level → retry ONCE with a fresh `planner` and the same goal and context. If both attempts fail, stop.

One fresh primary retry and one final fresh attempt are permitted per operational researcher failure; no retry is justified by unfavorable substantive findings.

---

## PHASE 2 — CONTEXT AGGREGATION

Synthesize all scout and researcher outputs into ONE consolidated context file:

```text
.pi/context/<SESSION_SLUG>-context.md
```

Do NOT create a per-scout file directory. Do NOT simply concatenate raw outputs — synthesize them. Preserve useful file:line evidence, external URLs/provenance, constraints, and unresolved gaps.

```markdown
# Context: <SESSION_SLUG>

Generated: <ISO datetime>
Task: <ORIGINAL_GOAL>

## Research Findings

### <topic>
...

## External Research
...

## Constraints
...

## Gaps / Unknowns
...
```

This ONE file is the input to the planner.

---

## PHASE 3 — PLANNING

Spawn a foreground `planner` passing the full context content and the ORIGINAL GOAL verbatim:

```text
Agent({
  subagent_type: "planner",
  prompt: "ORIGINAL GOAL:\n<ORIGINAL_GOAL>\n\nCONTEXT:\n<full content of .pi/context/<SESSION_SLUG>-context.md>\n\nProduce an evidence-backed implementation plan for the ORIGINAL GOAL. Do not replace it with a meta-task. Do NOT implement anything. Save the plan to .pi/plan/<SESSION_SLUG>-plan.md",
  description: "Plan implementation"
})
```

---

## PHASE 4 — PRESENT / STOP

Read `.pi/plan/<SESSION_SLUG>-plan.md` and perform a lightweight check: the plan must answer `ORIGINAL_GOAL`, use the context, and not redefine the task as future tooling. If it drifted, send it back to a fresh `planner` once with the correction. Otherwise present the plan.

Display the final plan, then state:

```text
═══════════════════════════════════════════════════════
📋  SCOUT PLANNING COMPLETE
═══════════════════════════════════════════════════════

No production code was changed.

📁 Artifacts:
  - Context: .pi/context/<SESSION_SLUG>-context.md
  - Plan:    .pi/plan/<SESSION_SLUG>-plan.md
```

Stop. Do NOT invoke `/harness`. Do NOT spawn a worker.

The plan is planning output only; it is not itself implementation authorization.

---

GOAL: $@
