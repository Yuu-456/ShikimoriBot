"""
STATUS: Code is working. ✅
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from Shikimori.vars import ALIVE_MEDIA, UPDATE_CHANNEL, SUPPORT_CHAT, OWNER_USERNAME, NETWORK, NETWORK_USERNAME
from Shikimori import dispatcher
from Shikimori.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

bot_name = f"{dispatcher.bot.first_name}"

ALIVE_ID = ALIVE_MEDIA.split(".")
alive_id = ALIVE_ID[-1]

SHIKIMORI = [
        [
        InlineKeyboardButton(
            text="Updates",
            url=f"https://t.me/{UPDATE_CHANNEL}"),
        InlineKeyboardButton(
            text="Support",
            url=f"https://t.me/{SUPPORT_CHAT}"),
        ],
     ]
@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(1)
    await accha.edit("ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.1)
    await accha.edit("ᴀʟɪᴠɪɴɢ ʙᴀʙʏ ....")
    await accha.delete()
    await asyncio.sleep(0.1)
    umm = await m.reply_sticker(
        "CAACAgUAAx0CZIiVngABBHAzYwdi9OIVTQ7DYELAqMl46fgnK4wAAjsIAAKagolX-O0V64tvzK8pBA"
    )
    await asyncio.sleep(0.1)

    TEXT = f"""
    <b>Hi <a href="tg://user?id={user.id}">{first_name}</a>, I'm {bot_name} Robot.

⚪ I'm Working Properly

⚪ My Owner : <a href="https://t.me/{OWNER_USERNAME}">{OWNER_USERNAME}</a></b>
    """
    if NETWORK:
        TEXT = TEXT + f'\n⚪ <b>I am Powered by : <a href="https://t.me/{NETWORK_USERNAME}">{NETWORK}</a>\n\n' + 'Thanks For Adding Me Here ❤️</b>'
    
    else:
        TEXT = TEXT + "\n<b>Thanks For Adding Me Here ❤️</b>"

    try:
        if alive_id in ("jpeg", "jpg", "png"):
            message.reply_photo(ALIVE_MEDIA, caption=TEXT, reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.HTML)
        elif alive_id in ("mp4", "mkv"):
            message.reply_video(ALIVE_MEDIA, caption=TEXT, reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.HTML)
        elif alive_id in ("gif", "webp"):
            message.reply_animation(ALIVE_MEDIA, caption=TEXT, reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.HTML)
        else:
            message.reply_text(TEXT, reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.HTML)

    except:
        message.reply_text(TEXT, reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.HTML)

ALIVE_HANDLER = DisableAbleCommandHandler("alive", awake, run_async=True)
dispatcher.add_handler(ALIVE_HANDLER)
__command_list__ = ["alive"]
__handlers__ = [
    ALIVE_HANDLER,
]

__mod_name__ = "Alive ✨"
__help__ = """
*ALIVE*
 ❍ `/alive` :Check BOT status
"""
