#!/usr/bin/env python3
"""Run every knowledge-base validation gate in sequence.

Usage:
    python tools/kb-validate/run_all.py            # from the repository root
    python tools/kb-validate/run_all.py --lint     # also run markdownlint (needs npx)

Exit code is non-zero if any gate fails, so this is usable directly in CI.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
PY = sys.executable

GATES = [
    ("frontmatter contract", [PY, os.path.join(HERE, "check_frontmatter.py")]),
    ("internal links", [PY, os.path.join(HERE, "check_links.py")]),
    ("provenance paths", [PY, os.path.join(HERE, "check_sources.py")]),
    ("wiki publication", [PY, os.path.join(HERE, "check_wiki.py")]),
]


def main(argv):
    failures = []
    for name, cmd in GATES:
        print(f"== {name}")
        rc = subprocess.run(cmd, cwd=ROOT).returncode
        if rc != 0:
            failures.append(name)

    if "--lint" in argv:
        print("== markdownlint")
        cmd = ["npx", "--yes", "markdownlint-cli2",
               "--config", os.path.join(HERE, "markdownlint.json"),
               "knowledge-base/**/*.md", "!knowledge-base/raw-input/**",
               "sources/**/*.md", "analysis/**/*.md", "reports/**/*.md",
               "labs/**/*.md", "README.md", "AGENTS.md"]
        if subprocess.run(cmd, cwd=ROOT).returncode != 0:
            failures.append("markdownlint")

    if failures:
        print("\nVALIDATION FAILED: " + ", ".join(failures))
        return 1
    print("\nVALIDATION PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
