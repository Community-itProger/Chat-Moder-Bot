from aiogram.dispatcher.filters import Text
import messages
from funcs import is_chat_admin
from loader import dp, bot
from aiogram.types import Message


@dp.message_handler(Text(equals="!unmute"))
async def unmute_chat_member(message: Message):
    if not await is_chat_admin(message):
        await message.reply(
            text=messages.error_message
        )
    else:
        if message.reply_to_message:
            await message.delete()
            await bot.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True
            )
            await message.answer(
                text=f"{message.reply_to_message.from_user.full_name} {message.from_user.full_name}"
                     f" tomonidan ovozsiz rejimdan chiqarildi!"
            )
        else:
            await message.delete()
            await message.reply(
                text=messages.reply_to_message_error
            )
