from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from callback_datas import callback_data_language

language_list = ["Русский", "O`zbek tili"]

language_keyboard = InlineKeyboardMarkup(row_width=1)
for item in language_list:
    language_keyboard.insert(InlineKeyboardButton(text=item, callback_data=callback_data_language.new(language=item)))
