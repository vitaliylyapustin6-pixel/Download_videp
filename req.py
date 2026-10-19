from aiogram import Bot,Dispatcher,F,types
from aiogram.types import Message
from aiogram.types import FSInputFile

import psycopg2

import yt_dlp

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from dotenv import load_dotenv
import os
import asyncio

conn = psycopg2.connect(dbname='utub1',user='postgres',password='20222',host='localhost')

load_dotenv()

token = os.getenv('TOKEN')
bot = Bot(token=token)
dp = Dispatcher()

class Req(StatesGroup):
    ytdl = State()

#Обработчик команды start
@dp.message(F.text == '/start')
async def start(message: Message, state: FSMContext):
    cursor = conn.cursor()
    message_id = message.from_user.id
    cursor.execute('SELECT * FROM id_users WHERE id = %s;',(message_id,))
    user = cursor.fetchone()

    if user:
        await message.answer(f'Привет {message.from_user.first_name}\nСкинь Link на видео)')
    else:
        cursor.execute('INSERT INTO id_users(id) VALUES(%s);',(message_id,))
        conn.commit()
        cursor.close()
    await state.set_state(Req.ytdl)
@dp.message(Req.ytdl)
async def ytdll(message: Message, state: FSMContext): 
    try:
        message_user = message.text
        # Натсройка библиотеки = ydl_dlp
        ydl_opts = {
        'outtmpl':'temp.mp4',
        'format':'mp4'
        }
        # Устанавливаем параметры
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Скачиваем видео
            ydl.download([message_user])
        # Находим ролик среди файлов
        download = FSInputFile('temp.mp4')
        await message.answer_video(caption='Вот ваше видео',video=download)
    # Обработка ошыбок 
    except Exception as e:
        print(f'Bug: {e}')
        await message.answer('Извините ролик не получилось скачать=)')
    # Удаляем видео
    finally:
        await asyncio.sleep(5)
        if os.path.isfile('temp.mp4'): 
            os.remove('temp.mp4')
# Запускаем Бота 
async def main():    
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())