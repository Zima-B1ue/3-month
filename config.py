from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import decouple
from decouple import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


TOKEN = config('TOKEN')

bot = Bot(TOKEN)
db = Dispatcher(bot=bot)