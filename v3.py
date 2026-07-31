import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
import requests
from dotenv import load_dotenv 
import os
import aiosqlite

load_dotenv(".env")
token = os.getenv("TOKEN")
bot = Bot(token=token)
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(CommandStart())
async def cmd_start(message: Message):
        name = message.from_user.first_name
        async with aiosqlite.connect("baza.db") as conn:
          async with conn.cursor() as cursor:

            await cursor.execute("INSERT INTO baza(name)VALUES(?)",(name,))

            await conn.commit()
            await message.answer(f"Привет, {name}")
    


@dp.message(F.text == "погода")
async def погода(message: Message):
    url = "https://wttr.in/Izmail?format=j1"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"
    }
    res = requests.get(url)
    date = res.json()
    temp = date['current_condition'][0]['temp_C']
    tt = date['current_condition'][0]['FeelsLikeC']
    await message.answer(f"Привет, Izmail:{temp}, ощущается как:{tt}")


async def main():
  # Запуск процесса поллинга (прослушивания новых сообщений)
  logging.basicConfig(level=logging.INFO)
  print("Бот запущен!")
  await dp.start_polling(bot)


if __name__ == "__main__":
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    print("Бот остановлен.")
import requests







