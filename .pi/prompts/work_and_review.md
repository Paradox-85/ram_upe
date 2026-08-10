---
description: Worker → Reviewer → human decision pipeline for an approved plan or inline task
argument-hint: "[plan path or inline task]"
---

# Work & Review Cycle

You are orchestrating a **Worker → Reviewer → Human Decision** pipeline. This is NOT the autonomous harness: write access stays behind an explicit human gate before every worker, and after every review the human chooses whether to accept, revise, replan, or abort. Never skip a gate.

The input is EITHER a path to an approved plan file (e.g. `.pi/plan/20260615-134502-auth-refactor-plan.md`) OR an inline task description.

The `worker` and `reviewer` role contracts (their agent files) own their methodology — do NOT paste generic methodology or checklists into this prompt or into their prompts. This prompt is orchestration only.

---
## PHASE 0 — SETUP

1. Resolve the task source:
   - A `.pi/plan/*.md` path → read that file; its content is the immutable `ORIGINAL_PLAN`.
   - An inline description → use it directly as the immutable `ORIGINAL_TASK`.
2. Determine `SESSION_SLUG`:
   - From an existing plan file → extract the slug from its filename.
   - Otherwise → generate `YYYYMMDD-HHMMSS-<two-word-slug>`.
3. Set the deterministic artifact paths for the base round and every revision round:
   - Round 1 (base): impl `.pi/implementation/<SLUG>-impl.md`, review `.pi/review/<SLUG>-review.md`.
   - Revision rN (N ≥ 2): impl `.pi/implementation/<SLUG>-r<N>-impl.md`, review `.pi/review/<SLUG>-r<N>-review.md`.
4. **Artifact safety before the first write.** If inside a git repository, verify the exact base paths with `git check-ignore -q` for the base impl and base review targets. If either is not ignored — STOP before any write and ask the user to add the appropriate `.gitignore` rule. Never modify `.gitignore` yourself. Tracked files elsewhere under `.pi/` are allowed. Before each revision worker (Phase 5), likewise verify that revision's exact impl and review paths.
5. Only then create dirs: `bash("mkdir -p .pi/implementation .pi/review")`.

`ORIGINAL_PLAN` / `ORIGINAL_TASK` is immutable throughout the cycle: no agent may silently replace it with a different meta-task, and the worker prompt always carries it verbatim.

---
## GROUPED ROLE FAILURE POLICY (operational errors only)

For each foreground role below, apply ONE fresh retry of the same role on an **operational failure only** — defined strictly as: the role call itself errored, produced empty/whitespace output or `No output.`, or failed to produce its **mandatory deliverable** (worker → impl artifact; reviewer → structured returned output, which the orchestrator persists). On such a failure, retry the SAME prompt once with a fresh spawn of the same role (`worker` / `reviewer`). Do NOT retry because the primary returned an unfavorable but valid verdict. `accept/revise/replan/abort` are human verdicts, not operational failures.

If the primary and its retry BOTH fail operationally, do not advance: STOP, report the actual repo/artifact state, and ask the user to `retry` or `abort`. The orchestrator never edits production code directly.

---
## PHASE 1 — ⏸️ EXECUTION APPROVAL GATE (before every worker)

Before spawning ANY worker (initial or revision), present the full task and require an explicit `GO`:

```
═══════════════════════════════════════════════════════
⏸️  CONFIRM TO PROCEED — TYPE "go"
═══════════════════════════════════════════════════════

Plan / Task:
<full ORIGINAL_PLAN or ORIGINAL_TASK content>

Worker role: worker (contract in agents/worker.md)
Execution context: current directory unless the runtime reports isolation

Type "go" to start execution, or "abort" to cancel.
```

Wait for the explicit `GO` (or `abort`) before proceeding. No worker runs without it.

---
## PHASE 2 — WORKER EXECUTION (foreground)

After `GO`, spawn a **foreground** `worker`:

```
Agent({
  subagent_type: "worker",
  prompt: "<full ORIGINAL_PLAN or ORIGINAL_TASK verbatim>\n\nSave your implementation summary to: <this round's impl path>",
  description: "Implement: <2-word summary>"
})
```

Rules:
- Worker executes in the current agent/runtime context unless the runtime explicitly provides isolation; if isolated, capture and report that context.
- This is a **blocking foreground call** — wait for completion.
- The worker OWNS its impl artifact at the deterministic round path. Its agent file contract is authoritative for methodology; this prompt states only ownership.
- State check before review: run `bash("git status --short")` (read-only) and confirm the round's impl artifact exists. If it is missing, the worker did not complete — apply the GROUPED ROLE FAILURE POLICY instead of proceeding to review.

`ORIGINAL_PLAN` / `ORIGINAL_TASK` is never modified by the worker.

---
## PHASE 3 — REVIEW (foreground)

Spawn a **foreground** `reviewer`:

```
Agent({
  subagent_type: "reviewer",
  prompt: "ORIGINAL PLAN/TASK:\n<ORIGINAL_PLAN or ORIGINAL_TASK verbatim>\n\nIMPLEMENTATION SUMMARY:\n<content of the round's impl artifact>\n\nExecution context: <current directory or isolated branch/worktree if provided>\n\nReview the implementation against the original plan/task using your normal reviewer contract. Return a complete, self-contained, actionable report for the human gate and any later user-authorized revision. Clearly distinguish Correct, Blockers, Findings, Risks, and Verification; state explicitly if no material defects exist. For each material problem provide severity/importance, observed problem, exact evidence, why it is incorrect or risky, required outcome, and verification criterion. Return the review only; do not modify files.",
  description: "Review implementation"
})
```

The reviewer NEVER writes review files — **the orchestrator persists the reviewer's complete returned output VERBATIM** to the round's review path (`.pi/review/<...>-review.md`). This self-contained report is the correction input for any later user-authorized revision. A failure to return valid output is an operational failure → one fresh `reviewer` retry per GROUPED ROLE FAILURE POLICY.

---
## PHASE 4 — ⏸️ REVIEW GATE — HUMAN DECISION

Display the full persisted review and ask:

```
═══════════════════════════════════════════════════════
⏸️  REVIEW COMPLETE — YOUR DECISION REQUIRED
═══════════════════════════════════════════════════════

<display full round review>

Choose one:
  1. "accept"  — accept the implementation
  2. "revise: <instructions>" — send the worker back with specific corrections
  3. "replan"  — return to the planning phase with revised requirements
  4. "abort"   — stop without accepting further changes
```

---
## PHASE 5 — HANDLE DECISION

- **`accept`**: confirm acceptance and report: final execution context (directory or isolated branch/worktree), the current implementation artifact path and its content, the current review artifact path and its content, and `git status --short` output (only if in a git repository). No commit/merge/push.
- **`revise: <instructions>`**: determine the next deterministic revision round `r<N>` and its impl/review paths (verify they are git-ignored if in a repo), then loop back to **Phase 1**, presenting to the worker: the immutable `ORIGINAL_PLAN`/`ORIGINAL_TASK` verbatim, the current implementation summary content, the latest review content, and the USER REVISION verbatim, with an instruction to continue/preserve valid work and make only the minimal authorized change. The revision instructions do NOT replace the original contract — the original remains authoritative. The revision requires its own explicit `GO` before the worker.
- **`replan`**: stop and direct the user to run `/scout_planner <revised goal>` themselves. Never auto-invoke it.
- **`abort`**: confirm cancellation; if an isolated branch/worktree was used, note the user may need manually to clean it up.

No automatic git action: never commit, never push, never reset. Git is used only for read-only state/ignore checks.

STOP. Do NOT invoke `/harness`.

TASK: $@
