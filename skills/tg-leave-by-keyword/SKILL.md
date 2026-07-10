---
name: tg-leave-by-keyword
description: Use when user wants to bulk-leave Telegram groups/channels by keyword (e.g. "leave all roblox groups"). Enumerate via MTProto userbot, then LeaveChannelRequest with dry-run + confirm.
version: 1.2.0
author: mocasus
license: MIT
metadata:
  hermes:
    tags: [telegram, telethon, mtproto, cleanup, userbot]
    related_skills: [tg-fetch-post]
---

# tg-leave-by-keyword
Bulk-leave Telegram groups/channels whose name/username contains a keyword, via MTProto userbot (Telethon). Groups + channels only.

## Need
- `pip install telethon python-dotenv`
- `.session` user-account file + `.env` (`TELEGRAM_API_ID`, `TELEGRAM_API_HASH`)
- Never commit `.env` / `*.session`.

## 1. Dry-run — enumerate matches
```python
import asyncio, os
from dotenv import load_dotenv
load_dotenv()
from telethon import TelegramClient

SESSION = os.getenv("TG_SESSION_PATH", "session.session")
API_ID = int(os.getenv("TELEGRAM_API_ID"))
API_HASH = os.getenv("TELEGRAM_API_HASH")
KEYWORD = "roblox"

async def main():
    client = TelegramClient(SESSION, API_ID, API_HASH)
    await client.start()
    hits = []
    async for d in client.iter_dialogs():
        ent = d.entity
        title = getattr(ent, "title", None) or getattr(ent, "username", None) or ""
        uname = getattr(ent, "username", None) or ""
        if KEYWORD in (str(title) + " " + str(uname)).lower():
            kind = "channel" if getattr(ent, "broadcast", False) else ("group" if d.is_group else "user")
            hits.append((d.id, kind, title, uname))
    for cid, kind, title, uname in hits:
        print(f"[{kind}] id={cid} | {title} | @{uname}")
    print(f"Found {len(hits)} matches")
    await client.disconnect()

asyncio.run(main())
```

## 2. Leave (after confirm)
```python
import asyncio, os
from dotenv import load_dotenv
load_dotenv()
from telethon import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.errors import FloodWaitError

TARGET_IDS = [-1001954950895, -1002228606855]  # from dry-run; skip kind=="user"

async def main():
    client = TelegramClient(os.getenv("TG_SESSION_PATH", "session.session"),
                            int(os.getenv("TELEGRAM_API_ID")), os.getenv("TELEGRAM_API_HASH"))
    await client.start()
    for cid in TARGET_IDS:
        try:
            await client(LeaveChannelRequest(await client.get_entity(cid)))
            print(f"LEFT {cid}")
        except FloodWaitError as e:
            print(f"FLOOD {cid}: {e.seconds}s"); await asyncio.sleep(e.seconds + 3)
        except Exception as e:
            print(f"ERR {cid}: {e!r}")
        await asyncio.sleep(2)
    await client.disconnect()

asyncio.run(main())
```

## Gotchas
- Bots/users: `LeaveChannelRequest` only works on groups + channels. Bot DM → block/delete instead; exclude `kind=="user"`.
- FloodWait: space ~2s between leaves; honor the wait. Don't batch-leave 5+ on a primary account without confirm.
- Wrong keyword: substring match can catch unintended groups — always dry-run first.
- Primary account: heavy automation risks restriction; prefer a throwaway.
