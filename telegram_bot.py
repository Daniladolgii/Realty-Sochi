from telegram import Bot
from config import BOT_TOKEN, CHANNEL_ID

def send_message_to_telegram(message):
    bot = Bot(token=BOT_TOKEN)
    try:
        bot.send_message(chat_id=CHANNEL_ID, text=message)
   
