# Handoff Prompt: Restructure M01 Branching

You are implementing a repository branching correction for the UPE (Unified Project Execution) knowledge base at Ramboll.

Repository: `https://github.com/Paradox-85/ram_upe`  
Working directory expected: repository root, currently `C:/Development/upe/UPE` in the planning environment.  
Current incorrect state: all artifacts are on `main`. `main` must contain only approved/reviewed artifacts. M01 work-in-progress must live on `feature/m01-project-initialization` and enter `main` only through Pull Request / architecture review.

As you execute, mark each completed step in your final response with `[DONE:n]` tags corresponding to the numbered steps below.

## Critical Constraints / Gotchas
- Do not delete or modify these protected artifacts except where explicitly instructed:
  - `knowledge-base/master.md` (only update M01 status/note on `main`)
  - `knowledge-base/00_index.md` (only remove moved entries, update stats, add Active Feature Branches on `main`)
  - `knowledge-base/00_principles.md`
  - `knowledge-base/00_glossary.md`
  - `knowledge-base/00_changelog.md` (only add restructure entry on `main`)
  - `knowledge-base/demo_script.md`
  - `knowledge-base/architecture/arch_overview.md`
  - `knowledge-base/architecture/module_interfaces.md`
  - `knowledge-base/architecture/decisions/ADR-0001-docs-as-data.md`
  - `knowledge-base/reports/stakeholder_brief_2026-05-26.md`
  - `knowledge-base/prototypes/sprint-01_project_initialization/prototype_prompt.md`
- The fork filename intentionally contains a typo: `project-intialization-module.md`. Preserve it exactly.
- Create `feature/m01-project-initialization` from current `main` before removing WIP files from `main`, so the branch retains the M01 artifacts.
- After `main` cleanup, the PR from feature to main should show M01 WIP artifacts as proposed additions/changes for review. This is expected.
- If direct pushes to `main` are blocked, stop and report that branch protection requires a separate cleanup PR or admin action.
- If GitHub CLI (`gh`) is unavailable or unauthenticated, create the PR manually in the GitHub web UI using the exact title/body below.

## Files to Move Off `main`
These must remain on `feature/m01-project-initialization` and must no longer exist on `main` after cleanup:

- `knowledge-base/modules/m01_project_initialization/index.md`
- `knowledge-base/modules/m01_project_initialization/requirements.md`
- `knowledge-base/modules/m01_project_initialization/data_model.md`
- `knowledge-base/modules/m01_project_initialization/workflows.md`
- `knowledge-base/modules/m01_project_initialization/api_spec.md`
- `knowledge-base/modules/m01_project_initialization/backlog.md`
- `knowledge-base/backlog/forks/project-intialization-module.md`
- `knowledge-base/sessions/2026-05-26_m01_project_initialization_llm_session.md`

## Current Relevant File Context

### `knowledge-base/master.md`
Currently has a Module Registry row like:

```markdown
| **M01** | Project Initialization & Provisioning | @module-owner-m01 | `in-review-demo` | Phase 1 |
```

On `main`, change this status to `draft` and add the requested note under the Module Registry section:

```markdown
**M01 is currently in active design on branch `feature/m01-project-initialization`.
Review via Pull Request before merge to main.**
```

### `knowledge-base/00_index.md`
Currently lists 19 files, including M01 module, fork, and session tables. On `main`, remove entries for the moved files. Expected statistics after cleanup:

```markdown
| Metric | Count |
|---|---|
| Total files | 11 |
| Architecture files | 3 |
| Module files (M01) | 0 |
| Fork files | 0 |
| Session logs | 0 |
| Prototype prompts | 1 |
| Reports | 1 |
| Demo scripts | 1 |
| Root files (index, principles, glossary, changelog, master) | 5 |
| Files with `approved` status | 6 |
| Files with `in-review-demo` status | 0 |
| Files with `accepted` status | 1 |
| Files with `draft` status | 4 |
```

Add at the bottom:

```markdown
## Active Feature Branches

| Branch | Module | Status | PR |
|--------|--------|--------|----|
| `feature/m01-project-initialization` | M01 Project Initialization | `in-review-demo` | [Open PR →] |
```

### `knowledge-base/00_changelog.md`
Add this entry at the top after the intro separator and before existing entries:

```markdown
---
date: 2026-05-26
type: restructure
author: "@chief-architect"
summary: "Moved M01 work-in-progress to feature branch. Main now contains only approved artifacts. Correct Git branching model adopted per DDDM principles."
files_affected:
  - knowledge-base/master.md
  - knowledge-base/00_index.md
  - knowledge-base/00_changelog.md
  - knowledge-base/modules/m01_project_initialization/ (moved to feature branch)
  - knowledge-base/backlog/forks/ (moved to feature branch)
  - knowledge-base/sessions/ (moved to feature branch)
---
```

### `knowledge-base/backlog/forks/project-intialization-module.md`
On the feature branch only, update YAML front matter to include:

```yaml
status: in-review
branch: feature/m01-project-initialization
merge_target: main
merge_via: Pull Request
```

Keep other useful front matter fields unless directly conflicting. Insert immediately after the front matter:

```markdown
## Branch Context

This file is the design brief for branch `feature/m01-project-initialization`.
All module artifacts in this branch are work-in-progress.

**Merge path:**
1. Complete merge checklist below
2. Architecture review session (Pull Request review)
3. Approved changes merge to `main` via PR
4. `master.md` updated on `main` to reflect M01 as `approved`
```

## Implementation Plan

1. Verify repository state on `main`:
   - Run `git status --short --branch`.
   - Ensure the branch is `main` and working tree is clean.
   - If dirty, stop and resolve before continuing.

2. Create the feature branch from current `main`:
   ```bash
   git switch -c feature/m01-project-initialization
   ```

3. On `feature/m01-project-initialization`, edit `knowledge-base/backlog/forks/project-intialization-module.md`:
   - `status: draft` → `status: in-review`
   - add `branch: feature/m01-project-initialization`
   - set `merge_target: main` (replace old relative target if present)
   - add `merge_via: Pull Request`
   - add the `## Branch Context` section immediately after YAML front matter.

4. Commit the feature branch change:
   ```bash
   git add knowledge-base/backlog/forks/project-intialization-module.md
   git commit -m "Update M01 fork branch context"
   ```

5. Push the feature branch:
   ```bash
   git push -u origin feature/m01-project-initialization
   ```

6. Switch back to `main`:
   ```bash
   git switch main
   ```

7. Remove WIP artifacts from `main` using `git rm`:
   ```bash
   git rm \
     knowledge-base/modules/m01_project_initialization/index.md \
     knowledge-base/modules/m01_project_initialization/requirements.md \
     knowledge-base/modules/m01_project_initialization/data_model.md \
     knowledge-base/modules/m01_project_initialization/workflows.md \
     knowledge-base/modules/m01_project_initialization/api_spec.md \
     knowledge-base/modules/m01_project_initialization/backlog.md \
     knowledge-base/backlog/forks/project-intialization-module.md \
     knowledge-base/sessions/2026-05-26_m01_project_initialization_llm_session.md
   ```

8. Update `knowledge-base/master.md` on `main`:
   - Change M01 row status to `draft`.
   - Add the requested branch/PR review note under the Module Registry section, immediately after the table is a good location.

9. Update `knowledge-base/00_index.md` on `main`:
   - Remove moved file entries from index tables.
   - Remove or replace now-empty `Module M01`, `Backlog & Forks`, and `Sessions` tables so no moved file path is listed as present on `main`.
   - Update statistics to the expected 11-file totals.
   - Add `## Active Feature Branches` section at the bottom with the exact requested row.

10. Update `knowledge-base/00_changelog.md` on `main`:
    - Add the restructure metadata entry exactly as specified before the existing `## [1.0.1] — 2026-05-26` section.

11. Verify `main` cleanup:
    - `git ls-files knowledge-base/modules/m01_project_initialization knowledge-base/backlog/forks knowledge-base/sessions` should return no tracked moved files on `main` after staging/removal.
    - Confirm protected files still exist.
    - Review diff with `git diff --cached` and/or `git diff`.

12. Commit `main` cleanup:
    ```bash
    git add knowledge-base/master.md knowledge-base/00_index.md knowledge-base/00_changelog.md
    git commit -m "Move M01 work in progress to feature branch"
    ```
    Note: `git rm` deletions should already be staged; if not, add them before commit.

13. Push `main`:
    ```bash
    git push origin main
    ```
    If denied due to branch protection, stop and report the issue.

14. Create the Pull Request from feature to main.
    Preferred CLI approach:
    - Save the PR body below to a temporary file such as `/tmp/m01-pr-body.md`.
    - Run:
      ```bash
      gh pr create \
        --base main \
        --head feature/m01-project-initialization \
        --title "[M01] Project Initialization & Provisioning — Architecture Review" \
        --body-file /tmp/m01-pr-body.md
      ```
    - If `gh` is missing or not authenticated, use GitHub web UI to open the PR from `feature/m01-project-initialization` to `main` with the same title/body.

15. PR body to use exactly:

```markdown
## Purpose
This PR contains the complete design for Module M01 — Project Initialization & Provisioning.
It is submitted for Architecture Review per the DDDM framework.

## What's included
- `modules/m01_project_initialization/` — full module slice (requirements, data model,
  workflows, api spec, backlog)
- `backlog/forks/project-intialization-module.md` — design brief, hypotheses,
  requirements delta, interface impact
- `sessions/2026-05-26_m01_...` — LLM session log

## Review Checklist
- [ ] Requirements reviewed and IDs stable (REQ-M01-001...)
- [ ] Data model reviewed by Chief Architect (13 entities confirmed)
- [ ] Interface contracts validated in `architecture/module_interfaces.md`
- [ ] Workflows cover failure/retry paths
- [ ] Mermaid diagrams render correctly in GitHub
- [ ] No orphan files — 00_index.md updated
- [ ] 00_changelog.md updated
- [ ] master.md Module Registry updated (M01 status → `approved`)

## Architecture Decisions Required
1. Parallel vs sequential provisioning (ERP + M365 + CDE)?
2. Knowledge Graph interface (IF-M01-KG-001) in MVP scope or defer to Sprint 2?
3. ProjectWise support in MVP or Sprint 2?

## References
- Design brief: `knowledge-base/backlog/forks/project-intialization-module.md`
- LLM session: `knowledge-base/sessions/2026-05-26_m01_project_initialization_llm_session.md`
- Framework: `knowledge-base/00_principles.md`
```

16. Final verification and response:
    - Run `git status --short --branch`.
    - Confirm feature branch and main were pushed.
    - Confirm PR URL if created.
    - In the final response, list each completed step with `[DONE:n]` tags and include any blockers or deviations.
