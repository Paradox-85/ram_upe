# Handoff Prompt: Create `.idx` Repository File List

You are performing a simple test task in the repository `C:/Development/upe/UPE`: read the repository structure and create a file list in the `.idx` folder.

## Critical Constraints
- Work in the repository root: `C:/Development/upe/UPE`.
- Do not modify existing product/source files in `docs/`, `prompts/`, `src/`, `.plans/` and `azure-pipelines.yml`.
- Permitted changes for implementing the task: only create/update files inside `.idx/`.
- Do not include `.git/**` in the index.
- Do not include `.idx/**` in the source set of indexed files, so the index does not reference itself as a source input.
- After execution, mark completed steps in your response with `[DONE:n]` tags.

## Codebase Context
The current repository is a knowledge/materials repo for UPE (Unified Project Execution), primarily Markdown and text documents.

Top level found during the planning phase:
- `.git/` — Git metadata, exclude from index.
- `.plans/` — planning artifacts; can be included in the index as part of the repository unless instructed otherwise.
- `docs/` — main UPE documents:
  - `docs/UPE_Executive_Summary_v1.md`
  - `docs/UPE_Functional_Blocks_v1.md`
  - `docs/UPE_Functional_Blocks_v1.pdf`
  - `docs/brainstorming.md`
- `prompts/`:
  - `prompts/LLM-Native Product Design Framework.md`
- `src/`:
  - `src/chat/UPE Platform Architects Chat.md`
  - `src/loop/loop.md`
  - `src/moms/*` meeting notes/transcripts
  - `src/vendors/*` vendor notes
- `azure-pipelines.yml` — pipeline config.

The `.idx/` folder did not exist during the planning phase.

## Full Plan to Execute

1. Check the repository state with read-only commands/tools: `git status --short`, `ls`, `find`. Verify whether `.idx/` exists.
2. Collect the file list for indexing according to the rule:
   - include regular repository files;
   - exclude `.git/**`;
   - exclude `.idx/**`;
   - for the test, include `.plans/**` unless the user asked to exclude planning artifacts.
3. Create the `.idx/` folder in the repository root if it does not exist.
4. Create `.idx/files.md` as the primary human-readable index. Format:
   ```markdown
   # Repository File Index

   Generated: <ISO or local date-time>

   Scope: all repository files except `.git/**` and `.idx/**`.

   Total files: <N>

   ## Root
   - `azure-pipelines.yml`

   ## .plans
   - `.plans/...`

   ## docs
   - `docs/...`

   ## prompts
   - `prompts/...`

   ## src
   - `src/...`
   ```
   Paths must be relative from the repository root and sorted alphabetically.
5. Optionally create `.idx/files.txt` with the same list, one relative path per line. If you want to keep the task to a bare minimum — you may skip it, but then state this explicitly in the final response.
6. Perform a sanity check:
   - read `.idx/files.md`;
   - verify that key paths are present: `azure-pipelines.yml`, `docs/UPE_Executive_Summary_v1.md`, `prompts/LLM-Native Product Design Framework.md`, `src/loop/loop.md`;
   - verify that `.git/HEAD` and `.idx/files.md` are not in the source files list.
7. In the final response, briefly state:
   - which files were created in `.idx/`;
   - how many files were indexed;
   - which exclusions were applied;
   - execution tags `[DONE:1]` ... `[DONE:7]`.

## Gotchas
- Some paths contain spaces and parentheses, e.g. `prompts/LLM-Native Product Design Framework.md` and files in `src/moms/`. Do not break such names when generating the list.
- The repository has no `.gitignore`, so do not rely solely on ignore rules; explicitly exclude `.git` and `.idx`.
- There is no need to read or parse PDF/large transcript files — the task is only about a list of paths.
- If using a shell, handle names with spaces carefully; prefer using `find` with sorting, or a script that handles paths correctly.
