from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor  # для запуска бота
import logging
import decouple
from decouple import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
TOKEN='6226973447:AAFdY9l51fisGvXGr5gzs5gKt0uqzgES4O8'

bot = Bot(TOKEN)
db = Dispatcher(bot=bot)



@db.message_handler(commands=['start', 'hello'])
async def start_handler(massage: types.Message):
    await bot.send_message(massage.from_user.id, f'привет {massage.from_user.first_name}')
    await massage.answer('это ансфер')
    await massage.reply(massage.from_user.first_name)


@db.message_handler(commands=['button'])
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


@db.callback_query_handler(text='button')
async def quiz2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next', callback_data='button2')
    markup.add(button)
    ques = 'куда?'
    answer = [
        'Судная ночь',
        'Фильм Ававта 2',
        'Уроки Бекболота ',
        'Тик-ток'
    ]
    photo = open('media/mem.jpg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='Тик-ток',
        open_period=30,
        reply_markup=markup
    )

@db.callback_query_handler(text='button2')
async def quiz3(call: types.CallbackQuery):
    answer = [
        'BMW',
        'Volcvagen',
        'Жигули',
        'нету правельного ответа',

    ]
    ques = 'Какое это Авто?'
    photo = open('media/mem2.jpg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='нету правельного ответа!',
        open_period=30)


@db.message_handler()
async def echo(massage: types.Message):
    await bot.send_message(massage.from_user.id, massage.text)
    await massage.answer('что-то еще?')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)