from aiogram import types
from loader import bot


async def is_chat_admin(message: types.Message):
    user = await bot.get_chat_member(
        chat_id=message.chat.id,
        user_id=message.from_user.id
    )
    if user.status not in ["creator", "administrator"]:
        return False
    else:
        return True
