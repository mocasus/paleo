---
name: paleo-trim-context
description: Use when context window is large / token cost high / long session. Proactively trim, summarize, or drop stale content to save context tokens without losing the task state.
version: 2.0.0
author: mocasus
license: MIT
metadata:
  hermes:
    tags: [tokens, context, trim, summarize, efficiency]
    related_skills: [paleo, paleo-skip-preamble]
---

# paleo-trim-context
Keep context small. Drop stale, keep task state.

## Rules
- Summarize old tool output into 1-2 lines; keep only the result that matters.
- Drop: resolved errors, obsolete file reads, duplicate logs.
- Keep: current plan, open TODO, key IDs/paths, last decision.
- Use session_search / notes for history instead of re-pasting.
- Prefer code/script over long prose explanations in context.

## When
- Long session (>20 turns), big file dumps, repeated similar output.
- Before calling expensive model — shrink first.

## Gotchas
- Don't trim the user's latest instruction.
- Keep ground truth (file paths, IDs) — summarize derivations only.
- If unsure what's stale, ask once. Don't guess-drop critical state.
