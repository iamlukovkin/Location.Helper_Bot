from main import *
note_save = False


def new_note(message):
    note_save = True
    bot.send_message(message.chat.id, 'Введи текст:')
    return note_save

     
def last_note(message):
    bot.send_message(message.chat.id, 'last_note')
    pass


def messages_friend(message):
    bot.send_message(message.chat.id, 'messages_friend')
    pass


def new_doc(message):
    bot.send_message(message.chat.id, 'new_doc')
    pass


def load_doc(message):
    pass


def pers_doc(message):
    bot.send_message(message.chat.id, 'pers_doc')
    pass


def new_diary(message):
    bot.send_message(message.chat.id, 'new_diary')
    pass


def comments_diary(message):
    bot.send_message(message.chat.id, 'comments_diary')
    pass


def unreaded(message):
    bot.send_message(message.chat.id, 'unreaded')
    pass


def readed(message):
    bot.send_message(message.chat.id, 'readed')
    pass


def squad_info(message):
    bot.send_message(message.chat.id, 'squad_info')
    pass
