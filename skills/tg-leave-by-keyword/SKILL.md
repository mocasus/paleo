---
name: tg-leave-by-keyword
description: Use when the user wants to leave or bulk-clean Telegram groups/channels by keyword (e.g. "leave all roblox groups"). Finds matching dialogs via an MTProto userbot (Telethon) and leaves them, with dry-run + confirmation guards.
version: 1.0.0
author: mocasus
license: MIT
metadata:
  hermes:
    tags: [telegram, telethon, mtproto, cleanup, userbot]
    related_skills: []
---

# Telegram Leave-by-Keyword

Bulk-leave Telegram groups and channels whose name/username matches a keyword, using a real
Telegram user account (MTProto / Telethon). Built for cleanup of stale or mass-joined groups — not for bots.

## When to Use
- User says "leave all <keyword> groups", "clean up telegram", "keluar dari grup roblox", etc.
- You need to enumerate dialogs by keyword before taking action.
- **Don't use for:** Bot API bots (they cannot leave user groups), or leaving one known group (just do it directly).

## Prerequisites
- Python 3.10+, `pip install telethon python-dotenv`
- A Telegram user-account session file (`.session`) — sign in once via Telethon.
- API credentials in `.env`: `TELEGRAM_API_ID`, `TELEGRAM_API_HASH`.
- **Never commit `.env` or `*.session`** (see repo `.gitignore`).

## Dry-run first (always)
Enumerate before leaving so the user can verify scope:

```python
import asyncio, os
from dotenv import load_dotenv
load_dotenv()
from telethon import TelegramClient

SESSION = os.getenv("TG_SESSION_PATH", "session.session")
API_ID = int(os.getenv("TELEGRAM_API_ID"))
API_HASH = os.getenv("TELEGRAM_API_HASH")
KEYWORD = "roblox"  # case-insensitive substring

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

## Leave (after confirmation)
```python
import asyncio, os
from dotenv import load_dotenv
load_dotenv()
from telethon import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.errors import FloodWaitError

# Populate from the dry-run output; skip kind=="user" if you only want groups+channels
TARGET_IDS = [-1001954950895, -1002228606855]

async def main():
    client = TelegramClient(os.getenv("TG_SESSION_PATH", "session.session"),
                            int(os.getenv("TELEGRAM_API_ID")), os.getenv("TELEGRAM_API_HASH"))
    await client.start()
    for cid in TARGET_IDS:
        try:
            ent = await client.get_entity(cid)
            await client(LeaveChannelRequest(ent))
            print(f"LEFT {cid}")
        except FloodWaitError as e:
            print(f"FLOOD {cid}: wait {e.seconds}s"); await asyncio.sleep(e.seconds + 3)
        except Exception as e:
            print(f"ERR {cid}: {e!r}")
        await asyncio.sleep(2)
    await client.disconnect()

asyncio.run(main())
```

## Pitfalls
1. **Bots/users can't be "left".** `LeaveChannelRequest` works on groups + channels (supergroups/broadcast).
   For a bot DM, use block/delete-chat instead — exclude `kind == "user"` from targets.
2. **FloodWait on bulk leave.** Space ~2s between leaves; honor `FloodWaitError` sleeps.
   Never batch-leave 5+ on a primary account without explicit confirmation.
3. **Wrong keyword matches.** Always dry-run first — substring match can catch unintended groups.
4. **Primary-account risk.** Heavy automation on a personal primary account risks restriction.
   Prefer a throwaway account for bulk ops.

## Verification
- [ ] Dry-run lists only the expected dialogs
- [ ] User confirmed the leave scope
- [ ] After leave, re-run dry-run → 0 matches
- [ ] No `FloodWaitError` left unhandled
