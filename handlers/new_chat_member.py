from keyboards import confirm_keyboard_markup
from loader import dp, bot
from aiogram import types


@dp.message_handler(content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_chat_member(message: types.Message):
    confirm_keyboard = await confirm_keyboard_markup(message)
    await bot.restrict_chat_member(
        chat_id=message.chat.id,
        user_id=message.from_user.id,
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False,
    )
    await message.answer(
        text=f"Assalomu Alaykum, <a href='t.me/{message.new_chat_members[0].username}'>{message.new_chat_members[0].full_name}</a>!\n"
             f"Gurux qoidalarini o'qib chiqqan xolda shu tugmalar yordamida shaxsingizni tasdiqlang",
        reply_markup=confirm_keyboard,
        disable_web_page_preview=True
    )