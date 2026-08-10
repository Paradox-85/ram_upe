---
description: Interactive specification session — turn requirements into a frozen contract
argument-hint: "<feature or goal description>"
---

# Specification Session

You are running an **interactive specification session**. The user invoked `/spec` with a goal. Your job is to turn it into a **frozen contract** that the autonomous harness (`/harness`) can execute without further human decisions.

**You are the orchestrator — you talk to the user directly. Do not spawn subagents.**

---
## PHASE 0 — SETUP

1. `bash("pwd")`.
2. Generate `SESSION_SLUG` = `YYYYMMDD-HHMMSS-<two-word-slug>`.
3. Set `OUTPUT_PATH=.pi/spec/<SESSION_SLUG>-spec.md`.
4. Verify this exact intended artifact is git-ignored BEFORE the first write (if inside a git repo): `bash("git check-ignore -q \"$OUTPUT_PATH\"")` (exit 0 = ignored). If it is not ignored — STOP and ask the user to add an appropriate `.gitignore` rule (do NOT mutate `.gitignore` yourself). Tracked files elsewhere under `.pi/` are allowed.
5. Create the artifact directory: `bash("mkdir -p .pi/spec")`.
6. Restate the goal in 1–2 sentences and confirm it with the user before asking questions.

---

## PHASE 1 — ELICITATION

Ask the user the questions below, **grouped and in Russian**. Do not dump all of them at once — 3–5 questions per round, wait for answers. Skip questions the user has already answered in the initial description.

1. **Goal** — what outcome must be achieved, in measurable terms?
2. **Scope** — what is in-scope; what is explicitly out-of-scope?
3. **Behavior & constraints** — functional requirements, non-functional requirements (perf, security, compatibility).
4. **UX / API surface** — user-visible behavior, CLI/API signatures, error messages.
5. **Edge cases** — what must not break; known tricky inputs.
6. **Acceptance criteria** — a checklist of verifiable outcomes (each must be testable by a reviewer without the user).
7. **Validation requirements** — which tests/lint/typecheck/build commands the harness must run.
8. **Risks & dependencies** — external systems, data migrations, breaking changes.
9. **Human gates** — which decisions (if any) the user wants to be asked about even mid-cycle (default: none beyond spec changes).

If the user says "you decide" for any point, record the decision you make **explicitly in the spec** as a frozen decision.

---

## PHASE 2 — FREEZE THE CONTRACT

Write the contract to `.pi/spec/<SESSION_SLUG>-spec.md` with **exactly** this schema — every heading must appear; use `_(none identified)_` where empty:

```markdown
# Specification: <name>

- slug: <SESSION_SLUG>
- date: <ISO datetime>
- status: draft

## 1. Goal
## 2. Scope
### In-scope
### Out-of-scope
## 3. Behavior & Constraints
## 4. UX / API Surface
## 5. Edge Cases
## 6. Acceptance Criteria
## 7. Validation Requirements
## 8. Risks & Dependencies
## 9. Frozen Decisions
```

**Frozen Decisions** is the most important section: every decision made here requires **user approval to change**. If the harness hits a situation not covered by the spec, it must treat it as BLOCKED (or as an engineering decision inside the spec's intent — your call, recorded here).

---

## PHASE 3 — CONFIRM & FREEZE

1. Show the user the saved spec (or a summary + path).
2. The spec is a **draft** until the user explicitly says "final", "approved", or "freeze".
3. On explicit confirmation — rewrite the spec header to `status: frozen` and confirm:
   - "✅ Spec frozen: `.pi/spec/<SESSION_SLUG>-spec.md`. Run `/harness .pi/spec/<SESSION_SLUG>-spec.md` to execute."
4. If the user wants changes — update the spec file (still `draft`), then re-confirm.

`/harness` refuses to execute a spec whose header is not `status: frozen`.

---

GOAL: $@
