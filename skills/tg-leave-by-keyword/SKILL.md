---
name: tg-leave-by-keyword
description: Use when user wants to bulk-leave Telegram groups/channels by keyword (e.g. "leave all roblox groups"). Enumerate via MTProto userbot, then LeaveChannelRequest with dry-run + confirm.
version: 1.3.0
author: mocasus
license: MIT
metadata:
  hermes:
    tags: [telegram, telethon, mtproto, cleanup, userbot]
    related_skills: [tg-fetch-post, tg-list-dialogs]
---

# tg-leave-by-keyword
Bulk-leave TG groups/channels by keyword. MTProto userbot. Groups+channels only.

## Need
- `pip install telethon python-dotenv`
- `.session` user file + `.env` (`TELEGRAM_API_ID`, `TELEGRAM_API_HASH`)
- Never commit `.env`/`*.session`

## 1. Dry-run — find matches
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
- `LeaveChannelRequest` = groups+channels only. Bot DM → block/delete. Drop `kind=="user"`.
- FloodWait: ~2s gap between leaves. No 5+ batch on main account w/o confirm.
- Substring match catches wrong groups. Dry-run first.
- Main account heavy use = ban risk. Use throwaway.
