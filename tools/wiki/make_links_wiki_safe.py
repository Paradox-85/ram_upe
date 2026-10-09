#!/usr/bin/env python3
"""Make Markdown links inside `knowledge-base/` safe for the Azure DevOps Code Wiki.

Why this exists
---------------
The Code Wiki publishes only `knowledge-base/` (config: tools/wiki/wiki.config.json). Azure DevOps
does **not** navigate relative links that point outside the published folder: clicking
`../../sources/...` from a wiki page tries to serve that path from the wiki root and fails or
downloads the file. Links that stay inside `knowledge-base/` are correct and are left alone.

So: out-of-published-folder links become absolute repository web URLs; in-KB links stay relative.

Scope
-----
* Only **Markdown link targets** `](...)` in body text are touched.
* Frontmatter (`sources:`, `upe.relations[].target`) is the machine-facing provenance surface and is
  deliberately left repo-relative — it is validated by tools/kb-validate/check_sources.py.
* Idempotent; `--revert` restores relative links.

Usage
-----
    python tools/wiki/make_links_wiki_safe.py            # convert (dry-run unless --apply)
    python tools/wiki/make_links_wiki_safe.py --apply
    python tools/wiki/make_links_wiki_safe.py --revert --apply
"""
import argparse
import glob
import json
import os
import re
import sys
from urllib.parse import quote, unquote

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
PUBLISHED = "knowledge-base"
LINK_RE = re.compile(r"\]\(([^)\s]+)(\s+\"[^\"]*\")?\)")


def load_config():
    with open(os.path.join(HERE, "wiki.config.json"), encoding="utf8") as fh:
        return json.load(fh)


def is_external(target):
    return bool(re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", target)) or target.startswith("#") \
        or target.startswith("mailto:")


def escapes_published(resolved_repo_rel):
    return not (resolved_repo_rel == PUBLISHED or resolved_repo_rel.startswith(PUBLISHED + "/"))


def to_url(repo_rel, cfg):
    return f"{cfg['repo_web_url']}?path={quote('/' + repo_rel)}&version=GB{cfg['branch']}"

def from_url_spellings(cfg):
    """Return a matcher for URLs produced by to_url (branch and version are optional)."""
    base = re.escape(cfg["repo_web_url"])
    return re.compile(base + r"\?path=/([^&\s]+)(?:&version=GB[\w./-]+)?")


def convert(text, fp, cfg, revert=False):
    repo_rel_dir = os.path.relpath(os.path.dirname(fp), REPO).replace(os.sep, "/")
    changed = []

    def repl(m):
        target, title = m.group(1), m.group(2) or ""
        if revert:
            mu = from_url_spellings(cfg).fullmatch(target)
            if not mu:
                return m.group(0)
            dest = unquote(mu.group(1))
            rel = os.path.relpath(os.path.join(REPO, dest.replace("/", os.sep)),
                                  os.path.join(REPO, repo_rel_dir.replace("/", os.sep)))
            rel = rel.replace(os.sep, "/").replace(" ", "%20")
            changed.append((target, rel))
            return f"]({rel}{title})"
        if is_external(target):
            return m.group(0)
        resolved = os.path.normpath(os.path.join(repo_rel_dir, unquote(target).split("#")[0])).replace(os.sep, "/")
        if not escapes_published(resolved):
            return m.group(0)                      # inside the wiki: leave relative
        url = to_url(resolved, cfg)
        changed.append((target, url))
        return f"]({url}{title})"

    return LINK_RE.sub(repl, text), changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    ap.add_argument("--revert", action="store_true", help="restore relative links")
    args = ap.parse_args()
    cfg = load_config()

    files_touched = links = 0
    for fp in sorted(glob.glob(os.path.join(REPO, PUBLISHED, "**", "*.md"), recursive=True)):
        txt = open(fp, encoding="utf8").read()
        new, changed = convert(txt, fp, cfg, revert=args.revert)
        if not changed:
            continue
        files_touched += 1
        links += len(changed)
        rel = os.path.relpath(fp, REPO).replace(os.sep, "/")
        if args.apply:
            with open(fp, "w", encoding="utf8", newline="") as fh:
                fh.write(new)
            print(f"{'reverted' if args.revert else 'converted'} {len(changed):3d} link(s)  {rel}")
        else:
            print(f"WOULD {'revert' if args.revert else 'convert'} {len(changed):3d}  {rel}")
            for old, newt in changed[:2]:
                print(f"      {old[:70]}\n   -> {newt[:100]}")

    verb = "reverted" if args.revert else "converted"
    print(f"\n{'(dry run) ' if not args.apply else ''}{files_touched} file(s), {links} link(s) "
          f"{verb if args.apply else 'to ' + verb}")
    if not args.apply:
        print("re-run with --apply to write")
    return 0


if __name__ == "__main__":
    sys.exit(main())
