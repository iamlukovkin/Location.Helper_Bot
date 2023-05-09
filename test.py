
from github import Github
import requests

bot_token = '6048732407:AAEGRA6prdW1ymtjLamIvn53_vDh_IyQ5yE'
updater = Updater(bot=bot_token, update_queue=True)
dispatcher = updater.dispatcher
github_token = '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'
g = Github(github_token)



# Для обработки команды на скачивание файлов, создадим функцию download, которая будет принимать параметры:
# пользователя, имя репозитория и путь к файлу:


def download(update, context):
    user = context.args[0]
    repo_name = context.args[1]
    file_path = context.args[2]
    repo = g.get_repo(user + '/' + repo_name)
    contents = repo.get_contents(file_path)
    download_url = contents.download_url
    response = requests.get(download_url)
    with open(file_path, 'wb') as f:
        f.write(response.content)
    context.bot.send_message(chat_id=update.effective_chat.id, text='Файл {} был успешно скачан'.format(file_path))


# Для получения информации о содержимом репозитория или конкретной папке, создадим функцию list_files, которая также
# принимает параметры пользователя и имя репозитория:




# Теперь создадим обработчики для команд /download и /list, которые будут вызывать соответствующие функции:

download_handler = CommandHandler('download', download)
dispatcher.add_handler(download_handler)

list_handler = CommandHandler('list', list_files)
dispatcher.add_handler(list_handler)

updater.start_polling()
