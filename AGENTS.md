# Working on this repository

This repo distributes one Agent Skill: `skills/bangla-writer/`. It is prose, not code — the deliverable is the quality of the instructions and the accuracy of the Bengali in them.

## Layout

- `skills/<name>/SKILL.md` — the skill. Always loaded by the host, so it stays short and carries only rules that apply to every Bengali text.
- `skills/<name>/references/*.md` — loaded on demand. One topic per file, one level deep.
- `evals/` — prompts and rubric for behavioral testing. Not part of the installed skill.
- `scripts/` — repo tooling. `validate.py` checks spec compliance, `install.sh` places the skill in a host's skills directory.

## Rules for edits

1. **Run `python3 scripts/validate.py .` before finishing.** It enforces the [Agent Skills spec](https://agentskills.io/specification): frontmatter fields, `name` matching the directory, the 1024-character description cap, no `<` or `>` in frontmatter, `SKILL.md` under 500 lines, reference depth, link integrity.
2. **Every Bengali example must be correct Bengali.** Examples teach more than prose rules do, so an example that violates one of the skill's own rules is the worst possible defect. Before/after pairs must preserve meaning exactly — a rewrite that adds a fact demonstrates the failure it is meant to prevent.
3. **Keep the register spread wide.** The skill covers all writing, not software writing. If you add examples, check that you are not tilting the whole file toward one genre.
4. **Prefer narrowing to prohibiting.** Bengali usage varies by region, register, and writer. A rule stated as universal will be applied mechanically and will produce overcorrection, which the skill treats as a failure in its own right.
5. **Do not reorganize into deeper directories.** Hosts load references relative to `SKILL.md`, and the spec asks for one level.

## Do not

- Add frontmatter fields outside the spec (`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`). Custom keys belong under `metadata`.
- Rename the skill directory without updating `name` in the frontmatter; they must match or the skill will not load.
- Link from a reference file to anything outside the skill directory — it breaks once the skill is installed on its own.
- Claim the skill is validated. No scored eval run exists yet; see `evals/rubric.md`.
