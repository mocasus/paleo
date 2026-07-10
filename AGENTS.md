# paleo

Token-saving skills for LLM agents. Cut output & context tokens without rewriting code — compress *verbosity*, keep code, commands, and technical terms byte-exact.

## Install (open Agent Skills standard)
```bash
npx skills add mocasus/paleo
```
Installs all 4 skills into every supported agent: Claude Code, Codex, Gemini CLI, Qwen Code, OpenCode, Cursor, GitHub Copilot, Cline, Windsurf, and 40+ clients.

Or clone and copy `skills/paleo*/` into your agent's skills directory.

## Skills
- `paleo` — terse output mode (cut output tokens ~50–70%, code-exact)
- `paleo-trim-context` — proactive context trimming before overflow
- `paleo-skip-preamble` — strip greetings / apologies / hedging
- `paleo-budget` — hard token budget per task, auto-summarize over cap

## Triggers (plain phrases, no slash commands)
`paleo mode` · `save tokens` · `be brief` · `budget 2000` · `trim context`

Full docs + reproducible benchmarks: see [README.md](./README.md).
