#!/usr/bin/env python3
"""Generate the human-surface views in `knowledge-base/views/`.

Views are **non-authoritative projections** of canonical KB records. They are regenerated, never
hand-maintained: run this script after any change to canonical knowledge.

    python tools/kb-views/generate.py

Reads frontmatter only, plus the `## Traceability` / `## Open questions` body sections where a view
needs them. Writes ten views and stamps each one with its provenance banner.

Anything outside `knowledge-base/` (evidence, analysis, reports) is linked by absolute repository
URL, because Azure DevOps Code Wiki cannot navigate relative links out of the published folder —
the URLs come from `tools/wiki/wiki.config.json` so they exist in exactly one place.
"""
import datetime
import glob
import json
import os
import re
import sys

try:
    import yaml
except ImportError:
    print("generate.py: PyYAML is required (pip install pyyaml)")
    sys.exit(2)

ROOT = "knowledge-base"
VIEWS = os.path.join(ROOT, "views")
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
TODAY = datetime.date.today().isoformat()
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))

BANNER = (
    "> **Generated / non-authoritative projection of canonical KB entities.**\n"
    "> Regenerate: `python tools/kb-views/generate.py`. Do not hand-edit; the records win.\n"
)
GBA_CATEGORIES = {"vendors", "meetings", "ramboll", "standards", "legacy"}
EXPECTED_GBAS = ["Buildings", "Energy", "Water", "Architecture & Landscape"]


def load_config():
    try:
        with open(os.path.join(REPO, "tools", "wiki", "wiki.config.json"), encoding="utf8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {}


CFG = load_config()


def repo_url(path):
    """Absolute repository URL for a path outside the published folder."""
    from urllib.parse import quote
    return f"{CFG.get('repo_web_url', '')}?path={quote('/' + path)}&version=GB{CFG.get('branch', 'main')}"


def listdir(rel):
    """Visible entries in a repo folder: no dotfiles, no '~$' Office lock files."""
    abs_path = os.path.join(REPO, rel.replace("/", os.sep))
    try:
        return sorted(n for n in os.listdir(abs_path)
                      if not n.startswith(".") and not n.startswith("~$"))
    except OSError:
        return []


def is_dir(rel):
    return os.path.isdir(os.path.join(REPO, rel.replace("/", os.sep)))


def load():
    """Return {path: frontmatter} for every KB record."""
    recs = {}
    for f in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
        rel = f.replace(os.sep, "/")
        if rel.startswith("knowledge-base/views/"):
            continue
        txt = open(f, encoding="utf8").read()
        m = FM_RE.match(txt)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except Exception:  # noqa: BLE001
            continue
        fm["_path"] = rel
        fm["_slug"] = os.path.splitext(os.path.basename(rel))[0]
        fm["_body"] = txt[m.end():]
        recs[rel] = fm
    return recs


def link(rel):
    """Link from views/<name>.md to a KB record."""
    return os.path.relpath(rel, VIEWS).replace(os.sep, "/")


def by_type(recs, t):
    return sorted((r for r in recs.values() if r.get("type") == t), key=lambda r: r["_path"])


def write(name, title, description, body):
    path = os.path.join(VIEWS, name)
    slug = os.path.splitext(name)[0]
    stale = (datetime.date.today() + datetime.timedelta(days=365)).isoformat()
    fm = (
        "---\n"
        "type: view\n"
        f"title: {title}\n"
        f'description: "{description}"\n'
        f"tags: [view, generated, {slug}, draft]\n"
        "sources: []\n"
        f"generated: {TODAY}T00:00:00Z\n"
        "verified: false\n"
        "status: draft\n"
        f"stale_after: {stale}\n"
        "upe:\n"
        "  lifecycle: draft\n"
        '  owner: "@chief-architect"\n'
        "  relations:\n"
        "    - type: supports\n"
        "      target: index\n"
        "---\n\n"
    )
    with open(path, "w", encoding="utf8", newline="") as fh:
        fh.write(fm)
        fh.write(f"# {title}\n\n{BANNER}\n")
        fh.write(body)
        fh.write(f"\n---\n\n_Generated {TODAY} from {len(RECS)} canonical records._\n")
    print(f"wrote {path}")


RECS = load()
domains = by_type(RECS, "domain")
arch = by_type(RECS, "architecture")
decisions = [r for r in by_type(RECS, "decision") if "template" not in r["_slug"]]
caps = by_type(RECS, "capability")
reqs = by_type(RECS, "requirement")
evidence = by_type(RECS, "source-reference")

# ---------------------------------------------------------------- architecture
lines = ["## Governed architecture records", "", "| Record | Description |", "|---|---|"]
for r in arch:
    lines.append(f"| [`{r['_slug']}`]({link(r['_path'])}) | {(r.get('description') or '').strip()} |")
lines += ["", "## Decision catalog", "", "| Decision | Title | Status | Lifecycle |", "|---|---|---|---|"]
for r in decisions:
    lc = (r.get("upe") or {}).get("lifecycle", "-")
    lines.append(f"| [`{r['_slug']}`]({link(r['_path'])}) | {r.get('title','')} | {r.get('status','-')} | {lc} |")
lines += ["", "## Candidate functional domains (not bounded contexts)", "",
          "| ID | Domain | Priority | Key outcome |", "|---|---|---|---|"]
for r in sorted(domains, key=lambda r: (r.get("upe") or {}).get("id", "")):
    did = (r.get("upe") or {}).get("id", "-")
    pri = re.search(r"## Priority\s*\n+([^\n]+)", r["_body"])
    out = re.search(r"## Key outcome \(source\)\s*\n+([^\n]+)", r["_body"])
    lines.append(
        f"| {did} | [`{r.get('title','')}`]({link(r['_path'])}) | "
        f"{pri.group(1).strip() if pri else '-'} | {out.group(1).strip() if out else '-'} |")
write("architecture-overview.md", "Architecture Overview",
      "Current UPE architecture state and its major parts, as recorded in the canonical KB.",
      "\n".join(lines) + "\n")

# -------------------------------------------------------------- capability map
by_section = {}
for c in caps:
    fb = (c.get("upe") or {}).get("functional_block") or ""
    sec = fb.split(" ")[0].split(".")[0] if fb else "unassigned"
    by_section.setdefault(sec, []).append(c)

dom_by_num = {}
for d in domains:
    m = re.match(r"M(\d+)$", (d.get("upe") or {}).get("id", ""))
    if m:
        dom_by_num[str(int(m.group(1)))] = d

lines = [f"**{len(caps)} capability records** grouped by the candidate functional domain they were "
         f"extracted under (`upe.functional_block`). These atomic records are the machine surface; "
         f"this page is only a way in.", ""]
for sec in sorted(by_section, key=lambda s: (s == "unassigned", int(s) if s.isdigit() else 999)):
    d = dom_by_num.get(sec)
    heading = (f"M{int(sec):02d} — {d.get('title','')}" if d
               else ("Unassigned" if sec == "unassigned" else f"Section {sec}"))
    lines.append(f"## {heading}")
    if d:
        lines.append(f"[domain record]({link(d['_path'])}) · {len(by_section[sec])} capabilities")
    lines.append("")
    for c in sorted(by_section[sec], key=lambda c: c["_slug"]):
        lines.append(f"- [{(c.get('title') or c['_slug']).replace('|', '/')}]({link(c['_path'])})")
    lines.append("")
write("capability-map.md", "Capability Map",
      "Navigable grouping of the atomic capability records by candidate functional domain.",
      "\n".join(lines) + "\n")

# ------------------------------------------------------- requirements coverage
lines = ["| Requirement | Kind | Status | Evidence | Realising capabilities |", "|---|---|---|---|---|"]
for r in reqs:
    kind = (r.get("requirement") or {}).get("kind", "-")
    src = ", ".join(f"`{s.split('/')[-1]}`" for s in (r.get("sources") or [])) or "-"
    tr = re.search(r"## Traceability\s*(.*?)(?=\n## |\Z)", r["_body"], re.S)
    caplinks = re.findall(r"\]\(([^)]*capabilities/[^)]+)\)", tr.group(1)) if tr else []
    caps_cell = ", ".join(
        f"[{os.path.splitext(os.path.basename(c))[0]}]"
        f"({os.path.relpath(os.path.join(ROOT, 'capabilities', os.path.basename(c)), VIEWS).replace(os.sep, '/')})"
        for c in caplinks) or "—"
    lines.append(f"| [{r.get('title', r['_slug'])}]({link(r['_path'])}) | {kind} | {r.get('status','-')} "
                 f"| {src} | {caps_cell} |")
if not reqs:
    lines.append("| _none yet_ | | | | |")
lines += ["", "Traceability chain: `Source → Problem → Requirement → Capability → Architecture → "
              "Decision → Lab/Implementation → Evidence`.", ""]
write("requirements-coverage.md", "Requirements Coverage",
      "Requirement to capability and evidence traceability across the requirements collection.",
      "\n".join(lines) + "\n")

# ------------------------------------------------------------------- gba views
gba_dirs = [d for d in listdir("sources")
            if d not in GBA_CATEGORIES and is_dir(f"sources/{d}")]
lines = []
if not gba_dirs:
    lines.append("_No GBA-specific source material has been received yet._")
for gba in gba_dirs:
    files = [f for f in listdir(f"sources/{gba}")
             if os.path.isfile(os.path.join(REPO, "sources", gba, f))]
    lines += [f"## {gba.capitalize()}", "", f"[source folder]({repo_url(f'sources/{gba}')})", ""]
    if files:
        lines.append("**Received source material** (evidence, not knowledge)")
        lines.append("")
        for f in files:
            lines.append(f"- [{f}]({repo_url(f'sources/{gba}/{f}')})")
        lines.append("")
    ev = [e for e in evidence
          if gba in json.dumps(e.get("source") or {}, ensure_ascii=False, default=str).lower()]
    if ev:
        lines.append("**Source records** (canonical metadata about the evidence)")
        lines.append("")
        for e in ev:
            lines.append(f"- [{e.get('title', e['_slug'])}]({link(e['_path'])})")
        lines.append("")
    an = [d for d in listdir("analysis/ai") if gba in d.lower()] + \
         [d for d in listdir("analysis/human") if gba in d.lower()] + \
         [d for d in listdir("analysis/reviewed") if gba in d.lower()]
    lines.append("**Analysis of this material** (non-canonical)")
    lines.append("")
    if an:
        for d in sorted(set(an)):
            for base in ("ai", "human", "reviewed"):
                if d in listdir(f"analysis/{base}"):
                    lines.append(f"- [{base}/{d}]({repo_url(f'analysis/{base}/{d}')})")
    else:
        lines.append("- _none yet — this is where a human or AI analysis would land_")
    lines.append("")
    rq = [r for r in reqs if gba in json.dumps(r.get("sources") or [], ensure_ascii=False, default=str).lower()]
    lines.append("**Canonical requirements citing this material**")
    lines.append("")
    if rq:
        for r in rq:
            lines.append(f"- [{r.get('title', r['_slug'])}]({link(r['_path'])})")
    else:
        lines.append("- _none yet_")
    lines.append("")
lines += ["## GBAs not yet represented", "",
          "Expected GBA input areas with no material in the repository yet: "
          + ", ".join(f"**{g}**" for g in EXPECTED_GBAS) + ".",
          "", "Nothing is pre-created for them: a GBA appears above as soon as it has a folder under "
          "`sources/`. Transport is an example, not the ontology.", ""]
write("gba-overview.md", "GBA Needs & Coverage",
      "Per-GBA navigation over received source material, non-canonical analysis and the canonical "
      "requirements that cite them.",
      "\n".join(lines) + "\n")

# ---------------------------------------------------------------- vendor view
lines = ["Vendor material is **received evidence**, not approved architecture. Nothing on this page "
         "asserts that a vendor is selected, endorsed or rejected.", ""]
for vendor in listdir("sources/vendors"):
    files = [f for f in listdir(f"sources/vendors/{vendor}")
             if os.path.isfile(os.path.join(REPO, "sources", "vendors", vendor, f))]
    lines += [f"## {vendor.capitalize()}", "",
              f"[source folder]({repo_url(f'sources/vendors/{vendor}')}) · {len(files)} document(s)", ""]
    for f in files:
        lines.append(f"- [{f}]({repo_url(f'sources/vendors/{vendor}/{f}')})")
    hits = [r for r in RECS.values()
            if vendor in ((r.get("title") or "") + " " + (r.get("description") or "")).lower()]
    if hits:
        lines += ["", "**KB records mentioning this vendor**"]
        lines += [f"- [{r.get('title', r['_slug'])}]({link(r['_path'])})"
                  for r in sorted(hits, key=lambda r: r["_path"])[:12]]
    lines.append("")
write("vendor-overview.md", "Vendors & Technology",
      "Navigation over vendor documentation held as evidence, plus the KB records that mention each vendor.",
      "\n".join(lines) + "\n")

# --------------------------------------------------------- sources & evidence
lines = ["Original material is held under [`sources/`](" + repo_url("sources") + ") and is **evidence**, "
         "never canonical knowledge. Every canonical record that claims support points here through its "
         "`sources:` metadata.", "",
         f"[Open the whole sources folder in Repos]({repo_url('sources')})", ""]
for group in listdir("sources"):
    n = sum(len(fs) for _, _, fs in os.walk(os.path.join(REPO, "sources", group)))
    lines += [f"## {group.capitalize()}",
              f"[{n} file(s)]({repo_url(f'sources/{group}')})", ""]
    for sub in listdir(f"sources/{group}"):
        if os.path.isdir(os.path.join(REPO, "sources", group, sub)):
            c = sum(len(fs) for _, _, fs in os.walk(os.path.join(REPO, "sources", group, sub)))
            lines.append(f"- [{sub}]({repo_url(f'sources/{group}/{sub}')}) — {c} file(s)")
    lines.append("")
lines += ["## Registered source records", "",
          "Canonical metadata about received sources (location, revision, hash):", ""]
for e in evidence:
    lines.append(f"- [{e.get('title', e['_slug'])}]({link(e['_path'])})")
lines += ["", "## Analysis of this material", "",
          "Analysis is non-canonical and lives outside the KB: "
          f"[human]({repo_url('analysis/human')}) · [AI]({repo_url('analysis/ai')}) · "
          f"[reviewed]({repo_url('analysis/reviewed')}).", ""]
write("sources-and-evidence.md", "Sources & Evidence",
      "Where original material lives, how it is registered, and how it differs from canonical knowledge.",
      "\n".join(lines) + "\n")

# ---------------------------------------------------------------- reports view
LABELS = {"working": "working — internal draft", "architecture-committee": "committee — for review",
          "published": "published — issued"}
lines = ["Reports are **never canonical**. They present knowledge or analysis to an audience and must "
         "trace back to canonical records or named analysis.", ""]
for group in listdir("reports"):
    if not os.path.isdir(os.path.join(REPO, "reports", group)):
        continue
    lines.append(f"## {LABELS.get(group, group)}")
    lines.append("")
    lines.append(f"[{group}/ folder]({repo_url(f'reports/{group}')})")
    lines.append("")
    items = [f for f in listdir(f"reports/{group}") if f.endswith(".md")
             and not f.startswith("README")]
    if items:
        for f in items:
            lines.append(f"- [{f[:-3]}]({repo_url(f'reports/{group}/{f}')})")
    else:
        lines.append("- _none yet_")
    lines.append("")
lines += ["## How to add a report", "",
          f"See the report contract: [reports/README.md]({repo_url('reports/README.md')}).", ""]
write("reports.md", "Reports",
      "Audience-facing deliverables by status, with links into the reports area outside the KB.",
      "\n".join(lines) + "\n")

# ------------------------------------------------------------------ roadmap
prio = {}
for d in domains:
    m = re.search(r"## Priority\s*\n+([^\n]+)", d["_body"])
    key = (m.group(1).strip() if m else "unspecified").lower()
    prio.setdefault(key, []).append(d)
kinds = {}
for r in reqs:
    k = (r.get("requirement") or {}).get("kind", "unspecified")
    kinds[k] = kinds.get(k, 0) + 1
pending = [r for r in decisions if (r.get("upe") or {}).get("lifecycle") in ("idea", "draft", "in-review")]
lines = ["> **No governed roadmap exists yet.** This page is a projection of what the records "
         "currently say about priority, requirement kinds and open decisions — not a plan, and not "
         "approved sequencing.", "",
         "A real roadmap becomes expressible once requirements are reviewed and the Architecture "
         "Committee accepts priorities; when that happens, record them as decisions rather than "
         "editing this page.", "",
         "## Candidate domain priorities (source-derived)", "",
         "| Priority | Candidate domains |", "|---|---|"]
for k in sorted(prio, key=lambda k: (k != "high", k)):
    names = ", ".join(f"[{d.get('title','')}]({link(d['_path'])})" for d in prio[k])
    lines.append(f"| {k} | {names} |")
lines += ["", "## Requirement coverage by kind", "", "| Kind | Count |", "|---|---|"]
for k, n in sorted(kinds.items()):
    lines.append(f"| {k} | {n} |")
lines += ["", f"## Decisions needing input ({len(pending)})", "",
          f"See [open decisions](open-decisions.md) for the detail.", ""]
write("roadmap.md", "Roadmap",
      "Projection of candidate priorities, requirement kinds and open decisions. No governed roadmap exists yet.",
      "\n".join(lines) + "\n")

# ----------------------------------------------------- architecture committee
boards = CFG.get("boards_url", "")
pipelines = CFG.get("pipelines_url", "")
lines = ["## Backlog", ""]
if boards:
    lines.append(f"- [Azure Boards backlog]({boards}) — planning and execution live in Boards, "
                 f"not in Markdown")
else:
    lines.append("- **Azure Boards link not configured.** Set `boards_url` in "
                 "`tools/wiki/wiki.config.json` and this page will link it. The board URL is not "
                 "guessed here on purpose.")
lines += ["", f"## Open decisions ({len(pending)})", "",
          f"- [Open decisions and open questions](open-decisions.md) — every decision awaiting input, "
          f"plus the open questions recorded on canonical records", ""]
lines += ["", "## Architecture Decision Records", ""]
for r in decisions:
    lines.append(f"- [{r.get('title','')}]({link(r['_path'])}) — `{r.get('status','-')}`")
lines += ["", f"- [ADR catalog]({link('knowledge-base/architecture/decisions/index.md')})", ""]
lines += ["## Priorities and roadmap", "",
          "- [Roadmap projection](roadmap.md) — candidate priorities; no governed roadmap yet", ""]
lines += ["## Analysis awaiting review", ""]
candidates = [f for f in listdir("analysis/reviewed") if f.endswith(".md") and f != "README.md"]
if candidates:
    for f in candidates:
        lines.append(f"- [{f[:-3]}]({repo_url(f'analysis/reviewed/{f}')})")
else:
    lines.append(f"- _Nothing in the review queue yet._ Reviewed analysis lands in "
                 f"[analysis/reviewed/]({repo_url('analysis/reviewed')}).")
lines += ["", "## Committee reports", "",
          f"- [Reports index](reports.md) · "
          f"[committee folder]({repo_url('reports/architecture-committee')})", ""]
if pipelines:
    lines += ["## Pipelines", "", f"- [Build and validation]({pipelines})", ""]
write("architecture-committee.md", "Architecture Committee",
      "Committee hub: backlog, open decisions, ADRs, roadmap, analysis awaiting review and reports.",
      "\n".join(lines) + "\n")

# --------------------------------------------------------------- open decisions
lines = ["## Decisions awaiting a human decision", "",
         "| Decision | Title | Status | Lifecycle |", "|---|---|---|---|"]
for r in pending or decisions:
    lc = (r.get("upe") or {}).get("lifecycle", "-")
    lines.append(f"| [`{r['_slug']}`]({link(r['_path'])}) | {r.get('title','')} | {r.get('status','-')} | {lc} |")
lines += ["", "## Open questions recorded on canonical records", ""]
for r in sorted(RECS.values(), key=lambda r: r["_path"]):
    if r.get("type") in ("capability", "navigation", "log"):
        continue  # atomic/boilerplate records: their open questions are not decision-level
    m = re.search(r"## Open questions\s*\n(.*?)(?=\n## |\Z)", r["_body"], re.S)
    if not m:
        continue
    items = [ln.strip("- ").strip() for ln in m.group(1).strip().splitlines()
             if ln.strip().startswith("-")]
    # links copied out of a record would resolve relative to views/ — keep the label only
    items = [re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", i) for i in items]
    if not items:
        continue
    lines.append(f"### [{r.get('title', r['_slug'])}]({link(r['_path'])})")
    lines += [f"- {i}" for i in items]
    lines.append("")
write("open-decisions.md", "Open Decisions",
      "Decisions and open questions currently needing human input.",
      "\n".join(lines) + "\n")
