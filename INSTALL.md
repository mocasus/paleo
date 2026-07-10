# Install paleo

Pick the agent you use. All methods pull from `mocasus/paleo` on GitHub.

## Claude Code

```bash
claude plugin marketplace add mocasus/paleo
claude plugin install tg-leave-by-keyword@paleo
```

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
cp -r skills/tg-leave-by-keyword ~/.hermes/skills/software-development/
```

The skill loads on the next Hermes session.

## Manual (any agent)

Clone and copy the skill folder you want:

```bash
git clone https://github.com/mocasus/paleo.git
cp -r paleo/skills/tg-leave-by-keyword <your-agent-skills-dir>/
```

## Prerequisites for `tg-leave-by-keyword`

- Python 3.10+ and `pip install telethon python-dotenv`
- A Telegram user-account `.session` file (sign in once via Telethon)
- `.env` with `TELEGRAM_API_ID` and `TELEGRAM_API_HASH`

Never commit `.env` or `*.session` — they are git-ignored.
