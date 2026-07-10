# paleo — repo guidance (Gemini CLI)

- Skills live in `skills/<name>/SKILL.md` with `name` + `description` frontmatter.
- Installable as a Gemini extension via `gemini-extension.json`.
- Register new skills in `gemini-extension.json` (skills array) and `.claude-plugin/plugin.json`.
- Keep `README.md` version badge (badge row + footer) and plugin `version` in sync.
- Never commit `.env` or `*.session` (git-ignored).

## Token budget (hard rule)
Skills load into the LLM context, so keep them token-minimal: caveman-compressed prose (drop filler, short clauses), exact code only. Smaller SKILL.md = cheaper + faster agents.
