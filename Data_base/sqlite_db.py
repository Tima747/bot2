import sqlite3 as sq
from creat_bot import bot


async def db_start():
    global db, cur, base

    db = sq.connect('Cars.db')
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS profile(name TEXT PRIMARY KEY, img TEXT, engine TEXT, description TEXT, price TEXT)")

    db.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОбемь: {ret[2]}\nОписание: {ret[3]}\nЦена {ret[-1]}')
