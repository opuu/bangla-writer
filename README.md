# bangla-writer

An [Agent Skill](https://agentskills.io/specification) that teaches an AI agent to write, translate, and edit **natural Bengali (Bangla)** — prose that reads as if it was conceived in Bengali rather than mapped word by word from English.

It covers everyday messages, letters, literary prose, journalism, essays and academic writing, official and legal notices, education, health information, business, marketing, and product or technical text, in Bangladeshi and West Bengal varieties.

## Install

The skill is a plain folder containing `SKILL.md`. Every host below reads the same folder — only the location differs.

**Any agent, via the skills.sh CLI** (knows the paths for 76+ agents):

```bash
npx skills add opuu/bangla-writer
```

**Without Node**, using the bundled installer:

```bash
./scripts/install.sh claude                  # ~/.claude/skills
./scripts/install.sh codex                   # ~/.agents/skills
./scripts/install.sh copilot --scope project # .github/skills
./scripts/install.sh --list                  # show every path
```

**By hand** — copy or symlink `skills/bangla-writer/` into:

| Host | User scope | Project scope |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| OpenAI Codex | `~/.agents/skills/` | `.agents/skills/` |
| Antigravity 2.0 / CLI | `~/.agents/skills/` | `.agents/skills/` |
| Gemini CLI | `~/.gemini/skills/` | `.gemini/skills/` |
| Cursor | `~/.cursor/skills/` | `.cursor/skills/` |
| GitHub Copilot | `~/.copilot/skills/` | `.github/skills/` |
| OpenCode | `~/.config/opencode/skills/` | `.opencode/skills/` |

`.agents/skills/` is the emerging host-neutral location; Codex and Antigravity 2.0 both read it. Codex scans `.agents/skills` from the working directory up to the repository root, so a project-scope install works for every subdirectory.

## Use

Once installed, the agent loads the skill on its own when a task matches the description — writing, translating, localizing, or editing Bengali. You can also invoke it explicitly (`$bangla-writer` in Codex CLI, `@bangla-writer` in ChatGPT, `/bangla-writer` in Claude Code).

```
এই ইমেইলটা বাংলায় লিখে দাও, অফিসের জন্য।
Translate this for a West Bengal audience, respectful address.
Review this paragraph and tell me why it sounds translated. Don't rewrite it.
```

## What's inside

```
skills/bangla-writer/
├── SKILL.md                                  # always loaded: targeting, 8 core rules, output contract
└── references/                               # loaded only when the task needs them
    ├── genres.md                             # what natural means per genre, from text message to court notice
    ├── grammar-and-syntax.md                 # negation, tense/aspect, compound verbs, plurals, agreement
    ├── naturalness-patterns.md               # translationese and machine-prose diagnostics
    ├── region-and-register.md                # Bangladesh vs West Bengal, forms of address, formality
    ├── orthography-and-typography.md         # spelling, ষ/ণ in loanwords, numerals, লাখ/কোটি, punctuation
    ├── product-and-technical-language.md     # UI, support, placeholders, mixed-script text
    └── examples.md                           # worked before/after rewrites across genres
```

The design follows the spec's progressive disclosure: `SKILL.md` stays under 100 lines and carries the rules that apply to every text; the references are pulled in only when the task calls for them.

## Develop

```bash
python3 scripts/validate.py .     # spec compliance: frontmatter, naming, limits, link integrity
```

The validator checks the [Agent Skills specification](https://agentskills.io/specification) rules — required and optional frontmatter fields, `name` matching the directory, the 1024-character description cap, no angle brackets in frontmatter, the 500-line `SKILL.md` recommendation, reference depth — plus the 2 MB per-file limit that skills.sh applies when building packs. Standard library only; no dependencies.

## Evaluate

`evals/` holds the behavioral test suite: 48 prompts across every task type and a rubric with anchored 1–5 scoring, hard-failure gates, and mechanical pre-checks.

**The skill is not yet behaviorally validated.** No scored run exists. See [evals/rubric.md](evals/rubric.md) for the protocol — three samples per prompt per condition, two native reviewers per locale, blinded, reported by task group — and record results under `evals/results/`.

## Contributing

The rules in this skill are claims about Bengali, and native-speaker corrections are the point. When proposing a change:

- give a concrete before/after pair rather than an abstract rule
- say which region and register it applies to, and where it does not
- prefer narrowing an existing rule over adding a universal prohibition
- run `python3 scripts/validate.py .` before opening a PR

## License

MIT. See [LICENSE](LICENSE).
