#!/usr/bin/env python3
"""Azure DevOps Code Wiki gate: validates everything the Wiki publication depends on.

The Code Wiki publishes `knowledge-base/` (see tools/wiki/wiki.config.json). What can break it:

1. **Cross-boundary links.** Azure DevOps does not navigate relative links pointing outside the
   published folder. Every out-of-KB link must be an absolute repository URL — and that URL's
   `?path=` must resolve to a real path (this replaces the internal-link checking that
   `check_links.py` gives up once the link becomes a URL).
2. **`.order` integrity.** A `.order` file defines the page sequence; a stale or incomplete entry
   means a page is mis-ordered or effectively unreachable from the navigation pane.
3. **Page-name constraints** (Microsoft-documented limits): no spaces, no leading/trailing period,
   no `/ \\ #`, ≤ 235 characters for the full path, unique within its folder.
4. **Entry pages exist** so the published home page and its ten sections are never dead.

Exit codes: 0 = OK (warnings allowed), 1 = failures found.
"""
import glob
import json
import os
import re
import sys
from urllib.parse import unquote

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
PUBLISHED = "knowledge-base"
CONFIG = os.path.join(REPO, "tools", "wiki", "wiki.config.json")
LINK_RE = re.compile(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
URL_PATH_RE = re.compile(r"\?path=([^&\s]+)")
ILLEGAL_NAME_RE = re.compile(r"[/\\#]")
MAX_FULL_PATH = 235

failures = []
warnings = []


def to_posix(p):
    return p.replace(os.sep, "/")


def load_config():
    try:
        with open(CONFIG, encoding="utf8") as fh:
            return json.load(fh)
    except OSError:
        failures.append(f"missing wiki config: {to_posix(os.path.relpath(CONFIG, REPO))}")
        return {}


def md_files():
    return sorted(glob.glob(os.path.join(REPO, PUBLISHED, "**", "*.md"), recursive=True))


# ----------------------------------------------------------------- 1. links
def check_links(cfg):
    repo_url = cfg.get("repo_web_url", "")
    checked = resolved = 0
    for fp in md_files():
        rel = to_posix(os.path.relpath(fp, REPO))
        rel_dir = os.path.dirname(rel)
        text = open(fp, encoding="utf8").read()
        for m in LINK_RE.finditer(text):
            target = m.group(1)
            if target.startswith("#") or target.startswith("mailto:"):
                continue
            if not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", target):
                # relative link: must stay inside the published folder
                dest = os.path.normpath(os.path.join(rel_dir, unquote(target).split("#")[0])).replace(os.sep, "/")
                if not (dest == PUBLISHED or dest.startswith(PUBLISHED + "/")):
                    failures.append(
                        f"{rel}: relative link escapes the published folder -> {target} "
                        f"(make it an absolute repo URL: python tools/wiki/make_links_wiki_safe.py --apply)")
                continue
            if repo_url and target.startswith(repo_url):
                mp = URL_PATH_RE.search(target)
                if not mp:
                    failures.append(f"{rel}: repo URL without ?path= -> {target}")
                    continue
                dest = unquote(mp.group(1)).lstrip("/")
                checked += 1
                if os.path.exists(os.path.join(REPO, dest.replace("/", os.sep))):
                    resolved += 1
                else:
                    failures.append(f"{rel}: repo URL points at a missing path -> /{dest}")
                if dest == PUBLISHED or dest.startswith(PUBLISHED + "/"):
                    warnings.append(f"{rel}: absolute repo URL points inside the KB; prefer a relative "
                                    f"link for portability -> /{dest}")
    return checked, resolved


# ---------------------------------------------------------------- 2. .order
def check_order():
    orders = sorted(glob.glob(os.path.join(REPO, PUBLISHED, "**", ".order"), recursive=True))
    for order in orders:
        folder = os.path.dirname(order)
        folder_rel = to_posix(os.path.relpath(folder, REPO))
        raw = open(order, encoding="utf8").read()
        if raw.startswith("\ufeff"):
            failures.append(f"{folder_rel}/.order: starts with a UTF-8 BOM (write plain UTF-8)")
            raw = raw.lstrip("\ufeff")
        entries = [ln.strip() for ln in raw.splitlines() if ln.strip()]
        if len(entries) != len(set(entries)):
            failures.append(f"{folder_rel}/.order: contains duplicate entries")
        actual = set()
        for name in os.listdir(folder):
            if name.startswith("."):
                continue
            full = os.path.join(folder, name)
            if os.path.isdir(full):
                actual.add(name)
            elif name.endswith(".md"):
                actual.add(name[:-3])
        listed = set(entries)
        for stale in sorted(listed - actual):
            failures.append(f"{folder_rel}/.order: entry '{stale}' does not exist in this folder")
        for missing in sorted(actual - listed):
            failures.append(f"{folder_rel}/.order: '{missing}' exists but is not listed "
                            f"(navigation order would be undefined)")
    return orders


# ------------------------------------------------------- 3. page-name limits
def check_page_names():
    seen = {}
    for fp in md_files():
        rel = to_posix(os.path.relpath(fp, REPO))
        name = os.path.basename(rel)
        stem = name[:-3]
        if " " in stem:
            failures.append(f"{rel}: page file name contains a space (use '-')")
        if stem.startswith(".") or stem.endswith("."):
            failures.append(f"{rel}: page file name starts or ends with '.'")
        if ILLEGAL_NAME_RE.search(stem):
            failures.append(f"{rel}: page file name contains an illegal character (/ \\ #)")
        if len(rel) > MAX_FULL_PATH:
            failures.append(f"{rel}: path length {len(rel)} exceeds the {MAX_FULL_PATH}-character wiki limit")
        key = (os.path.dirname(rel), stem.lower())
        if key in seen and seen[key] != rel:
            failures.append(f"{rel}: page name collides with {seen[key]} (case-insensitive clash in one folder)")
        seen[key] = rel


# --------------------------------------------------------- 4. required pages
REQUIRED = [
    "knowledge-base/index.md",
    "knowledge-base/product-overview.md",
    "knowledge-base/contributing.md",
    "knowledge-base/views/architecture-committee.md",
    "knowledge-base/views/architecture-overview.md",
    "knowledge-base/views/capability-map.md",
    "knowledge-base/views/requirements-coverage.md",
    "knowledge-base/views/gba-overview.md",
    "knowledge-base/views/vendor-overview.md",
    "knowledge-base/views/sources-and-evidence.md",
    "knowledge-base/views/reports.md",
    "knowledge-base/views/open-decisions.md",
    "knowledge-base/views/roadmap.md",
]


def check_required():
    for rel in REQUIRED:
        if not os.path.exists(os.path.join(REPO, rel.replace("/", os.sep))):
            failures.append(f"required wiki entry page is missing: {rel}")


def main():
    cfg = load_config()
    checked, resolved = check_links(cfg)
    orders = check_order()
    check_page_names()
    check_required()

    print(f"check_wiki: {len(md_files())} wiki pages, {len(orders)} .order file(s), "
          f"{resolved}/{checked} absolute repo links resolved")
    if warnings:
        print(f"  {len(warnings)} warning(s):")
        for w in warnings[:10]:
            print("   ~", w)
    if failures:
        print(f"check_wiki: {len(failures)} issue(s)")
        for f in failures[:40]:
            print(" -", f)
        return 1
    print("check_wiki: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
