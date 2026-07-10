![version](https://img.shields.io/badge/version-1.3.0-blue) ![license](https://img.shields.io/badge/license-MIT-green) ![skills](https://img.shields.io/badge/skills-3-orange) ![agents](https://img.shields.io/badge/agents-Claude%20Code%20%7C%20Codex%20%7C%20Gemini%20%7C%20Hermes-lightgrey)

# 🪨 paleo

Personal, public skill collection by **mocasus** — works on Claude Code, Codex, Gemini CLI, Hermes Agent. Same idea as *caveman* repo, my own toolbox.

**Token-minimal + caveman-compressed:** prose is caveman-style (no filler, short clauses); code + technical terms stay exact. Loading a skill costs less LLM context.

Each skill = `skills/<name>/SKILL.md` with `name` + `description` frontmatter (loads in Claude Code plugins, `npx skills` registry, Gemini extensions, Hermes).

## Skills

| Skill | What it does |
|---|---|
| `tg-leave-by-keyword` | Bulk-leave TG groups/channels by keyword (dry-run + confirm). |
| `tg-fetch-post` | Pull TG post text + URL + buttons from a `t.me/.../<id>` link. |
| `tg-list-dialogs` | Dump all dialogs (id, type, title) — inventory / cleanup prep. |

## Install

See [INSTALL.md](./INSTALL.md) for per-agent setup.

```bash
# Claude Code
claude plugin marketplace add mocasus/paleo
claude plugin install tg-leave-by-keyword@paleo
claude plugin install tg-fetch-post@paleo
claude plugin install tg-list-dialogs@paleo

# Universal (Codex / Cursor / Windsurf / 30+ agents)
npx skills add mocasus/paleo

# Gemini CLI
gemini extensions install https://github.com/mocasus/paleo

# Hermes Agent
cp -r skills/tg-leave-by-keyword ~/.hermes/skills/software-development/
cp -r skills/tg-fetch-post ~/.hermes/skills/software-development/
cp -r skills/tg-list-dialogs ~/.hermes/skills/software-development/
```

## Add a skill
1. `skills/<name>/SKILL.md` with `name` + `description` frontmatter.
2. Register in `.claude-plugin/plugin.json` + `gemini-extension.json`.
3. Bump version badge (this file + footer) + plugin `version`.
4. Commit + push.

## License
MIT — see [LICENSE](./LICENSE).

---

<p align="center">🪨 paleo · v1.3.0 · MIT · by mocasus</p>
