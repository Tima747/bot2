from aiogram.utils import executor
from creat_bot import dp
from Data_base import sqlite_db

from handlers import client, other, admin


async def on_startup(_):
    print('Бот вышел в онлайн')
    await sqlite_db.db_start()

client.register_handler_client(dp)
admin.register_handler_admin(dp)
other.register_handler_other(dp)

if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)


