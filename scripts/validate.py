#!/usr/bin/env python3
"""Validate skills in this repository against the Agent Skills specification.

Checks the rules published at https://agentskills.io/specification plus the
practical limits imposed by distribution channels (skills.sh, Codex, Copilot).
Standard library only, so it runs anywhere Python 3.9+ does.

Usage:  python3 scripts/validate.py [root]
Exit:   0 = valid (warnings allowed), 1 = one or more errors
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

SPEC_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

MAX_NAME = 64
MAX_DESCRIPTION = 1024
MAX_COMPATIBILITY = 500
MAX_SKILL_LINES = 500       # spec recommendation
MAX_FILE_BYTES = 2 * 1024 * 1024  # skills.sh pack builder omits larger files

errors: list[str] = []
warnings: list[str] = []


def err(where: Path, msg: str) -> None:
    errors.append(f"{where}: {msg}")


def warn(where: Path, msg: str) -> None:
    warnings.append(f"{where}: {msg}")


def parse_frontmatter(text: str, path: Path):
    """Minimal YAML-subset parser: scalars and one level of nested mapping."""
    if not text.startswith("---\n"):
        err(path, "missing YAML frontmatter (file must start with '---')")
        return None, text
    end = text.find("\n---\n", 3)
    if end == -1:
        err(path, "frontmatter is not terminated by a closing '---'")
        return None, text
    raw, body = text[4:end + 1], text[end + 5:]
    data, current = {}, None
    for lineno, line in enumerate(raw.splitlines(), start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")):
            if current is None or ":" not in line:
                err(path, f"line {lineno}: unexpected indented line in frontmatter")
                continue
            k, v = line.strip().split(":", 1)
            data.setdefault(current, {})[k.strip()] = v.strip().strip("'\"")
            continue
        if ":" not in line:
            err(path, f"line {lineno}: frontmatter line is not 'key: value'")
            continue
        k, v = line.split(":", 1)
        k, v = k.strip(), v.strip()
        if v == "":
            data[k], current = {}, k
        else:
            data[k], current = v.strip("'\""), None
    if "<" in raw or ">" in raw:
        err(path, "frontmatter contains '<' or '>', which can inject instructions into the system prompt")
    return data, body


def check_skill(skill_dir: Path, repo: Path) -> None:
    md = skill_dir / "SKILL.md"
    rel = md.relative_to(repo)
    text = md.read_text(encoding="utf-8")
    data, body = parse_frontmatter(text, rel)
    if data is None:
        return

    unknown = set(data) - SPEC_FIELDS
    if unknown:
        warn(rel, f"non-spec frontmatter field(s): {', '.join(sorted(unknown))} "
                  f"(spec-compliant runtimes ignore them; consider metadata:)")

    name = data.get("name")
    if not name:
        err(rel, "frontmatter is missing the required 'name' field")
    else:
        if len(name) > MAX_NAME:
            err(rel, f"name is {len(name)} characters (max {MAX_NAME})")
        if not NAME_RE.match(name):
            err(rel, f"name '{name}' must be lowercase a-z, 0-9 and single hyphens, "
                     "and must not start or end with a hyphen")
        if name != skill_dir.name:
            err(rel, f"name '{name}' must match the parent directory '{skill_dir.name}'")

    desc = data.get("description")
    if not desc:
        err(rel, "frontmatter is missing the required 'description' field")
    else:
        if len(desc) > MAX_DESCRIPTION:
            err(rel, f"description is {len(desc)} characters (max {MAX_DESCRIPTION})")
        if len(desc) < 40:
            warn(rel, "description is very short; state both what the skill does and when to use it")

    compat = data.get("compatibility")
    if isinstance(compat, str) and len(compat) > MAX_COMPATIBILITY:
        err(rel, f"compatibility is {len(compat)} characters (max {MAX_COMPATIBILITY})")

    meta = data.get("metadata")
    if meta is not None and not isinstance(meta, dict):
        err(rel, "metadata must be a mapping of string keys to string values")

    lines = len(text.splitlines())
    if lines > MAX_SKILL_LINES:
        err(rel, f"SKILL.md is {lines} lines (spec recommends under {MAX_SKILL_LINES}); "
                 "move detail into references/")
    elif lines > MAX_SKILL_LINES * 0.8:
        warn(rel, f"SKILL.md is {lines} lines, approaching the {MAX_SKILL_LINES}-line recommendation")

    if not body.strip():
        err(rel, "SKILL.md has no body content after the frontmatter")

    # Link integrity across every markdown file in the skill.
    for md_file in sorted(skill_dir.rglob("*.md")):
        mrel = md_file.relative_to(repo)
        for target in LINK_RE.findall(md_file.read_text(encoding="utf-8")):
            target = target.split("#", 1)[0].strip()
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            resolved = (md_file.parent / target).resolve()
            if not resolved.exists():
                err(mrel, f"broken relative link: {target}")
            elif skill_dir.resolve() not in resolved.parents and resolved != skill_dir.resolve():
                warn(mrel, f"link escapes the skill directory: {target} "
                           "(it will break once the skill is installed on its own)")

    # Depth and size limits.
    for f in sorted(skill_dir.rglob("*")):
        if not f.is_file():
            continue
        frel = f.relative_to(repo)
        depth = len(f.relative_to(skill_dir).parts) - 1
        if depth > 1:
            warn(frel, f"nested {depth} levels below SKILL.md; the spec recommends keeping "
                       "references one level deep")
        size = f.stat().st_size
        if size > MAX_FILE_BYTES:
            err(frel, f"file is {size / 1e6:.1f} MB; skills.sh omits files over 2 MB")

    print(f"  checked {rel}  ({lines} lines, "
          f"{len(list(skill_dir.rglob('*.md'))) - 1} reference files)")


def main() -> int:
    repo = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    skills = sorted(p.parent for p in repo.rglob("SKILL.md")
                    if ".git" not in p.parts and "node_modules" not in p.parts)
    if not skills:
        print(f"No SKILL.md found under {repo}", file=sys.stderr)
        return 1

    print(f"Validating {len(skills)} skill(s) in {repo}")
    for s in skills:
        check_skill(s, repo)

    for w in warnings:
        print(f"warning  {w}")
    for e in errors:
        print(f"ERROR    {e}", file=sys.stderr)

    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
