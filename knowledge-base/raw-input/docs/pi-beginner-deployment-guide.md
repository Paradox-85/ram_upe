
# Pi Coding Agent Deployment Guide for Windows

**Purpose:** Reproduce the anonymized multi-profile Pi coding-agent setup described in the attached deployment report and context files, starting from a clean Windows PC.  
**Audience:** A beginner who can use PowerShell or Windows Terminal but has not yet installed Pi.  
**Date:** 2026-07-22  
**Scope:** Windows-first setup, with notes for Linux/macOS only where useful.  
**Secret policy:** This guide never includes real API keys, OAuth tokens, private hostnames, raw IP addresses, private SSH material, or full connection strings.

---

## 0. What This Guide Builds

By the end, you will have a Pi setup with:

- the global `pi` command from `@earendil-works/pi-coding-agent`;
- a default online profile using an authenticated online provider such as `openai-codex`;
- an optional local profile using a local OpenAI-compatible model provider such as `local-qwen`;
- the same class of Pi packages described in the attached deployment context: web access, MCP bridge, hashline editing, Context7 docs lookup, LSP code intelligence, subagents, usage tracking, PostgreSQL skill, and RTK output optimization;
- reusable global instructions in `AGENTS.md`;
- local skills such as `infra-context`, `llm-switcher`, `slidev`, and a presentation-design skill;
- custom prompt templates for multi-agent planning, implementation, review, and handoff workflows;
- a repeatable validation checklist to prove the installation works.

This guide combines two sources of truth:

1. **The attached anonymized deployment context and report**, which describe the target setup, versions, packages, skills, prompts, profiles, and orchestration rules.
2. **The official Pi repository and documentation**, especially Quickstart, Providers, Models, Skills, Packages, Settings, Usage, and the package pages for the installed extensions.

Where the local deployment context and official docs differ, this guide separates:

- **Target setup facts**: what was observed in the attached deployment.
- **Official installation method**: what the Pi documentation says to do now.
- **Reasonable template**: a safe example you can adapt without copying secrets.

---

## 1. Safety and Redaction Rules

Never paste real secrets into documentation, chats, screenshots, commits, or shared prompts.

### 1.1 Redacted placeholders used in this guide

| Placeholder | Meaning |
|---|---|
| `<USER_HOME>` | Your Windows home directory, for example `C:\Users\<USERNAME>` |
| `<USERNAME>` | Your Windows username |
| `<PI_AGENT_HOME>` | `<USER_HOME>\.pi\agent` |
| `<ROAMING_NPM>` | `<USER_HOME>\AppData\Roaming\npm` |
| `<PI_AGENT_NPM>` | `<PI_AGENT_HOME>\npm` |
| `<PI_AGENT_GIT>` | `<PI_AGENT_HOME>\git` |
| `<PI_AGENT_SKILLS>` | `<PI_AGENT_HOME>\skills` |
| `<PI_AGENT_PROMPTS>` | `<PI_AGENT_HOME>\prompts` |
| `<PI_AGENT_EXTENSIONS>` | `<PI_AGENT_HOME>\extensions` |
| `<INFRA_KB>` | Your private infrastructure knowledge-base path |
| `<LLM_CONTAINER>` | Your local machine, VM, container, or server running local LLMs |
| `<PROXMOX_HOST>` | Your private virtualization host, if used |
| `<POSTGRES_HOST>` | Your PostgreSQL host |
| `[REDACTED]` | Any secret or private identifier removed intentionally |

### 1.2 Files you must not publish

Do **not** publish these files unless you have scrubbed them:

```text
<PI_AGENT_HOME>/auth.json
<PI_AGENT_HOME>/mcp.json
<PI_AGENT_HOME>/trust.json
<PI_AGENT_HOME>/models.json       # may contain local endpoints, headers, or dummy keys
<PI_AGENT_HOME>/models-store.json # may contain provider cache information
<PI_AGENT_HOME>/sessions/         # contains conversation history and tool outputs
```

You may describe that a credential exists, for example “API key present”, but do not include the key value or its prefix.

---

## 2. Architecture in One Page

Pi is a minimal terminal coding harness. In the target setup it becomes a larger orchestrated system through packages, extensions, skills, prompt templates, custom profiles, and subagents.

```text
Windows Terminal / PowerShell
        |
        v
Global pi CLI
@earendil-works/pi-coding-agent
        |
        | loads settings, auth, skills, prompts, packages
        v
<PI_AGENT_HOME>
├── settings.json          -> online profile
├── settings.local.json    -> local LLM profile
├── AGENTS.md              -> global behavior rules
├── skills/                -> local skills
├── prompts/               -> slash-command prompt templates
├── agents/                -> subagent definitions
├── npm/                   -> npm-installed Pi packages
├── git/                   -> git-installed Pi packages
└── extensions/            -> extension runtime state/config
        |
        +--> LLM providers
        |    ├── subscription login: openai-codex, Claude, Copilot, etc.
        |    ├── API-key providers: OpenAI, Anthropic, Groq, DeepSeek, ZAI, OpenRouter, etc.
        |    └── custom/local providers: Ollama, vLLM, LM Studio, llama.cpp, proxies
        |
        +--> extensions/tools
        |    ├── web search/fetch/PDF/video
        |    ├── MCP bridge
        |    ├── hashline read/replace
        |    ├── Context7 docs lookup
        |    ├── LSP code intelligence
        |    ├── subagent orchestration
        |    ├── usage tracking
        |    └── RTK command/output optimization
        |
        +--> skills
        |    ├── local files
        |    └── package-provided skills
        |
        +--> workflows
             ├── scout_planner
             ├── work_and_review
             ├── scout_review
             └── handoff
```

The local deployment described in the attached files used Pi v0.81.0 on Windows, an online profile with 9 packages, a local profile with 4 packages, 8 primary subagent-style roles plus 5 fallback roles, and a package/skill layout under `<PI_AGENT_HOME>`.

---

## 3. Prerequisites

### 3.1 Required software

Install these first:

| Component | Why it is needed | Minimum / recommendation |
|---|---|---|
| Windows 10/11 | Target platform in the attached setup | Windows Terminal recommended |
| Node.js | Pi is distributed as an npm package | Attached setup states Node `>=22.19.0` |
| npm | Installs Pi and npm packages | Attached setup used npm `11.16.0` |
| Git for Windows | Installs git-sourced Pi packages and clones repos | Latest stable |
| PowerShell 7 or Windows PowerShell | Command shell | PowerShell 7 preferred |
| ripgrep (`rg`) | Fast text search, useful for agents | Optional but recommended |
| fd | Fast file finding, useful for agents | Optional but recommended |
| VS Code or another editor | Editing config files | Optional |

### 3.2 Verify prerequisites

Open PowerShell and run:

```powershell
node --version
npm --version
git --version
where.exe node
where.exe npm
where.exe git
```

Expected:

```text
node --version  -> v22.x or newer
npm --version   -> 11.x or compatible
git --version   -> any modern Git for Windows version
```

If `node` or `npm` is missing, install Node.js LTS/current from the official Node.js site and reopen your terminal.

### 3.3 Recommended terminal settings

Use **Windows Terminal** with PowerShell. For multi-line Pi input, Windows Terminal supports Ctrl+Enter according to Pi usage docs, and `Alt+Enter` may need remapping if you want Pi to receive that shortcut.

---

## 4. Install Pi

### 4.1 Official npm install

The official Quickstart installs Pi globally with npm:

```powershell
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
```

The `--ignore-scripts` flag is intentional. Official Pi documentation says normal npm installs do not require lifecycle scripts.

### 4.2 Verify the CLI

```powershell
where.exe pi
pi --version
pi --help
```

Expected:

```text
where.exe pi -> a path under <ROAMING_NPM>
pi --version -> a Pi version, for example 0.81.0 or newer
```

### 4.3 Install location model

In the target deployment:

| Item | Location type | Example placeholder |
|---|---|---|
| Pi CLI | global npm | `<ROAMING_NPM>\node_modules\@earendil-works\pi-coding-agent\` |
| User Pi config | Pi agent home | `<PI_AGENT_HOME>` |
| npm Pi packages | user-scoped package store | `<PI_AGENT_NPM>\node_modules\...` |
| git Pi packages | user-scoped git store | `<PI_AGENT_GIT>\github.com\...` |

Pi package installation is separate from the global CLI installation. `pi install ...` writes package entries to user settings by default and installs package resources under `<PI_AGENT_HOME>`.

### 4.4 Uninstall note

To remove the global Pi CLI installed by npm:

```powershell
npm uninstall -g @earendil-works/pi-coding-agent
```

This removes the global command but does not necessarily delete your `<PI_AGENT_HOME>` settings, credentials, sessions, or installed Pi packages.

---

## 5. First Launch and Authentication

### 5.1 Start Pi in a project directory

Create or choose a working directory:

```powershell
mkdir C:\Work\pi-sandbox
cd C:\Work\pi-sandbox
pi
```

Inside Pi, type a simple request:

```text
Summarize this directory and tell me what files you can see.
```

### 5.2 Authenticate with a subscription provider

In interactive mode:

```text
/login
```

Select a provider. Official Pi provider docs list subscription logins such as ChatGPT Plus/Pro through Codex, Claude Pro/Max, GitHub Copilot, xAI subscription, and Radius. The attached target setup used `openai-codex` as the default online provider.

### 5.3 Authenticate with an API-key provider

You can either use `/login` and select an API-key provider, or set environment variables before launch.

PowerShell examples:

```powershell
$env:OPENAI_API_KEY = "REPLACE_WITH_REAL_KEY"
$env:ANTHROPIC_API_KEY = "REPLACE_WITH_REAL_KEY"
$env:GROQ_API_KEY = "REPLACE_WITH_REAL_KEY"
$env:DEEPSEEK_API_KEY = "REPLACE_WITH_REAL_KEY"
$env:OPENROUTER_API_KEY = "REPLACE_WITH_REAL_KEY"
$env:ZAI_API_KEY = "REPLACE_WITH_REAL_KEY"
pi
```

Do not save these commands with real values in a public script.

### 5.4 Credential resolution order

Pi resolves credentials in this order:

1. CLI `--api-key` flag.
2. `auth.json` entry.
3. Environment variable.
4. Custom provider keys from `models.json`.

For long-term use, `/login` is convenient, but `auth.json` must be treated as secret-bearing.

---

## 6. Provider and Model Setup

### 6.1 Online default profile

The target deployment used:

```json
{
  "defaultProvider": "openai-codex",
  "defaultModel": "gpt-5.5",
  "thinking": "medium",
  "theme": "dark"
}
```

Use this as a template, not as a guarantee that every model name is available in your current account. Model availability depends on your provider, plan, Pi version, and model catalog cache.

### 6.2 Switch models interactively

Inside Pi:

```text
/model
```

Then choose a provider and model.

Common session controls:

```text
/settings          # thinking level, theme, transport, etc.
/scoped-models     # enable/disable models used for cycling
/session           # inspect current session metadata
/new               # start a new session
/resume            # resume a previous session
```

### 6.3 Switch models from the command line

Examples:

```powershell
pi --provider openai-codex --model gpt-5.5
pi --provider groq --model openai/gpt-oss-20b
pi --provider deepseek --model deepseek-v4-flash
```

For one-shot print mode:

```powershell
pi -p --provider openai-codex --model gpt-5.5 "Summarize this repository."
```

### 6.4 Custom local provider with `models.json`

Official Pi docs support adding custom providers and local models through `<PI_AGENT_HOME>/models.json`. This is useful for Ollama, vLLM, LM Studio, llama.cpp routers, or private OpenAI-compatible servers.

Create:

```powershell
notepad $env:USERPROFILE\.pi\agent\models.json
```

Example for a local OpenAI-compatible server:

```json
{
  "providers": {
    "local-qwen": {
      "baseUrl": "http://127.0.0.1:11434/v1",
      "api": "openai-completions",
      "apiKey": "local-placeholder-key",
      "compat": {
        "supportsDeveloperRole": false,
        "supportsReasoningEffort": false
      },
      "models": [
        {
          "id": "qwen36-35b-moe",
          "name": "Qwen 3 235B MoE Local",
          "reasoning": false,
          "input": ["text"],
          "contextWindow": 128000,
          "maxTokens": 32000,
          "cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 }
        }
      ]
    }
  }
}
```

Notes:

- `apiKey` may be a dummy placeholder for local servers that ignore it.
- Use `compat.supportsDeveloperRole=false` if your server does not support the OpenAI `developer` role.
- Use `compat.supportsReasoningEffort=false` if your server rejects `reasoning_effort`.
- Restart Pi or run `/reload` after editing model configuration.

### 6.5 Test local provider

Start your local model server first, then run:

```powershell
pi --provider local-qwen --model qwen36-35b-moe -p "Reply with one sentence: local model is connected."
```

If the model does not appear in `/model`, check:

```powershell
Get-Content $env:USERPROFILE\.pi\agent\models.json
```

Then verify the local endpoint with curl or PowerShell:

```powershell
curl.exe http://127.0.0.1:11434/v1/models
```

Adapt the URL if you use vLLM, LM Studio, llama.cpp, or a custom gateway.

---

## 7. Create the Directory Structure

Pi creates many directories automatically. For this target setup, create explicit folders so the layout is predictable:

```powershell
$PiHome = "$env:USERPROFILE\.pi\agent"
New-Item -ItemType Directory -Force $PiHome | Out-Null
New-Item -ItemType Directory -Force "$PiHome\agents" | Out-Null
New-Item -ItemType Directory -Force "$PiHome\prompts" | Out-Null
New-Item -ItemType Directory -Force "$PiHome\skills" | Out-Null
New-Item -ItemType Directory -Force "$PiHome\extensions" | Out-Null
New-Item -ItemType Directory -Force "$PiHome\backups" | Out-Null
New-Item -ItemType Directory -Force "$PiHome\bin" | Out-Null
New-Item -ItemType Directory -Force "$PiHome\reports" | Out-Null
```

Expected target layout:

```text
<PI_AGENT_HOME>/
├── AGENTS.md
├── aliases.sh
├── settings.json
├── settings.local.json
├── models.json
├── agents/
├── prompts/
├── skills/
├── extensions/
├── npm/
├── git/
├── sessions/
├── backups/
└── bin/
```

---

## 8. Configure the Online Profile

Create or edit:

```powershell
notepad $env:USERPROFILE\.pi\agent\settings.json
```

Recommended starting template:

```json
{
  "defaultProvider": "openai-codex",
  "defaultModel": "gpt-5.5",
  "thinking": "medium",
  "theme": "dark",
  "packages": [
    "npm:pi-web-access",
    "npm:pi-mcp-adapter",
    "git:github.com/aporcelli/pi-usage",
    "git:github.com/patrixr/pi-psql",
    "npm:@dreki-gg/pi-context7",
    "npm:@dreki-gg/pi-lsp",
    "npm:@tintinweb/pi-subagents",
    "npm:pi-hashline-edit-pro",
    "git:github.com/MasuRii/pi-rtk-optimizer"
  ],
  "skills": [
    "skills"
  ],
  "prompts": [
    "prompts"
  ],
  "extensions": [
    "extensions"
  ],
  "enableSkillCommands": true
}
```

Important:

- This mirrors the package list in the attached target setup.
- If your account does not have `gpt-5.5`, choose an available model from `/model` and update `defaultModel`.
- `skills`, `prompts`, and `extensions` paths are relative to `<PI_AGENT_HOME>`.

---

## 9. Configure the Local LLM Profile

Create:

```powershell
notepad $env:USERPROFILE\.pi\agent\settings.local.json
```

Template matching the target local profile concept:

```json
{
  "defaultProvider": "local-qwen",
  "defaultModel": "local-qwen/qwen36-35b-moe",
  "thinking": "low",
  "hideThinking": true,
  "packages": [
    "npm:pi-web-access",
    "npm:pi-mcp-adapter",
    "git:github.com/aporcelli/pi-usage",
    "npm:pi-hashline-edit-pro"
  ],
  "skills": [
    "skills/llm-switcher.md",
    "skills/infra-context"
  ],
  "prompts": [
    "prompts"
  ],
  "enableSkillCommands": true
}
```

If your local model uses another provider or model ID, update both fields.

### 9.1 Run online profile

```powershell
pi
```

### 9.2 Run local profile

```powershell
pi --settings settings.local.json
```

### 9.3 Run local profile without skills

```powershell
pi --settings settings.local.json --no-skills
```

### 9.4 Run local profile with one explicit skill

```powershell
pi --settings settings.local.json --no-skills --skill skills/llm-switcher.md
```

---

## 10. Install Packages

Pi packages can bundle extensions, skills, prompts, and themes. Official package docs state that user-scoped package commands write to `~/.pi/agent/settings.json` by default, and project-local install uses `-l`.

### 10.1 Install the npm packages

Run in PowerShell:

```powershell
pi install npm:pi-web-access
pi install npm:pi-mcp-adapter
pi install npm:@dreki-gg/pi-context7
pi install npm:@dreki-gg/pi-lsp
pi install npm:@tintinweb/pi-subagents
pi install npm:pi-hashline-edit-pro
```

### 10.2 Install the git packages

```powershell
pi install git:github.com/aporcelli/pi-usage
pi install git:github.com/patrixr/pi-psql
pi install git:github.com/MasuRii/pi-rtk-optimizer
```

### 10.3 Verify installed packages

```powershell
pi list
```

You should see entries similar to:

```text
npm:pi-web-access
npm:pi-mcp-adapter
git:github.com/aporcelli/pi-usage
git:github.com/patrixr/pi-psql
npm:@dreki-gg/pi-context7
npm:@dreki-gg/pi-lsp
npm:@tintinweb/pi-subagents
npm:pi-hashline-edit-pro
git:github.com/MasuRii/pi-rtk-optimizer
```

### 10.4 Package inventory from the target deployment

| Package | Target version | Install type | Purpose |
|---|---:|---|---|
| `@earendil-works/pi-coding-agent` | 0.81.0 | global npm | Main `pi` CLI |
| `@earendil-works/pi-ai` | 0.74.2 observed | dependency | Unified LLM API and provider abstraction |
| `@earendil-works/pi-tui` | 0.74.2 observed | dependency | Terminal UI rendering |
| `@earendil-works/pi-agent-core` | 0.81.0 inferred | bundled/core | Agent loop, tools, state management |
| `pi-web-access` | 0.13.0 | Pi npm package | Web search, URL fetch, GitHub clone, PDF/YouTube/video analysis, librarian skill |
| `pi-mcp-adapter` | 2.11.0 | Pi npm package | MCP bridge for tools/resources/prompts |
| `pi-hashline-edit-pro` | 0.16.14 | Pi npm package | Hash-anchored read/replace editing |
| `@dreki-gg/pi-context7` | 0.2.0 | Pi npm package | Context7 documentation lookup |
| `@dreki-gg/pi-lsp` | 0.5.2 | Pi npm package | LSP diagnostics, hover, definitions, references |
| `@tintinweb/pi-subagents` | 0.14.2 | Pi npm package | Subagent orchestration |
| `pi-usage` / `@porche/pi-usage` | 0.3.5 | Pi git package | Token and provider usage tracking |
| `pi-psql` | 2.2.0 | Pi git package | PostgreSQL skill/client |
| `pi-rtk-optimizer` | 0.9.0 | Pi git package | RTK command rewriting and output compaction |
| `pdf2svg` | 0.1.2 | global npm utility | PDF-to-SVG conversion, not a Pi package |
| `npm` | 11.16.0 | bundled/global | Node package manager |

### 10.5 Update packages

```powershell
pi update                 # update Pi and packages
pi update --extensions    # update packages only
pi update --self          # update Pi CLI only
pi update npm:pi-web-access
```

Use `pi update --self --force` only when you need to reinstall the CLI even if the current version is detected.

### 10.6 Security rule for packages

Pi packages can execute code and influence agent behavior. Review third-party repositories before installing them, especially git-sourced packages.

---

## 11. What Each Package Adds

### 11.1 `pi-web-access`

Install:

```powershell
pi install npm:pi-web-access
```

What it adds:

- web search;
- URL fetch;
- content extraction;
- GitHub repository cloning/reading;
- PDF extraction;
- YouTube and local video understanding;
- a package-provided `librarian` skill.

Optional API keys may improve or switch search backends. Depending on your configuration, possible providers include OpenAI, Brave, Parallel, Tavily, Exa, Perplexity, and Gemini.

Beginner test:

```text
Search the web for the official Pi packages documentation and summarize how pi install works.
```

### 11.2 `pi-mcp-adapter`

Install:

```powershell
pi install npm:pi-mcp-adapter
```

What it adds:

- one compact MCP gateway into Pi;
- tool/resource/prompt discovery from MCP servers;
- commands such as MCP setup/management commands, depending on package version;
- on-demand MCP server startup instead of injecting all tool definitions into context.

Beginner flow:

```text
/mcp setup
```

Then follow the UI to add or inspect MCP servers. Treat MCP server configuration as sensitive because it may include local commands, hostnames, or credentials.

### 11.3 `pi-hashline-edit-pro`

Install:

```powershell
pi install npm:pi-hashline-edit-pro
```

What it adds:

- replacement `read` and `replace` workflow;
- hash-anchored edits instead of raw line-number edits;
- stale-context protection when files changed after reading.

Beginner test:

```text
Create a file named hello.txt with one sentence, then read it and replace one line using the safe replacement tool.
```

### 11.4 `@dreki-gg/pi-context7`

Install:

```powershell
pi install npm:@dreki-gg/pi-context7
```

What it adds:

- direct Context7 documentation lookup;
- persistent cache under the extension configuration area;
- no MCP dependency for docs lookup.

Beginner test:

```text
Use Context7 to look up the latest docs for the package I am using and show a minimal example.
```

### 11.5 `@dreki-gg/pi-lsp`

Install:

```powershell
pi install npm:@dreki-gg/pi-lsp
```

What it adds:

- LSP diagnostics;
- hover info;
- go-to-definition;
- find references;
- document/workspace symbols;
- call hierarchy;
- code actions.

The target setup had TypeScript, Pyright, Rust, and Go LSP servers configured but disabled. Start with disabled servers to avoid noisy or broken tooling, then enable only the language servers you really need.

Example config path:

```text
<PI_AGENT_EXTENSIONS>/lsp/config.json
```

Safe starter config:

```json
{
  "servers": {
    "typescript": { "disabled": true },
    "pyright": { "disabled": true },
    "rust": { "disabled": true },
    "go": { "disabled": true }
  }
}
```

### 11.6 `@tintinweb/pi-subagents`

Install:

```powershell
pi install npm:@tintinweb/pi-subagents
```

What it adds:

- subagents as separate Pi processes;
- custom agent definitions;
- parallel execution;
- mid-run steering;
- live widget for running/queued/completed agents;
- optional model-scope enforcement.

Beginner test:

```text
Use a scout subagent to inspect this repository and return only a file map and key risks.
```

### 11.7 `pi-usage`

Install:

```powershell
pi install git:github.com/aporcelli/pi-usage
```

What it adds:

- token usage tracking;
- provider account limit awareness;
- historical local usage summaries.

Use it to decide when to switch from premium models to cheaper/faster models.

### 11.8 `pi-psql`

Install:

```powershell
pi install git:github.com/patrixr/pi-psql
```

What it adds:

- a PostgreSQL-focused skill;
- encrypted credential storage according to the attached deployment context;
- query execution;
- schema inspection;
- table/view/index exploration;
- health checks.

Do not put database passwords into prompts. Store credentials through the package’s intended flow and redact all examples.

### 11.9 `pi-rtk-optimizer`

Install:

```powershell
pi install git:github.com/MasuRii/pi-rtk-optimizer
```

What it adds:

- RTK command rewriting;
- tool output compaction;
- truncation/aggregation for noisy outputs such as tests, build logs, git output, and searches.

Target behavior:

```json
{
  "enabled": true,
  "mode": "rewrite",
  "guardWhenRtkMissing": true,
  "showRewriteNotifications": true,
  "compaction": {
    "stripAnsi": true,
    "truncate": true,
    "aggregate": true
  }
}
```

---

## 12. Configure Global Instructions: `AGENTS.md`

Create:

```powershell
notepad $env:USERPROFILE\.pi\agent\AGENTS.md
```

Starter file:

```markdown
# Global Pi Agent Instructions

## Language and style
- User-facing explanations should use the user's language unless they request otherwise.
- Commands, code, filenames, and config examples should remain in English.
- Prefer concise progress updates for long tasks.

## Safety and approval
- Before modifying files, summarize the intended change and ask for approval unless the user explicitly requested direct edits.
- Never reveal API keys, OAuth tokens, passwords, private SSH keys, cookies, or raw connection strings.
- Double-confirm destructive actions such as delete, reset, rollback, or `rm -rf`.

## Editing policy
- Prefer hashline `replace` for edits after reading a file.
- Use `write` only for new files or full replacement when appropriate.
- Re-read files after edits and verify the intended change landed.

## Validation
- After code edits, run the smallest meaningful check first.
- If checks fail, summarize the failure and propose or apply the smallest fix.

## Output convention
- End implementation tasks with:
  - changed files;
  - commands run;
  - validation result;
  - remaining risks or next step.
```

Pi also loads project-level `AGENTS.md` or `CLAUDE.md` files from parent directories and the current directory. Use project-level files for repository-specific rules.

---

## 13. Configure Skills

Skills are on-demand capability packages. Pi scans only the skill name and description at startup, then the model can load full `SKILL.md` when relevant. This keeps context small.

### 13.1 Skill locations

Typical locations:

```text
<PI_AGENT_HOME>/skills/
<PROJECT>/.pi/skills/
<PROJECT>/.agents/skills/
```

A skill can be:

```text
skills/my-skill/SKILL.md
```

or, in some locations, a top-level Markdown file:

```text
skills/llm-switcher.md
```

### 13.2 Minimal skill template

Create:

```powershell
mkdir $env:USERPROFILE\.pi\agent\skills\example-skill
notepad $env:USERPROFILE\.pi\agent\skills\example-skill\SKILL.md
```

Template:

```markdown
---
name: example-skill
description: Use this skill when the user asks for a reproducible example workflow with setup, commands, validation, and cleanup.
---

# Example Skill

## When to use
Use this skill for small, reproducible setup guides.

## Workflow
1. Confirm the goal.
2. List prerequisites.
3. Provide commands.
4. Explain expected output.
5. Add troubleshooting.

## Safety
Never include real secrets. Use placeholders.
```

Reload Pi:

```text
/reload
```

Then force skill use:

```text
/skill:example-skill Create a tiny setup checklist.
```

### 13.3 Recreate target local skills

#### 13.3.1 `llm-switcher.md`

Create:

```powershell
notepad $env:USERPROFILE\.pi\agent\skills\llm-switcher.md
```

Template:

```markdown
---
name: llm-switcher
description: Use when the user asks to check, activate, or switch local LLM services such as Qwen or Gemma through MCP tools.
---

# LLM Switcher

## Purpose
Manage local LLM service state through the configured MCP tools.

## Available operations
- Check model status with `llm_status`.
- Activate a model with `llm_activate`.

## Rules
- Never expose SSH hostnames, IP addresses, credentials, or private container IDs.
- Before switching models, report the current active model if the tool is available.
- After switching, verify status.

## Example requests
- `/skill:llm-switcher status`
- `/skill:llm-switcher switch to qwen`
- `/skill:llm-switcher switch to gemma`
```

#### 13.3.2 `infra-context/SKILL.md`

```powershell
mkdir $env:USERPROFILE\.pi\agent\skills\infra-context
notepad $env:USERPROFILE\.pi\agent\skills\infra-context\SKILL.md
```

Template:

```markdown
---
name: infra-context
description: Use when the user asks about private infrastructure notes, Proxmox, Docker, GPU, LLM services, databases, networking, monitoring, or local deployment history.
---

# Infra Context

## Purpose
Use a local private knowledge base to retrieve infrastructure facts before answering.

## Private paths
- Knowledge base root: `<INFRA_KB>`

## Workflow
1. Search the local knowledge base for relevant facts.
2. Cite the local note name or path only if it is safe.
3. Generalize private hostnames and IPs unless the user explicitly needs them.
4. If no relevant note exists, say so instead of guessing.

## Safety
Do not reveal secrets, SSH keys, tokens, passwords, cookies, or full connection strings.
```

#### 13.3.3 `bami-presentation-design/SKILL.md`

```powershell
mkdir $env:USERPROFILE\.pi\agent\skills\bami-presentation-design
notepad $env:USERPROFILE\.pi\agent\skills\bami-presentation-design\SKILL.md
```

Template:

```markdown
---
name: bami-presentation-design
description: Use when the user asks to create BAMi-branded slide decks, business presentations, proposals, or Slidev/PPTX outputs using the local presentation generation workflow.
---

# BAMi Presentation Design

## Purpose
Create branded presentations using local PPTX and Slidev tooling.

## Workflow
1. Clarify the audience, purpose, and required output format.
2. Use the approved template and design rules from the local repository.
3. Generate the deck.
4. Render or preview the output.
5. Report generated file paths and validation results.

## Safety
Do not include client-confidential data unless explicitly provided for the deck.
```

#### 13.3.4 `slidev` skill

The target deployment used `slidev` as a symlink to an external skill directory. For a portable beginner setup, start with a local normal skill instead:

```powershell
mkdir $env:USERPROFILE\.pi\agent\skills\slidev
notepad $env:USERPROFILE\.pi\agent\skills\slidev\SKILL.md
```

Template:

```markdown
---
name: slidev
description: Use when the user asks to create technical Slidev web presentations, code walkthrough decks, or Markdown-based slides.
---

# Slidev

## Purpose
Create Markdown-based Slidev decks.

## Typical commands
```bash
npm create slidev@latest my-deck
cd my-deck
npm install
npm run dev
npm run export
```

## Output rules
- Keep slides concise.
- Use code blocks for developer examples.
- Include speaker notes only when requested.
```

### 13.4 Package-provided skills

Two target skills come from packages:

| Skill | Provider | How it appears |
|---|---|---|
| `librarian` | `pi-web-access` | Package skill under `skills/librarian` |
| `pi-psql` | `pi-psql` | Root `SKILL.md` in git package |

You do not need to manually create these if the packages are installed correctly.

### 13.5 Validate skills

Run:

```powershell
pi
```

Check startup header for loaded skills, or type:

```text
/skill:
```

You should see skill completions. You can also force one:

```text
/skill:llm-switcher status
```

---

## 14. Configure Prompt Templates

Prompt templates are reusable Markdown files expanded from slash commands. Place them in:

```text
<PI_AGENT_HOME>/prompts/
```

### 14.1 `scout_planner.md`

Create:

```powershell
notepad $env:USERPROFILE\.pi\agent\prompts\scout_planner.md
```

Template:

```markdown
---
description: Scout the codebase, synthesize findings, and produce an implementation plan with an approval gate.
---

# Scout Planner Workflow

User request:
$@

## Goal
Produce a grounded implementation plan before any write operations.

## Phase 0 — Scope
- Restate the task.
- Identify files, modules, docs, commands, and risks likely relevant.
- Do not modify files.

## Phase 1 — Scout
Use scout-style investigation:
- inspect file tree;
- search for relevant symbols and docs;
- read only the highest-value files;
- produce a compact context handoff.

## Phase 2 — Synthesize / Plan
Convert scout findings into:
- implementation objective;
- files to modify;
- exact steps;
- tests/checks;
- rollback plan;
- open questions or assumptions.

## Phase 3 — Human approval gate
Stop and ask for approval before implementation.

## Output
Return:
1. Context summary.
2. Proposed plan.
3. Files likely touched.
4. Validation commands.
5. Approval request.
```

Usage:

```text
/scout_planner Add validation for SVG title extraction before classifying infographic files.
```

### 14.2 `work_and_review.md`

Create:

```powershell
notepad $env:USERPROFILE\.pi\agent\prompts\work_and_review.md
```

Template:

```markdown
---
description: Execute an approved plan with a worker, review the result, and ask for a human decision.
---

# Work and Review Workflow

Approved task:
$@

## Phase 0 — Pre-flight
- Confirm that the task is approved.
- Identify expected files and commands.
- If there is no approved plan, create a brief execution plan first.

## Phase 1 — Worker execution
Use worker-style behavior:
- make minimal necessary edits;
- prefer hashline replace after reading;
- run small checks early;
- keep a change log.

## Phase 2 — Reviewer audit
Use reviewer-style behavior:
- inspect diff;
- check correctness, safety, edge cases, tests, and documentation;
- classify findings as blocking, important, or optional.

## Phase 3 — Human decision
Return one of:
- accept;
- apply reviewer fixes;
- revise plan;
- stop and rollback.

## Output
1. Implementation summary.
2. Files changed.
3. Commands run.
4. Review findings.
5. Final recommendation.
```

Usage:

```text
/work_and_review Implement the approved SVG validation plan.
```

### 14.3 `scout_review.md`

Create:

```powershell
notepad $env:USERPROFILE\.pi\agent\prompts\scout_review.md
```

Template:

```markdown
---
description: Run an independent scout-and-review audit of a codebase, plan, or proposed solution.
---

# Scout Review Workflow

Audit target:
$@

## Phase 0 — Setup
- Define the audit target.
- Do not modify files.

## Phase 1 — Parallel scouts
Gather independent context:
- file structure;
- relevant implementation points;
- docs and tests;
- risks and contradictions.

## Phase 2 — Context aggregation
Merge findings without inventing facts.

## Phase 3 — Reviewer audit
Evaluate:
- correctness;
- completeness;
- missed requirements;
- security and data risks;
- test coverage;
- maintainability.

## Phase 4 — Human approval gate
Ask whether to apply recommendations.

## Output
1. Audit summary.
2. Evidence.
3. Findings by severity.
4. Suggested fixes.
5. Approval request.
```

Usage:

```text
/scout_review Review the current remediation plan and identify missing validation steps.
```

### 14.4 `handoff.md`

Create:

```powershell
notepad $env:USERPROFILE\.pi\agent\prompts\handoff.md
```

Template:

```markdown
---
description: Produce a compact handoff for the next agent or future session.
---

# Handoff

Task/context:
$@

## Required output
Prepare a handoff with:

1. Goal.
2. Current state.
3. Decisions already made.
4. Files and commands involved.
5. Constraints and red lines.
6. Remaining work.
7. Recommended next action.

## Rules
- Do not include secrets.
- Prefer stable paths with placeholders.
- Mark uncertain facts explicitly.
- Keep it compact enough to paste into a new session.
```

Usage:

```text
/handoff Summarize where we stopped in the Pi deployment setup.
```

### 14.5 Reload prompts

```text
/reload
```

Then type `/` and check that prompt templates appear as slash commands.

---

## 15. Configure Subagents

The target setup uses the `@tintinweb/pi-subagents` package and an `agents/` folder with primary and fallback agents.

### 15.1 Create subagent runtime config

Create:

```powershell
notepad $env:USERPROFILE\.pi\agent\subagents.json
```

Template based on the attached setup:

```json
{
  "maxConcurrent": 6,
  "defaultMaxTurns": 80,
  "joinMode": "group"
}
```

### 15.2 Create primary agent definitions

Each agent is a Markdown file under:

```text
<PI_AGENT_HOME>/agents/
```

The exact frontmatter supported depends on the subagents package version. Use the package README as the authority. The following templates express the target roles and should be adapted if the package expects different field names.

#### `researcher.md`

```markdown
---
name: researcher
description: Autonomous web researcher that searches, evaluates sources, and synthesizes research briefs.
model: groq/openai/gpt-oss-20b
thinking: none
tools: read, write
prompt_mode: replace
---

You are a research subagent. Produce concise, source-grounded briefs. Do not modify project code.
```

#### `scout.md`

```markdown
---
name: scout
description: Fast codebase reconnaissance agent that produces compact context handoffs.
model: deepseek/deepseek-v4-flash
thinking: none
tools: read, grep, find, ls, bash, write
prompt_mode: replace
---

You inspect codebases quickly. Prefer search and targeted reads. Return a compact map of relevant files, facts, risks, and next steps.
```

#### `planner.md`

```markdown
---
name: planner
description: Planning specialist that turns requirements and context into implementation plans.
model: openai-codex/gpt-5.5
thinking: high
tools: read, grep, find, ls, write
prompt_mode: replace
---

You create concrete implementation plans. Do not edit code. Include validation and rollback.
```

#### `worker.md`

```markdown
---
name: worker
description: Implementation agent that executes approved plans as the single writer thread.
model: deepseek/deepseek-v4-flash
thinking: auto
tools: read, grep, find, ls, bash, write, ext:pi-hashline-edit-pro/replace
prompt_mode: replace
---

You implement approved plans. Make minimal edits, verify them, and report files changed and checks run.
```

#### `reviewer.md`

```markdown
---
name: reviewer
description: Review specialist for diffs, plans, codebase health, PRs, and issue validation.
model: zai/glm-5.2
thinking: high
tools: read, grep, find, ls, bash, write, ext:pi-hashline-edit-pro/replace
prompt_mode: replace
---

You review work critically. Identify blocking issues first, then important and optional findings.
```

#### `context-builder.md`

```markdown
---
name: context-builder
description: Requirements-to-context agent that gathers relevant facts and prepares handoff material.
model: zai/glm-4.5-air
thinking: none
tools: read, grep, find, ls, bash, write
prompt_mode: replace
---

You build compact, accurate task context from requirements and repository evidence.
```

#### `oracle.md`

```markdown
---
name: oracle
description: High-context decision-consistency agent that prevents drift and protects inherited state.
model: zai/glm-5.1
thinking: high
tools: read, grep, find, ls, bash
prompt_mode: replace
---

You check whether proposed actions preserve prior decisions, constraints, and user intent.
```

#### `delegate.md`

```markdown
---
name: delegate
description: Lightweight direct-execution subagent inheriting parent context/model where appropriate.
model: groq/openai/gpt-oss-20b
tools: read, grep, find, ls, bash, write, ext:pi-hashline-edit-pro/replace
prompt_mode: append
---

You perform small delegated tasks with minimal context and concise output.
```

### 15.3 Create fallback agents

Fallback agents are cheaper or alternate-model versions used when the primary provider is exhausted or fails.

Recommended files:

| Fallback file | Role | Example model |
|---|---|---|
| `context-builder-fb.md` | fallback for context-builder | `deepseek/deepseek-v4-flash` |
| `oracle-fb.md` | fallback for oracle | `deepseek/deepseek-v4-flash` |
| `planner-fb.md` | fallback for planner | `deepseek/deepseek-v4-flash` |
| `reviewer-fb.md` | fallback for reviewer | `deepseek/deepseek-v4-flash` |
| `worker-fb.md` | fallback for worker | `openrouter/deepseek/deepseek-v4-flash` |

Example:

```markdown
---
name: planner-fb
description: Fallback planning specialist for provider exhaustion or failed primary planner runs.
model: deepseek/deepseek-v4-flash
thinking: none
max_turns: 20
tools: read, grep, find, ls, write
prompt_mode: replace
---

Create a concise implementation plan under 400 words. State assumptions and validation steps.
```

### 15.4 Validate subagents

Restart Pi and use the subagents package UI/commands, for example:

```text
/agents
```

Then ask:

```text
Use the scout agent to inspect this repository and return a compact handoff.
```

If the command is not available, check:

```powershell
pi list
Get-ChildItem $env:USERPROFILE\.pi\agent\agents
```

---

## 16. Configure MCP

The target deployment used:

- `pi-mcp-adapter` as the bridge;
- a configured `llm-switcher` MCP server;
- cached/discovered `aveva-pml` and `proxmox` MCP servers;
- an SSH gateway with remote tools.

### 16.1 Start with MCP setup

Inside Pi:

```text
/mcp setup
```

Follow the adapter UI. Keep generated config private.

### 16.2 Minimal local MCP concept

MCP server configuration usually defines:

- server name;
- transport (`stdio`, HTTP, SSE, or another supported transport depending on adapter);
- command and args for stdio servers;
- environment variables;
- auth or headers when required.

Never publish the real config if it includes hostnames, API tokens, SSH usernames, database URLs, or internal commands.

### 16.3 Example redacted `llm-switcher` concept

```json
{
  "mcpServers": {
    "llm-switcher": {
      "transport": "stdio",
      "command": "node",
      "args": [
        "<PI_AGENT_HOME>/mcp-llm-switcher/server.js"
      ],
      "env": {
        "LLM_HOST": "<LLM_CONTAINER>",
        "SSH_HOST": "<PROXMOX_HOST>"
      }
    }
  }
}
```

This is illustrative only. Use the real schema required by the MCP adapter version you install.

### 16.4 Validate MCP tools

Ask Pi:

```text
List available MCP servers and summarize what each can do without revealing secrets.
```

Then test a safe tool, such as status-only:

```text
Use the llm-switcher status tool and report only the active model name.
```

---

## 17. Configure LSP

The target setup installed `@dreki-gg/pi-lsp` but kept TypeScript, Pyright, Rust, and Go servers disabled.

### 17.1 Why start disabled

LSP can be very useful, but it can also produce noisy diagnostics or require language-specific server binaries. Start disabled, then enable one language at a time.

### 17.2 Example disabled config

```json
{
  "servers": {
    "typescript": { "disabled": true },
    "pyright": { "disabled": true },
    "rust": { "disabled": true },
    "go": { "disabled": true }
  }
}
```

### 17.3 Enable one server later

Example concept for TypeScript:

```powershell
npm install -g typescript typescript-language-server
```

Then update LSP config according to the `@dreki-gg/pi-lsp` documentation and set only TypeScript to enabled.

---

## 18. Configure Web Search and Research

After installing `pi-web-access`, test basic web capability:

```text
Search for the official Pi Quickstart documentation and summarize the install command.
```

### 18.1 Optional search provider keys

Depending on your needs, set one or more keys:

```powershell
$env:BRAVE_API_KEY = "REPLACE_WITH_REAL_KEY"
$env:TAVILY_API_KEY = "REPLACE_WITH_REAL_KEY"
$env:EXA_API_KEY = "REPLACE_WITH_REAL_KEY"
$env:PERPLEXITY_API_KEY = "REPLACE_WITH_REAL_KEY"
$env:GOOGLE_API_KEY = "REPLACE_WITH_REAL_KEY"
```

Use only providers you actually need. Fewer keys means less secret surface.

### 18.2 Research prompt pattern

```text
Use web research. Prefer official documentation and repository READMEs. Include source links. Separate verified facts from assumptions.
```

---

## 19. Configure PostgreSQL Skill

Install:

```powershell
pi install git:github.com/patrixr/pi-psql
```

Use the skill only when needed:

```text
/skill:pi-psql Inspect the schema of the configured reporting database and list tables only.
```

### 19.1 Safe database rules

- Do not paste passwords in chat.
- Prefer read-only users.
- Avoid write queries unless explicitly approved.
- Ask the agent to show SQL before executing any destructive query.
- Redact hostnames and connection strings in reports.

### 19.2 Example read-only query request

```text
Use the PostgreSQL skill to list schemas and table counts. Do not run INSERT, UPDATE, DELETE, DROP, ALTER, TRUNCATE, or CREATE.
```

---

## 20. Configure Shell Aliases / Shortcuts

The target deployment used shell aliases to switch profiles. In PowerShell, define functions in your profile.

Open your profile:

```powershell
notepad $PROFILE
```

Add:

```powershell
function pi-online {
  pi @args
}

function pi-local-bare {
  pi --settings settings.local.json --no-skills @args
}

function pi-local {
  pi --settings settings.local.json --no-skills --skill skills/llm-switcher.md @args
}

function pi-local-infra {
  pi --settings settings.local.json --no-skills --skill skills/llm-switcher.md --skill skills/infra-context/SKILL.md @args
}

function pi-local-db {
  pi --settings settings.local.json --no-skills --skill skills/llm-switcher.md --skill skills/infra-context/SKILL.md --skill git/pi-psql/SKILL.md @args
}
```

Restart PowerShell and test:

```powershell
pi-online --version
pi-local-bare --version
```

If you prefer Git Bash, create `<PI_AGENT_HOME>/aliases.sh`:

```bash
alias pi-online='pi'
alias pi-local-bare='pi --settings settings.local.json --no-skills'
alias pi-local='pi --settings settings.local.json --no-skills --skill skills/llm-switcher.md'
alias pi-local-infra='pi --settings settings.local.json --no-skills --skill skills/llm-switcher.md --skill skills/infra-context/SKILL.md'
alias pi-local-db='pi --settings settings.local.json --no-skills --skill skills/llm-switcher.md --skill skills/infra-context/SKILL.md --skill ../git/pi-psql/SKILL.md'
```

---

## 21. Start and Manage Sessions

### 21.1 New session

```powershell
cd C:\Work\your-project
pi
```

Inside Pi:

```text
/name Setup investigation
```

### 21.2 Continue recent session

```powershell
pi -c
```

### 21.3 Resume from a list

```powershell
pi -r
```

### 21.4 One-shot print mode

```powershell
cat README.md | pi -p "Summarize this text and list setup commands."
```

### 21.5 Branching and compaction

Inside Pi:

```text
/tree
/fork
/clone
/compact Summarize decisions, files changed, and next steps.
```

Use `/compact` before large context-sensitive tasks, before switching models, or before handing off to another session.

---

## 22. Recommended Beginner Workflows

### 22.1 Investigate before editing

```text
/scout_planner Analyze how this repository validates SVG files and propose a plan to include SVG title/description text as a classification signal.
```

Expected output:

- relevant files;
- current behavior;
- gaps;
- implementation plan;
- tests;
- approval request.

### 22.2 Implement after approval

```text
/work_and_review Implement the approved SVG title/description validation plan.
```

Expected output:

- worker changes;
- reviewer findings;
- commands run;
- human decision point.

### 22.3 Independent audit

```text
/scout_review Review the current plan and identify weak points, missing tests, and hidden assumptions.
```

### 22.4 Handoff

```text
/handoff Summarize the current state for a new session. Include decisions, files, commands, risks, and next action.
```

---

## 23. Typical Prompts to Use With This Setup

### 23.1 Repository onboarding

```text
Analyze this repository as a new maintainer. First inspect docs and package files, then summarize architecture, build/test commands, main risks, and the safest first task. Do not edit files.
```

### 23.2 Planning prompt

```text
Create an implementation plan. Include files to inspect, exact change strategy, tests, rollback, and uncertainty. Do not modify files until I approve.
```

### 23.3 Worker prompt

```text
Implement the approved plan. Make the smallest safe changes. Use hashline replacement where available. Re-read edited files and run the smallest meaningful checks.
```

### 23.4 Reviewer prompt

```text
Review the diff as if this were a production PR. Focus on correctness, edge cases, security, data leakage, tests, and maintainability. Mark findings as blocking, important, or optional.
```

### 23.5 Research prompt

```text
Use official docs and primary repositories first. Include links. Separate verified facts from assumptions. Do not rely on stale cached knowledge when current docs are available.
```

### 23.6 Secret-safe infrastructure prompt

```text
Use the infrastructure skill only for context. Redact private hostnames, IPs, usernames, tokens, SSH paths, database URLs, and client-confidential details in the final answer.
```

### 23.7 Local model switching prompt

```text
Check the current local LLM status. If the requested model is inactive, switch to it and verify status. Do not reveal hostnames, IP addresses, or SSH commands.
```

---

## 24. Validation Checklist

Run these after setup.

### 24.1 CLI validation

```powershell
pi --version
pi --help
pi list
```

Pass criteria:

- `pi` is found in PATH;
- version prints;
- installed packages are listed.

### 24.2 Online model validation

```powershell
pi -p --provider openai-codex --model gpt-5.5 "Say: online provider works."
```

If model unavailable, use `/model` interactively and choose a visible model.

### 24.3 Local model validation

```powershell
pi --settings settings.local.json -p "Say: local profile works."
```

Pass criteria:

- request returns without provider auth errors;
- local endpoint is reachable;
- model ID matches `models.json`.

### 24.4 Skills validation

```text
/skill:llm-switcher status
/skill:infra-context Summarize available infra topics without private details.
/skill:example-skill Create a setup checklist.
```

### 24.5 Prompt validation

Type `/` inside Pi and confirm these exist:

```text
/scout_planner
/work_and_review
/scout_review
/handoff
```

### 24.6 Web validation

```text
Search for the official Pi Quickstart and tell me the install command with a source link.
```

### 24.7 MCP validation

```text
List configured MCP servers and their safe, high-level purpose. Do not reveal secrets or host details.
```

### 24.8 Subagent validation

```text
Use a scout subagent to inspect the current directory and return a compact map.
```

### 24.9 Hashline editing validation

Create a temporary file and ask Pi to safely edit it:

```powershell
Set-Content .\pi-test.txt "line one`nline two`nline three"
```

Inside Pi:

```text
Read pi-test.txt and replace line two with "line two edited" using the hashline replacement workflow.
```

Then:

```powershell
Get-Content .\pi-test.txt
```

---

## 25. Troubleshooting

### 25.1 `pi` is not recognized

Check npm global bin path:

```powershell
npm config get prefix
where.exe npm
```

Add npm global bin to PATH. Usually this is:

```text
<USER_HOME>\AppData\Roaming\npm
```

Restart terminal.

### 25.2 Package install fails

Try:

```powershell
npm cache verify
pi update --self
pi install npm:pi-web-access
```

For git packages:

```powershell
git ls-remote https://github.com/aporcelli/pi-usage.git
```

If corporate network blocks GitHub or npm, use a trusted network or configure proxy settings.

### 25.3 Model not visible in `/model`

Check:

- provider credentials;
- `models.json` syntax;
- model ID spelling;
- endpoint availability;
- dummy API key for local OpenAI-compatible servers;
- restart Pi or run `/reload`.

### 25.4 Local model rejects requests

Try adding compatibility flags:

```json
"compat": {
  "supportsDeveloperRole": false,
  "supportsReasoningEffort": false
}
```

Then restart Pi.

### 25.5 LSP errors

Disable all servers first. Enable one server at a time after installing the language server binary.

### 25.6 MCP server not found

Inside Pi:

```text
/mcp setup
```

Then inspect safe configuration paths. Do not paste secret-bearing `mcp.json` into public channels.

### 25.7 Subagent does not start

Check:

```powershell
pi list
Get-ChildItem $env:USERPROFILE\.pi\agent\agents
Get-Content $env:USERPROFILE\.pi\agent\subagents.json
```

Also verify that the selected subagent model exists and is authenticated.

### 25.8 Hashline edit fails because of stale anchors

This is expected protection. Ask Pi to re-read the file and retry the replacement using fresh hashes.

---

## 26. Reproducible Setup Script Skeleton

This script creates directories and installs packages. It intentionally does not create secrets.

```powershell
# setup-pi.ps1
$ErrorActionPreference = "Stop"

$PiHome = "$env:USERPROFILE\.pi\agent"

Write-Host "Creating Pi directories..."
$dirs = @(
  $PiHome,
  "$PiHome\agents",
  "$PiHome\prompts",
  "$PiHome\skills",
  "$PiHome\extensions",
  "$PiHome\backups",
  "$PiHome\bin",
  "$PiHome\reports"
)
foreach ($d in $dirs) { New-Item -ItemType Directory -Force $d | Out-Null }

Write-Host "Installing Pi CLI..."
npm install -g --ignore-scripts @earendil-works/pi-coding-agent

Write-Host "Installing Pi npm packages..."
pi install npm:pi-web-access
pi install npm:pi-mcp-adapter
pi install npm:@dreki-gg/pi-context7
pi install npm:@dreki-gg/pi-lsp
pi install npm:@tintinweb/pi-subagents
pi install npm:pi-hashline-edit-pro

Write-Host "Installing Pi git packages..."
pi install git:github.com/aporcelli/pi-usage
pi install git:github.com/patrixr/pi-psql
pi install git:github.com/MasuRii/pi-rtk-optimizer

Write-Host "Installed package list:"
pi list

Write-Host "Next steps:"
Write-Host "1. Run: pi"
Write-Host "2. Run: /login"
Write-Host "3. Create settings.json, settings.local.json, models.json, skills, prompts, and agents."
Write-Host "4. Never commit auth.json, mcp.json, trust.json, or sessions."
```

---

## 27. Relationship Maps

### 27.1 Package -> extension -> tool / capability map

| Package | Extension? | Skill? | Major capability |
|---|---|---|---|
| `pi-web-access` | Yes | `librarian` | Search, fetch, repo/PDF/video analysis |
| `pi-mcp-adapter` | Yes | No | MCP bridge and server management |
| `pi-hashline-edit-pro` | Yes | No | Hashline `read` / `replace` editing |
| `@dreki-gg/pi-context7` | Yes | No | Docs lookup and cache |
| `@dreki-gg/pi-lsp` | Yes | No | LSP intelligence |
| `@tintinweb/pi-subagents` | Yes | No | Subagent orchestration |
| `pi-usage` | Yes | No | Token and usage tracking |
| `pi-psql` | No / skill-focused | `pi-psql` | PostgreSQL schema/query operations |
| `pi-rtk-optimizer` | Yes | No | Output compaction and command rewriting |

### 27.2 Skill -> dependency map

| Skill | Origin | External dependency |
|---|---|---|
| `bami-presentation-design` | local skill | local presentation repository/tooling |
| `infra-context` | local skill | `<INFRA_KB>` private KB |
| `llm-switcher` | local skill | MCP server and local LLM host |
| `slidev` | local/symlink skill | Slidev project tooling |
| `librarian` | `pi-web-access` | web/repo search tools |
| `pi-psql` | `pi-psql` git package | PostgreSQL connection configuration |

### 27.3 Agent -> model -> role map

| Agent | Target model | Role |
|---|---|---|
| `researcher` | `groq/openai/gpt-oss-20b` | Web/source research brief |
| `scout` | `deepseek/deepseek-v4-flash` | Fast codebase reconnaissance |
| `planner` | `openai-codex/gpt-5.5` | Detailed implementation planning |
| `reviewer` | `zai/glm-5.2` | Review and audit |
| `worker` | `deepseek/deepseek-v4-flash` | Implementation |
| `context-builder` | `zai/glm-4.5-air` | Requirements-to-context |
| `oracle` | `zai/glm-5.1` | Decision consistency guard |
| `delegate` | `groq/openai/gpt-oss-20b` | Lightweight direct task execution |

### 27.4 Prompt -> agent pipeline map

| Prompt | Pipeline | Output |
|---|---|---|
| `scout_planner` | Scout -> synthesize/plan -> approval | Implementation plan |
| `work_and_review` | Worker -> reviewer -> human decision | Implemented changes + review |
| `scout_review` | Scout(s) -> aggregate -> reviewer -> approval | Independent audit |
| `handoff` | Current context -> compact handoff | Future-session summary |

### 27.5 Provider -> usage map

| Provider | Typical use |
|---|---|
| `openai-codex` | default online planning, high-value reasoning |
| `zai` | reviewer/oracle/context-builder models |
| `deepseek` | scout and worker fast execution |
| `groq` | researcher/delegate fast inference |
| `openrouter` | fallback routing when direct providers are unavailable |
| `local-qwen` | local/private low-cost tasks |

---

## 28. Evidence and Verification Sources

### 28.1 Attached deployment evidence

The attached context and report support the target setup facts:

- Pi CLI version `0.81.0`.
- Windows platform.
- Package list and versions.
- Online and local profile concepts.
- Installed extensions and skills.
- Agent and fallback-agent map.
- Prompt-template workflow names.
- MCP server categories.
- Redaction policy and uncertainty notes.

### 28.2 Official Pi documentation checked

Use these official sources when validating this guide:

| Topic | Source |
|---|---|
| Main repository | `https://github.com/earendil-works/pi` |
| Quickstart | `https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/quickstart.md` |
| Using Pi | `https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/usage.md` |
| Providers | `https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/providers.md` |
| Custom models | `https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/models.md` |
| Skills | `https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md` |
| Packages | `https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/packages.md` |
| Settings | `https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/settings.md` |
| Extensions | `https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/extensions.md` |

### 28.3 Package pages and repositories checked

| Package | Verification source |
|---|---|
| `pi-web-access` | `https://pi.dev/packages/pi-web-access` and `https://github.com/nicobailon/pi-web-access` |
| `pi-mcp-adapter` | `https://pi.dev/packages/pi-mcp-adapter` and `https://github.com/nicobailon/pi-mcp-adapter` |
| `pi-hashline-edit-pro` | `https://pi.dev/packages/pi-hashline-edit-pro` and `https://github.com/YuGiMob/pi-hashline-edit-pro` |
| `@tintinweb/pi-subagents` | `https://github.com/tintinweb/pi-subagents` |
| `@dreki-gg/pi-context7` | `https://github.com/dreki-gg/pi-extensions` |
| `@dreki-gg/pi-lsp` | `https://github.com/jalbarrang/pi-lsp` |
| `pi-usage` | `https://github.com/aporcelli/pi-usage` |
| `pi-psql` | `https://github.com/patrixr/pi-psql` |
| `pi-rtk-optimizer` | `https://github.com/MasuRii/pi-rtk-optimizer` |

---

## 29. Known Uncertainties and How to Handle Them

| Uncertainty | Handling in this guide |
|---|---|
| `@earendil-works/pi-agent-core` was not directly located as a separate installed package in the attached context | Treat as inferred from the Pi CLI version unless independently verified |
| Attached context observed `pi-ai` and `pi-tui` at v0.74.2 while CLI dependency ranges may reference newer versions | Report observed versions separately from declared ranges; use `npm ls` to verify your install |
| Some prompt files had EPERM/content-access issues during the original scan | Use the summarized workflow intent and safe templates, not secret or unavailable raw content |
| Secret-bearing files were intentionally not inspected | Do not attempt to reconstruct credentials; configure your own |
| Cached MCP state may differ from live MCP state | Treat cached servers as examples; validate with `/mcp` in your installation |
| Local provider `local-qwen` was inferred from profile/settings context | Adapt to your actual local model endpoint |
| `slidev` was a symlink outside the allowed scan scope | Use a local portable skill unless you intentionally maintain a shared skill directory |
| Package versions may change after this document date | Use `pi list`, package pages, and repository tags to verify current versions |

---

## 30. Final Beginner Checklist

Use this checklist after completing setup:

```text
[ ] Node.js installed and node --version works.
[ ] npm installed and npm --version works.
[ ] Git installed and git --version works.
[ ] Pi CLI installed globally.
[ ] pi --version works.
[ ] /login completed for at least one online provider, or API key env vars configured.
[ ] models.json created only if local/custom models are needed.
[ ] settings.json created for online profile.
[ ] settings.local.json created for local profile.
[ ] All required Pi packages installed.
[ ] pi list shows expected packages.
[ ] AGENTS.md created with safety and editing rules.
[ ] Local skills created and visible through /skill: completion.
[ ] Prompt templates created and visible through / completion.
[ ] Subagent package installed and agents folder populated.
[ ] MCP configured only with redacted/private-safe settings.
[ ] LSP starts disabled; servers enabled one at a time later.
[ ] Web access tested.
[ ] Online model tested.
[ ] Local model tested if applicable.
[ ] No secrets committed or copied into shared docs.
```

---

## Appendix A. Minimal Files to Back Up

Back up these files, but keep the backup private and encrypted if it includes secrets:

```text
<PI_AGENT_HOME>/settings.json
<PI_AGENT_HOME>/settings.local.json
<PI_AGENT_HOME>/models.json        # secret-sensitive
<PI_AGENT_HOME>/AGENTS.md
<PI_AGENT_HOME>/agents/
<PI_AGENT_HOME>/prompts/
<PI_AGENT_HOME>/skills/
<PI_AGENT_HOME>/subagents.json
```

Back up these only to encrypted storage:

```text
<PI_AGENT_HOME>/auth.json
<PI_AGENT_HOME>/mcp.json
<PI_AGENT_HOME>/trust.json
<PI_AGENT_HOME>/sessions/
```

---

## Appendix B. Quick Command Reference

```powershell
# Install Pi
npm install -g --ignore-scripts @earendil-works/pi-coding-agent

# Verify
pi --version
pi --help

# Start
pi

# Login inside Pi
/login

# Select model inside Pi
/model

# One-shot mode
pi -p "Summarize this repository."

# Continue/resume
pi -c
pi -r

# Install packages
pi install npm:pi-web-access
pi install npm:pi-mcp-adapter
pi install npm:@dreki-gg/pi-context7
pi install npm:@dreki-gg/pi-lsp
pi install npm:@tintinweb/pi-subagents
pi install npm:pi-hashline-edit-pro
pi install git:github.com/aporcelli/pi-usage
pi install git:github.com/patrixr/pi-psql
pi install git:github.com/MasuRii/pi-rtk-optimizer

# List/update
pi list
pi update
pi update --extensions
pi update --self

# Local profile
pi --settings settings.local.json
pi --settings settings.local.json --no-skills
```

---

## Appendix C. Recommended `.gitignore` Entries

If you maintain a project-level `.pi` folder, add:

```gitignore
# Pi local/private state
.pi/auth.json
.pi/mcp.json
.pi/trust.json
.pi/models.json
.pi/models-store.json
.pi/sessions/
.pi/cache/
.pi/tmp/

# Optional: keep local settings private unless intentionally shared
.pi/settings.local.json
```

For the global `<PI_AGENT_HOME>`, do not put it under a public repository.

---

## Appendix D. Source-Derived Target Inventory

This table is a compact reproduction target from the attached context. Adapt versions to the current package registry if necessary.

| Category | Items |
|---|---|
| Global packages | `@earendil-works/pi-coding-agent`, `npm`, `pdf2svg` |
| Pi npm packages | `pi-web-access`, `pi-mcp-adapter`, `pi-hashline-edit-pro`, `@dreki-gg/pi-context7`, `@dreki-gg/pi-lsp`, `@tintinweb/pi-subagents` |
| Pi git packages | `pi-usage`, `pi-psql`, `pi-rtk-optimizer` |
| Local skills | `bami-presentation-design`, `infra-context`, `llm-switcher`, `slidev` |
| Package skills | `librarian`, `pi-psql` |
| Primary agents | `researcher`, `scout`, `planner`, `reviewer`, `worker`, `context-builder`, `oracle`, `delegate` |
| Fallback agents | `context-builder-fb`, `oracle-fb`, `planner-fb`, `reviewer-fb`, `worker-fb` |
| Prompt templates | `scout_planner`, `work_and_review`, `scout_review`, `handoff` |
| MCP examples | `llm-switcher`, `aveva-pml`, `proxmox`, SSH gateway |
| Provider examples | `openai-codex`, `zai`, `openrouter`, `groq`, `deepseek`, `local-qwen` |

---

## Appendix E. Proof Checklist Against Official Docs

Before relying on this setup in production, verify:

1. The official Quickstart still recommends the same global install command.
2. The package docs still support the `pi install npm:...` and `pi install git:...` forms.
3. Provider docs still list your intended provider and auth method.
4. Models docs still support your custom local server API mode.
5. Skills docs still support your skill location and `SKILL.md` structure.
6. Package pages still show the package versions and package manifests you expect.
7. Git repositories for all third-party packages are still maintained and safe enough for your environment.

