from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import random
from callback_datas import callback_data_confirm

confirm_items = ["Men odamman", "Men maymunman", "Men robotman"]


async def confirm_keyboard_markup(message: Message):
    confirm_keyboard = InlineKeyboardMarkup(row_width=1)
    for item in random.sample(confirm_items, len(confirm_items)):
        confirm_keyboard.insert(InlineKeyboardButton(text=item, callback_data=callback_data_confirm.new(button=item, id=message.from_user.id)))

    return confirm_keyboard