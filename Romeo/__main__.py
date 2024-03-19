import asyncio
import importlib
from pyrogram import Client, idle
from Romeo import client, app

async def start_bot(salam):
    await app.start()
    print("LOG: Əsas Bot token Booting..")
    print("USERBOT UĞURLA BAŞLADI✅✅")
    await client.start()
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
