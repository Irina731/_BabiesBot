from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


animals = [
    {"name": "Корова","image_url": "https://montessoriself.ru/wp-content/uploads/2017/09/KOROVA.jpg"},
    {"name": "Лошадь", "image_url": "https://montessoriself.ru/wp-content/uploads/2017/09/LOSHAD.jpg"},
    {"name": "Коза","image_url": "https://montessoriself.ru/wp-content/uploads/2017/09/KOZA.jpg"},
    {"name": "Осел","image_url": "https://montessoriself.ru/wp-content/uploads/2017/09/OSEL.jpg"},
   {"name": "Собака","image_url": "https://montessoriself.ru/wp-content/uploads/2017/09/SOBAKA.jpg"},
    { "name": "Кошка","image_url": "https://montessoriself.ru/wp-content/uploads/2017/09/KOSHKA.jpg"},
    {"name": "Черепаха","image_url": "https://montessoriself.ru/wp-content/uploads/2017/09/CHEREPAHA.jpg"},
    {"name": "Хомяк","image_url": "https://montessoriself.ru/wp-content/uploads/2017/09/HOMYAK.jpg"}
]

animals_callback = CallbackData("animals", "page")


def get_animals_keyboard(page: int = 0) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    next_page = len(animals) > page +1
    if page != 0:
        keyboard.add(InlineKeyboardButton(text="Назад",callback_data=animals_callback.new(page=page -1)))
        keyboard.add(InlineKeyboardButton(text="(o˘◡˘o)", callback_data="click"))
    if next_page:
        keyboard.add(InlineKeyboardButton(text="Вперёд",callback_data=animals_callback.new(page=page + 1)))
    return keyboard


