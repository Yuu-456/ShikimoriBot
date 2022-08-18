#This module was orignally programmed by VOID [gitub.com/voidxtoxic] 

from Shikimori import NETWORK_USERNAME, dispatcher
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode

from telegram.ext import (
    CallbackContext,
    CommandHandler,
)

PHOTO = "https://telegra.ph/file/267bcc4e46603f7fabfdd.jpg"

network_name = NETWORK_USERNAME.lower()

if network_name == "ezn_network":
    def EZN(update: Update, context: CallbackContext):

        TEXT = f"""
ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ [❛EZN❛ 𝘕𝘌𝘛𝘞𝘖𝘙𝘒](https://t.me/EZN_NETWORK),
EZN 𝙞𝙨 𝙖𝙣 𝙖𝙣𝙞𝙢𝙚 𝙗𝙖𝙨𝙚𝙙 𝘾𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮 𝙬𝙞𝙩𝙝 𝙖 𝙢𝙤𝙩𝙞𝙫𝙚 𝙩𝙤 𝙨𝙥𝙧𝙚𝙖𝙙 𝙡𝙤𝙫𝙚 𝙖𝙣𝙙 𝙥𝙚𝙖𝙘𝙚 𝙖𝙧𝙤𝙪𝙣𝙙 𝙩𝙚𝙡𝙚𝙜𝙧𝙖𝙢. 𝙂𝙤 𝙩𝙝𝙧𝙤𝙪𝙜𝙝 𝙩𝙝𝙚 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙖𝙣𝙙 𝙟𝙤𝙞𝙣 𝙩𝙝𝙚 𝘾𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮, 𝙞𝙛 𝙞𝙩 𝙙𝙧𝙖𝙬𝙨 𝙮𝙤𝙪𝙧 𝙖𝙩𝙩𝙚𝙣𝙩𝙞𝙤𝙣.
"""

        update.effective_message.reply_photo(
            PHOTO, caption= TEXT,
            parse_mode=ParseMode.MARKDOWN,

                reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text=" ❛EZN❛ 𝙉𝙚𝙩𝙬𝙤𝙧𝙠", url="https://t.me/EZN_NETWORK")],
                    [
                    InlineKeyboardButton(text="[ᴜꜱᴇʀ ᴛᴀɢ]", url="https://t.me/EZN_NETWORK"),
                    InlineKeyboardButton(text="[ᴏꜰꜰɪᴄɪᴀʟ ɢʀᴏᴜᴘ]", url="https://t.me/ANIMEXEZNCLUB")
                    ],
                ]
            ),
        )


    EZN_handler = CommandHandler(("EZN", "network", "net"), EZN, run_async = True)
    dispatcher.add_handler(EZN_handler)

    __help__ = """
    ──「❛EZN❛ 𝘕𝘌𝘛𝘞𝘖𝘙𝘒」──                         
    
    ❂ /EZN: Get information about our community! Using it in groups may create promotion so we don't support using it in groups."""
    
    __mod_name__ = "❛EZN❛"
