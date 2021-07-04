import datetime
import messages
from funcs import is_chat_admin
from loader import dp, bot
from aiogram.types import Message


@dp.message_handler(text_startswith=["!mute"])
async def mute_chat_member(message: Message):
    if not await is_chat_admin(message):
        await message.reply(
            text=messages.error_message
        )
    else:
        if message.reply_to_message:
            await message.delete()
            args = message.text[6:]
            hours = args[:-1]
            await bot.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_other_messages=False,
                until_date=datetime.timedelta(hours=int(hours))
            )
            await message.answer(
                text=f"{message.reply_to_message.from_user.full_name} {message.from_user.full_name} "
                     f"tomonidan {hours} soatga ovozsiz rejimga o'tkazildi!"
            )
        else:
            await message.delete()
            await message.reply(
                text=messages.reply_to_message_error
            )
