from aiogram import Bot,Dispatcher,types
from aiogram.utils import executor
import logging
import decouple
from decouple import config



TOKEN = config('TOKEN')


bot = Bot(TOKEN)
db = Dispatcher(bot=bot)

if __name__ == '__main__':
    executor.start_polling(db,skip_updates=True)
