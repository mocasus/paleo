# paleo — repo guidance (Gemini CLI)

- Skills live in `skills/<name>/SKILL.md` with `name` + `description` frontmatter.
- This repo is installable as a Gemini extension via `gemini-extension.json`.
- Register new skills in `gemini-extension.json` (skills array) and `.claude-plugin/plugin.json`.
- Keep `README.md` version badge (badge row + footer) and plugin `version` in sync.
- Never commit `.env` or `*.session` (git-ignored).

## Token budget (hard rule)
Skills load into the LLM context, so keep them token-minimal: no filler prose, exact code only, terse bullets. Smaller SKILL.md = cheaper + faster agents.
