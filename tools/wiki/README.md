# `tools/wiki` — Azure DevOps Code Wiki integration

Publishes `knowledge-base/` as an Azure DevOps **code wiki** named **UPE Knowledge Hub**: the
human-facing browser/search/navigation layer over the repository.

> **Principle (do not weaken):** the wiki is a publication and navigation surface over the existing
> repository. It does not alter the operating model and it does not become an independent source of
> truth. Canonical knowledge remains in `knowledge-base/`; the wiki only makes it readable.

## Target configuration

| Setting | Value |
|---|---|
| Repository | this repository (`UPE`) |
| Branch | `main` |
| Folder | `/knowledge-base` |
| Wiki name | `UPE Knowledge Hub` |

Branch strategy is deliberately **not** changed for the wiki: the wiki follows `main`, exactly like
everything else.

## Manual setup (Azure DevOps UI)

1. Open the project → **Overview → Wiki**. If no wiki exists yet, the page offers two choices; pick
   **Publish code as wiki**.
2. Fill in:
   - **Repository** — the UPE repository;
   - **Branch** — `main`;
   - **Folder** — `/knowledge-base`;
   - **Wiki name** — `UPE Knowledge Hub`.
3. Select **Publish**. The wiki opens with `knowledge-base/index.md` as the home page.
4. Verify the ten home-page links resolve and that `Architecture`, `Requirements`, `Capabilities`,
   `views`, `governance` appear in the navigation pane in the intended order.

**Permissions.** You need to be a member of **Contributors** in the project; publishing code as a wiki
additionally requires the **Create Repository** permission, which by default belongs to Project
Administrators. After publishing, ordinary contributors read the wiki without any extra permission.

**How it stays current.** A code wiki is a view over a branch: it reflects `main` as soon as changes
land. There is no separate publishing step, no upload, and nothing to keep in sync.

**Changing the mapping later** (e.g. the wiki should move to a different folder): wiki **⋯ menu →
Settings**, or the REST call below. Do not edit the pages to compensate for a path change — change the
mapping.

## Navigation order and titles

- Order comes from the `.order` files committed in `knowledge-base/` (root and per folder). Without
  one, Azure DevOps sorts alphabetically. `tools/kb-validate/check_wiki.py` fails if an `.order` entry
  points at a missing page, or if a page is missing from `.order`.
- **Page titles come from file names.** That is why the collection guides are named
  `requirements-guide.md`, `evidence-guide.md` and `views-guide.md` rather than `README.md`, and why
  page names carry no spaces (both are Microsoft-documented constraints, enforced by the gate).
- A folder that contains only subfolders renders blank in the wiki, so every published folder has at
  least one page of its own.

## The one platform limitation, and how it is handled

Azure DevOps **does not navigate relative links that leave the published folder**. A link like
`../../sources/…` from a wiki page cannot resolve, so evidence, analysis, reports and tools are linked
by **absolute repository URL** instead:

```text
https://dev.azure.com/ramboll-bim/_git/UPE?path=/sources/transport/<file>&version=GBmain
```

- `tools/wiki/make_links_wiki_safe.py` performs that conversion for every `](…)` link in
  `knowledge-base/**` that points outside `knowledge-base/` — in the body only. Frontmatter
  (`sources:`, `upe.relations[].target`) stays repo-relative: that is the machine-facing provenance
  surface, validated by `check_sources.py`.
- It is idempotent and reversible:

  ```bash
  python tools/wiki/make_links_wiki_safe.py                 # dry run, lists what would change
  python tools/wiki/make_links_wiki_safe.py --apply         # convert
  python tools/wiki/make_links_wiki_safe.py --revert --apply  # back to relative links
  ```

- Links *inside* `knowledge-base/` stay relative on purpose, so they work in both Repos and the wiki
  and survive a future change of the published folder.

All repository URLs live in **one** place: [`wiki.config.json`](wiki.config.json). Do not paste the
URL into pages by hand — regenerate instead.

## Validation

```bash
python tools/kb-validate/check_wiki.py     # also runs as part of tools/kb-validate/run_all.py
```

It checks: every out-of-KB link is an absolute repo URL whose `?path=` exists; no relative link
escapes the published folder; `.order` integrity; page-name constraints (no spaces, no illegal
characters, length, per-folder uniqueness); and that the home page and its ten section pages exist.

## Optional automation

[`setup_wiki.py`](setup_wiki.py) creates or updates the wiki mapping through the REST API. It defaults
to **dry run** and prints the exact request, so it is safe to inspect first:

```bash
export AZURE_DEVOPS_EXT_PAT=<personal access token with "Wiki (Read & Write)" scope>

python tools/wiki/setup_wiki.py --project <project> --dry-run   # print the request
python tools/wiki/setup_wiki.py --project <project> --apply     # create or update the mapping
```

> **Unverified against the live organisation.** It was written from the documented REST contract
> (`_apis/wiki/wikis`, api-version 7.1) and cannot be tested without credentials. The UI steps above
> are the authoritative path; treat the script as a convenience. The project name must be supplied —
> it is deliberately not guessed (the repository URL does not show it).

Endpoints used:

| Purpose | Request |
|---|---|
| List wikis | `GET {org}/{project}/_apis/wiki/wikis?api-version=7.1` |
| Create code wiki | `POST {org}/{project}/_apis/wiki/wikis?api-version=7.1` with `{"name","projectId","repositoryId","mappedPath","type":"codeWiki"}` |
| Update mapping | `PATCH {org}/{project}/_apis/wiki/wikis/{id}?api-version=7.1` with `{"mappedPath":"/knowledge-base"}` |

## What the wiki must never become

- A place where canonical knowledge is written and the repository is not.
- A second knowledge base, a parallel taxonomy, or a substitute for `knowledge-base/`.
- A reason to restructure the repository: the KB keeps its atomic, machine-readable structure, and
  wiki usability is delivered through indexes, views, ordering and links.
- The only editing surface for canonical records — those are reviewed and promoted in the repository.
