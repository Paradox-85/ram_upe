# Read Repo IDX File List

Plan for a simple test task: read the current repository and create a file index under `.idx`.

## Context
- The repository is located at `C:/Development/upe/UPE`.
- Current top-level structure: `.git/`, `.plans/`, `docs/`, `prompts/`, `src/`, `azure-pipelines.yml`.
- The `.idx` folder does not yet exist.
- The project contains primarily Markdown/text knowledge files about UPE:
  - `docs/` — executive summary, functional blocks, brainstorming, PDF.
  - `prompts/` — framework prompt `LLM-Native Product Design Framework.md`.
  - `src/chat/`, `src/loop/`, `src/moms/`, `src/vendors/` — source notes, transcripts, vendor materials.
- A `.plans/` folder already exists with the previous plan `upe-knowledge-repo-demo`; these are planning artifacts that can be included or excluded from `.idx` according to the chosen rule.
- No `.gitignore` was found in the repository, so it is better to explicitly exclude service folders `.git/` and, if needed, `.idx/` from the generated list.

## Plan:
1. Check the current repository state with read-only commands: `git status --short`, `find`/`ls` for the top level, verify that `.idx/` is absent or understand which files are already in it.
2. Define a simple indexing rule: include all project files except `.git/**` and `.idx/**` itself; for the test, `.plans/**` can be included so the index reflects the full working repository, or excluded if only product/source content is needed.
3. Create the `.idx/` folder in the repository root.
4. Generate the main file `.idx/files.md` with the file list. Recommended format:
   - heading `# Repository File Index`;
   - generation date/time;
   - brief inclusion/exclusion rule;
   - sections by directory (`docs/`, `prompts/`, `src/`, `.plans/`, root files);
   - relative paths in Markdown bullet list.
5. Additionally, if a maximally simple machine-readable variant is needed, create `.idx/files.txt` with one relative path per line. For this test task it is optional; `.idx/files.md` alone is the minimum.
6. Use a stable alphabetical sort for the path list. Do not read the full contents of all large files; the task is an index of paths, not content.
7. Ensure that `.idx/files.md` does not include `.git/**` and does not include itself recursively as a source indexing file. If `.idx/files.txt` is created, also exclude `.idx/**` from the source set.
8. Perform a sanity check: re-read `.idx/files.md`, verify the presence of key files (`azure-pipelines.yml`, `docs/UPE_Executive_Summary_v1.md`, `prompts/LLM-Native Product Design Framework.md`, `src/loop/loop.md`) and the absence of `.git/HEAD`.
9. In the final response briefly list what was created: `.idx/files.md` and, if the optional step was taken, `.idx/files.txt`; state the number of indexed files.

## Risks / Open Questions
- It is unclear whether the index should include `.plans/**`. For the test it is acceptable to include it, but if `.idx` is intended only as an index of product materials, `.plans/**` should be excluded.
- It is unclear whether only a human-readable Markdown file is needed or also plain text/JSON. The plan proposes `.idx/files.md` as the minimum and `.idx/files.txt` as a simple optional artifact.
- PDF and large transcript/vendor files do not need to be parsed for this task: the file path is indexed, not the content.
