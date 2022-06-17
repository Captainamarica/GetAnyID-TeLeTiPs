from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import Message
import os

bot=Client(
    "Night Vission",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"]
)

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
