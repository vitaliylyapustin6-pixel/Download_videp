import asyncio
import logging
import os

# Загрузка переменных окружения из .env
from dotenv import load_dotenv

# Основные модули aiogram
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command, CommandStart

# Работа с FSM (состояниями)
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

# Сообщения и клавиатуры
from aiogram.types import (
    CallbackQuery,
    Message,
)
# Удобные билдеры для динамических клавиатур
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

import aiosqlite

from sqll import sql

from gg import selff

#Подключение Токена
load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)
#Роутер
router = Router()
dp = Dispatcher()

#Делаем дикаротор/фенцию для обработки Start
@router.message(CommandStart())
async def start(message: Message):
    #Сохраняем ID в переменую
    user_id = message.from_user.id
    await sql(user_id)
    #Делаем кнопки инляйн
    b = InlineKeyboardBuilder()
    b.button(text='Население Одессы',callback_data='1')
    b.button(text='Население Киев',callback_data='2')
    b.button(text='Население Shanghai',callback_data='3')

    #Отправляем пользывателю первое сообщение
    await message.answer(f'Hello {message.from_user.first_name},тут ты можешь посомтреть насчиление людей',reply_markup=b.as_markup())

#Первый каллбек для Одессы
@router.callback_query(F.data == '1')
async def b1(call: CallbackQuery):
    await call.answer()
    #Подключаем Нашее gg.py
    info = selff("Odesa")
    res = await info.get()
    await call.message.answer(res)

#Второй каллбек для Киева
@router.callback_query(F.data == '2')
async def b1(call: CallbackQuery):
    await call.answer()
    info = selff("Kyiv")
    res = await info.get()
    await call.message.answer(res)

@router.callback_query(F.data == '3')
async def b1(call: CallbackQuery):
    await call.answer()
    info = selff("Shanghai")
    res = await info.get()
    await call.message.answer(res)


async def main():
    # Включаем логирование, чтобы видеть события и ошибки в консоли
    logging.basicConfig(level=logging.INFO)
    
    # Подключаем роутер к диспетчеру
    dp.include_router(router)
    
    # Сбрасываем накопленные сообщения во время оффлайна и запускаем бота
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


