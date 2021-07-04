import datetime
from aiogram.dispatcher.filters import Text
import messages
from funcs import is_chat_admin
from loader import dp, bot
from aiogram.types import Message


@dp.message_handler(Text(equals="!ban"))
async def kick_chat_member(message: Message):
    if not await is_chat_admin(message):
        await message.reply(
            text=messages.error_message
        )
    else:
        if message.reply_to_message:
            await message.delete()
            await bot.kick_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
            )
            await message.answer(
                text=f"{message.reply_to_message.from_user.full_name} {message.from_user.full_name}"
                     f" tomonidan guruxdan chetlashtirildi!"
            )
        else:
            await message.delete()
            await message.reply(
                text=messages.reply_to_message_error
            )
