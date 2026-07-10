![version](https://img.shields.io/badge/version-2.1.0-blue) ![license](https://img.shields.io/badge/license-MIT-green) ![skills](https://img.shields.io/badge/skills-4-orange) ![agents](https://img.shields.io/badge/agents-Claude%20Code%20%7C%20Codex%20%7C%20Gemini%20%7C%20Hermes-lightgrey)

<p align="center"><img src="./assets/logo.jpg" alt="paleo" width="460"></p>

# 🪨 paleo

> Token-saving skill collection for LLM agents. Cut token use, keep output exact.

**paleo** is a small, focused toolkit of skills that make any LLM agent spend fewer tokens — without dumbing down the work. It runs on Claude Code, Codex, Gemini CLI, and Hermes Agent. Instead of one vague "be concise" instruction, paleo splits token-saving into composable skills you switch on per task.

### Why paleo?
- **Tokens cost money and latency.** Every trimmed token means faster, cheaper inference.
- **One-size-fits-all prompting fails.** Sometimes you want terse output, sometimes a hard budget, sometimes just no fluff. paleo gives each as a separate, well-scoped skill.
- **Skills stay minimal.** Every `SKILL.md` is written terse on purpose — loading one costs less context than a long prompt.

### How it works
Each skill lives in `skills/<name>/SKILL.md` with `name` + `description` frontmatter. Agents (Claude Code plugins, `npx skills` registry, Gemini extensions, Hermes) auto-discover and load the relevant skill when its trigger matches. Skills compose: run `paleo` together with `paleo-budget` for maximum savings, or use any single one standalone.

## Skills

| Skill | What it does |
|---|---|
| `paleo` | Terse output mode — cut output tokens ~60–70%, keep code/terms exact. |
| `paleo-trim-context` | Proactively trim/summarize context to save tokens without losing task state. |
| `paleo-skip-preamble` | Strip greetings/apologies/hedging from replies. |
| `paleo-budget` | Hard token budget per task — cap spend, summarize if exceeded. |

## Install

```bash
# Universal (any agent) — clone + copy skills manually
git clone https://github.com/mocasus/paleo.git
# copy skills/paleo*/ into your agent's skills directory

# Claude Code (one plugin bundles all 4 skills)
claude plugin marketplace add https://github.com/mocasus/paleo
claude plugin install paleo@paleo

# Codex / Cursor / Windsurf / 30+ agents (npx skills registry)
npx skills add mocasus/paleo

# Gemini CLI
gemini extensions install https://github.com/mocasus/paleo

# Hermes Agent
cp -r skills/paleo skills/paleo-trim-context skills/paleo-skip-preamble skills/paleo-budget ~/.hermes/skills/
```

> Full per-agent steps in [INSTALL.md](./INSTALL.md).

## Custom skills

paleo is open — wire your own token-saving skills:

1. `skills/<your-name>/SKILL.md` with `name` + `description` frontmatter.
2. Register in `.claude-plugin/plugin.json` + `gemini-extension.json`.
3. Bump version badge (this file + footer) + plugin `version`.
4. Commit + push.

No repo edit needed — just drop any `SKILL.md` into your agent's skills dir (e.g. `~/.hermes/skills/<name>/`). paleo loads whatever it finds under `skills/`.

## License

MIT — see [LICENSE](./LICENSE).

---

<p align="center">🪨 paleo · v2.1.0 · MIT</p>
