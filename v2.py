from aiogram import Bot,Dispatcher,types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
import asyncio
import os
import time
from translate import Translator
#Подключаем Токен
load_dotenv("token.env")
tokeen = os.getenv("TOKEN")
bot = Bot(token=tokeen)

dp = Dispatcher()
#Обрабатывает команду старт 
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Привет, этот бот умеет переводить с руского на англиский")
    await message.answer("Бот так же удаляет текст через 4 секунды:)")
#Перевод текста 
@dp.message()
async def s(message: types.Message):
    t = Translator(from_lang="en",to_lang="ru")
    tt = message.text
    t1 = t.translate(tt)
    await message.answer(t1)
    

#Запуск бота
async def main():
    await dp.start_polling(bot)
    print("Погнали")
if __name__ == "__main__":
    asyncio.run(main())

