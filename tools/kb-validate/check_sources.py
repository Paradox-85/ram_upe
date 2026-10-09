#!/usr/bin/env python3
"""Provenance validator (fixes audit finding F5).

Every canonical KB record that claims support must point at something that exists:

  * `sources:`      — payload paths (bundle-relative to knowledge-base/, or file-relative).
                      URL-encoded spellings (%20) are decoded before resolution.
  * `upe.relations` — `target` values: either a concept path without extension
                      (resolved as <target>.md) or a payload path with an extension.

Rationale: `check_frontmatter.py` validates the metadata contract and `check_links.py`
validates Markdown links, but neither looked at frontmatter provenance paths — which is how
a dangling `sources: raw-input/DDD.md` survived unnoticed.

Exit codes: 0 = OK, 1 = issues found.
"""
import glob
import os
import re
import sys
from urllib.parse import unquote

try:
    import yaml
except ImportError:
    print("check_sources: PyYAML is required (pip install pyyaml)")
    sys.exit(2)

ROOT = "knowledge-base"
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
URL_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*://")
EXT_RE = re.compile(r"\.(md|pdf|docx|xlsx|excalidraw|txt|vtt|ya?ml|json|csv|png|svg|pptx|zip)$", re.I)

errors = []
checked = 0


def candidates(ref, fpath):
    """Return the paths a reference could mean (bundle-relative and file-relative)."""
    ref = unquote(ref.strip())
    if not ref or URL_RE.match(ref) or ref.startswith("#"):
        return None                              # external / anchor: not our business
    if os.path.isabs(ref):
        return ["<absolute path rejected>"]
    return [
        os.path.normpath(os.path.join(ROOT, ref)),
        os.path.normpath(os.path.join(os.path.dirname(fpath), ref)),
    ]


def resolves(ref, fpath):
    cands = candidates(ref, fpath)
    if cands is None:
        return None                              # skipped
    return any(os.path.exists(c) for c in cands)


files = []
for f in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
    norm = f.replace("\\", "/")
    if norm.startswith("knowledge-base/raw-input/"):
        continue                                 # legacy corpus is frozen evidence
    files.append(f)

for f in sorted(files):
    txt = open(f, encoding="utf-8").read()
    m = FM_RE.match(txt)
    if not m:
        continue
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except Exception as e:                        # noqa: BLE001 - report and continue
        errors.append(f"BAD_YAML {f}: {e}")
        continue

    # --- sources: -----------------------------------------------------------
    for entry in (fm.get("sources") or []):
        if not isinstance(entry, str):
            errors.append(f"BAD_SOURCE_ENTRY {f}: {entry!r} (expected a path string)")
            continue
        res = resolves(entry, f)
        if res is None:
            continue
        checked += 1
        if not res:
            errors.append(f"UNRESOLVED_SOURCE {f}: sources -> {entry}")

    # --- upe.relations[].target --------------------------------------------
    upe = fm.get("upe") or {}
    for rel in (upe.get("relations") or []):
        if not isinstance(rel, dict):
            continue
        target = rel.get("target")
        if not isinstance(target, str) or not target:
            continue
        if EXT_RE.search(target):
            res = resolves(target, f)
        else:
            # concept path-as-ID: bundle-relative, extension added
            res = resolves(target + ".md", f)
        if res is None:
            continue
        checked += 1
        if not res:
            errors.append(f"UNRESOLVED_RELATION {f}: {rel.get('type')} -> {target}")

if errors:
    print(f"check_sources: {len(errors)} issue(s) ({checked} provenance references checked)")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print(f"check_sources: OK ({checked} provenance references resolved across {len(files)} files)")
sys.exit(0)
