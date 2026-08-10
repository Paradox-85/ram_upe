---
description: Synthesize and save a session handoff document into .pi/context/
argument-hint: "[session slug or scope description]"
---

# Session Handoff Documentation

You are orchestrating a **Gather → Synthesize → Save** pipeline that produces ONE handoff document (`.pi/context/<SESSION_SLUG>-handoff.md`) capturing what was done this session: technical and architectural decisions, rejected alternatives, and next steps — so a future agent or human can resume without rediscovery. The `context-builder` role owns the handoff structure and synthesis methodology; this workflow supplies only the session identity, the gathered sources, and the output path.

Informational only — no approval gate: corrections are applied on request. After presenting the document, stop.

---
## PHASE 0 — SETUP

1. `bash("pwd")`.
2. Determine `SESSION_SLUG`:
   - If the user supplies a session slug or an artifact path (e.g. `.pi/implementation/20260615-134502-auth-refactor-impl.md`) → extract the slug `20260615-134502-auth-refactor`.
   - Otherwise generate `YYYYMMDD-HHMMSS-<two-word-slug>` using the current datetime + a 2-word summary of the session scope.
3. Set `OUTPUT_PATH=.pi/context/<SESSION_SLUG>-handoff.md`.
4. Apply the global `.pi` artifact safety invariant before the first write (see AGENTS.md): inside a git repo, verify `git check-ignore -q "$OUTPUT_PATH"`. If this exact intended artifact is not ignored, STOP and ask the user to add an appropriate `.gitignore` rule. Tracked files elsewhere under `.pi/` are allowed. Never modify `.gitignore` yourself.
5. `bash("mkdir -p .pi/context")`.

## PHASE 1 — CONTEXT GATHERING (orchestrator, no subagent)

Collect the sources of truth for the session (read-only tools only). Do NOT synthesize yet — just gather raw material. No artifact is saved in this phase.

- **Recent artifacts:** newest files in `.pi/plan/`, `.pi/implementation/`, `.pi/review/`, `.pi/research/`, `.pi/context/` matching `SESSION_SLUG` — read them.
- **Recent audits:** if the session included an audit, read `.pi/audit/<SESSION_SLUG>/report.md` (and relevant `evidence/` files when they matter for decisions).
- **Repo state:** `bash("git status --short")`, `bash("git log --oneline -20")`, `bash("git diff --stat")` (if within a git repo).
- **Original goal/task:** from the context file's `Task:` header, the plan's goal section, or the `$@` argument.
- **Decisions found:** scan impl files for "Applied decisions" and "Key Decisions" sections.

Assemble a compact brief with all gathered inputs.

## PHASE 2 — HANDOFF SYNTHESIS (foreground context-builder)

Spawn a **foreground** `context-builder` with the gathered sources. The context-builder's role contract defines the handoff document structure (13-field schema) — do NOT restate it here:

```text
Agent({
  subagent_type: "context-builder",
  prompt: "SESSION_SLUG: <SESSION_SLUG>\nORIGINAL GOAL/TASK: <gathered goal>\n\nSOURCES OF TRUTH (gathered):\n<compact brief: plan/impl/review artifacts, git status, changed files, decisions found>\n\nWrite the session handoff document per your role contract. Save it to: .pi/context/<SESSION_SLUG>-handoff.md",
  description: "Write session handoff"
})
```

### Failure handling
- `context-builder` errors / returns empty / produces no handoff artifact → retry ONCE with a fresh `context-builder` and the SAME prompt. One retry attempt per primary failure.
- If both attempts fail → STOP: ask the user to choose "direct" (the orchestrator writes the handoff itself from the gathered material), "retry", or "abort".

## PHASE 3 — SAVE & REPORT / STOP

1. Display the full contents of `.pi/context/<SESSION_SLUG>-handoff.md`.
2. State:

```text
═══════════════════════════════════════════════════════
📄  HANDOFF DOCUMENT SAVED
═══════════════════════════════════════════════════════

📁 Artifact saved:
  - Handoff: .pi/context/<SESSION_SLUG>-handoff.md

If any section is wrong or missing, tell me and I will regenerate it.
```

3. Stop.

---

SESSION: $@
