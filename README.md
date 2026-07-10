<div align="center">

![version](https://img.shields.io/badge/version-2.3.0-blue) ![license](https://img.shields.io/badge/license-MIT-green) ![skills](https://img.shields.io/badge/skills-4-orange) ![tokens saved](https://img.shields.io/badge/tokens%20saved-%7E54%25-brightgreen) ![agents](https://img.shields.io/badge/agents-Claude%20Code%20%7C%20Codex%20%7C%20Gemini%20%7C%20Hermes-lightgrey)

<img src="./assets/logo.jpg" alt="paleo" width="420">

# 🦴 paleo

**Token-saving skill collection for LLM agents. Cut token use, keep output exact — modular skills, not a caveman persona, and never a rewrite of your code.**

[Why](#why-paleo) · [See it](#see-it-before--after) · [Features](#features) · [Skills](#skills) · [Quick Start](#quick-start) · [Benchmarks](#benchmarks) · [Comparison](#comparison) · [Tips](#tips--triggers) · [Install](#installation)

</div>

## Why paleo?

- **Tokens cost money and latency.** Every trimmed token means faster, cheaper inference.
- **One-size-fits-all prompting fails.** Sometimes you want terse output, sometimes a hard budget, sometimes just no fluff. paleo gives each as a separate, well-scoped skill.
- **Skills stay minimal.** Every `SKILL.md` is written terse on purpose — loading one costs less context than a long prompt.

## See it (Before / After)

paleo compresses *delivery*, not meaning. Code, commands, and technical terms stay byte-exact.

| Normal agent | 🦴 paleo |
|---|---|
| "The re-render happens because you create a new object literal on every render. That inline object is a fresh reference each time, so React sees a changed prop and re-renders. Wrap it in `useMemo` to keep a stable reference." | "New object each render → new ref → re-render. Wrap in `useMemo`. Stable ref = no re-render." |
| "To authenticate requests, add middleware that checks the token on each request and returns 401 if it is missing or expired." | "Add auth middleware. Check token per request. 401 if missing/expired." |

> [!NOTE]
> paleo keeps technical accuracy at 100% — it drops filler, not facts.

## Features

- [x] **Modular & composable** — load one skill or all four, mix per task.
- [x] **Output + context savings** — ~50–70% fewer output tokens (median ~54% on a 6-task sample — see [BENCHMARK.md](./BENCHMARK.md)), plus proactive context trimming.
- [x] **Production-safe** — compresses output and context only; never rewrites your code.
- [x] **Hard token budget** — `paleo-budget` caps spend and summarizes the tail.
- [x] **Cross-agent** — works on Claude Code, Codex, Gemini CLI, and Hermes Agent.
- [x] **Zero-setup triggers** — plain English phrases, no slash commands to register.
- [x] **Low overhead** — each `SKILL.md` is intentionally terse, so loading stays cheap.
- [x] **Open & extensible** — drop in your own token-saving skills.

## Skills

| Skill | What it does | Trigger example |
|---|---|---|
| `paleo` | Terse output mode — cut output tokens ~50–70%, keep code/terms exact. | `paleo mode` · `be brief` · `save tokens` |
| `paleo-trim-context` | Proactively trim/summarize context to save tokens without losing task state. | `trim context` (auto on long sessions) |
| `paleo-skip-preamble` | Strip greetings/apologies/hedging from replies. | auto on every reply |
| `paleo-budget` | Hard token budget per task — cap spend, summarize if exceeded. | `budget 2000` · `stay under 2000 tokens` |

## Quick Start

```bash
# 1. Clone the collection
git clone https://github.com/mocasus/paleo.git

# 2. Claude Code — one plugin bundles all 4 skills
claude plugin marketplace add https://github.com/mocasus/paleo
claude plugin install paleo@paleo

# 3. Any agent via the npx skills registry
npx skills add mocasus/paleo
```

Then just talk to your agent — no command to register:

> `paleo mode` · `save tokens` · `budget 2000` · `trim context`

## Benchmarks

Real, reproducible numbers — not hand-waved claims.

| Model | Tasks | Median output savings | Mean |
|---|---|---|---|
| `claude-sonnet-4.5` | 6 | **53.8%** | 45.1% |

Full method, per-task table, and the runnable harness are in [BENCHMARK.md](./BENCHMARK.md). Rerun on your own stack:

```bash
export IDROUTER_API_KEY=your_key
python3 bench/benchmark.py --model claude-sonnet-4.5
```

> [!TIP]
> Savings are task-dependent: biggest on verbose generative work (code, walkthroughs, comparisons — 54–79%), smaller on already-compact factual answers. paleo also cuts *context* tokens via `paleo-trim-context`, a layer Caveman cannot reach.

## Comparison

paleo is often compared with two other token-saving approaches: **Caveman** (a terse-persona system prompt) and **Ponytail** (a code-reuse coding skill). Here is how they differ.

| Dimension | 🦴 paleo | Caveman | Ponytail |
|---|---|---|---|
| **Form** | 4 composable skills | Single system prompt (persona) | Single coding skill / workflow |
| **What it targets** | Output tokens **+** old-turn context | Output tokens only | Volume of code the agent writes (+ MCP caching) |
| **Granularity** | Per-task, mix & match | One mode | One workflow |
| **Touches your code** | ❌ No (output/context only) | ❌ No | ⚠️ Yes — refactors / reuses code |
| **Context & reasoning savings** | ✅ `paleo-trim-context` | ❌ None | ◑ Partial (caching) |
| **Hard budget** | ✅ `paleo-budget` | ❌ | ❌ |
| **Cross-agent** | ✅ Claude / Codex / Gemini / Hermes | ➖ Portable prompt, but monolithic | ➖ Claude Code skill |
| **Activation** | Plain phrases | Edit system prompt | Install + invoke skill |
| **Reasoning-model safe** | ✅ Never compresses thought | ❌ Can *raise* tokens (e.g. +3% on Opus) | ➖ |
| **Known risk** | None (output-only) | Can fight "expand" heuristics; may *raise* tokens on reasoning models | Refactor can change behavior |
| **Open benchmark** | ✅ Reproducible harness | ❌ Claim only | ❌ Claim only |

> [!TIP]
> **They're complementary, not rivals.** Ponytail cuts the *code you have to write*; paleo cuts the *tokens in the conversation*. Caveman proved a terse prompt helps output — paleo takes that same idea and makes it modular, adds context-trimming and a hard budget, and drops the caveman persona. Use Ponytail for code-heavy work and paleo for chatty, long sessions.

## Tips & Triggers

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

## Installation

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

## Custom Skills

paleo is open — wire your own token-saving skills:

1. `skills/<your-name>/SKILL.md` with `name` + `description` frontmatter.
2. Register in `.claude-plugin/plugin.json` + `gemini-extension.json`.
3. Bump version badge (this file + footer) + plugin `version`.
4. Commit + push.

No repo edit needed — just drop any `SKILL.md` into your agent's skills dir (e.g. `~/.hermes/skills/<name>/`). paleo loads whatever it finds under `skills/`.

## Contributing

Contributions are welcome — new token-saving skills, better triggers, or benchmark data.

- Open an issue describing the skill or improvement.
- Keep `SKILL.md` files terse (they load into context).
- Add `name` + `description` frontmatter and register in both plugin manifests.
- Bump the version badge and `version` fields before opening a PR.

## License

MIT — see [LICENSE](./LICENSE).

---

<div align="center">

## Sponsors

<a href="https://kliqo.co"><img src="./assets/kliqo-banner.jpg" alt="Kliqo.co" width="420"></a>

**Kliqo.co** sponsors paleo · <a href="https://kliqo.co">kliqo.co</a>

🦴 paleo · v2.3.0 · MIT

</div>
