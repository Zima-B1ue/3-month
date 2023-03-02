from aiogram import executor  # для запуска бота
import logging
from config import db

from handler import client, callback, admin, extra, fsm_anketa

fsm_anketa.reg_hand_anketa(db)
callback.reg_hand_callback(db)
client.reg_client(db)
admin.reg_ban(db)
extra.reg_hand_extra(db)
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)