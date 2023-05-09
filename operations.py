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
    user = message.context.args[0]
    repo_name = message.context.args[1]
    repo = g.get_repo(user + '/' + repo_name)
    contents = repo.get_contents('')
    file_list = []
    for content_file in contents:
        if content_file.type == 'dir':
            sub_contents = repo.get_contents(content_file.path)
            for sub_content_file in sub_contents:
                file_list.append(sub_content_file.path)
        else:
            file_list.append(content_file.path)
    message.context.bot.send_message(chat_id=message.update.effective_chat.id, text='\n'.join(file_list))


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
