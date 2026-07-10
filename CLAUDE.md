# paleo — repo guidance

Token-saving skill collection. Skills make LLM usage cheaper: compress output, trim context, skip filler.

- Skills live in `skills/<name>/SKILL.md`.
- Every SKILL.md MUST start with YAML frontmatter: `name` + `description`.
- `name`: lowercase, hyphens, <=64 chars. `description`: <=1024 chars, starts with "Use when ...".
- Register each skill in `.claude-plugin/plugin.json` + `gemini-extension.json`.
- Bump version badge in README.md (badge row + footer) + plugin `version` on every change.
- Never commit `.env` / `*.session` (git-ignored).

## Token budget (hard rule)
Skills load into the LLM context, so they MUST be token-minimal:
- Prose: caveman-compressed — drop filler/articles, short clauses, one idea per line.
- Code + technical terms (API names, CLI commands, error strings) stay EXACT. Never abbreviate.
- No redundant examples. Smaller SKILL.md = cheaper + faster agents.
