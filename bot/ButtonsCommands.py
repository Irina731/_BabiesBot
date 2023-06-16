from aiogram import types


keyboard_markup = types.ReplyKeyboardMarkup(row_width=True)
btn1 = types.KeyboardButton('/animals')
btn2 = types.KeyboardButton('/colors')
btn3 = types.KeyboardButton('/poems')
btn4 = types.KeyboardButton('/bodyParts')
btn5 = types.KeyboardButton('/help')
keyboard_markup.row(btn1, btn2,btn3,btn4).insert(btn5)
