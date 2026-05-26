# Restructure M01 Branching

Plan to correct the UPE repository branching model so `main` contains only approved artifacts, M01 work-in-progress lives on `feature/m01-project-initialization`, and a PR is opened for architecture review.

## Context
- Current branch is `main` tracking `origin/main`.
- `knowledge-base/` currently contains 19 tracked Markdown artifacts.
- Work-in-progress artifacts currently tracked on `main` and needing removal from `main` are:
  - `knowledge-base/modules/m01_project_initialization/index.md`
  - `knowledge-base/modules/m01_project_initialization/requirements.md`
  - `knowledge-base/modules/m01_project_initialization/data_model.md`
  - `knowledge-base/modules/m01_project_initialization/workflows.md`
  - `knowledge-base/modules/m01_project_initialization/api_spec.md`
  - `knowledge-base/modules/m01_project_initialization/backlog.md`
  - `knowledge-base/backlog/forks/project-intialization-module.md` (intentional filename typo)
  - `knowledge-base/sessions/2026-05-26_m01_project_initialization_llm_session.md`
- Approved/root artifacts that must remain on `main` include `master.md`, index/principles/glossary/changelog, architecture docs, report, demo script, and prototype prompt.
- `knowledge-base/master.md` currently lists M01 status as `in-review-demo` in the Module Registry.
- `knowledge-base/00_index.md` currently includes tables for M01 module files, the fork, and session log; statistics currently show total files 19, module files 6, fork files 1, session logs 1, in-review-demo 6.
- After removal from `main`, expected `00_index.md` statistics are: total files 11; architecture files 3; module files (M01) 0; fork files 0; session logs 0; prototype prompts 1; reports 1; demo scripts 1; root files 5; approved 6; in-review-demo 0; accepted 1; draft 4.
- The feature branch should be created from current `main` before deletion so it preserves the M01 artifacts, then update the fork file there.

## Plan:
1. Verify clean working tree on `main` with `git status --short --branch`. If dirty, stop and resolve before proceeding.
2. Create the feature branch from the current `main`: `git switch -c feature/m01-project-initialization`.
3. On `feature/m01-project-initialization`, update `knowledge-base/backlog/forks/project-intialization-module.md` front matter:
   - change `status: draft` to `status: in-review`
   - replace the existing relative-path `merge_target` value with `merge_target: main`
   - add `branch: feature/m01-project-initialization`
   - add `merge_via: Pull Request`
   Keep existing relevant metadata such as `id`, `type`, `owner`, `version`, `last_updated`, `fork_of`, `target_module`, and `tags` unless there is a direct conflict.
4. In the same fork file, insert immediately after the YAML front matter a new `## Branch Context` section with the exact requested text explaining that this is the design brief for the feature branch, artifacts are WIP, and merge path is checklist → architecture PR review → merge to `main` → update `master.md` to M01 `approved`.
5. Commit the feature branch change with a message such as `Update M01 fork branch context`.
6. Push the feature branch to origin: `git push -u origin feature/m01-project-initialization`.
7. Switch back to `main`: `git switch main`.
8. Remove the eight WIP artifacts from `main` using `git rm` on the six files under `knowledge-base/modules/m01_project_initialization/`, the fork file, and the session log. The now-empty directories may disappear naturally; no placeholder files are required unless project policy requires them.
9. Update `knowledge-base/master.md` on `main`: change the M01 Module Registry row status from `` `in-review-demo` `` to `` `draft` `` and add the requested note under the Module Registry section: `**M01 is currently in active design on branch \`feature/m01-project-initialization\`. Review via Pull Request before merge to main.**`
10. Update `knowledge-base/00_index.md` on `main`: remove entries for the moved module files, fork file, and session log. Prefer removing the now-empty `Module M01`, `Backlog & Forks`, and `Sessions` tables or replacing them with explicit “no approved artifacts on main” notes, but ensure no moved file path remains listed as present on `main`.
11. In `knowledge-base/00_index.md`, update the Statistics table to reflect `main` after removal: Total files 11; Architecture files 3; Module files (M01) 0; Fork files 0; Session logs 0; Prototype prompts 1; Reports 1; Demo scripts 1; Root files 5; Files with `approved` status 6; Files with `in-review-demo` status 0; Files with `accepted` status 1; Files with `draft` status 4.
12. Add this section at the bottom of `knowledge-base/00_index.md` exactly as requested:
    ```markdown
    ## Active Feature Branches

    | Branch | Module | Status | PR |
    |--------|--------|--------|----|
    | `feature/m01-project-initialization` | M01 Project Initialization | `in-review-demo` | [Open PR →] |
    ```
13. Update `knowledge-base/00_changelog.md` on `main` by adding the requested restructure entry at the top, immediately after the introductory `---` separator and before `## [1.0.1] — 2026-05-26`. Preserve existing changelog history below it.
14. Verify on `main` that the moved paths no longer exist (`git ls-files knowledge-base/modules/m01_project_initialization knowledge-base/backlog/forks knowledge-base/sessions`) and that protected files still exist unchanged except the three requested main updates.
15. Commit the `main` changes with a message such as `Move M01 work in progress to feature branch`.
16. Push `main` to origin: `git push origin main`.
17. Create the Pull Request from `feature/m01-project-initialization` to `main` with title `[M01] Project Initialization & Provisioning — Architecture Review` and the exact body provided in the user request. Use `gh pr create --base main --head feature/m01-project-initialization --title ... --body-file ...` if GitHub CLI is available and authenticated; otherwise create the PR in the GitHub web UI and paste the exact body.
18. After PR creation, optionally update the `00_index.md` PR cell on `main` from placeholder `[Open PR →]` to an actual PR link if the user wants the index to point to the created PR. This is optional because the user specified the placeholder text.
19. Final verification: confirm branch state with `git status --short --branch`, confirm PR exists, and summarize commits/branch/PR URL.

## Risks / Open Questions
- Creating a PR after pushing `main` deletion means the PR diff will show the M01 artifacts being added back to `main` for review; this matches the requested review flow.
- If branch protection prevents direct push to `main`, perform the same `main` cleanup on a separate admin/restructure branch and open a separate PR first, or ask the repository owner to apply the cleanup.
- GitHub CLI authentication may be unavailable; in that case, manual web PR creation is required.
- `knowledge-base/00_index.md` active branch PR value was specified as `[Open PR →]` without a URL target. Keep it exact unless instructed to add an actual link after PR creation.
