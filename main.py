import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        # """Метод загруджает файл file_path на яндекс диск"""
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                params=dict(path='upload_file.txt'),
                                headers={'Authorization': f'OAuth {self.token}'})

        print(response.status_code)
        print(response.json())
        href = response.json()['href']
        with open(file_path) as f:
            requests.put(href, files={'file': f})
        return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    uploader = YaUploader('<token>')
    result = uploader.upload('new_file.txt')
