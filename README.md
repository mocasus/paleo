![version](https://img.shields.io/badge/version-1.1.0-blue) ![license](https://img.shields.io/badge/license-MIT-green) ![skills](https://img.shields.io/badge/skills-2-orange) ![agents](https://img.shields.io/badge/agents-Claude%20Code%20%7C%20Codex%20%7C%20Gemini%20%7C%20Hermes-lightgrey)

# 🪨 paleo

Personal, public collection of reusable skills by **mocasus** — built to work across multiple AI coding agents
(Claude Code, Codex, Gemini CLI, and Hermes Agent). Same idea as the *caveman* repo, but my own toolbox.

Every skill lives in `skills/<name>/SKILL.md` with a `name` + `description` frontmatter, so it loads natively in
Claude Code plugins, the `npx skills` registry, Gemini extensions, and Hermes.

## Skills

| Skill | What it does |
|---|---|
| `tg-leave-by-keyword` | Bulk-leave Telegram groups/channels by keyword via MTProto userbot (dry-run + confirm). |
| `tg-fetch-post` | Extract a Telegram post's text, linked URL, and buttons from a `t.me/.../<id>` link. |

## Install

See [INSTALL.md](./INSTALL.md) for per-agent setup. Quick start:

```bash
# Claude Code
claude plugin marketplace add mocasus/paleo
claude plugin install tg-leave-by-keyword@paleo
claude plugin install tg-fetch-post@paleo

# Universal (Codex / Cursor / Windsurf / 30+ agents)
npx skills add mocasus/paleo

# Gemini CLI
gemini extensions install https://github.com/mocasus/paleo

# Hermes Agent
cp -r skills/tg-leave-by-keyword ~/.hermes/skills/software-development/
cp -r skills/tg-fetch-post ~/.hermes/skills/software-development/
```

## Adding a skill

1. Create `skills/<your-skill>/SKILL.md` with `name` + `description` frontmatter.
2. Register it in `.claude-plugin/plugin.json` and `gemini-extension.json`.
3. Bump the version badge (this file + footer) and the plugin `version`.
4. Commit + push.

## License

MIT — see [LICENSE](./LICENSE).

---

<p align="center">🪨 paleo · v1.1.0 · MIT · by mocasus</p>
