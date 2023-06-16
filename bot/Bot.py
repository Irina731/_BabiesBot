from aiogram import Bot, Dispatcher, executor
import config
from animals import *
from colors import *
from body_parts import *
from poems import *
from ButtonsCommands import *
from aiogram.types import CallbackQuery, InputMedia


bot = Bot(token=config.BOT_API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def starting(message: types.Message):
    img_ = open(r"C:\Users\lenovo t14\Downloads\privetstvie.jpg", "rb")
    await bot.send_photo( message.chat.id, photo=img_)
    await bot.send_message(message.chat.id, f'{message.from_user.first_name},'
                                             f'добро пожаловать в наш чат,\U00002763!', reply_markup=keyboard_markup)

@dp.message_handler(commands=['help'])
async def help_handler(message):
    await bot.send_message(chat_id=message.chat.id,
                text=f'Список доступных команд:\n /start - начать работу с ботом\n'
                f'/poems - разучим веселые четверостишья с малышом и потешки.\n'
                f'/animals - Картинки с животными .\n/colors - Изучаем цвета.\n/bodyParts - Изучаем части тела.')


@dp.message_handler(commands='poems')
async def poems_for_baby(message: types.Message):
    await message.answer(text='Почитаем малышу:', reply_markup=keyboardURL)


@dp.message_handler(commands=["animals"])
async def image1(message:types.Message):
    animals_data = animals[0]
    caption = animals_data.get('name')
    keyboard = get_animals_keyboard()
    await bot.send_photo(chat_id=message.chat.id,photo=animals_data.get("image_url"), caption=caption,
                         parse_mode="HTML",reply_markup=keyboard)


@dp.callback_query_handler(animals_callback.filter())
async def animals_page(query: CallbackQuery, callback_data: dict):
    page = int(callback_data.get("page"))
    animals_data = animals[page]
    caption = animals_data.get('name')
    keyboard = get_animals_keyboard(page)
    photo = InputMedia(type="photo", media=animals_data.get("image_url"), caption=caption)
    await query.message.edit_media(photo, keyboard)

@dp.message_handler(commands=["colors"])
async def image2(message:types.Message):
    colors_data = colors[0]
    caption = colors_data.get('name')
    keyboard = get_colors_keyboard()
    await bot.send_photo(chat_id=message.chat.id,photo=colors_data.get("image_url"),caption=caption,
                         parse_mode="HTML",reply_markup=keyboard)


@dp.callback_query_handler(colors_callback.filter())
async def colors_page(query: CallbackQuery, callback_data: dict):
    page = int(callback_data.get("page"))
    colors_data = colors[page]
    caption = colors_data.get('name')
    keyboard = get_colors_keyboard(page)
    photo = InputMedia(type="photo", media=colors_data.get("image_url"), caption=caption)
    await query.message.edit_media(photo, keyboard)

@dp.message_handler(commands=["bodyParts"])
async def image3(message:types.Message):
    body_parts_data = body_parts[0]
    caption = body_parts_data.get('name')
    keyboard = get_body_parts_keyboard()
    await bot.send_photo(chat_id=message.chat.id,photo=body_parts_data.get("image_url"),caption=caption, reply_markup=keyboard)


@dp.callback_query_handler(body_parts_callback.filter())
async def colors_page(query: CallbackQuery, callback_data: dict):
    page = int(callback_data.get("page"))
    body_parts_data = body_parts[page]
    caption = body_parts_data.get('display_name')
    keyboard = get_body_parts_keyboard(page)
    photo = InputMedia(type="photo", media=body_parts_data.get("image_url"), caption=caption)
    await query.message.edit_media(photo, keyboard)

@dp.message_handler(content_types=['text'])
async def get_text(message):
    await bot.send_message(message.from_user.id, "Простите, не понимаю команду\U0001F614."
                                               "Давайте попробуем еще раз.")


if __name__ == '__main__':
    executor.start_polling(dp)
