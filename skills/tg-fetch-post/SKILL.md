---
name: tg-fetch-post
description: Use when the user pastes a t.me channel/post link (or gives a channel username + message id) and wants the post content extracted — text, linked URL/preview, and inline buttons. Fetches via MTProto userbot (Telethon).
version: 1.0.0
author: mocasus
license: MIT
metadata:
  hermes:
    tags: [telegram, telethon, mtproto, fetch, scrape]
    related_skills: [tg-leave-by-keyword]
---

# Telegram Fetch Post

Extract the content of a Telegram channel/group post given a `t.me/<channel>/<id>` link or a channel
username + message id, using a real Telegram user account (MTProto / Telethon). Returns the message text,
any web-page preview URL/title/description, and inline button labels/URLs.

## When to Use
- User pastes a `https://t.me/.../<id>` link and asks "what's in this" / "ambil isinya".
- You need the linked URL or button targets from a post.
- **Don't use for:** private chats you're not a member of, or DMs (resolve by entity id instead).

## Prerequisites
- `pip install telethon python-dotenv`
- User-account `.session` file + `.env` with `TELEGRAM_API_ID` / `TELEGRAM_API_HASH`.
- Never commit `.env` / `*.session`.

## Fetch by link (resolve entity first — URL lookups fail)
```python
import asyncio, os, re
from dotenv import load_dotenv
load_dotenv()
from telethon import TelegramClient

SESSION = os.getenv("TG_SESSION_PATH", "session.session")
API_ID = int(os.getenv("TELEGRAM_API_ID"))
API_HASH = os.getenv("TELEGRAM_API_HASH")

LINK = "https://t.me/kiroglobal_channel/15"   # t.me/<channel>/<id>
m = re.search(r"t\.me/([^/]+)/(\d+)", LINK)
username, msg_id = m.group(1), int(m.group(2))

async def main():
    client = TelegramClient(SESSION, API_ID, API_HASH)
    await client.start()
    entity = await client.get_entity(username)          # resolve first
    msg = await client.get_messages(entity, ids=msg_id)
    print("TEXT:\n", msg.message)
    if msg.media and getattr(msg.media, "webpage", None):
        wp = msg.media.webpage
        print("URL:", wp.url, "| TITLE:", wp.title)
        print("DESC:", wp.description)
    if msg.buttons:
        for row in msg.buttons:
            for b in row:
                print("BTN:", b.text, "| url:", b.url)
    await client.disconnect()

asyncio.run(main())
```

## Pitfalls
1. **`get_messages("https://t.me/...")` raises `ValueError: Cannot find any entity`.** Always
   `get_entity(username)` first, then `get_messages(entity, ids=<id>)`.
2. **Buttons vs webpage.** A post's interactive content is either inline buttons (`msg.buttons`) or a
   web-page preview (`msg.media.webpage`) — check both.
3. **Forwarded/empty posts.** `get_messages` can return `None` for deleted or inaccessible ids.
4. **FloodWait on cold `get_entity`.** First username resolve after idle may FloodWait (~seconds). Retry after the wait.

## Verification
- [ ] Entity resolved without error
- [ ] Text printed matches the post
- [ ] Linked URL / button targets captured when present
