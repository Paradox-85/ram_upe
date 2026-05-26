---
id: demo-script
type: report
status: approved
owner: "@chief-architect"
version: 1.0
last_updated: 2026-05-26
parent: master.md
tags: [demo, script, stakeholder, presentation]
---

> ⚠️ **This is a derived snapshot generated on 2026-05-26. For current authoritative knowledge, refer to `master.md` and `modules/`.**

# Demo Script — UPE Knowledge Repository & DDDM Framework

**Total Duration:** ~25 minutes  
**Presenter:** Chief Architect  
**Audience:** Stakeholders, GBA leads, Product Owners  

---

## Part 1: The Problem with Traditional Specs (3 minutes)

**Slide/Talking Points:**
- Traditional ТЗ (specifications) are dead on arrival — written once, outdated immediately
- Engineers don't read 50-page Word documents
- Diagrams in Visio are disconnected from the actual design
- No way to track WHO decided WHAT and WHEN
- LLMs can't help with binary/proprietary formats

**Key message:** _"We need a living, LLM-compatible knowledge system, not dead documents."_

**Show:** Side-by-side comparison table (Traditional vs. DDDM) from stakeholder brief

---

## Part 2: master.md — Living Product Architecture (5 minutes)

**Open `knowledge-base/master.md` in Obsidian/VS Code**

1. **Show YAML front matter** — every file has machine-readable metadata
2. **Scroll to Vision** — UPE as enterprise digital backbone, clear scope/non-goals
3. **Show 14 domains table** — compact, with priority indicators
4. **Render Mermaid architecture diagram** — 6 layers + governance cross-cutting
5. **Show Module Registry** — M01 has status `in-review-demo`, others are `idea`
6. **Show Phase 1 focus** — what we're building first and why

**Key message:** _"This single file gives you the full picture. And it's always current because it's maintained through the review/merge process."_

---

## Part 3: M01 Fork and Review/Merge Model (7 minutes)

**Open `knowledge-base/modules/m01_project_initialization/`**

1. **Show `index.md`** — module purpose, scope, dependencies, status
2. **Show `requirements.md`** — 25+ requirements with stable IDs (REQ-M01-001...)
3. **Show `data_model.md`** — Mermaid ERD with 13 entities
4. **Show `workflows.md`** — state machine + flowchart, failure/retry paths
5. **Open the fork:** `knowledge-base/backlog/forks/project-intialization-module.md`
   - Show fork hypothesis
   - Show proposed requirements delta
   - Show interface impact table
   - Show open questions
   - Show merge checklist
6. **Explain the lifecycle:** fork → review → merge → master update → changelog

**Key message:** _"Module owners work safely in forks. Nothing enters master without passing review gates."_

---

## Part 4: Prototype Prompt as Generated Output (5 minutes)

**Open `knowledge-base/prototypes/sprint-01_project_initialization/prototype_prompt.md`**

1. **Show the prompt** — it references master.md and M01 artifacts
2. **Walk through screens:** Creation Wizard, Provisioning Status, Dashboard, Team Setup
3. **Show data objects** — TypeScript interfaces derived from data_model.md
4. **Explain the principle:** _"We don't manually write specs for developers. We generate prompts FROM the knowledge base."_

**Key message:** _"The prototype prompt is a derived output. If the knowledge base changes, we regenerate. No manual sync."_

**If prototype is ready:** Demo the clickable UI

---

## Part 5: Governance & Adoption Discussion (5 minutes)

**Discussion Topics:**
1. **Should we adopt DDDM as our design methodology?** Pilot with 2 modules or full adoption?
2. **What tool do we use?** Obsidian (local) vs. Azure DevOps Wiki (enterprise) vs. GitHub (developer-friendly)
3. **Who owns what?** Module owners, architect reviews, scrum master maintains changelog
4. **How do we scale?** Start with M01, add modules incrementally
5. **How does this interact with existing processes?** Jira for task tracking, this for knowledge

**Key message:** _"This is not another tool. This is a different way of working. The question is: are we ready to commit to data-first design?"_

---

## Appendix: Key Files for Reference

| File | Purpose |
|---|---|
| `knowledge-base/master.md` | Main integration document |
| `knowledge-base/00_principles.md` | Framework rules and standards |
| `knowledge-base/00_index.md` | Complete file inventory |
| `knowledge-base/architecture/` | Architecture overview and interface contracts |
| `knowledge-base/modules/m01_*/` | M01 complete module slice |
| `knowledge-base/backlog/forks/` | Working fork demo |
| `knowledge-base/reports/stakeholder_brief_2026-05-26.md` | This brief |
