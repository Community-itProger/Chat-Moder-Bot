from typing import Dict
from loader import dp
from aiogram.types import CallbackQuery
from callback_datas import callback_data_language
from loader import connect, cursor


@dp.callback_query_handler(callback_data_language.filter(language=["Русский", "O`zbek tili"]))
async def language_query_handler(callback_query: CallbackQuery, callback_data: Dict[str, str]):
    cursor.execute(f"INSERT INTO data(id, language) VALUES('{callback_query.message.chat.id}', '{callback_data['language']}')")
    connect.commit()