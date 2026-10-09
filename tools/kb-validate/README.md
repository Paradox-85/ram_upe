# `tools/kb-validate` — knowledge-base validation gate

Reusable, maintained validation for the canonical KB. This is a **tool**, not a lab: it has an
owner, a contract and a stable entry point, and it is meant to be run by humans, agents and CI.

> Replaces the previous, non-reproducible workflow: validation scripts used to live in the
> gitignored `.pi/temp/` directory, so a fresh clone could not run any documented check
> (audit finding F6).

## Run everything

```bash
# from the repository root
python tools/kb-validate/run_all.py            # all gates
python tools/kb-validate/run_all.py --lint     # + markdownlint (needs npx)
```

Exit code is non-zero if any gate fails, so `run_all.py` is directly usable in CI.

## Gates

| Script | Contract it enforces |
|---|---|
| `check_frontmatter.py` | every KB record has parseable frontmatter with `type`, a valid `status`, a DDDM `upe.lifecycle`, a unique `upe.id`, and never `approved` |
| `check_links.py` | every local Markdown link inside `knowledge-base/` resolves (URLs and anchors ignored, `%20` decoded) |
| `check_sources.py` | **every `sources:` payload and `upe.relations[].target` resolves** — closes the gap that let a dangling provenance path survive (audit finding F5) |
| `check_wiki.py` | **Azure DevOps code-wiki gate**: out-of-KB links are absolute repo URLs whose target exists; no relative link escapes `knowledge-base/`; `.order` files are complete and valid; page names obey the platform constraints; the home page and its ten section pages exist |
| `markdownlint.json` | lint config; `MD013` (line length) disabled |

## Requirements

`python` 3.x with `PyYAML`. No other dependencies. `npx markdownlint-cli2` only for `--lint`.

## Scope

The gates read `knowledge-base/**` only — the published wiki surface. `sources/`, `analysis/`,
`reports/` and `labs/` hold non-canonical material and are deliberately **not** governed by the KB
metadata contract, except that the analysis layer has its own lightweight frontmatter contract (see
`analysis/README.md`). Wiki-relevant rules (ordering, page names, cross-boundary links) are enforced by
`check_wiki.py`.

## Reviewer note

A green run means *structurally* valid. It does **not** mean governed: promotion to canonical
knowledge is a human decision (see `knowledge-base/governance/operating-model.md`).
