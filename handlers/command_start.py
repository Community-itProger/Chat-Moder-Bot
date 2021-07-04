from aiogram.dispatcher.filters import CommandStart
from keyboards import language_keyboard
from loader import dp
from aiogram.types import Message


@dp.message_handler(CommandStart(), chat_type="private")
async def command_start(message: Message):
    await message.answer(
        text=f"Привет! Выберите язык\n"
             f"Salom! Tilni tanlang",
        reply_markup=language_keyboard
    )
