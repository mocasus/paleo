# Install paleo

## Quick (recommended)

```
npx skills add mocasus/paleo
```

This works for Claude Code, Codex, Gemini CLI, Hermes, Cursor, Copilot, and Windsurf.

## Per-agent

<details><summary>Claude Code</summary>

```
npx skills add mocasus/paleo -a claude-code
```
</details>

<details><summary>Codex</summary>

```
npx skills add mocasus/paleo -a codex
```
</details>

<details><summary>Gemini CLI</summary>

```
npx skills add mocasus/paleo -a gemini
```
</details>

<details><summary>Hermes Agent</summary>

```
hermes skills install mocasus/paleo
```
Or: `npx skills add mocasus/paleo -a hermes`
</details>

<details><summary>Cursor</summary>

```
npx skills add mocasus/paleo -a cursor
```
</details>

<details><summary>GitHub Copilot</summary>

```
npx skills add mocasus/paleo -a copilot
```
</details>

<details><summary>Windsurf</summary>

```
npx skills add mocasus/paleo -a windsurf
```
</details>

## Manual

```
git clone https://github.com/mocasus/paleo.git
cp -r paleo/skills/paleo* <your-agent-skills-dir>/
```

## Verify

In your agent chat, type `paleo`. Agent should respond tersely, code-first.

For auto-mode: `paleo-auto`.
