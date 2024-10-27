import requests
from bs4 import BeautifulSoup
import fake_useragent

#GET ЗАПРОСЫ

# user_agent = fake_useragent.UserAgent().random

# headers = {
#     'user-agent': user_agent
# }

#создание юзер бота чтобы сайт не распознал нас как бота


# url = 'https://www.coingecko.com/ru'
# response = requests.get(url, headers = headers)

#получаем html код страницы

# html = BeautifulSoup(response.content, 'html.parser')
# table = html.select('.tw-border-y.tw-border-gray-200')[0]
# trs = table.select('tr')[1:]
# for tr in trs[:10]:
#     c = tr.select('.tw-block.tw-text-xs.tw-leading-4.tw-text-gray-500.tw-font-medium')
#     if c:
#         print(c[0].text)
        
#сначала ищем таблицу с классами .tw-border-y.tw-border-gray-200, в ней ищем элементы с классами .tw-border-y.tw-border-gray-200, а в них ищем элементы с классами .tw-block.tw-text-xs.tw-leading-4.tw-text-gray-500.tw-font-medium, которые содержат названия монет

#POST ЗАПРОСЫ

import json

user_agent = fake_useragent.UserAgent().random

headers = {
    'user-agent': user_agent
}

data = {
    'data': {"ticketid": 12341234}
}

payload = {
    'data': json.dumps(data),
    'jsontemplate': 1,
    'jsonspec': 4,
    'jsonfix': 'on',
    'autoprocess': '',
    'version': 2,  
}

url = 'https://jsonformatter.curiousconcept.com/process'
response = requests.post(url, headers = headers, params = payload)
print(response.json())