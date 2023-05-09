import scopes
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
import io
import os
import shutil
# import tempfile

from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

# Авторизация приложения в Google Drive API
creds = Credentials.from_authorized_user_file('token.json', scopes)
service = build('drive', 'v3', credentials=creds)


# Функция загрузки файла на Google Drive
def upload_file(file_path, folder_id=None):
    file_metadata = {'name': os.path.basename(file_path)}
    if folder_id:
        file_metadata['parents'] = [folder_id]
    media = MediaFileUpload(file_path, resumable=True)
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    print(f'File ID: {file.get("id")}')


# Пример использования функции загрузки файла
upload_file('/path/to/file.pdf', folder_id='abc123')


# Функция скачивания файла с Google Drive
def download_file(file_id, file_name):
    request = service.files().get_media(fileId=file_id)
    with io.BytesIO() as fh:
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(f'Download {int(status.progress() * 100)}.')
        fh.seek(0)
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(fh, f)


# Пример использования функции скачивания файла
download_file('xyz456', '/path/to/file.pdf')


# Функция получения списка файлов в папке
def get_files_in_folder(folder_id):
    query = f"'{folder_id}' in parents and trashed = false"
    results = service.files().list(
        q=query,
        fields="nextPageToken, files(id, name)"
    ).execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
