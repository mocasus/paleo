# 🦴 paleo

[![Benchmark](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/mocasus/paleo/main/bench/badge.json)](https://github.com/mocasus/paleo/blob/main/BENCHMARK.md)
[![npm](https://img.shields.io/npm/v/paleo?label=npm)](https://www.npmjs.com/package/paleo)
[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

**Token-saving skills for LLM agents.** Cut output & context tokens ~50-70% (median ~54%) without losing code/technical accuracy.

7 composable skills: terse mode, context trim, budget cap, conversation compress, summary, JSON compact, and auto-detect.

---

## Skills

| # | Skill | Trigger | What it does |
|---|---|---|---|
| 1 | `paleo` | `paleo` / `terse` | Terse output — no preambles, no "I'll do X now", code-first |
| 2 | `paleo-trim-context` | long session, big context | Proactively trim stale info from context window |
| 3 | `paleo-budget` | `budget 2000` / `token limit` | Hard token cap per task, summarize if exceeded |
| 4 | `paleo-converse` | `compress conversation` | Condense old turns, merge duplicates, keep last N verbatim |
| 5 | `paleo-summary` | `tldr` / bulky output | Shrink tool results, logs, diffs to concise intisari |
| 6 | `paleo-json` | `compact json` / `minify` | Minify structured output, collapse arrays, keep parseable |
| 7 | `paleo-auto` | `paleo-auto` / `auto paleo` | 🆕 Auto-detect session state and enable right skills automatically |

[Full skill reference →](https://github.com/mocasus/paleo/tree/main/skills)

---

## Quick Start

```
npx skills add mocasus/paleo
```

Or clone + copy:

```
git clone https://github.com/mocasus/paleo.git
```

### One-shot: activate all 6

In your agent chat, say `paleo` once — the agent loads the base skill which chains the others. For automatic mode: `paleo-auto`.

---

## Installation

<details>
<summary><strong>🐚 Claude Code</strong></summary>

```
# Install via skills CLI
npx skills add mocasus/paleo -a claude-code

# Or manual: copy to Claude skills directory
cp -r skills/paleo* ~/.claude/skills/
```

Plugin format available at `.claude-plugin/plugin.json`.
</details>

<details>
<summary><strong>⚡ Codex (OpenAI)</strong></summary>

```
# Install via skills CLI
npx skills add mocasus/paleo -a codex

# Or manual
cp -r skills/paleo* ~/.codex/skills/
```
</details>

<details>
<summary><strong>🔷 Gemini CLI</strong></summary>

```
# Install via skills CLI
npx skills add mocasus/paleo -a gemini

# Or manual: copy to Gemini skills path
cp -r skills/paleo*/ ./gemini/skills/
```

See `gemini-extension.json` for Gemini extension config.
</details>

<details>
<summary><strong>⚙️ Hermes Agent</strong></summary>

```
# Install via skills CLI
npx skills add mocasus/paleo -a hermes

# Or: Hermes built-in skills install
hermes skills install mocasus/paleo

# Or manual
cp -r skills/paleo* ~/.hermes/skills/
```

See [Hermes Integration](#hermes-integration) below for detailed setup.

</details>

<details>
<summary><strong>🖱️ Cursor</strong></summary>

```
npx skills add mocasus/paleo -a cursor
```
</details>

<details>
<summary><strong>👨‍💻 GitHub Copilot</strong></summary>

```
npx skills add mocasus/paleo -a copilot
```
</details>

<details>
<summary><strong>🌊 Windsurf</strong></summary>

```
npx skills add mocasus/paleo -a windsurf
```
</details>

---

## Hermes Integration

**I use Hermes myself — paleo is battle-tested here first.**

### Install

```
hermes skills install mocasus/paleo
```

### Manual trigger

Just type in your Hermes chat (Telegram, WhatsApp, etc.):

```
paleo
```

Or for auto-mode:

```
paleo-auto
```

### Example session

```
> [20 turns in, context filling up]
> paleo-auto
🦴 paleo-auto: enabled paleo + trim-context + converse (session length 22 turns)

> build a REST API with FastAPI
[terse, code-first response — no preamble]

> budget 2000
🦴 paleo-budget: 2000 output tokens, hard mode
```

### Tips
- `paleo` gives immediate token savings — start there
- `paleo-auto` watches your session and enables the right skills (best for >15 turns)
- Combine `paleo` + `budget` for expensive models (GPT-4, Claude Opus)
- Use `paleo-converse` when context hits 60%+ capacity

---

## Benchmarks

[![Benchmark](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/mocasus/paleo/main/bench/badge.json)](https://github.com/mocasus/paleo/blob/main/BENCHMARK.md)

Automated benchmark runs weekly via GitHub Actions. Each task is run with and without paleo, measuring delivery tokens.

**Latest**: median **~54%** savings across 12 task types.

| Task | Baseline | paleo | Savings |
|---|---|---|---|
| Code review | 1,847 | 891 | **51.8%** |
| Bug fix | 2,234 | 987 | **55.8%** |
| Architecture plan | 2,891 | 1,312 | **54.6%** |
| API design | 1,956 | 923 | **52.8%** |
| Config setup | 1,124 | 498 | **55.7%** |
| Documentation | 2,103 | 1,089 | **48.2%** |
| Debug log analysis | 2,645 | 1,156 | **56.3%** |
| Data pipeline | 2,478 | 1,203 | **51.5%** |
| Test generation | 1,892 | 812 | **57.1%** |
| Refactoring | 2,156 | 1,034 | **52.0%** |
| Shell scripting | 1,467 | 612 | **58.3%** |
| SQL queries | 1,345 | 598 | **55.5%** |

[Full benchmark methodology →](BENCHMARK.md) · [Run it yourself →](bench/benchmark.py)

---

## User Stats

> Share your numbers and get listed. PR your stats to the table below.

| User / Team | Agent | Tokens/month saved | Skills used |
|---|---|---|---|
| *[Your name here](https://github.com/mocasus/paleo/issues/new?title=stats)* | — | — | — |

### How to measure
1. Use agent for 1 week without paleo → note token usage from provider dashboard
2. Enable `paleo` or `paleo-auto` for 1 week → note new usage
3. Diff = your monthly savings (×4 for monthly estimate)

**Template for PR:**
```
| @yourgithub | claude-code | 1,200,000 | paleo + budget |
```

---

## Why paleo?

LLMs ship with verbose defaults — preambles, "Sure, I'll help...", re-stating context, over-explaining. That burns tokens on every single turn. paleo strips the fluff while keeping the code and accuracy intact.

### What it saves
- **Output tokens**: No preambles, no "let me explain", code-first
- **Context tokens**: Trim stale history, compress conversation, summarize bulky output
- **Structured tokens**: Minify JSON, collapse arrays

### What it doesn't touch
- Code correctness
- Technical accuracy
- File paths, IDs, error strings
- The user's latest instruction

---

## Contributing

New skill ideas? Optimization suggestions? [Open an issue](https://github.com/mocasus/paleo/issues) or PR.

### Local benchmark
```
IDROUTER_API_KEY=sk-... python3 bench/benchmark.py --model deepseek/deepseek-v4-pro
```

---

MIT © 2026. No AI/agent credit in this repo. Built for humans who read code.
