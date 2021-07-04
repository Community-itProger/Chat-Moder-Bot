from loader import dp
from aiogram.types import Message


@dp.message_handler(commands="help")
async def help(message: Message):
    await message.answer(
        text=f"👮🏻‍♂️ <b>Adminlar uchun</b>\n\n"
             f"<code>!ban</code> - Gurux a'zosini guruxdan o'chirish;\n\n"
             f"<code>!mute [soat]h</code> - Gurux a'zosini [soat]ga ovozsiz rejimga o'tkazish;\n\n"
             f"<code>!unmute</code> - Gurux azosini ovozsiz rejimdan chiqarish;\n\n"
             f"<code>!pin</code> - Guruxdagi xabarni biriktirish;\n\n"
             f"<code>!unpin</code> - Guruxdagi xabarni biriktirilgan xabarlardan olish;\n\n"

    )
