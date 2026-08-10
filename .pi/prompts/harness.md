---
description: Autonomous bounded development harness — spec → plan → implement → validate → review → fix
argument-hint: "<path to .pi/spec/*-spec.md>"
---

# Autonomous Development Harness

The user invoked `/harness` with a **frozen specification**. This invocation IS the authorization for the entire bounded development cycle.

**No approval gates between phases. Do not stop for confirmation after plan, after implementation, or after review. Only BLOCKED stops the cycle.**

Engineering decisions inside the frozen spec → decide yourself. Product/scope/architecture decisions NOT covered by the spec → BLOCKED.

---

## AGENT FAILURE POLICY

For every critical foreground role, retry the exact same task ONCE with a fresh spawn of the same role:

| Role | Retry policy |
|------|--------------|
| `planner` | retry once with a fresh `planner` |
| `worker` | retry once with a fresh `worker` |
| `reviewer` | retry once with a fresh `reviewer` |
| `scout` | retry once with a fresh `scout` |

Retry triggers (infrastructure/model exhaustion ONLY):
- Agent call errors.
- Result is empty, whitespace-only, or `No output.`.
- Agent failed to produce its **mandatory deliverable**:
  - an artifact, when the role owns an artifact (`planner` → plan.md, `worker` → impl.md);
  - structured returned output, when the orchestrator owns persistence (`reviewer` returns output; `scout` returns findings — ephemeral planning context, no artifact).

**Never advance to the next phase without the mandatory deliverable.**
**`FIX`, `REPLAN`, `BLOCKED` are verdicts, not agent failures — do NOT retry on them.**
**Never retry because the primary returned an unfavorable but valid result.**

If both attempts fail: STOP, report to the user, do not proceed.

---

## PHASE 0 — PREFLIGHT & CHECKPOINT

`/harness` accepts ONLY a frozen spec artifact. If the user supplies an inline task instead of a spec path — STOP and instruct them to run `/spec` first. The frozen spec IS the authorization boundary.

All checks below are non-mutating. NO `mkdir`, NO checkpoint writes until every check has passed.

1. **Read the spec file** at the given path.
2. **Verify the spec is usable:**
   - file exists and contains all required sections (spec §1–§9);
   - `status: frozen` in the header — a `draft` spec must NOT be executed; ask the user to finalize it via /spec.
3. **Verify git repo** (if the task requires file edits): `bash("git rev-parse --is-inside-work-tree")` — no repo → BLOCKED.
4. **Verify no Git operation in progress:** run `bash("git status")` and reject if it reports a merge, rebase, cherry-pick, or revert in progress.
5. **Check ORIGINAL working tree state:** `bash("git status --porcelain=v1")` (stable machine format — empty output = clean), `bash("git branch --show-current")`, `bash("git log --oneline -3")`.
   - **Dirty repo → BLOCKED.** Pre-existing changes must NOT be mixed with harness work (`isolation: "worktree"` is per-spawn only and cannot carry state across rounds). Ask the user to commit/stash or start the harness from a dedicated clean worktree. Clean repo → the main tree is the execution context.
6. **Verify exact intended `.pi` artifacts are git-ignored:** after extracting `SESSION_SLUG` from the spec filename, verify each planned new target with `git check-ignore -q`: `.pi/checkpoints/<SESSION_SLUG>-checkpoint.md`, `.pi/plan/<SESSION_SLUG>-plan.md`, `.pi/implementation/<SESSION_SLUG>-impl.md`, `.pi/implementation/<SESSION_SLUG>-validation.md`, and `.pi/review/<SESSION_SLUG>-review.md`. If any target is not ignored — do NOT mutate `.gitignore`; BLOCKED with the failing path and an instruction to add an appropriate project `.gitignore` rule. Tracked files elsewhere under `.pi/` are allowed.
7. **Only then create artifact dirs:** `bash("mkdir -p .pi/spec .pi/plan .pi/implementation .pi/review .pi/checkpoints")`.
8. **Record baseline:** `BASELINE_SHA = git rev-parse HEAD` → save `.pi/checkpoints/<SESSION_SLUG>-checkpoint.md` (baseline SHA, branch, clean state). HEAD itself is the pre-development checkpoint; no artificial empty commit.

---

## PHASE 1 — CONTEXT & PLAN

1. If the codebase area is unfamiliar, spawn **background** `scout` agents (2–3, independent questions, parallel). Scouts return findings as their output — they create no artifacts in harness:
   ```text
   Agent({
     subagent_type: "scout",
     prompt: "<question>",
     description: "<label>",
     run_in_background: true
   })
   ```
   Collect with `get_subagent_result({ agent_id, wait: true })`. If a scout errored or returned empty findings — retry once with a fresh `scout`; if still empty, mark that investigation dimension as NOT EXAMINED and proceed (do not silently pretend it was covered).
2. Spawn a **foreground** `planner` with spec + scout context. The planner OWNS the plan artifact:
   ```
   Agent({
     subagent_type: "planner",
     prompt: "<spec content>\n\n<scout findings>\n\nProduce the implementation plan and save it to: .pi/plan/<SESSION_SLUG>-plan.md",
     description: "Plan implementation"
   })
   ```
3. After completion verify the plan artifact: exists → read → validate. The orchestrator never writes the plan itself.
4. **Plan validation:** every acceptance criterion from spec §6 must map to at least one plan task; every validation command from §7 must appear in the plan's validation section. If not — send the plan back to `planner` once with the gaps listed. Do not proceed with a plan that doesn't cover the acceptance criteria.

---

## PHASE 2 — IMPLEMENT (single writer)

1. Spawn a **foreground** `worker` — the ONLY agent allowed to modify source:
   ```
   Agent({
     subagent_type: "worker",
     prompt: "<spec content>\n\n<plan content>\n\nSave your implementation summary to: .pi/implementation/<SESSION_SLUG>-impl.md",
     description: "Implement: <slug>"
   })
   ```
2. Verify `.pi/implementation/<SESSION_SLUG>-impl.md` exists after completion (failure → retry once with a fresh `worker`, per AGENT FAILURE POLICY).

---

## PHASE 3 — VALIDATE

Run the validation commands from spec §7 yourself (targeted tests → lint/typecheck → build). Record results to `.pi/implementation/<SESSION_SLUG>-validation.md`.

- All green → proceed to Phase 4.
- Failures → do NOT notify the user. Record a **`VALIDATION_FAILURE`** input for the fix loop (Phase 5, input type A): failing commands + their output. This is mechanical validation state — it is NOT a reviewer verdict.

---

## PHASE 4 — INDEPENDENT REVIEW

Spawn a **foreground fresh-context** `reviewer` (it never sees the implementation conversation, only artifacts). **The reviewer NEVER writes artifacts — the orchestrator persists the reviewer's returned output verbatim.**

```
Agent({
  subagent_type: "reviewer",
  prompt: "SPEC:\n<spec content>\n\nPLAN:\n<plan content>\n\nIMPLEMENTATION SUMMARY:\n<impl artifact>\n\nVALIDATION EVIDENCE:\n<validation artifact>\n\nReview the implementation against the spec and plan. Return exactly one machine-readable verdict as the FIRST line:\n\nPASS\nFIX:<issues>\nREPLAN:<reason>\nBLOCKED:<reason>\n\nDo not prefix it with \"VERDICT:\" or any other text. Then detailed findings with file:line evidence.",
  description: "Review implementation"
})
```

Orchestrator saves the reviewer's full returned output to `.pi/review/<SESSION_SLUG>-review.md` verbatim (failure → retry once with a fresh `reviewer`, per AGENT FAILURE POLICY).

**Verdict grammar (machine-readable, first line):**
- `PASS` — implementation meets spec; validation evidence is sound.
- `FIX:<issues>` — concrete defects; each issue must name the file/behavior and the expected fix.
- `REPLAN:<reason>` — the plan itself was wrong (misunderstood the codebase, missed a constraint); fixes can't be scoped without a new plan.
- `BLOCKED:<reason>` — spec gap or external blocker; a human decision is required.

---

## PHASE 5 — BOUNDED AUTOFIX LOOP (max 3 rounds)

Initialize `ROUND = 0` after the initial implementation (the initial worker run is NOT counted). Before each corrective implementation cycle: `ROUND += 1`. Allowed corrective rounds: 1, 2, 3. Each reviewer is a NEW spawn (fresh context).

**Round semantics:** increment `ROUND` immediately BEFORE starting any corrective worker cycle. `REPLAN` does NOT reset `ROUND`. After 3 corrective cycles without `PASS` — STOP.

**Explicit transitions (state machine):**

```
A. VALIDATION_FAILURE (Phase 3 mechanical state):
   if ROUND >= 3 → STOP (do not spawn worker)
   ROUND += 1
   spawn worker [validation failure: failing commands + output]
   → Phase 3 validate → Phase 4 review

B. reviewer FIX:<issues>:
   if ROUND >= 3 → STOP (do not spawn worker)
   ROUND += 1
   spawn worker [reviewer findings verbatim + current diff context]
   → Phase 3 validate → Phase 4 review

C. reviewer REPLAN:<reason>:
   if ROUND >= 3 → STOP (do not spawn planner or worker)
   ROUND += 1
   spawn planner [reason + current repo state]  →  verify rewritten plan
   spawn worker [revised plan + continuation instructions]
   → Phase 3 validate → Phase 4 review

PASS → break to Phase 6.
BLOCKED:<reason> → STOP. Report to the user. Do not continue.
```

Every corrective worker (transitions A, B, C) MUST receive the continuation block:

```
This is a continuation of an existing harness run.
The repository already contains changes from prior rounds.
Preserve all valid existing work.
Apply the revised plan against the CURRENT repository state.
Do not revert prior changes unless the revised plan explicitly requires it.
```

- `PASS` → break to Phase 6.
- `BLOCKED:<reason>` → **STOP. Report to the user with the reviewer's reason. Do not continue.**

**Hard cap:** after 3 rounds without `PASS`, STOP. Do not spawn a 4th round even if the reviewer says "almost there". Report: rounds used, last verdict, remaining issues, artifacts.

The cap is enforced by YOU, the orchestrator — never delegate the round counter to a prompt phrase inside a subagent.

---

## PHASE 6 — FINALIZE

1. Run the FULL validation suite from spec §7 one final time.
   - **If final full validation FAILS:** do NOT commit. If `ROUND < 3` — feed it back into the correction loop as `VALIDATION_FAILURE` (transition A). If `ROUND == 3` — STOP with the validation failure and NO final commit. A reviewer `PASS` never overrides an actually failing validation.
2. Commit the work (only after final validation is green):
   - `git add` ONLY the explicit relevant source paths (never `git add -A` / `git add .` — `.pi/` artifacts must stay out of the commit) and `git commit` with a message referencing the slug.
   - **Never `git push`.** Push is a separate explicit user command.
3. Write the final report as the response, including:
   - artifacts: spec/plan/impl/validation/review paths,
   - final verdict + rounds used,
   - commit SHA (if committed),
   - validation evidence summary,
   - remaining risks / open questions.

---

## STOP CONDITIONS (report to user immediately)

- BLOCKED verdict (spec gap, external blocker).
- Round cap reached without PASS (3 corrective cycles).
- Final full validation fails at `ROUND == 3` (no commit).
- Destructive operation required (delete/reset/rollback/rm -rf/format/migration of real data) — ask first.
- Secrets/credentials, remote/production/cloud infrastructure, force-push/history rewrite — ask first.
- Spec change required — ask first (the spec is frozen).
- Any critical agent (planner/worker/reviewer/scout) fails twice to produce the mandatory deliverable.

---

SPEC: $@
