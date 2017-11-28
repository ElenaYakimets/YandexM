import requests
from urllib.parse import urljoin

AUTH_URL = 'https://oauth.yandex.ru/authorize'
APP_ID = 'a5c1df0de4fe47e7987be8a449dc4b92'

auth_data = {
    'response_type': 'token',
    'client_id': APP_ID
}

# print('?'.join((AUTH_URL, urlencode(auth_data))) )

TOKEN = 'AQAAAAABHBaxAASt0yT51Qj13UOgtBeZLNq1RsE'


class YMuser:
    manag_URL = 'https://api-metrika.yandex.ru/management/v1/'
    stat_URL = 'https://api-metrika.yandex.ru/stat/v1/data'


def get_headers(self):
    headers = {
        'Authorization': 'OAuth {}'.format(self.token),
        'Content-Type': 'appliaction/x-yametrika+json'
    }
    return headers


def get_count(self):
    url = urljoin(self.manag_URL, 'counters')
    headers = self.get_headers()
    response = requests.get(url, headers=headers)
    return response.json()


# def get_users(self, counter_id=APP_ID):
#     if counter_id is None:
#         counter_id = self.get_counters()['counters'][0]['id']
#         headers = self.get_headers()
#         params = dict(id=counter_id, metrics='ym:s:users')
#         response = requests.get(self.analytics_URL, params=params, headers=headers)
#         return response.json()
