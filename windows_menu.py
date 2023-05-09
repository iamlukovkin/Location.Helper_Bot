from main import *


def main(bot, message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    i1 = types.InlineKeyboardButton(text="👥", callback_data='person')
    i2 = types.InlineKeyboardButton(text="🔍", callback_data='library')
    markup.add(i1, i2)
    bot.send_message(message.chat.id,
                     'Выбери действие\n\n'
                     '👥 - Личный профиль\n'
                     '🔍 - Поиск материалов',
                     reply_markup=markup)


def person(bot, message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    i1 = types.InlineKeyboardButton(text="ℹ️", callback_data='squad_info')
    i2 = types.InlineKeyboardButton(text="✍️", callback_data='pers_notes')
    markup.add(i1, i2)
    bot.send_message(message.chat.id,
                     'Выбери действие\n\n'
                     'ℹ️ - Информация об отряде\n'
                     '✍️ - Личные заметки',
                     reply_markup=markup)


def library(bot, message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    i1 = types.InlineKeyboardButton(text="📚", callback_data='methods')
    i2 = types.InlineKeyboardButton(text="📔", callback_data='diary')
    i3 = types.InlineKeyboardButton(text="📥", callback_data='messanger')
    markup.add(i1, i2, i3)
    bot.send_message(message.chat.id,
                     'Выбери действие\n\n'
                     '📚 - Методички\n'
                     '📔 - Педагогический дневник\n'
                     '📥 - Сообщения от методистов',
                     reply_markup=markup)


def notes(bot, message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    i1 = types.InlineKeyboardButton(text="📓", callback_data='new_note')
    i2 = types.InlineKeyboardButton(text="🕐", callback_data='last_note')
    i3 = types.InlineKeyboardButton(text="👤", callback_data='mess_from_friend')
    markup.add(i1, i2, i3)
    bot.send_message(message.chat.id,
                     'Выбери действие\n\n'
                     '📓 - Новая заметка\n'
                     '🕐 - Предыдущие заметки\n'
                     '👤 - Заметки от напарника',
                     reply_markup=markup)


def methods(bot, message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    i1 = types.InlineKeyboardButton(text="📒", callback_data='new_doc')
    i2 = types.InlineKeyboardButton(text="⬇️", callback_data='load_doc')
    i3 = types.InlineKeyboardButton(text="📖", callback_data='pers_doc')
    markup.add(i1, i2, i3)
    bot.send_message(message.chat.id,
                     'Выбери действие\n\n'
                     '📒 - Найти новую методичку\n'
                     '⬇️ - Загрузить личный документ\n'
                     '📖 - Личная библиотека',
                     reply_markup=markup)


def diary(bot, message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    i1 = types.InlineKeyboardButton(text="📓", callback_data='new_diary')
    i2 = types.InlineKeyboardButton(text="🕐", callback_data='last_diary')
    i3 = types.InlineKeyboardButton(text="💬", callback_data='comments_diary')
    markup.add(i1, i2, i3)
    bot.send_message(message.chat.id,
                     'Выбери действие\n\n'
                     '📓 - Новая запись\n'
                     '🕐 - Просмотр предыдущих записей\n'
                     '💬 - Комментарии от руководителя',
                     reply_markup=markup)


def messenger(bot, message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    i1 = types.InlineKeyboardButton(text="🆕", callback_data='unreaded')
    i2 = types.InlineKeyboardButton(text="⏮", callback_data='readed')
    markup.add(i1, i2)
    bot.send_message(message.chat.id,
                     'Выбери действие\n\n'
                     '🆕 - Непрочитанные сообщения\n'
                     '⏮ - Предыдущие комментарии',
                     reply_markup=markup)
