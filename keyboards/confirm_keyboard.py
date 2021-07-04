from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
from callback_datas import callback_data_confirm

confirm_items = ["Men odamman", "Men maymunman", "Men robotman"]

confirm_keyboard = InlineKeyboardMarkup(row_width=1)
for item in random.sample(confirm_items, len(confirm_items)):
    confirm_keyboard.insert(InlineKeyboardButton(text=item, callback_data=callback_data_confirm.new(button=item)))