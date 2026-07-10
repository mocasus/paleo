---
name: tg-fetch-post
description: Use when user pastes a t.me channel/post link (or channel + msg id) and wants the post extracted — text, linked URL/preview, inline buttons. Fetches via MTProto userbot (Telethon).
version: 1.2.0
author: mocasus
license: MIT
metadata:
  hermes:
    tags: [telegram, telethon, mtproto, fetch, scrape]
    related_skills: [tg-leave-by-keyword]
---

# tg-fetch-post
Extract a Telegram post's text, web-page preview (URL/title/desc), and inline buttons from a `t.me/<channel>/<id>` link or channel username + message id, via MTProto userbot (Telethon).

## Need
- `pip install telethon python-dotenv`
- `.session` user-account file + `.env` (`TELEGRAM_API_ID`, `TELEGRAM_API_HASH`)
- Never commit `.env` / `*.session`.

## Fetch (resolve entity first — URL lookups fail)
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
- `get_messages("https://t.me/...")` → `ValueError: Cannot find any entity`. Always `get_entity(username)` first, then `get_messages(entity, ids=<id>)`.
- A post has either inline buttons (`msg.buttons`) OR a web-page preview (`msg.media.webpage`) — check both.
- Deleted/inaccessible id → `get_messages` returns `None`.
- Cold `get_entity` may FloodWait (~seconds) after idle; retry after the wait.
