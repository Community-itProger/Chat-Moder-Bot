from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN
import sqlite3


# Prepare bot
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


# Prepare database
connect = sqlite3.connect("database/data.db")
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS data(
                id INT PRIMARY KEY,
                language TEXT);
               """)
connect.commit()