# Knowledge Base Deployment Guide

**How to deploy an empty KB instance (Karpathy-pattern Obsidian Wiki) in your repository.**

Date: 2026-07-28  
Audience: developer/architect who wants to add a knowledge-base to an existing project  
Source: research from the production instance at `C:\Work\Development\knowledge-base`

---

## 0. What This KB Is

A three-layer Karpathy architecture for knowledge management via Obsidian Wiki:

```
Layer 3 (Schema):    kb.config.yaml + AGENTS.md + .pi/skills/     ← rules and config
Layer 2 (Wiki):      concepts/ entities/ references/ skills/ ...   ← Obsidian vault
Layer 1 (Sources):   docs/ src/ external KB paths (env vars)       ← raw data
```

**Core principles:**
- **Compile, don't retrieve** — no RAG, no vector DBs. Knowledge is compiled into markdown once during ingestion
- **Explicit-only** — no automatic ingestion, no auto-mining of chat history
- **Provenance markers** — `^[inferred]`, `^[ambiguous]` for unconfirmed information
- **Typed relationships** — `implements`, `depends-on`, `contradicts`, `synthesizes`
- **Tiered knowledge** — `seed → seedling → evergreen → retired`
- **Confidence model** — `certain | high | medium | low | speculative`

**Stack:**
- `obsidian-wiki` v2026.6.5 (MIT, Ar9av) — PyPI package, upstream framework
- `scripts/kb` — bash orchestrator (validation, status, ingestion)
- `pyyaml` — sole Python dependency (for parsing `kb.config.yaml`)
- Obsidian (optional) — for manual vault navigation

---

## 1. Where to Download

| Component | Source | Command |
|---|---|---|
| `obsidian-wiki` | [PyPI](https://pypi.org/project/obsidian-wiki/) | `pip install obsidian-wiki==2026.6.5` |
| `obsidian-wiki` (source) | [GitHub: Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) | `git clone https://github.com/Ar9av/obsidian-wiki.git` |
| `scripts/kb` | Copy from reference repository (see §3.6) | Manual |

**Note:** `obsidian-wiki` is the upstream framework. It provides skills for the Pi agent: `wiki-setup`, `wiki-ingest`, `wiki-query`, `wiki-status`, `wiki-lint`, `wiki-update`, `wiki-sync`. The KB repository itself **is not a Python project** — it is a bash-orchestrated Obsidian vault.

---

## 2. Prerequisites

### Required
| Tool | Version | Check |
|---|---|---|
| **Git** | 2.30+ | `git --version` |
| **Python** | 3.9+ | `python --version` or `py -3 --version` |
| **pip** | 21+ | `pip --version` |
| **Bash** | 4+ | `bash --version` (Windows: Git Bash, WSL, or MSYS2) |
| **pyyaml** | 5+ | `python -c "import yaml"` |

### Optional
- **Obsidian** — for manual vault browsing (https://obsidian.md)
- **QMD** — for semantic search (https://github.com/tobi/qmd)
- **PageIndex** — for long PDF ingestion (https://github.com/VectifyAI/PageIndex)

### Installing pyyaml
```bash
pip install pyyaml
# or
py -3 -m pip install pyyaml
```

---

## 3. Step-by-Step Empty KB Deployment

### 3.1 Create `.gitignore`

At the repository root:

```gitignore
# Secrets and env
.env
.env.bak-*

# KB runtime state (generated, never committed)
.kb/

# Python artifacts
__pycache__/
*.pyc

# OS
.DS_Store

# Legacy engine artifacts (pre-migration)
engine/index.db
engine/embeddings.json
engine/graph.json
.kb_state/
```

### 3.2 Create Directory Structure

```bash
mkdir -p knowledge-base
mkdir -p knowledge-base/concepts
mkdir -p knowledge-base/entities
mkdir -p knowledge-base/references
mkdir -p knowledge-base/skills
mkdir -p knowledge-base/synthesis
mkdir -p knowledge-base/journal
mkdir -p knowledge-base/projects
mkdir -p knowledge-base/modules
mkdir -p knowledge-base/backlog/forks
mkdir -p knowledge-base/sessions
mkdir -p knowledge-base/prototypes
mkdir -p .pi/skills
mkdir -p .pi/prompts
mkdir -p scripts
```

Add `.gitkeep` to empty directories so Git tracks them:

```bash
for dir in knowledge-base/concepts knowledge-base/entities knowledge-base/references \
           knowledge-base/skills knowledge-base/synthesis knowledge-base/journal \
           knowledge-base/projects knowledge-base/modules knowledge-base/backlog/forks \
           knowledge-base/sessions knowledge-base/prototypes; do
    touch "$dir/.gitkeep"
done
```

### 3.3 Create `.env.example`

Environment variable template (no real values):

```bash
# =============================================================================
# Obsidian Wiki — Environment Configuration
# Copy this to .env and set your paths
# =============================================================================

# --- Required ---
# Absolute path to your Obsidian vault (knowledge-base/ inside your repo)
OBSIDIAN_VAULT_PATH=

# --- Optional ---
# Comma-separated source directories to ingest documents from
OBSIDIAN_SOURCES_DIR=

# Wiki categories (directories created in the vault)
OBSIDIAN_CATEGORIES=concepts,entities,skills,references,synthesis,journal

# Max pages to create/update per ingest operation
OBSIDIAN_MAX_PAGES_PER_INGEST=15

# Lint schedule: daily | weekly | manual
LINT_SCHEDULE=weekly

# Internal link format for generated/updated pages
OBSIDIAN_LINK_FORMAT=wikilink

# --- Source paths (add your own KB_*_PATH entries below) ---
# Example:
# KB_MY_PROJECT_DOCS_PATH=C:/path/to/docs
# KB_MY_PROJECT_SRC_PATH=C:/path/to/src
```

### 3.4 Create `.env` (locally, DO NOT commit!)

Copy `.env.example` → `.env` and fill in:

```bash
cp .env.example .env
```

Edit `.env`, setting the absolute vault path:

```bash
OBSIDIAN_VAULT_PATH=C:/Work/Development/projects/ramboll/ram_upe/knowledge-base
```

### 3.5 Create `kb.config.yaml`

Declarative source config at the repository root:

```yaml
kb:
  version: 1
  vault_path_env: OBSIDIAN_VAULT_PATH
  default_ingest_mode: append
  staging_root: .kb/sources
  state_file: .kb/state/sources.json
  sections:
    # Add sections for your sources
    # Example local section:
    # - name: my-docs
    #   target: references/my-project/docs
    #   source_type: local
    #   location_env: KB_MY_PROJECT_DOCS_PATH
    #   delta: mtime+hash
    #   ingest_mode: append
    #   auth: {}
    #   include:
    #   - '**/*.md'
    #   - '**/*.pdf'
    #   - '**/*.txt'
    #   exclude:
    #   - '**/_draft/**'
    #   - '**/.git/**'
```

**Section fields:**

| Field | Description |
|---|---|
| `name` | Unique section name |
| `target` | Where in the vault to place compiled pages |
| `source_type` | `local` (directory) / `github` (git repo) / `sharepoint` / `cloud` |
| `location_env` | Env variable name with the source path |
| `delta` | `mtime+hash` — change detection strategy |
| `ingest_mode` | `append` (add pages) or `rebuild` (recreate all) |
| `include`/`exclude` | File glob filters |

### 3.6 Create `scripts/kb`

Bash orchestrator. **Copy** from the reference repository:

```bash
# From a working KB repository:
cp /c/Work/Development/knowledge-base/scripts/kb scripts/kb
cp /c/Work/Development/knowledge-base/scripts/kb.smoke.sh scripts/kb.smoke.sh
```

Or create manually — **408 lines** of bash + inline Python. Full code below:

<details>
<summary>scripts/kb (click to expand — 408 lines)</summary>

```bash
#!/usr/bin/env bash
# scripts/kb — thin project-scoped orchestrator for obsidian-wiki source ingestion.
# ============================================================================
# Source-side orchestrator. Does NOT reimplement ingestion and does NOT touch the
# upstream SHA-256 .manifest.json (that stays in the wiki-ingest skill).
#
# Responsibilities:
#   1. Parse kb.config.yaml.
#   2. Materialize/sync sources into .kb/sources/<section>/ (local pass-through
#      or filtered copy; remote backends = future, github/sharepoint/cloud stubs).
#   3. Apply include/exclude filters (for filtered-local + remote).
#   4. Update backend checkpoint in .kb/state/sources.json.
#   5. Rewrite ONLY the OBSIDIAN_SOURCES_DIR= line in .env (with .env.bak-<ts>).
#   6. Print changed/added/skipped/failed report + delegation instruction to
#      /wiki-ingest (append) for the actual SHA-256 file-level delta.
#
# Subcommands:
#   kb validate [--check-remote]   validate kb.config.yaml schema + env + local paths
#   kb status                       show per-section checkpoint + pending delta
#   kb ingest [section|all] [--dry-run]  materialize + rewrite .env + report
#
# Constraints:
#   - Never prints secret VALUES (only name + set/unset).
#   - Never hardcodes secrets; reads auth values from env via *_env name lookup.
#   - Forward-slash Windows paths (C:/...) everywhere incl. OBSIDIAN_SOURCES_DIR.
#   - No auto-ingest / no history mining. history-ingest skills are NEVER invoked.
# ============================================================================

set -uo pipefail

# --- locate project root (dir containing kb.config.yaml) ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
CONFIG="$PROJECT_ROOT/kb.config.yaml"
ENV_FILE="$PROJECT_ROOT/.env"

PYTHON_BIN="python"
command -v "$PYTHON_BIN" >/dev/null 2>&1 || PYTHON_BIN="py -3"

die() { echo "kb: ERROR: $*" >&2; exit 1; }

usage() {
  cat <<EOF
Usage: kb <command> [args]
  validate [--check-remote]          Validate kb.config.yaml + env + local paths.
  status                             Per-section checkpoint + pending delta.
  ingest [section|all] [--dry-run]   Materialize + rewrite OBSIDIAN_SOURCES_DIR + report.
EOF
}

# Load .env into the current shell environment (does not print values).
load_env() {
  [ -f "$ENV_FILE" ] || die ".env not found at $ENV_FILE"
  set -a
  . "$ENV_FILE"
  set +a
}

# Emit a small python snippet that loads kb.config.yaml and prints JSON of config.
cfg_json() {
  "$PYTHON_BIN" - "$CONFIG" <<'PY'
import sys, json, yaml
with open(sys.argv[1], encoding="utf-8") as f:
    d = yaml.safe_load(f)
kb = d.get("kb", {})
print(json.dumps(kb))
PY
}

# Resolve a *_env reference: echo "set"/"unset" by NAME (never the value).
auth_status() {
  local name="$1"
  local val
  eval "val=\${$name:-}"
  if [ -n "$val" ]; then echo "set"; else echo "unset"; fi
}

# Rewrite ONLY the OBSIDIAN_SOURCES_DIR= line in .env; backup first.
rewrite_sources_dir() {
  local newval="$1"
  local ts dryrun="$2"
  ts="$(date -u +%Y%m%dT%H%M%SZ)"
  if [ "$dryrun" = "1" ]; then
    echo "[dry-run] would rewrite OBSIDIAN_SOURCES_DIR= in .env (no write)"
    echo "[dry-run] proposed: OBSIDIAN_SOURCES_DIR=$newval"
    return
  fi
  [ -f "$ENV_FILE" ] || die ".env missing"
  cp "$ENV_FILE" "$ENV_FILE.bak-$ts"
  if grep -q '^OBSIDIAN_SOURCES_DIR=' "$ENV_FILE"; then
    awk -v v="$newval" '
      BEGIN{FS=OFS="="}
      /^OBSIDIAN_SOURCES_DIR=/{ $2="\"" v "\""; print; next }
      { print }
    ' "$ENV_FILE.bak-$ts" > "$ENV_FILE"
  else
    printf '\nOBSIDIAN_SOURCES_DIR="%s"\n' "$newval" >> "$ENV_FILE"
  fi
  echo "[ok] .env rewritten (backup: .env.bak-$ts)"
}

# ---- commands ----

cmd_validate() {
  local check_remote=0
  [ "${1:-}" = "--check-remote" ] && check_remote=1
  [ -f "$CONFIG" ] || die "kb.config.yaml not found at $CONFIG"
  load_env
  echo "== kb validate =="
  echo "config: $CONFIG"
  local vpe
  vpe="$("$PYTHON_BIN" - "$CONFIG" <<'PY'
import sys, yaml
d=yaml.safe_load(open(sys.argv[1],encoding="utf-8"))
print(d["kb"].get("vault_path_env","OBSIDIAN_VAULT_PATH"))
PY
)"
  echo "vault_path_env: $vpe -> $(auth_status "$vpe")"
  [ -z "$(eval echo \${$vpe:-})" ] && echo "  WARN: $vpe unset/empty"
  echo ""
  echo "sections:"
  "$PYTHON_BIN" - "$CONFIG" <<'PY'
import sys, yaml, os
d=yaml.safe_load(open(sys.argv[1],encoding="utf-8"))
for s in d["kb"]["sections"]:
    name=s["name"]; st=s["source_type"]; delta=s["delta"]
    loc_env = s.get("location_env")
    loc = os.environ.get(loc_env, "").replace("\\", "/") if loc_env else s.get("location")
    auths=s.get("auth",{}) or {}
    req=["name","target","source_type","delta","ingest_mode"]
    missing=[k for k in req if k not in s]
    line_parts = [f"  - {name}: type={st} delta={delta}"]
    if loc_env:
        resolved = f"{loc_env}={loc}" if loc else f"{loc_env}=(UNSET/EMPTY)"
        line_parts.append(resolved)
    line = " ".join(line_parts)
    if st=="local" and isinstance(loc,str) and loc:
        line+=f" path-exists={'YES' if os.path.isdir(loc) else 'NO'}"
    if st=="local" and (not loc or not isinstance(loc,str)):
        line+=f" path-exists=ERROR: no resolved path"
    if missing:
        print(f"    ERROR: missing keys {missing}")
    for k,v in auths.items():
        print(f"    auth {k}={v}")
    print(line)
PY
  if [ "$check_remote" = "1" ]; then
    echo ""
    echo "remote check (--check-remote):"
    "$PYTHON_BIN" - "$CONFIG" <<'PY'
import sys, yaml, subprocess, os
d=yaml.safe_load(open(sys.argv[1],encoding="utf-8"))
for s in d["kb"]["sections"]:
    if s["source_type"]=="github" and isinstance(s["location"],str) and s["location"].startswith("gh:"):
        spec=s["location"][3:].split("@",1)[0].split(":",1)[0]
        tok=os.environ.get(s.get("auth",{}).get("token_env","GH_TOKEN"),"")
        print(f"  github {s['name']}: git ls-remote https://github.com/{spec}")
        try:
            out=subprocess.run(["git","ls-remote","--heads",f"https://github.com/{spec}"],
                               capture_output=True,text=True,timeout=15,
                               env={**os.environ, "GIT_TERMINAL_PROMPT":"0"})
            heads=[l.split("\t")[1] for l in out.stdout.splitlines() if l][:3]
            print(f"    heads (first 3): {heads if heads else '(none / auth required)'}")
        except Exception as e:
            print(f"    ERROR: {e}")
PY
  fi
  echo ""
  echo "validate: DONE"
}

cmd_status() {
  [ -f "$CONFIG" ] || die "kb.config.yaml not found"
  load_env
  local state="$PROJECT_ROOT/.kb/state/sources.json"
  echo "== kb status =="
  "$PYTHON_BIN" - "$CONFIG" "$state" <<'PY'
import sys, yaml, json, os, datetime
cfg=yaml.safe_load(open(sys.argv[1],encoding="utf-8"))
state_path=sys.argv[2]
state={}
if os.path.exists(state_path):
    try: state=json.load(open(state_path,encoding="utf-8")).get("sources",{})
    except Exception: pass
def norm(p):
    return (os.path.normpath(p).replace("\\","/").lower()) if (isinstance(p,str) and p) else ""
vault=os.environ.get("OBSIDIAN_VAULT_PATH","")
manifest_keys={}
manifest_mtime=None
cands = ([os.path.join(vault,".manifest.json")] if vault else []) + [".manifest.json"]
for cand in cands:
    if os.path.exists(cand):
        try:
            m=json.load(open(cand,encoding="utf-8"))
            entries = m.get("sources", m.get("files", m)) if isinstance(m,dict) else m
            if isinstance(entries,dict): manifest_keys={norm(k):1 for k in entries.keys()}
            elif isinstance(entries,list): manifest_keys={norm(k):1 for k in entries}
            manifest_mtime=os.path.getmtime(cand)
        except Exception:
            pass
        break
def ingested(staged):
    if not manifest_keys or not staged: return None
    ns=norm(staged)
    return sum(1 for k in manifest_keys if k.startswith(ns))
print("%-16s %-9s %-13s %-12s %-9s %s" % ("section","type","status","checkpoint","ingested","staged/last_sync"))
print("-"*92)
for s in cfg["kb"]["sections"]:
    n=s["name"]; st=s["source_type"]; e=state.get(n,{})
    loc_env = s.get("location_env")
    loc_env_resolved = os.environ.get(loc_env, "").replace("\\", "/") if loc_env else None
    staged=e.get("staged_path") or (loc_env_resolved if loc_env_resolved else (s.get("location") if isinstance(s.get("location"),str) else ""))
    cp=e.get("checkpoint")
    cps=(cp[:10]+"...") if cp else "-"
    ing=ingested(staged); ings=(str(ing) if ing is not None else "-")
    print("%-16s %-9s %-13s %-12s %-9s %s" % (n,st,e.get("status","never-synced"),cps,ings,staged or "(remote)"))
print("-"*92)
if manifest_mtime:
    print("manifest: %d file(s) tracked, updated %s (vault manifest)" % (len(manifest_keys), datetime.datetime.fromtimestamp(manifest_mtime).strftime("%Y-%m-%d %H:%M")))
else:
    print("manifest: not yet created - run /wiki-ingest to populate the SHA-256 delta manifest")
PY
}

cmd_ingest() {
  local target="${1:-all}"
  local dryrun=0
  [ "${2:-}" = "--dry-run" ] && dryrun=1
  [ -f "$CONFIG" ] || die "kb.config.yaml not found"
  load_env
  echo "== kb ingest ${target} $( [ $dryrun -eq 1 ] && echo '[dry-run]' ) =="
  mkdir -p "$PROJECT_ROOT/.kb/sources" "$PROJECT_ROOT/.kb/state" "$PROJECT_ROOT/.kb/logs"

  local out
  out="$(DRYRUN="$dryrun" "$PYTHON_BIN" - "$CONFIG" "$target" "$PROJECT_ROOT/.kb/state/sources.json" "$PROJECT_ROOT/.kb/sources" <<'PY'
import sys, os, json, datetime, subprocess, shutil
import yaml
cfg_path, target, state_path, sources_dir = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
dryrun = os.environ.get("DRYRUN", "0") == "1"
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
cfg = yaml.safe_load(open(cfg_path, encoding="utf-8"))
sections = cfg["kb"]["sections"]
if target != "all":
    sections = [s for s in sections if s["name"] == target]
    if not sections:
        print("ERROR: no such section:", target, file=sys.stderr); sys.exit(2)
state = {"version": 1, "updated_at": now, "sources": {}}
if os.path.exists(state_path):
    try: state = json.load(open(state_path, encoding="utf-8"))
    except Exception: pass
if "sources" not in state: state["sources"] = {}
paths = []
def materialize_github(name, location, staged_dir, token, dryrun):
    spec = location[3:] if location.startswith("gh:") else location
    ref = None
    path = ""
    if "@" in spec:
        repo_part, rest = spec.split("@", 1)
        if ":" in rest:
            ref, path = rest.split(":", 1)
        else:
            ref = rest
    else:
        if ":" in spec:
            repo_part, path = spec.split(":", 1)
        else:
            repo_part = spec
    repo_part = repo_part.strip("/")
    pub_url = "https://github.com/" + repo_part
    auth_url = ("https://x-access-token:" + token + "@github.com/" + repo_part) if token else pub_url
    target = os.path.abspath(os.path.join(staged_dir, name))
    staged_subdir = os.path.join(target, path) if path else target
    def sanitize(s):
        return (s.replace(token, "***") if (token and s) else (s or ""))
    def run(cmd, cwd=None, timeout=60):
        env = dict(os.environ); env["GIT_TERMINAL_PROMPT"]="0"; env["GIT_LFS_SKIP_SMUDGE"]="1"
        return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, env=env, timeout=timeout)
    try:
        rr = run(["git","ls-remote", auth_url if token else pub_url, ref if ref else "HEAD"])
        if rr.returncode != 0 or not rr.stdout.strip():
            return False, "", None, "ls-remote failed: " + sanitize(rr.stderr)[:200]
        cur = rr.stdout.split()[0]
    except subprocess.TimeoutExpired:
        return False, "", None, "ls-remote timed out"
    except Exception as e:
        return False, "", None, "ls-remote error: " + str(e)
    cpfile = os.path.join(target, ".kb_commit")
    prev_cp = None
    if os.path.isfile(cpfile):
        try: prev_cp = open(cpfile, encoding="utf-8").read().strip()
        except Exception: prev_cp = None
    if prev_cp == cur and os.path.isdir(staged_subdir):
        return True, staged_subdir, cur, None
    if dryrun:
        return True, staged_subdir, cur, None
    if os.path.isdir(target):
        shutil.rmtree(target, ignore_errors=True)
    os.makedirs(os.path.dirname(target), exist_ok=True)
    genv = dict(os.environ); genv["GIT_TERMINAL_PROMPT"]="0"; genv["GIT_LFS_SKIP_SMUDGE"]="1"
    if subprocess.run(["git","init","--quiet",target], capture_output=True, text=True, env=genv).returncode != 0:
        return False, "", None, "git init failed"
    if subprocess.run(["git","remote","add","origin",auth_url], cwd=target, capture_output=True, text=True, env=genv).returncode != 0:
        return False, "", None, "git remote add failed"
    if path:
        subprocess.run(["git","sparse-checkout","init","--cone","--quiet"], cwd=target, capture_output=True, text=True, env=genv)
        subprocess.run(["git","sparse-checkout","set",path], cwd=target, capture_output=True, text=True, env=genv)
    fr = subprocess.run(["git","fetch","--depth=1","--quiet","--filter=blob:none","origin", ref if ref else "HEAD"], cwd=target, capture_output=True, text=True, env=genv, timeout=180)
    if fr.returncode != 0:
        return False, "", None, "git fetch failed: " + sanitize(fr.stderr)[:200]
    if subprocess.run(["git","checkout","--quiet","FETCH_HEAD"], cwd=target, capture_output=True, text=True, env=genv).returncode != 0:
        return False, "", None, "git checkout failed"
    subprocess.run(["git","remote","set-url","origin",pub_url], cwd=target, capture_output=True, text=True, env=genv)
    try: open(cpfile,"w",encoding="utf-8").write(cur)
    except Exception: pass
    if not os.path.exists(staged_subdir):
        return False, "", cur, "path '" + str(path) + "' not found in repo"
    return True, staged_subdir, cur, None
ok = 0
for s in sections:
    name = s["name"]; st = s["source_type"]
    loc_env = s.get("location_env")
    loc = os.environ.get(loc_env, "").replace("\\", "/") if loc_env else s.get("location")
    if st == "local" and isinstance(loc, str):
        if os.path.isdir(loc):
            print(f"  [ok] {name}: local staged={loc}")
            paths.append(loc)
            if not dryrun:
                state["sources"][name] = {"type":"local","staged_path":loc,"last_sync_at":now,"checkpoint":None,"status":"ok","last_error":None}
            ok += 1
        else:
            print(f"  [FAIL] {name}: source dir not found: {loc}")
            if not dryrun:
                state["sources"][name] = {"type":"local","staged_path":loc,"last_sync_at":now,"checkpoint":None,"status":"failed","last_error":"source dir not found"}
    elif st == "github":
        sp_env = (s.get("auth") or {}).get("token_env")
        token = os.environ.get(sp_env) if sp_env else None
        g_ok, g_path, g_cp, g_err = materialize_github(name, loc, sources_dir, token, dryrun)
        if g_ok:
            if g_path: g_path = g_path.replace("\\", "/")
            cph = (g_cp[:10] + "...") if g_cp else "?"
            print("  [ok] " + name + ": github staged=" + g_path + " (commit " + cph + ")")
            paths.append(g_path)
            if not dryrun:
                state["sources"][name] = {"type":"github","staged_path":g_path,"last_sync_at":now,"checkpoint":g_cp,"status":"ok","last_error":None}
            ok += 1
        else:
            print("  [FAIL] " + name + ": github " + str(g_err))
            if not dryrun:
                state["sources"][name] = {"type":"github","staged_path":"","last_sync_at":now,"checkpoint":None,"status":"failed","last_error":str(g_err)}
    elif st in ("sharepoint", "cloud"):
        print("  [skip] " + name + ": " + st + " backend not yet implemented")
        if not dryrun:
            state["sources"][name] = {"type":st,"staged_path":"","last_sync_at":now,"checkpoint":None,"status":"failed","last_error":"backend not implemented"}
    else:
        print(f"  [FAIL] {name}: unknown source_type={st}")
        if not dryrun:
            state["sources"][name] = {"type":str(st),"staged_path":"","last_sync_at":now,"checkpoint":None,"status":"failed","last_error":"unknown source_type"}
if not dryrun:
    state["updated_at"] = now
    os.makedirs(os.path.dirname(state_path), exist_ok=True)
    json.dump(state, open(state_path, "w", encoding="utf-8"), indent=2)
print(f"report: {ok} section(s) materialized")
print("NEWPATHS=" + ",".join(paths))
PY
)"
  out="${out%$'\r'}"
  local newpaths
  newpaths="$(printf '%s\n' "$out" | tail -1)"
  newpaths="${newpaths#NEWPATHS=}"
  newpaths="${newpaths%$'\r'}"
  printf '%s\n' "$out" | sed '$d'

  if [ "$dryrun" = "1" ]; then
    echo "[dry-run] no .env rewrite, no delegation"
    echo "[dry-run] proposed OBSIDIAN_SOURCES_DIR=$newpaths"
    return
  fi
  if [ -n "$newpaths" ]; then
    rewrite_sources_dir "$newpaths" "0"
    echo ""
    echo ">> NEXT: run /wiki-ingest (append mode) — OBSIDIAN_SOURCES_DIR is updated;"
    echo "         SHA-256 .manifest.json delta applies automatically (upstream skill)."
  else
    echo "[warn] no local paths materialized; .env left unchanged"
  fi
}

# ---- dispatch ----
[ $# -eq 0 ] && { usage; exit 1; }
case "$1" in
  validate) shift; cmd_validate "$@" ;;
  status)   cmd_status ;;
  ingest)   shift; cmd_ingest "$@" ;;
  -h|--help|help) usage ;;
  *) echo "kb: unknown command: $1" >&2; usage; exit 1 ;;
esac
```

</details>

### 3.7 Install `obsidian-wiki`

```bash
pip install obsidian-wiki==2026.6.5
```

Verify:
```bash
python -c "import obsidian_wiki; print(obsidian_wiki.__version__)"
# or
pip show obsidian-wiki
```

**Important:** do NOT run `obsidian-wiki setup` for this KB — it would create global skill installations. Use `scripts/kb` instead.

### 3.8 Create Obsidian Vault Config

`knowledge-base/.obsidian/app.json`:
```json
{
  "strictLineBreaks": false,
  "showFrontmatter": false,
  "defaultViewMode": "preview",
  "livePreview": true
}
```

`knowledge-base/.obsidian/appearance.json`:
```json
{
  "baseFontSize": 16
}
```

### 3.9 Create `AGENTS.md` at Repository Root

Agent instruction file for Pi agents. Adapt to your project:

```markdown
---
---

# <Project Name> — Obsidian Wiki Routing

This project is an Obsidian Wiki based on the Karpathy pattern (three-layer architecture: sources → wiki → schema). The agent is the primary maintainer; there is no local Python engine in this repository.

---

## Repo Structure

| Element | Description |
|---|---|
| `scripts/kb` | Bash orchestrator: config validation, checkpoint status, source materialization. The single entry point for source operations. |
| `kb.config.yaml` | Declarative source section config. |
| `.env` | GITIGNORED — real values. |
| `.env.example` | Template for `.env` — all values empty. |
| `.pi/skills/` | Active project-scoped Pi skills for this repository. |
| `.kb/` | Orchestrator internal state. Generated by `scripts/kb`, do not edit manually. |
| `.gitignore` | Ignores `.env`, `.kb/`, `__pycache__/`, and standard artifacts. |

---

## Stack

- **Package:** `obsidian-wiki` v2026.6.5 (MIT, Ar9av, PyPI)
- **Languages:** Python (pyyaml) + bash (orchestration via `scripts/kb`)
- **VCS:** Git
- **No RAG:** vector DBs, embeddings, semantic search are not used.

---

## Core Idea (Why Not RAG)

1. **Compile, don't retrieve** — knowledge is compiled into markdown once during ingestion.
2. **Provenance markers** — `^[inferred]`, `^[ambiguous]`.
3. **Typed relationships** — `implements`, `depends-on`, `contradicts`, `synthesizes`.
4. **Tiered knowledge** — `seed → seedling → evergreen → retired`.
5. **Confidence model** — `certain | high | medium | low | speculative`.
6. **Cost hierarchy** — `index.md` → frontmatter summary → `grep` → full read.
7. **Persistent manifest** — SHA-256 `.manifest.json`.

---

## Three-Layer Architecture

```
Layer 3: Schema     → kb.config.yaml, AGENTS.md, .pi/skills/
Layer 2: Wiki       → concepts/, entities/, references/, skills/, synthesis/, journal/
Layer 1: Sources    → external directories (KB_*_PATH env vars)
```

---

## Workflow

```
validate → status → ingest → /wiki-ingest (append)
```

All steps are **explicit-only** — no hooks, no auto-mining.

1. `kb validate` — validate config and env.
2. `kb status` — checkpoint state.
3. `kb ingest [section|all] [--dry-run]` — materialize sources.
4. `/wiki-ingest (append)` — SHA-256 delta (run manually via agent).

---

## Project Conventions

- Default prose language: **Russian**; commands, paths, hostnames, env vars, ports: **English**.
- Forward-slash Windows paths everywhere.
- Workflow: `scripts/kb validate` → `scripts/kb status` → `scripts/kb ingest [section|all] [--dry-run]`, then `/wiki-ingest` (append).
- Do NOT run `obsidian-wiki setup` — use `scripts/kb`.

---

## Skill Routing

- Setup/init vault: `wiki-setup`
- Ingest source documents: `wiki-ingest` (append mode)
- Query compiled vault knowledge: `wiki-query`
- Sync current project knowledge: `wiki-update`
- Audit/status/maintenance: `wiki-status`, `wiki-lint`

---

## Links

- Upstream: [github.com/Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki)
- PyPI: [pypi.org/project/obsidian-wiki](https://pypi.org/project/obsidian-wiki/)
```

### 3.10 Create `.manifest.json` (empty)

At the vault root (`knowledge-base/.manifest.json`):

```json
{
  "version": 1,
  "stats": {
    "total_sources_ingested": 0,
    "total_pages": 0
  },
  "sources": {}
}
```

---

## 4. Validation

After creating all files:

```bash
# 1. Check structure
ls knowledge-base/
ls scripts/
ls .pi/skills/
ls .pi/prompts/

# 2. Validate config
bash scripts/kb validate

# 3. Status (will show empty sections — this is normal)
bash scripts/kb status

# 4. Check .gitignore
git status --short --ignored
# Should show .env and .kb/ as ignored

# 5. Check Python dependencies
python -c "import yaml; print('pyyaml OK')"
pip show obsidian-wiki
```

---

## 5. How to Add Your First Source

### 5.1 Add a Section to `kb.config.yaml`

```yaml
  - name: my-project-docs
    target: references/my-project
    source_type: local
    location_env: KB_MY_PROJECT_PATH
    delta: mtime+hash
    ingest_mode: append
    auth: {}
    include:
    - '**/*.md'
    - '**/*.pdf'
    exclude:
    - '**/_draft/**'
    - '**/.git/**'
```

### 5.2 Add the Path to `.env`

```bash
KB_MY_PROJECT_PATH=C:/path/to/your/source/documents
```

### 5.3 Run Ingestion

```bash
# Dry-run — preview what will happen
bash scripts/kb ingest my-project-docs --dry-run

# Real ingestion
bash scripts/kb ingest my-project-docs

# Then via Pi agent:
# /wiki-ingest (append)
```

---

## 6. Working Cycle

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│ Added        │     │ scripts/kb   │     │ /wiki-ingest │
│ documents    │────▶│ ingest       │────▶│ (append)     │
│ to source    │     │ (dry-run     │     │ via Pi       │
│              │     │  → real)     │     │ agent        │
└─────────────┘     └──────────────┘     └─────────────┘
```

---

## 7. Troubleshooting

| Problem | Solution |
|---|---|
| `kb: ERROR: kb.config.yaml not found` | Run from repository root |
| `kb: ERROR: .env not found` | `cp .env.example .env` and fill in `OBSIDIAN_VAULT_PATH` |
| `ModuleNotFoundError: No module named 'yaml'` | `pip install pyyaml` |
| `python: command not found` | Script fallbacks to `py -3`; or add Python to PATH |
| `obsidian-wiki not found` | `pip install obsidian-wiki==2026.6.5` |
| `WARN: OBSIDIAN_VAULT_PATH unset/empty` | Set absolute path in `.env` |
| `path-exists=NO` | Verify the path in the env variable exists and is accessible |
| Git Bash won't run `.sh` | `bash scripts/kb validate` (explicitly via bash) |

---

## 8. Final Checklist

- [ ] `.gitignore` — `.env`, `.kb/`, Python artifacts
- [ ] Directories: `knowledge-base/concepts/`, `entities/`, `references/`, `skills/`, `synthesis/`, `journal/`, `projects/`, `modules/`
- [ ] `.env.example` — template with no secrets
- [ ] `.env` — local only, `OBSIDIAN_VAULT_PATH` set
- [ ] `kb.config.yaml` — at least one section (or empty `sections: []`)
- [ ] `scripts/kb` — orchestrator (408 lines, copied)
- [ ] `obsidian-wiki==2026.6.5` — `pip install` + verified
- [ ] `pyyaml` — `pip install` + verified
- [ ] `knowledge-base/.obsidian/app.json` + `appearance.json`
- [ ] `AGENTS.md` — agent instructions
- [ ] `.pi/skills/` — project-scoped Pi skills
- [ ] `.manifest.json` — empty manifest
- [ ] `bash scripts/kb validate` — passes
- [ ] `bash scripts/kb status` — shows state
- [ ] `git status --ignored` — `.env` and `.kb/` are ignored
