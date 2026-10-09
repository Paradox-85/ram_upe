#!/usr/bin/env python3
"""Create or update the Azure DevOps code-wiki mapping for this repository.

Documented REST contract (api-version 7.1):
    GET   {org}/{project}/_apis/wiki/wikis
    POST  {org}/{project}/_apis/wiki/wikis            -> create a code wiki
    PATCH {org}/{project}/_apis/wiki/wikis/{id}       -> change the mapped path

This script is a **convenience, not the authoritative path** — the UI steps in
tools/wiki/README.md are authoritative, and this code has not been run against the live
organisation. It defaults to `--dry-run` and prints the exact request it would send.

    export AZURE_DEVOPS_EXT_PAT=<PAT with "Wiki (Read & Write)">
    python tools/wiki/setup_wiki.py --project UPE --dry-run
    python tools/wiki/setup_wiki.py --project UPE --apply

The project name is required: it is not present in the repository URL and must not be guessed.
"""
import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
API = "7.1"


def load_config():
    with open(os.path.join(HERE, "wiki.config.json"), encoding="utf8") as fh:
        return json.load(fh)


def org_from_repo_url(repo_web_url):
    """https://dev.azure.com/<org>/_git/<repo>  ->  ('<org>', '<repo>')"""
    parts = [p for p in repo_web_url.split("/") if p]
    try:
        i = parts.index("_git")
        return "/".join(parts[2:i]), parts[i + 1]
    except (ValueError, IndexError):
        return "", ""


def request(method, url, pat, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Content-Type", "application/json")
    if pat:
        req.add_header("Authorization",
                       "Basic " + base64.b64encode((":" + pat).encode()).decode())
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = resp.read().decode("utf8")
        return resp.status, (json.loads(payload) if payload.strip() else {})


def main():
    cfg = load_config()
    org_default, repo_default = org_from_repo_url(cfg["repo_web_url"])

    ap = argparse.ArgumentParser()
    ap.add_argument("--org", default=org_default, help=f"Azure DevOps organisation (default: {org_default})")
    ap.add_argument("--project", required=True, help="project name (not visible in the repo URL)")
    ap.add_argument("--repo", default=repo_default, help=f"repository name (default: {repo_default})")
    ap.add_argument("--name", default=cfg["wiki_name"])
    ap.add_argument("--path", default=cfg["wiki_path"])
    ap.add_argument("--branch", default=cfg["branch"])
    ap.add_argument("--pat-env", default="AZURE_DEVOPS_EXT_PAT")
    ap.add_argument("--apply", action="store_true", help="perform the call (default: dry run)")
    args = ap.parse_args()

    base = f"https://dev.azure.com/{args.org}/{args.project}/_apis/wiki/wikis"
    list_url = f"{base}?api-version={API}"

    print(f"organisation : {args.org}")
    print(f"project      : {args.project}")
    print(f"repository   : {args.repo}")
    print(f"wiki name    : {args.name}")
    print(f"mapped path  : {args.path}  (branch {args.branch})")
    print()

    if args.path != "/knowledge-base":
        print(f"note: this repository's wiki path is /knowledge-base per tools/wiki/wiki.config.json; "
              f"you passed {args.path}")

    if not args.apply:
        print("DRY RUN — no request sent. It would:")
        print(f"  1. GET   {list_url}")
        print(f"  2. POST  {list_url}   (if no wiki named '{args.name}' exists)")
        print(json.dumps({"name": args.name, "projectId": "<project-id>", "repositoryId": args.repo,
                          "mappedPath": args.path, "type": "codeWiki"}, indent=6))
        print(f"     or PATCH {base}/<wiki-id>?api-version={API}")
        print(json.dumps({"mappedPath": args.path}, indent=6))
        print("\nManual equivalent: see tools/wiki/README.md (Overview → Wiki → Publish code as wiki).")
        return 0

    pat = os.environ.get(args.pat_env, "")
    if not pat:
        print(f"error: set {args.pat_env} to a PAT with the 'Wiki (Read & Write)' scope")
        return 2

    try:
        status, listing = request("GET", list_url, pat)
        existing = next((w for w in listing.get("value", []) if w.get("name") == args.name), None)
        if existing:
            wid = existing.get("id")
            print(f"found existing wiki '{args.name}' (id {wid}); updating mappedPath")
            status, out = request("PATCH", f"{base}/{wid}?api-version={API}", pat,
                                  {"mappedPath": args.path})
        else:
            print("no wiki with that name; creating a code wiki")
            status, out = request("POST", list_url, pat,
                                  {"name": args.name, "repositoryId": args.repo,
                                   "mappedPath": args.path, "type": "codeWiki"})
        print(f"HTTP {status}")
        print(json.dumps({k: v for k, v in out.items() if k in
                          ("id", "name", "mappedPath", "type", "remoteUrl", "url")}, indent=2))
        return 0
    except urllib.error.HTTPError as exc:
        print(f"HTTP {exc.code}: {exc.read().decode('utf8', 'replace')[:500]}")
        return 1
    except urllib.error.URLError as exc:
        print(f"network error: {exc.reason}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
