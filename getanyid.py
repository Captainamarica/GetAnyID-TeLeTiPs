from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import Message
import os

bot = Client(
"Night Vission",
api_id = 16884543,
api_hash = "cc4535cefe1fa2e167d75a5e2ac24246",
bot_token = "5595279208:AAFH1UbljDXD6pVwC8UnM0K7QTOPWmGlMaM")

START_MESSAGE = "Heya im Test Bot"
START_MESSAGE_BUTTONS = [
[InlineKeyboardButton('CHANEL', url='https://t.me/NightVission')]
]

@bot.on_message(filters.command('start') & filters.private)
async def start(client, message):
    text = START_MESSAGE
    reply_markup = InlineKeyboardMarkup(START_MESSAGE_BUTTONS)
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )
	
print("Night Vission Test Bot Alive Chek It Now </>")
bot.run()
