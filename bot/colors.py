from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


colors = [
    { "name": "Синий", "image_url": "https://amelica.com/wp-content/uploads/2015/04/kartochki_domana_skachat_besplatno.jpg"},
    { "name": "Красный", "image_url": "https://amelica.com/wp-content/uploads/2015/04/kartochki_domana_skachat_besplatno_1.jpg"},
    {"name": "Желтый", "image_url": "https://amelica.com/wp-content/uploads/2015/04/kartochki_domana_skachat_besplatno_2.jpg"},
    {"name": "Зеленый", "image_url": "https://amelica.com/wp-content/uploads/2015/04/kartochki_domana_skachat_besplatno_3.jpg"},
    {"name": "Фиолетовый", "image_url": "https://amelica.com/wp-content/uploads/2015/04/kartochki_domana_skachat_besplatno_5.jpg"},
    {"name": "Оранжевый", "image_url": "https://amelica.com/wp-content/uploads/2015/04/kartochki_domana_skachat_besplatno_6.jpg"},
    { "name": "Голубой", "image_url": "https://amelica.com/wp-content/uploads/2015/04/kartochki_domana_skachat_besplatno_8.jpg"},
    {"name": "Черный", "image_url": "https://amelica.com/wp-content/uploads/2015/04/kartochki_domana_skachat_besplatno_9.jpg"},
    {"name": "Белый","image_url": "https://amelica.com/wp-content/uploads/2015/04/kartochki_domana_skachat_besplatno_10.jpg"}
]

colors_callback = CallbackData("colors", "page")


def get_colors_keyboard(page: int = 0) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    next_page = len(colors) > page +1
    if page != 0:
        keyboard.add(InlineKeyboardButton(text="Назад", callback_data=colors_callback.new(page=page -1)))
        keyboard.add(InlineKeyboardButton(text=" (｡◕‿◕｡) ", callback_data="click"))
    if next_page:
        keyboard.add(InlineKeyboardButton(text="Вперёд", callback_data=colors_callback.new(page=page + 1)))
    return keyboard

