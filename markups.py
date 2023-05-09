from telebot.types import *

start_menu = InlineKeyboardMarkup(row_width=2)
select = InlineKeyboardButton(text="🔄 Выбор", callback_data="select")
help_btn = InlineKeyboardButton(text="🆘 Помощь", callback_data="help")

start_menu.add(select, help_btn)


# Back
back_ = InlineKeyboardMarkup(row_width=1)
back = InlineKeyboardButton(text="🔙 Назад", callback_data="back")
back_.add(back)


# akses
akses = InlineKeyboardMarkup(row_width=3)

ИгровыеСборки = InlineKeyboardButton(text="Игровые Сборки", callback_data="ИгровыеСборки")
Ноутбуки = InlineKeyboardButton(text="Ноутбуки", callback_data="Ноутбуки")
Клавиатуры = InlineKeyboardButton(text="Клавиатуры", callback_data="Клавиатуры")
Наушники = InlineKeyboardButton(text="Наушники", callback_data="Наушники")
Мышки = InlineKeyboardButton(text="Мышки", callback_data="Мышки")
back = InlineKeyboardButton(text="🔙 Назад", callback_data="back")
akses.add(ИгровыеСборки, Ноутбуки, Клавиатуры, Наушники, Мышки, back)