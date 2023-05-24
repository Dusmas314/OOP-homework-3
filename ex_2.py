import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        res = requests.get('https://cloud-api.yandex.net:443/v1/disk/resources/upload?path=Photo1.jpg', headers={'Authorization': f'OAuth {token}'}).json()
        with open(file_path, 'rb') as f:
            requests.put(res['href'], files={'file': f})


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ''
    token = ''
    uploader = YaUploader(token)
    uploader.upload(path_to_file)

