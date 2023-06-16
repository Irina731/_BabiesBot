from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

body_parts = [
    {"name": "Глаза","image_url": "https://orechi.ru/wp-content/uploads/2018/11/glaza-212x300.jpg"},
    { "name": "Рот","image_url": "https://orechi.ru/wp-content/uploads/2018/11/rot-212x300.jpg"},
    {"name": "Голова", "image_url": "https://orechi.ru/wp-content/uploads/2018/11/golova-212x300.jpg"},
    {"name": "Уши", "image_url": "https://orechi.ru/wp-content/uploads/2018/11/ushi-212x300.jpg"},
    { "name": "Брови", "image_url": "https://orechi.ru/wp-content/uploads/2018/11/brovi-212x300.jpg"},
    { "name": "Волосы", "image_url": "https://orechi.ru/wp-content/uploads/2018/11/volos-212x300.jpg"},
    {"name": "Руки", "image_url": "https://orechi.ru/wp-content/uploads/2018/11/ruki-212x300.jpg"},
    {"name": "Ноги", "image_url": "https://orechi.ru/wp-content/uploads/2018/11/nogi-212x300.jpg"},
    {"name": "Животик", "image_url": "https://orechi.ru/wp-content/uploads/2018/11/zhivot-1-212x300.jpg"},
    {"name": "Носик", "image_url": "https://orechi.ru/wp-content/uploads/2018/11/nosik-212x300.jpg"},
    {"name": "Шея", "image_url": "https://orechi.ru/wp-content/uploads/2018/11/sheya-212x300.jpg"},
]

body_parts_callback = CallbackData("body_parts", "page")


def get_body_parts_keyboard(page: int = 0) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    next_page = len(body_parts) > page +1
    if page != 0:
        keyboard.add(InlineKeyboardButton(text="Назад", callback_data=body_parts_callback.new(page=page -1)))
        keyboard.add(InlineKeyboardButton(text=" (´｡• ᵕ •｡`)", callback_data="click"))
    if next_page:
        keyboard.add(InlineKeyboardButton(text="Вперёд", callback_data=body_parts_callback.new(page=page + 1)))
    return keyboard
