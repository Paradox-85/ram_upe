#!/usr/bin/env node
/**
 * agent-include.mjs — deterministic @include resolver for agent definitions.
 *
 * pi-subagents does NOT support includes in agent body; frontmatter is
 * authoritative and the body goes verbatim into the system prompt.
 * This script rewrites the BODY of agent definition files in place:
 *
 *   agents/worker.md            agent-roles/worker.md
 *   ───────────────             ─────────────────────
 *   ---                         (role instructions, shared)
 *   model: ...                  ▲
 *   ---                         │ expanded into body
 *   <!-- @include ../agent-roles/worker.md -->  ← directive (kept as marker)
 *   <expanded role body>
 *
 * The directive must be the FIRST non-empty line of the body. Everything after
 * it is regenerated on every run (idempotent): the old expanded body is
 * replaced, never appended.
 *
 * Rules:
 *   1. include directive allowed only in the body, first non-empty line after frontmatter
 *   2. includes are allowed ONLY inside agent-roles/ (physical realpath containment)
 *   3. max include depth = 2
 *   4. circular includes are rejected
 *   5. missing include file → hard error (exit 1)
 *   6. contents are expanded before the model runs (files on disk are the source)
 *   7. frontmatter exists only in the concrete agent file, never in roles
 *   8. atomic: two-pass — resolve/render EVERYTHING first; if ANY error, write NOTHING
 *
 * Usage:
 *   node scripts/agent-include.mjs            # expand includes (idempotent, atomic)
 *   node scripts/agent-include.mjs --check    # verify only, no writes, exit 1 on drift
 */
import { existsSync, readdirSync, readFileSync, realpathSync, writeFileSync } from "node:fs";
import { dirname, join, resolve, sep } from "node:path";
import { fileURLToPath } from "node:url";

const AGENT_DIR = join(dirname(fileURLToPath(import.meta.url)), "..", "agents");
const ROLE_DIR = resolve(AGENT_DIR, "..", "agent-roles");
const MAX_DEPTH = 2;

const DIRECTIVE_RE = /^<!--\s*@include\s+(.+?)\s*-->\s*$/;

/** Physical root of the allowed include tree (resolved once). */
function resolveRoleRoot(roleDir) {
  if (!existsSync(roleDir)) {
    throw new Error(`agent-roles directory missing: ${roleDir}`);
  }
  return realpathSync(roleDir);
}

/** Return the include target from the first non-empty line of the body, or null. */
function findDirective(body) {
  for (const line of body.split(/\r?\n/)) {
    if (!line.trim()) continue;
    const m = line.match(DIRECTIVE_RE);
    return m ? m[1].trim() : null;
  }
  return null;
}

/**
 * Recursively expand a role file's own directives.
 * Containment is checked against the PHYSICAL path (realpath) of the target.
 * Returns full text.
 */
function expandFile(targetPath, baseDir, roleRootReal, stack, depth) {
  if (depth > MAX_DEPTH) {
    throw new Error(`include depth exceeds ${MAX_DEPTH}: ${stack.join(" -> ")}`);
  }
  const lexical = resolve(baseDir, targetPath);
  let real;
  try {
    real = realpathSync(lexical);
  } catch {
    throw new Error(`missing include file: ${targetPath} (resolved: ${lexical}), stack: ${stack.join(" -> ")}`);
  }
  if (real !== roleRootReal && !real.startsWith(roleRootReal + sep)) {
    throw new Error(`include outside agent-roles: ${real} (allowed: ${roleRootReal})`);
  }
  if (stack.includes(real)) {
    throw new Error(`circular include: ${[...stack, real].join(" -> ")}`);
  }
  const content = readFileSync(real, "utf-8");
  const stack2 = [...stack, real];
  const lines = content.split(/\r?\n/);
  const out = [];
  for (const line of lines) {
    const m = line.match(DIRECTIVE_RE);
    if (!m) {
      out.push(line);
      continue;
    }
    const nested = expandFile(m[1].trim(), dirname(real), roleRootReal, stack2, depth + 1);
    out.push(`<!-- @include ${m[1].trim()} -->`);
    out.push(nested.trim());
  }
  return out.join("\n");
}

/** Split frontmatter (--- ... ---) from body. Returns null if malformed. */
function splitFrontmatter(content) {
  const m = content.match(/^---\r?\n([\s\S]*?\r?\n)---\r?\n?([\s\S]*)$/);
  if (!m) return null;
  return { frontmatter: m[1], body: m[2] ?? "" };
}

/**
 * Render the canonical file content for a directive-bearing agent file.
 * Throws on any include error — used in both passes.
 */
function render(frontmatter, rawDirective, agentDir, roleRootReal) {
  const expanded = expandFile(rawDirective, agentDir, roleRootReal, [], 0);
  return `---\n${frontmatter}---\n\n<!-- @include ${rawDirective} -->\n${expanded.trim()}\n`;
}

/**
 * Compile all directive-bearing agent files.
 *
 * Atomic: PASS 1 resolves and renders every candidate; if ANY file errors,
 * NOTHING is written. PASS 2 writes only the changed files.
 *
 * Returns { results, errors }. Throws only if agentDir/roleDir are unusable.
 */
export function syncAgentIncludes(agentDir = AGENT_DIR, roleDir = ROLE_DIR) {
  const roleRootReal = resolveRoleRoot(roleDir);
  const files = readdirSync(agentDir).filter((f) => f.endsWith(".md")).sort();
  const results = [];
  const errors = [];

  // PASS 1 — resolve + render everything
  const candidates = [];
  for (const f of files) {
    const full = join(agentDir, f);
    try {
      const content = readFileSync(full, "utf-8");
      const parts = splitFrontmatter(content);
      if (!parts) {
        results.push({ file: f, status: "skipped", reason: "no frontmatter" });
        continue;
      }
      const directive = findDirective(parts.body);
      if (!directive) {
        results.push({ file: f, status: "skipped", reason: "no include directive" });
        continue;
      }
      const next = render(parts.frontmatter, directive, agentDir, roleRootReal);
      candidates.push({ file: f, content, next, changed: next !== content });
    } catch (e) {
      errors.push({ file: f, message: e.message });
      console.error(`[agent-include] ERROR ${f}: ${e.message}`);
    }
  }

  // PASS 2 — write only if the whole tree resolved cleanly
  if (errors.length === 0) {
    for (const c of candidates) {
      if (c.changed) {
        writeFileSync(join(agentDir, c.file), c.next);
        results.push({ file: c.file, status: "updated" });
      } else {
        results.push({ file: c.file, status: "ok" });
      }
    }
  } else {
    for (const c of candidates) results.push({ file: c.file, status: "pending" });
  }

  return { results, errors };
}

// CLI entry
const isMain =
  typeof import.meta.main !== "undefined"
    ? import.meta.main
    : process.argv[1] && import.meta.url === new URL(`file://${process.argv[1].replace(/\\/g, "/")}`).href;

if (isMain) {
  const checkOnly = process.argv.includes("--check");

  if (checkOnly) {
    let drifted = 0;
    let failed = 0;
    try {
      const roleRootReal = resolveRoleRoot(ROLE_DIR);
      for (const f of readdirSync(AGENT_DIR).filter((x) => x.endsWith(".md")).sort()) {
        const full = join(AGENT_DIR, f);
        try {
          const content = readFileSync(full, "utf-8");
          const parts = splitFrontmatter(content);
          if (!parts) continue;
          const directive = findDirective(parts.body);
          if (!directive) continue;
          const next = render(parts.frontmatter, directive, AGENT_DIR, roleRootReal);
          if (next !== content) {
            drifted++;
            console.error(`[agent-include] DRIFT ${f}`);
          }
        } catch (e) {
          failed++;
          console.error(`[agent-include] ERROR ${f}: ${e.message}`);
        }
      }
    } catch (e) {
      failed++;
      console.error(`[agent-include] ERROR: ${e.message}`);
    }
    console.log(`[agent-include] check done: ${drifted} file(s) out of sync, ${failed} error(s)`);
    process.exit(drifted > 0 || failed > 0 ? 1 : 0);
  }

  const { results, errors } = syncAgentIncludes();
  for (const r of results) {
    const label = r.status === "updated" ? "UPDATED" : r.status === "ok" ? "OK" : r.status === "pending" ? "PENDING" : "SKIPPED";
    console.log(`[agent-include] ${label} ${r.file}${r.reason ? ` (${r.reason})` : ""}`);
  }
  if (errors.length > 0) {
    console.error(`[agent-include] ${errors.length} error(s) — nothing was written (atomic). Fix and re-run.`);
    process.exit(1);
  }
}
