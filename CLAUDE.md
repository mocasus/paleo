# paleo — repo guidance

- Skills live in `skills/<name>/SKILL.md`.
- Every SKILL.md MUST start with YAML frontmatter containing `name` and `description`.
- `name`: lowercase, hyphens, <=64 chars. `description`: <=1024 chars, starts with "Use when ...".
- Register each skill in `.claude-plugin/plugin.json` (skills array) and `gemini-extension.json`.
- Bump the version badge in README.md (badge row + footer) and the plugin `version` on every change.
- Never commit `.env` or `*.session` (git-ignored).

## Token budget (hard rule)
Skills load into the LLM context, so they MUST be token-minimal:
- Prose: caveman-compressed — drop filler/articles, short clauses, one idea per line.
- Code + technical terms (API names, CLI commands, error strings) stay EXACT. Never abbreviate them.
- No redundant examples. Smaller SKILL.md = cheaper + faster agents.
