/**
 * agent-include.ts — compile @include directives in agent definitions at startup.
 *
 * pi-subagents reads ~/.pi/agent/agents/*.md on every Agent() call and puts the
 * body verbatim into the system prompt. This extension compiles the shared role
 * files (agent-roles/*.md) into the concrete agent files BEFORE the session
 * starts (async factory — pi awaits it, see docs/extensions.md).
 *
 * Fail-closed: if any include is missing, circular, or escapes agent-roles/,
 * the factory throws and pi startup fails loudly. A stale expanded body must
 * never silently keep running.
 *
 * Source of truth: agent-roles/*.md + frontmatter in agents/*.md (hand-maintained).
 * The body below the @include marker is generated and must not be hand-edited.
 *
 * Manual re-sync after editing a role: node ~/.pi/agent/scripts/agent-include.mjs
 */
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";
// @ts-ignore — plain JS module without type declarations
import { syncAgentIncludes } from "../scripts/agent-include.mjs";

export default async function (pi: ExtensionAPI) {
  const { results, errors } = syncAgentIncludes();

  for (const r of results) {
    if (r.status === "updated") console.log(`[agent-include] expanded ${r.file}`);
  }

  if (errors.length > 0) {
    throw new Error(
      `agent-include compilation failed: ${errors.map((e) => `${e.file}: ${e.message}`).join("; ")}`,
    );
  }
}
