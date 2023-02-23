from aiogram import Dispatcher,types
from config import bot
async def quiz3(call: types.CallbackQuery):
    answer = [
        'повар спрашивает повара',
        'coffin dance',
        'дережабль, ага',
        'я футбольный мячик',

    ]
    ques = 'откуда мем?'
    photo = open('media/mem2.jpg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='это coffing dance ты угадал!',
        open_period=30)

def reg_hand_callback(db:Dispatcher):
    db.register_callback_query_handler(quiz3, text='button')