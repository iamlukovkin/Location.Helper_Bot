import telebot as tb
from telebot import types
import operations as op
import windows_menu as menu


bot = tb.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    i1 = types.InlineKeyboardButton(text='Главное меню', callback_data='main')
    markup.add(i1)
    bot.send_message(message.chat.id,
                     f'Привет, {message.from_user.full_name}!\nТы находишься на '
                     f'главной странице бота Локация.Помощник📍\nЭтот бот поможет тебе '
                     f'упростить работу в смене.\n'
                     f'Если ты только начинаешь пользоваться ботом, можешь перейти выбрать Регистрация'
                     f'Если ты уже пользовался ботом, можешь перейти в Главное меню', reply_markup=markup)
    reply_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i = types.KeyboardButton('Главное меню')
    reply_markup.add(i)
    bot.send_message(message.chat.id, text='Ты в любой момент можешь вернуться в начало.\n'
                                           'Достаточно нажать на кнопку\n'
                                           'Главное меню внизу', reply_markup=reply_markup)


@bot.callback_query_handler(func=lambda call: True)
def logic_program(call):
    if call.data == 'reg':
        bot.send_message(call.message.chat.id, 'reg')
    elif call.data == 'main':
        menu.main(bot, call.message)
    else:
        if call.data == 'person':
            menu.person(bot, call.message)
        if call.data == 'library':
            menu.library(bot, call.message)
        else:
            if call.data == 'squad_info':
                op.squad_info(call.message)
            elif call.data == 'pers_notes':
                menu.notes(bot, call.message)
            elif call.data == 'methods':
                menu.methods(bot, call.message)
            elif call.data == 'diary':
                menu.diary(bot, call.message)
            elif call.data == 'messanger':
                menu.messenger(bot, call.message)
            else:
                if call.data == 'new_note':
                    op.new_note(call.message)
                elif call.data == 'last_note':
                    op.last_note(call.message)
                elif call.data == 'mess_from_friend':
                    op.messages_friend(call.message)
                elif call.data == 'new_doc':
                    op.new_doc(call.message)
                elif call.data == 'load_doc':
                    op.load_doc(call.message)
                elif call.data == 'pers_doc':
                    op.pers_doc(call.message)
                elif call.data == 'new_diary':
                    op.new_diary(call.message)
                elif call.data == 'comments_diary':
                    op.comments_diary(call.message)
                elif call.data == 'unreaded':
                    op.unreaded(call.message)
                elif call.data == 'readed':
                    op.readed(call.message)


@bot.message_handler(content_types=['text'])
def answer_text(message):
    if message.text == 'Главное меню':
        menu.main(bot, message)


if __name__ == '__main__':
    bot.polling(none_stop=True)
