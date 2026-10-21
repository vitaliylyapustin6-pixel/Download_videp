import aiosqlite

async def sql(user_id: int):
    # Подключаемся к таблице
    async with aiosqlite.connect('Tgg.db') as conn:
        async with conn.cursor() as cursor:
            # Название таблицы 'Id' должно совпадать и в CREATE, и в INSERT
            await cursor.execute('CREATE TABLE IF NOT EXISTS Id(id INTEGER PRIMARY KEY)')
            await cursor.execute('INSERT OR IGNORE INTO Id(id) VALUES(?)', (user_id,))
            await conn.commit()