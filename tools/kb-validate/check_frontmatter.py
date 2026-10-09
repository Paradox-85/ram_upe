#!/usr/bin/env python3
# Temporary frontmatter validator (VAL6). Excludes knowledge-base/raw-input/.
# Requires `type`; every present upe.id unique; no `approved`; allowed status; lifecycle idea|draft for new.
import os, re, sys, yaml, glob

ROOT = "knowledge-base"
RAW = "knowledge-base/raw-input/"

statuses = {"draft", "stable", "deprecated"}
lifecycles = {"idea", "draft", "in-review", "approved", "superseded", "deprecated"}

errors = []
files = []
for f in glob.glob(ROOT + "/**/*.md", recursive=True):
    norm = f.replace("\\", "/")
    if norm.startswith("knowledge-base/raw-input/"):
        continue
    files.append(f)
seen_ids = {}

for f in sorted(files):
    txt = open(f, encoding='utf-8').read()
    # extract frontmatter
    m = re.match(r'\A---\n(.*?)\n---\n', txt, re.S)
    if not m:
        errors.append(f"NO_FRONTMATTER {f}")
        continue
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except Exception as e:
        errors.append(f"BAD_YAML {f}: {e}")
        continue
    if "type" not in fm or not fm["type"]:
        errors.append(f"MISSING_TYPE {f}")
    st = fm.get("status")
    if st is None:
        errors.append(f"MISSING_STATUS {f}")
    elif st not in statuses:
        errors.append(f"BAD_STATUS {f}: {st}")
    if st == "approved":
        errors.append(f"APPROVED {f}")
    # reject "approved" anywhere obvious
    if "approved" in (fm.get("status") or ""):
        errors.append(f"APPROVED_STATUS {f}")
    upe = fm.get("upe") or {}
    uid = upe.get("id")
    if uid:
        if uid in seen_ids:
            errors.append(f"DUP_UPE_ID {uid} in {f} and {seen_ids[uid]}")
        else:
            seen_ids[uid] = f
    lc = upe.get("lifecycle")
    if lc is not None and lc not in lifecycles:
        errors.append(f"BAD_LIFECYCLE {f}: {lc}")

if not errors:
    print(f"check_frontmatter: OK ({len(files)} non-raw files)")
    sys.exit(0)
else:
    print(f"check_frontmatter: {len(errors)} issue(s)")
    for e in errors:
        print(" -", e)
    sys.exit(1)
