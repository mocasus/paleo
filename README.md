![version](https://img.shields.io/badge/version-2.2.0-blue) ![license](https://img.shields.io/badge/license-MIT-green) ![skills](https://img.shields.io/badge/skills-4-orange) ![agents](https://img.shields.io/badge/agents-Claude%20Code%20%7C%20Codex%20%7C%20Gemini%20%7C%20Hermes-lightgrey)

<p align="center"><img src="./assets/logo.jpg" alt="paleo" width="460"></p>

# 🦴 paleo

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

## Tips

> paleo activates from natural-language triggers — no slash command to register. Type the trigger, the skill loads and applies.

<details>
<summary>Activation & switches (plain phrases)</summary>

**paleo** — terse output
- On: `paleo mode` · `be brief` · `terse` · `compress output` · `save tokens`
- Level: `paleo full` (default) · `paleo lite` · `paleo ultra`
- Off: `stop paleo` · `normal mode`

**paleo-budget** — token cap
- On: `budget 2000` · `stay under 2000 tokens` · `token limit`
- Off: `no budget` · `unlimited`

**paleo-trim-context** — auto on long sessions; `trim context` to force.
**paleo-skip-preamble** — auto on every reply.

**Combo:** `paleo` + `paleo-budget` = max savings. Add `paleo-trim-context` on long sessions.

</details>

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

All 4 skills load automatically — `paleo`, `paleo-trim-context`, `paleo-skip-preamble`, `paleo-budget`.

> Full per-agent steps in [INSTALL.md](./INSTALL.md). See real compression numbers in [BENCHMARK.md](./BENCHMARK.md).

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

## Sponsors

<p align="center">
  <a href="https://kliqo.co"><img src="./assets/kliqo-banner.jpg" alt="Kliqo.co" width="420"></a>
</p>

<p align="center"><b>Kliqo.co</b> sponsors paleo · <a href="https://kliqo.co">kliqo.co</a></p>

<p align="center">🦴 paleo · v2.2.0 · MIT</p>
