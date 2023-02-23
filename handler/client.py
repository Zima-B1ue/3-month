from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot

async def start_handler(massage: types.Message):
    await bot.send_message(massage.from_user.id, f'привет {massage.from_user.first_name}')
    await massage.answer('это ансфер')
    await massage.reply(massage.from_user.first_name)



async def   quiz1(massage: types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next', callback_data='button')
    markup.add(button)

    ques = 'кто ты воин?'
    answer = [
        'Бетмен-рыцарь ночи',
        'томас шелби из семьи острые козырьки',
        'спанч боб:квадратные штаны',
        'Ахилес! Сын пелея ',
        'диктор канала "Мастерская настроения"',
        'оптимус прайм последний прайм'
    ]

    await bot.send_poll(
        chat_id=massage.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='ты ахилесс',
        open_period=15,
        reply_markup=markup
    )
async def info_hand(message:types.Message):
    await message.answer('новоя функция')
def reg_client(db:Dispatcher):
    db.register_message_handler(start_handler, commands=['start', 'hello'])
    db.register_message_handler(quiz1, commands=['quiz'])
    db.register_message_handler(info_hand, commands=['info'])