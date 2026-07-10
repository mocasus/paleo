---
name: tg-fetch-post
description: Use when user pastes a t.me channel/post link (or channel + msg id) and wants the post extracted — text, linked URL/preview, inline buttons. Fetches via MTProto userbot (Telethon).
version: 1.3.0
author: mocasus
license: MIT
metadata:
  hermes:
    tags: [telegram, telethon, mtproto, fetch, scrape]
    related_skills: [tg-leave-by-keyword, tg-list-dialogs]
---

# tg-fetch-post
Pull TG post text + webpage preview + buttons from `t.me/<channel>/<id>`. MTProto userbot.

## Need
- `pip install telethon python-dotenv`
- `.session` user file + `.env` (`TELEGRAM_API_ID`, `TELEGRAM_API_HASH`)
- Never commit `.env`/`*.session`

## Fetch (resolve entity first)
```python
import asyncio, os, re
from dotenv import load_dotenv
load_dotenv()
from telethon import TelegramClient

SESSION = os.getenv("TG_SESSION_PATH", "session.session")
API_ID = int(os.getenv("TELEGRAM_API_ID"))
API_HASH = os.getenv("TELEGRAM_API_HASH")
LINK = "https://t.me/kiroglobal_channel/15"   # t.me/<channel>/<id>

async def main():
    u, mid = re.search(r"t\.me/([^/]+)/(\d+)", LINK).groups()
    mid = int(mid)
    client = TelegramClient(SESSION, API_ID, API_HASH)
    await client.start()
    msg = await client.get_messages(await client.get_entity(u), ids=mid)
    print("TEXT:\n", msg.message)
    if msg.media and getattr(msg.media, "webpage", None):
        wp = msg.media.webpage
        print("URL:", wp.url, "| TITLE:", wp.title, "\nDESC:", wp.description)
    if msg.buttons:
        for row in msg.buttons:
            for b in row:
                print("BTN:", b.text, "| url:", b.url)
    await client.disconnect()

asyncio.run(main())
```

## Gotchas
- `get_messages("https://t.me/...")` → `ValueError: Cannot find any entity`. `get_entity(username)` first.
- Post = buttons (`msg.buttons`) OR webpage (`msg.media.webpage`). Check both.
- Deleted/id gap → `get_messages` returns `None`.
- Cold `get_entity` may FloodWait. Retry after wait.
