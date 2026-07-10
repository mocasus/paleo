![version](https://img.shields.io/badge/version-2.0.0-blue) ![license](https://img.shields.io/badge/license-MIT-green) ![skills](https://img.shields.io/badge/skills-3-orange) ![agents](https://img.shields.io/badge/agents-Claude%20Code%20%7C%20Codex%20%7C%20Gemini%20%7C%20Hermes-lightgrey)

# 🪨 paleo

Personal, public **token-saving** skill collection by **mocasus** — works on Claude Code, Codex, Gemini CLI, Hermes Agent. Same spirit as *caveman*: cut LLM token use. But paleo is my own toolbox of skills whose job is to save tokens — compress output, trim context, skip filler.

Skills are token-minimal + caveman-compressed: prose terse, code/terms exact. Loading one costs less context.

Each skill = `skills/<name>/SKILL.md` with `name` + `description` frontmatter (loads in Claude Code plugins, `npx skills` registry, Gemini extensions, Hermes).

## Skills

| Skill | What it does |
|---|---|
| `paleo-compress` | Terse caveman-style output — cut output tokens ~60-70%, keep code/terms exact. |
| `paleo-trim-context` | Proactively trim/summarize context to save tokens without losing task state. |
| `paleo-skip-preamble` | Strip greetings/apologies/hedging from replies. |

## Install

```bash
# Claude Code
claude plugin marketplace add mocasus/paleo
claude plugin install paleo-compress@paleo
claude plugin install paleo-trim-context@paleo
claude plugin install paleo-skip-preamble@paleo

# Universal (Codex / Cursor / Windsurf / 30+ agents)
npx skills add mocasus/paleo

# Gemini CLI
gemini extensions install https://github.com/mocasus/paleo

# Hermes Agent
cp -r skills/paleo-compress ~/.hermes/skills/software-development/
cp -r skills/paleo-trim-context ~/.hermes/skills/software-development/
cp -r skills/paleo-skip-preamble ~/.hermes/skills/software-development/
```

## Add a skill
1. `skills/<name>/SKILL.md` with `name` + `description` frontmatter.
2. Register in `.claude-plugin/plugin.json` + `gemini-extension.json`.
3. Bump version badge (this file + footer) + plugin `version`.
4. Commit + push.

## License
MIT — see [LICENSE](./LICENSE).

---

<p align="center">🪨 paleo · v2.0.0 · MIT · by mocasus</p>
