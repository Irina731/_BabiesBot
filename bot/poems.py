from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboardURL= InlineKeyboardMarkup(row_width=0)
urlButton1 = InlineKeyboardButton(text=' "Детские стишки" ',
    url='https://sidorenkoalla.jimdofree.com/%D0%B4%D0%BB%D1%8F-%D0%B2%D0%B0%D1%81-%D1%80%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D0%B8/%D1%87%D0%B8%D1%82%D0%B0%D0%B5%D0%BC-%D0%B4%D0%B5%D1%82%D1%8F%D0%BC/%D0%B0-%D0%B1%D0%B0%D1%80%D1%82%D0%BE/')
urlButton2 = InlineKeyboardButton(text=' "Потешки" ',
    url='https://sidorenkoalla.jimdofree.com/%D0%B4%D0%BB%D1%8F-%D0%B2%D0%B0%D1%81-%D1%80%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D0%B8/%D1%87%D0%B8%D1%82%D0%B0%D0%B5%D0%BC-%D0%B4%D0%B5%D1%82%D1%8F%D0%BC/%D0%BF%D0%BE%D1%82%D0%B5%D1%88%D0%BA%D0%B8/')
keyboardURL.row(urlButton1, urlButton2)

