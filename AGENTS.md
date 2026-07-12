# paleo

Token-saving skills for LLM agents. Cut output & context tokens without rewriting code — compress *verbosity*, keep code, commands, and technical terms byte-exact.

## Install (open Agent Skills standard)
```
npx skills add mocasus/paleo
```
Installs all 7 skills into every supported agent: Claude Code, Codex, Gemini CLI, Hermes, Cursor, GitHub Copilot, Windsurf, and 40+ clients.

Or clone and copy `skills/paleo*/` into your agent's skills directory.

## Skills
- `paleo` — terse output mode (cut output tokens ~50–70%, code-exact)
- `paleo-trim-context` — proactive context trimming before overflow
- `paleo-budget` — hard token budget per task, auto-summarize over cap
- `paleo-converse` — conversation compression, merge duplicates
- `paleo-summary` — shrink bulky tool output to tight intisari
- `paleo-json` — compact structured output, minify + collapse
- `paleo-auto` — 🆕 zero-touch auto-detection, enables right skills automatically

## Triggers (plain phrases, no slash commands)
`paleo mode` · `save tokens` · `be brief` · `budget 2000` · `trim context` · `paleo-auto`

Full docs + reproducible benchmarks: see [README.md](./README.md).
