from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

remove = ReplyKeyboardRemove()


admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Сделать рассылку', callback_data='mail')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

support = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Поддержка', callback_data='support')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

reference = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Перейти на сайт',
                url='https://habr.com/ru/companies/otus/articles/736244/',
            )
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

confirm = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Да'), KeyboardButton(text='Нет')]],
    resize_keyboard=True,
    one_time_keyboard=True,
)

end_dialog = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Завершить диалог', callback_data='end')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
