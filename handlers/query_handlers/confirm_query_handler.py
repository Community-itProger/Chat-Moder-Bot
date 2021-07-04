from typing import Dict
from loader import dp, bot
from aiogram.types import CallbackQuery
from callback_datas import callback_data_confirm


@dp.callback_query_handler(callback_data_confirm.filter(button=["Men odamman", "Men maymunman", "Men robotman"]))
async def language_query_handler(callback_query: CallbackQuery, callback_data: Dict[str, str]):
    if callback_data["button"] != "Men odamman":
        await bot.delete_message(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id
        )
        await bot.kick_chat_member(
            chat_id=callback_query.message.chat.id,
            user_id=callback_query.from_user.id
        )
    else:
        await bot.delete_message(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id
        )
        await bot.restrict_chat_member(
            chat_id=callback_query.message.chat.id,
            user_id=callback_query.from_user.id,
            can_add_web_page_previews=True,
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_other_messages=True
        )