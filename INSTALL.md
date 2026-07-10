# Install paleo

Pick the agent you use. All methods pull from the `paleo` repo on GitHub.

## Claude Code

```bash
claude plugin marketplace add https://github.com/mocasus/paleo
claude plugin install paleo@paleo
```

One plugin bundles all 6 skills: `paleo`, `paleo-trim-context`, `paleo-budget`, `paleo-converse`, `paleo-summary`, `paleo-json`.

## Codex / Cursor / Windsurf / Cline / 30+ agents

```bash
npx skills add mocasus/paleo
```

## Gemini CLI

```bash
gemini extensions install https://github.com/mocasus/paleo
```

## Hermes Agent

```bash
cp -r skills/paleo skills/paleo-trim-context skills/paleo-budget ~/.hermes/skills/
```

The skills load on the next Hermes session.

## Manual (any agent)

Clone and copy the skill folders you want:

```bash
git clone https://github.com/mocasus/paleo.git
cp -r paleo/skills/paleo ~/.hermes/skills/   # example: just the paleo skill
```

## Prerequisites

- No external dependencies — every skill is plain Markdown, nothing to install.
- For Hermes / Claude Code, just drop the `skills/<name>` folder into your agent's skills directory.

Never commit `.env` or `*.session` — they are git-ignored.
