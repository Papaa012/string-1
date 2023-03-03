import asyncio

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    alt = await bot.get_me()
    me2 = alt.mention
    await bot.send_photo(
        chat_id=msg.chat.id,
          photo"https://telegra.ph/file/70663a8e4fde7e68ae311.jpg",
         caption=f"""**ʜᴇʏ✨❣️🥀 {msg.from_user.mention},
         
ɪ'ᴍ ,

ᴀ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ ꜱᴛʀɪɴɢ
ᴘᴏᴡᴇʀᴇᴅ ʙʏ :@iro_bot_support***🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🥀ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ🥀", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("✨ᴜᴘᴅᴀᴛᴇꜱ✨", url="https://t.me/iro_bot_support"),
                    InlineKeyboardButton(" ❣️ᴅᴇᴠᴇʟᴏᴩᴇʀ❣️ ", user_id=OWNER_ID)
                ]
            ]
        ),
    )
