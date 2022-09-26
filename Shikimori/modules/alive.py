##MADE BY @KIRITO_1240

import random
import asyncio
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from Shikimori import pbot

PHOTO = [
    "https://telegra.ph/file/d7a5c3eb86548fcae64a8.jpg",
]

KIRITO = [
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ", url=f"https://t.me/UnmeiXBot?start=help"),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"http://t.me/UnmeiXBot?startgroup=true"),
    ],
]

@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    accha = await m.reply("⚡")
    await asyncio.sleep(2)
    await accha.edit("ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.3)
    await accha.edit("ᴀʟɪᴠɪɴɢ...")
    await accha.delete()
    await asyncio.sleep(1)
    umm = await m.reply_animation("https://telegra.ph/file/e00fa1d8eae64947f9a12.mp4")
    await asyncio.sleep(2)
    await umm.edit("ᴅᴇsᴛɪɴʏ")
    await asyncio.sleep(2)
    await umm.delete()
    await m.reply_photo(
        random.choice(PHOTO),
        caption=f"""**ʜᴇʏ​ ɪ ᴀᴍ ᴅᴇsᴛɪɴʏ​**
 ━━━━━━━━━━━━━━━━━━━
 » **ᴍʏ ʟᴏᴠᴇ :** ᴋɪʀɪᴛᴏ
 » **★ ɪ’ᴍ ᴏɴʟʏ ʜᴇʀᴇ sᴏ ʏᴏᴜ ᴄᴀɴ ᴀᴛʟᴇᴀsᴛ ʟɪᴠᴇ ʟɪᴋᴇ ᴀ ʜᴜᴍᴀɴ ʙᴇɪɴɢ**
 » **★ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [ᴋɪʀɪᴛᴏ](https://t.me/KIRITO_1240)**
 » **ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ʜᴇʀᴇ ❤️**
 ━━━━━━━━━━━━━━━━━━━""",
        reply_markup=InlineKeyboardMarkup(KIRITO)
    )
