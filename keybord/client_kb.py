from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,  # размер
    one_time_keyboard=True  # скрыть кнопки
)

start_button = KeyboardButton("/start")
info_button = KeyboardButton("/info")
quiz_button = KeyboardButton("/quiz")
reg_button = KeyboardButton("/reg")

location = KeyboardButton("location", request_location=True)
contact = KeyboardButton("contact", request_contact=True)
user = KeyboardButton("user", request_user=None)

start_markup.add(start_button, info_button, quiz_button, location, contact, user, reg_button)

cancel = KeyboardButton('cancel')

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton('да'),
    KeyboardButton('миш всё фигня давай по новой'),
    cancel
)

gender_murkup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton('мужчина'),
    KeyboardButton('женчина'),
    KeyboardButton('ленолиум'),
    KeyboardButton('ломинат'),
    KeyboardButton('индивиды'),
    cancel
)

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    cancel
)