#!/usr/bin/env python3
# Temporary internal-link validator (VAL5). Walks knowledge-base/ excluding raw-input/.
# Validates bundle-relative / local Markdown link targets; ignores URLs and anchors.
import os, re, sys, glob

ROOT = "knowledge-base"
RAW = os.path.join(ROOT, "raw-input")

LINK_RE = re.compile(r'\[[^\]]*\]\(([^)]+)\)')

def resolve(base_dir, target):
    # strip url
    if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*://', target):
        return None  # external url - ignore
    if target.startswith('#'):
        return None  # anchor - ignore
    # decode URL-encoded chars (e.g. %20) for filesystem resolution
    from urllib.parse import unquote
    target = unquote(target)
    # strip anchor fragment (after decode to handle #-in-name edge cases minimally)
    target = target.split('#')[0]
    if not target:
        return None
    path = os.path.normpath(os.path.join(base_dir, target))
    return path

errors = []
checked = 0
for f in sorted(glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)):
    if f.replace("\\", "/").startswith("knowledge-base/raw-input/"):
        continue
    base_dir = os.path.dirname(f)
    txt = open(f, encoding='utf-8').read()
    for m in LINK_RE.finditer(txt):
        target = m.group(1).strip()
        if '\n' in target or ' ' in target.replace('%20', ' '):
            pass
        path = resolve(base_dir, target)
        if path is None:
            continue
        checked += 1
        if not os.path.exists(path):
            errors.append(f"{f}: broken link -> {target}")

if errors:
    print(f"check_links: {len(errors)} broken link(s)")
    for e in errors:
        print(" -", e)
    sys.exit(1)
else:
    print(f"check_links: OK ({checked} internal links validated)")
    sys.exit(0)
