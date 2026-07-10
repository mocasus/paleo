# paleo — repo guidance

- Skills live in `skills/<name>/SKILL.md`.
- Every SKILL.md MUST start with YAML frontmatter containing `name` and `description`.
- `name`: lowercase, hyphens, <=64 chars. `description`: <=1024 chars, starts with "Use when ...".
- Register each skill in `.claude-plugin/plugin.json` (skills array) and `gemini-extension.json`.
- Bump the version badge in README.md (badge row + footer) and the plugin `version` on every change.
- Never commit `.env` or `*.session` (git-ignored).

## Token budget (hard rule)
Skills are loaded into the LLM context, so they MUST be token-minimal:
- No filler prose, no restated intros, no redundant examples.
- Keep code/commands byte-exact and necessary only.
- Use terse bullets; one idea per line.
- Smaller SKILL.md = cheaper + faster agents.
