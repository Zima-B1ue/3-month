from aiogram import Dispatcher,Bot
from decouple import config

TOKEN = config('TOKEN')
# TOKEN='6226973447:AAFdY9l51fisGvXGr5gzs5gKt0uqzgES4O8'

bot = Bot(TOKEN)
db = Dispatcher(bot=bot)

