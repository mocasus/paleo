---
name: tg-list-dialogs
description: Use when user wants to list or export all Telegram dialogs (groups, channels, DMs) with id, type, title — for inventory or cleanup prep. Via MTProto userbot (Telethon).
version: 1.0.0
author: mocasus
license: MIT
metadata:
  hermes:
    tags: [telegram, telethon, mtproto, inventory, userbot]
    related_skills: [tg-leave-by-keyword, tg-fetch-post]
---

# tg-list-dialogs
Dump all TG dialogs: id, type, title, username. Inventory / cleanup prep. MTProto userbot.

## Need
- `pip install telethon python-dotenv`
- `.session` user file + `.env` (`TELEGRAM_API_ID`, `TELEGRAM_API_HASH`)
- Never commit `.env`/`*.session`

## List + export JSON
```python
import asyncio, os, json
from dotenv import load_dotenv
load_dotenv()
from telethon import TelegramClient

SESSION = os.getenv("TG_SESSION_PATH", "session.session")
API_ID = int(os.getenv("TELEGRAM_API_ID"))
API_HASH = os.getenv("TELEGRAM_API_HASH")

async def main():
    client = TelegramClient(SESSION, API_ID, API_HASH)
    await client.start()
    out = []
    async for d in client.iter_dialogs():
        ent = d.entity
        kind = "channel" if getattr(ent, "broadcast", False) else ("group" if d.is_group else ("user" if d.is_user else "other"))
        out.append({
            "id": d.id,
            "type": kind,
            "title": getattr(ent, "title", None) or getattr(ent, "username", None) or getattr(ent, "first_name", None),
            "username": getattr(ent, "username", None),
        })
    print(json.dumps(out, indent=2))
    await client.disconnect()

asyncio.run(main())
```

## Gotchas
- `iter_dialogs()` walks all (groups, channels, DMs). Filter `type` for subset.
- Big account = many dialogs. Dump to file: `json.dump(out, open("dialogs.json","w"))`.
- Never commit `dialogs.json` — leaks private chat names. Git-ignore it.
