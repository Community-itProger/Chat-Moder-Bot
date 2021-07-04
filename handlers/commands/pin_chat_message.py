from aiogram.dispatcher.filters import Text
import messages
from funcs import is_chat_admin
from loader import dp, bot
from aiogram.types import Message


@dp.message_handler(Text(equals="!pin"))
async def pin_chat_message(message: Message):
    if not await is_chat_admin(message):
        await message.reply(
            text=messages.error_message
        )
    else:
        if message.reply_to_message:
            await message.delete()
            await bot.pin_chat_message(
                chat_id=message.chat.id,
                message_id=message.reply_to_message.message_id
            )
            await message.answer(
                text=f"{message.from_user.full_name} tomonidan biriktirildi!"
            )
        else:
            await message.delete()
            await message.reply(
                text=messages.reply_to_message_error
            )
