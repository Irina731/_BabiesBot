
import asyncio
from aiogram import Bot, types, Dispatcher, executor

import config

bot = Bot(token=config.BOT_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text=f'Добро пожаловать в наш чат,{message.from_user.first_name}!')




if __name__ == "__main__":
    executor.start_polling(dp)
