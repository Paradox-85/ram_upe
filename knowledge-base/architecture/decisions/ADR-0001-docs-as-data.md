---
id: ADR-0001
type: decision
status: accepted
owner: "@chief-architect"
version: 1.0
last_updated: 2026-05-26
parent: master.md
tags: [ADR, docs-as-data, markdown, mermaid, git]
---

# ADR-0001: Docs-as-Data with Markdown + Mermaid + Git-Style Workflow

## Status
**Accepted** (for demo; review by 2026-06-30)

## Context

The UPE product design process needs a source-of-truth system that:
- Supports iterative, LLM-assisted design sessions
- Enables modular ownership (multiple people working on different modules)
- Maintains traceability of decisions and requirements
- Generates documentation, diagrams, and reports as derived outputs
- Avoids the overhead and staleness of traditional Word/PDF specifications

Traditional approaches (Word specs, Confluence, Jira-only backlogs) have critical limitations:
- **Static documents** become stale immediately after creation
- **Manual diagrams** (Visio, Draw.io) drift from the actual design
- **No version discipline** — who approved what, when?
- **Siloed ownership** — no clear fork/review/merge workflow
- **LLM-incompatible** — binary formats can't be used in AI sessions

## Decision

We adopt **Markdown + Mermaid + Git-style workflow** as the source of truth for all UPE product design knowledge:

1. **All knowledge lives as `.md` files** in a structured repository (`knowledge-base/`)
2. **Diagrams are Mermaid blocks** embedded in Markdown — no external files
3. **Git-style discipline** governs knowledge evolution:
   - `master.md` + approved `modules/` = canonical knowledge
   - `backlog/forks/` = working hypotheses before review
   - Merge gates enforce completeness, traceability, and architecture review
4. **YAML front matter** on every file for machine-readable metadata
5. **Stable IDs** for requirements, entities, workflows, interfaces, and decisions
6. **Reports are derived snapshots** — never source of truth
7. **LLM sessions are logged** as part of the design process

## Consequences

### Positive
- **LLM-native:** Markdown is the ideal format for AI-assisted design sessions
- **Version-controlled:** Every change is tracked; rollback is trivial
- **Mermaid diagrams always in sync:** Diagrams live with the data they describe
- **Review-friendly:** PR/diff-based review of design changes
- **Tool-agnostic:** Any Markdown editor works (Obsidian, VS Code, GitHub, Azure DevOps)
- **Fast iteration:** No formatting overhead, no diagram export steps
- **Searchable & queryable:** Text-based knowledge is easy to search and index

### Negative
- **Mermaid limitations:** Complex diagrams (BPMN-level detail) are harder in Mermaid than in dedicated tools
- **Learning curve:** Team must learn Mermaid syntax and Git-style workflow
- **Rendering dependency:** Requires Mermaid-capable viewer (GitHub, Obsidian, VS Code)
- **Not a replacement for all documentation:** Legal contracts, compliance filings still need traditional formats

### Risks
- Risk of "Markdown fatigue" if too many files without clear ownership
- Mitigated by: strict folder structure, `00_index.md` for discoverability, merge gates for quality

## Alternatives Considered

| Alternative | Why Rejected |
|---|---|
| **Confluence / SharePoint Wiki** | Binary/proprietary format, poor Git integration, no Mermaid-native support, versioning is opaque |
| **Jira + Confluence** | Good for task tracking but not for structured product knowledge; diagrams still manual |
| **Pure Git repo (code-style)** | Missing the DDDM framework layer; too developer-centric for product/design audience |
| **Notion / Coda** | SaaS lock-in, limited Mermaid support, export is fragile |
| **Draw.io + Word** | Manual diagram hell, no automation, drift guaranteed |

## Review Date
**2026-06-30** — Re-evaluate after demo session with stakeholders. Consider:
- Whether Mermaid covers all diagram needs or if PlantUML supplement is needed
- Whether Azure DevOps Wiki or Obsidian becomes the primary rendering tool
- Adoption feedback from module owners

## References
- Inspired by: [Karpathy's vibe coding manifesto](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- Framework source: `prompts/LLM-Native Product Design Framework.md`
