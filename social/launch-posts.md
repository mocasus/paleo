# paleo — Launch Posts

Draft social posts to drive stars/adoption. Copy-paste ready.

---

## X / Twitter Thread

**1/**
🦴 paleo — token-saving skills for LLM agents.
Cut output & context tokens without choking the model.
No persona gimmicks. No code rewrite. Measured, not claimed. 🧵

**2/**
The problem: agents burn tokens on filler, preamble, and bloated context.
That's real $ and latency on every turn.
paleo attacks all 4 vectors 👇

**3/**
▸ `paleo` — aggressive verbosity compression (drop filler, keep code exact)
▸ `paleo-trim-context` — proactive context trim before overflow
▸ `paleo-budget` — hard token ceiling, auto-summarize

**4/**
Honest before/after. Same code, fewer words:
`function forceRerender(){ setState(s => !s); }` stays 100% exact.
"Great question! Let me help you with that…" → gone.

**5/**
We measured it.
10-turn synthetic harness — median 53.8% output reduction vs verbose baseline,
0 correctness regression on a reasoning model.
Reproducible: `python3 bench/benchmark.py`

**6/**
Terse-persona prompts claim 30–40% on output. Ponytail does conversation-only.
paleo does output + context + hard budget.
And we open the benchmark. They don't.

**7/**
Works with Claude Code, Codex, Gemini CLI, OpenCode, Qwen Code.
~3.5k chars total. MIT.
👉 github.com/mocasus/paleo
Star if you're tired of paying for filler.

---

## LinkedIn Post

**Headline:** I shipped paleo — token-saving skills that cut LLM agent costs without dumbing down the output.

Most token-saving tools make one of two mistakes: they either rewrite your code into something unreadable, or they wrap everything in a "persona" gimmick that doesn't survive contact with a real codebase.

paleo takes a different path. It's a set of pluggable agent skills that compress *verbosity* — filler words, preamble, redundant context — while leaving code, identifiers, and logic byte-for-byte intact.

What's inside:
• **paleo** — aggressive output compression, code-exact
• **paleo-trim-context** — trims context before it overflows the window
• **paleo-budget** — hard token ceiling with automatic summarization

The part I'm proudest of: it's *measured*, not marketed. A reproducible 10-turn benchmark shows a median 53.8% output reduction with zero correctness regression on a reasoning model. No screenshots of a single lucky run — clone it, run `python3 bench/benchmark.py`, see your own numbers.

Rivals in this space publish percentage claims with no way to verify them. paleo ships the harness.

MIT licensed, ~3.5k chars, works with Claude Code / Codex / Gemini CLI / OpenCode / Qwen Code.

→ github.com/mocasus/paleo

If you've ever watched your agent bill climb for words nobody reads, give it a star and try the benchmark.

---

## Reddit (r/LocalLLaMA / r/ClaudeAI) — short

Title: **paleo — token-saving agent skills (output + context), measured 54% median cut, code-exact, MIT**

Body:
I built paleo after getting frustrated that every "token saver" either mangled my code or was just a persona prompt. paleo compresses *verbosity* only — filler, preamble, bloated context — and leaves code byte-for-byte intact.

6 skills: paleo (output compression), paleo-trim-context, paleo-budget (hard ceiling), paleo-converse, paleo-summary, paleo-json. Works with Claude Code / Codex / Gemini CLI / OpenCode / Qwen Code.

Unlike competitors that publish unverifiable % claims, paleo ships a reproducible benchmark: `python3 bench/benchmark.py` → median 53.8% output reduction, 0 correctness regression.

github.com/mocasus/paleo — MIT, feedback welcome.
