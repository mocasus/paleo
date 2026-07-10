<div align="center">

![paleo logo](assets/logo.jpg)

[![Version](https://img.shields.io/badge/version-2.4.1-blue)](https://github.com/mocasus/paleo/releases) · [![License](https://img.shields.io/badge/license-MIT-green)](LICENSE) · [![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org) · [![Status](https://img.shields.io/badge/status-active-brightgreen)](https://github.com/mocasus/paleo) · [![Benchmarks](https://img.shields.io/badge/benchmarks-reproducible-orange)](BENCHMARK.md) · [![Agents](https://img.shields.io/badge/agents-40%2B-lightgrey)](https://agentskills.io)

# 🦴 paleo

> Token-saving skills for LLM agents — cut output & context tokens without choking the model.

[Why](#why-paleo) · [See it](#see-it-before--after) · [Features](#features) · [Skills](#skills) · [Combos](#recommended-combos) · [Quick Start](#quick-start) · [Benchmarks](#benchmarks) · [Comparison](#comparison) · [Tips](#tips--triggers) · [Install](#installation)

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

- [x] **Modular & composable** — load one skill or all six, mix per task.
- [x] **Output + context savings** — ~50–70% fewer output tokens (median ~54% on a 6-task sample — see [BENCHMARK.md](./BENCHMARK.md)), plus proactive context trimming.
- [x] **Production-safe** — compresses output and context only; never rewrites your code.
- [x] **Hard token budget** — `paleo-budget` caps spend and summarizes the tail.
- [x] **Cross-agent** — open Agent Skills standard: Claude Code, Codex, Gemini CLI, Qwen Code, OpenCode, Cursor, GitHub Copilot, Cline, Windsurf + **40+ agents** via `npx skills add`.
- [x] **Zero-setup triggers** — plain English phrases, no slash commands to register.
- [x] **Low overhead** — each `SKILL.md` is intentionally terse, so loading stays cheap.
- [x] **Open & extensible** — drop in your own token-saving skills.

## Skills

| Skill | What it does | Trigger example |
|---|---|---|
| `paleo` | Terse output mode — cut output tokens ~50–70%, keep code/terms exact. | `paleo mode` · `be brief` · `save tokens` |
| `paleo-trim-context` | Proactively trim/summarize context to save tokens without losing task state. | `trim context` (auto on long sessions) |
| `paleo-budget` | Hard token budget per task — cap spend, summarize if exceeded. | `budget 2000` · `stay under 2000 tokens` |
| `paleo-converse` | Condense old chat turns + merge duplicate messages; keep last N verbatim. | `condense chat` · `compress conversation` · `paleo-converse N=8` |
| `paleo-summary` | Tight intisari of bulky tool output / logs / diffs / dumps. | `tldr` · `condense this` · `summarize output` |
| `paleo-json` | Minify & compact structured/JSON output, stay parseable. | `compact json` · `minify` |

## Recommended combos

`paleo` is the base — keep it on. Layer the rest by what you're doing:

| Situation | Combo | Why |
|---|---|---|
| Daily driver (long / chatty sessions) | `paleo` + `paleo-trim-context` | Base + automatic context hygiene. |
| History piling up | + `paleo-converse` | Condense + merge duplicate turns once a session gets long. |
| Debugging / bulky tool output | `paleo` + `paleo-summary` + `paleo-json` | Logs → intisari; JSON → minified. |
| Tight cost / hard limit | `paleo` + `paleo-budget` (+ `paleo-trim-context`) | Hard ceiling + shrink context first. |
| Max savings (all on) | all six skills | Overkill daily, but safe for extreme thrift. |

> [!TIP]
> You rarely need every skill at once. `paleo` + `paleo-trim-context` is the default; add `paleo-converse` for messy chats, `paleo-summary` / `paleo-json` for heavy tool output, and `paleo-budget` only when a hard cap is required.

## Quick Start

```bash
# 1. Clone the collection
git clone https://github.com/mocasus/paleo.git

# 2. Claude Code — one plugin bundles all 6 skills
claude plugin marketplace add https://github.com/mocasus/paleo
claude plugin install paleo@paleo

# 3. Any agent via the open Agent Skills registry (installs to 40+ clients)
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
> Savings are task-dependent: biggest on verbose generative work (code, walkthroughs, comparisons — 54–79%), smaller on already-compact factual answers. paleo also cuts *context* tokens via `paleo-trim-context`, a layer a terse-persona prompt cannot reach.

## Comparison

paleo is often compared with two other token-saving approachesa **terse-persona system prompt** and **Ponytail** (a code-reuse coding skill). Here is how they differ.

| Dimension | 🦴 paleo | Terse-persona prompt | Ponytail |
|---|---|---|---|
| **Form** | 6 composable skills | Single system prompt (persona) | Single coding skill / workflow |
| **What it targets** | Output tokens **+** context **+** conversation turns | Output tokens only | Volume of code the agent writes (+ MCP caching) |
| **Granularity** | Per-task, mix & match | One mode | One workflow |
| **Touches your code** | ❌ No (output/context only) | ❌ No | ⚠️ Yes — refactors / reuses code |
| **Context & reasoning savings** | ✅ `paleo-trim-context` | ❌ None | ◑ Partial (caching) |
| **Hard budget** | ✅ `paleo-budget` | ❌ | ❌ |
| **Cross-agent** | ✅ 40+ agents (open standard) | ➖ Portable prompt, but monolithic | ➖ Claude Code skill |
| **Activation** | Plain phrases | Edit system prompt | Install + invoke skill |
| **Reasoning-model safe** | ✅ Never compresses thought | ❌ Can *raise* tokens (e.g. +3% on Opus) | ➖ |
| **Known risk** | None (output-only) | Can fight "expand" heuristics; may *raise* tokens on reasoning models | Refactor can change behavior |
| **Open benchmark** | ✅ Reproducible harness | ❌ Claim only | ❌ Claim only |

> [!TIP]
> **They're complementary, not rivals.** Ponytail cuts the *code you have to write*; paleo cuts the *tokens in the conversation*. Terse-persona prompts proved a terse prompt helps output — paleo takes that same idea and makes it modular, adds context-trimming and a hard budget, and drops the persona gimmick. Use Ponytail for code-heavy work and paleo for chatty, long sessions.

## FAQ

<details>
<summary><b>Prompt dipangkas, context dipotong, kualitas gak bakal sama dong?</b></summary>

Gak lebih jelek — malah sering lebih bagus. paleo bukan potong buta, dia buang *redundansi* (ulang-ulang, filler, boilerplate hasil tool, whitespace), bukan info esensial. Constraint, error, code, keputusan tetap utuh. Prompt lo gak diapa-apain — yang di-trim itu context kerja agent (hasil tool berulang, riwayat convo). Context bersih = model fokus ke signal, bukan lost track karena noise. Benchmark: median **53.8%** token turun, kualitas task gak drop. Trade-off jujur: budget ekstrem (token cap rendah banget) bisa turun kualitas, tapi setting *optional*. Intinya: lebih murah & cepet, kualitas tetap.

</details>

<details>
<summary><b>System prompt itu buat bikin model bagus, klo dipangkas banyak yg ilang dong?</b></summary>

paleo gak pernah sentuh system prompt. System prompt = aturan main, utuh 100%. Instruksi yang define behavior gak diapa-apain — paleo jalan *setelah* system prompt ke-load, cuma kerja di context dinamis. Yang di-trim itu context kerja (tool output berulang, convo kepanjangan), bukan instruksi. System prompt kecil dibanding noise yang numpuk dari tool output. Plus bisa whitelist bagian yang mau dijaga. Efeknya kebalik: context bersih bikin model *lebih* patuh ke system prompt. Aturan main tetep nempel.

</details>

<details>
<summary><b>Bisa ngerusak code / formatting gak?</b></summary>

Gak. paleo melindungi code block, structured output (JSON/table), dan error message secara default. Yang di-compress cuma prose bertele-tele & tool output redundant. Kalo masih ragu, bisa whitelist file/section tertentu biar 100% gak ke-trim.

</details>

<details>
<summary><b>Ini butuh API key atau service eksternal?</b></summary>

Enggak. paleo murni teknik prompt/context — gak ada server, gak ada API call, gak ada dependensi luar. Skill-nya tinggal di-load ke agent lo, jalan di lokal. No overengineering.

</details>

<details>
<summary><b>Token savings-nya beneran kelihatan di billing?</b></summary>

Kelihatan, terutama di session panjang & agent loop. Tiap token yang gak dikirim = gak dibayar. Benchmark kita median **53.8%** turun di context + output. Di agent yang muter 20+ tool call, itu selisih gede per run.

</details>

<details>
<summary><b>Works di semua model/provider?</b></summary>

Iya. paleo model-agnostic — kerja di level prompt & context, bukan di model tertentu. Claude, GPT, Gemini, GLM, Qwen, lokal — semua bisa. Sifatnya instruksi, bukan fine-tune.

</details>

<details>
<summary><b>Beda sama auto-compaction bawaan agent (Claude compaction, dll)?</b></summary>

Compaction bawaan itu generic & reaktif (baru jalan pas context mau penuh, sering blind truncation). paleo proaktif + selektif: jaga info esensial, buang redundansi, configurable, ada safety net (whitelist). Plus paleo juga ngurus output verbosity & tool-result summarization, bukan cuma convo history.

</details>

<details>
<summary><b>Cara enable/disable per task?</b></summary>

Trigger pakai natural language (`skip preamble`, `ringkas output`, `trim context`) — gak perlu slash command. Mau matiin? Tinggal gak dipanggil, atau cabut skill dari agent. No global lock-in.

</details>

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
**paleo-converse** — `condense chat` · `compress conversation` · `paleo-converse N=8`
**paleo-summary** — `tldr` · `condense this` · `summarize output`
**paleo-json** — `compact json` · `minify`

**Combo:** `paleo` + `paleo-budget` = max savings. Add `paleo-trim-context` on long sessions, `paleo-converse` on chatty ones, `paleo-summary` for bulky tool output.

</details>

## Installation

```bash
# Universal (any agent) — clone + copy skills manually
git clone https://github.com/mocasus/paleo.git
# copy skills/paleo*/ into your agent's skills directory

# Claude Code (one plugin bundles all 6 skills)
claude plugin marketplace add https://github.com/mocasus/paleo
claude plugin install paleo@paleo

# Codex / Cursor / Windsurf / 40+ agents (npx skills registry)
npx skills add mocasus/paleo

# Gemini CLI
gemini extensions install https://github.com/mocasus/paleo

# Hermes Agent
cp -r skills/paleo skills/paleo-trim-context skills/paleo-budget skills/paleo-converse skills/paleo-summary skills/paleo-json ~/.hermes/skills/
```

All 6 skills load automatically — `paleo`, `paleo-trim-context`, `paleo-budget`, `paleo-converse`, `paleo-summary`, `paleo-json`.

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

🦴 paleo · v2.4.1 · MIT

</div>
