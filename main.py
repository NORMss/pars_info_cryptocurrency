import json
from math import hypot
from re import I
from wsgiref import headers
import requests
from bs4 import BeautifulSoup
URL = "https://coinmarketcap.com/"
HEADERS = {
    "user-agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
cryptocurrency=[]

def get_html(url, params=None):
    page = requests.get(URL, headers=HEADERS, params=params)
    return page

def get_content(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    blocks = soup.find(class_="h7vnx2-1 bFzXgL").find_all('tr')
    for block in blocks:
        if (block.find(class_="sc-1eb5slv-0 iworPT") != None):
            item_name=block.find(class_='sc-1eb5slv-0 iworPT').text
            item_prise=block.find(class_ = 'sc-131di3y-0 cLgOOr').text
            items_percent24h=block.find_all(class_='sc-15yy2pl-0 kAXKAX')
            items_percent7d=block.find_all(class_='sc-15yy2pl-0 hzgCfk')
            item_marketcap=block.find(class_='sc-1ow4cwt-0 iosgXe').text
            item_volume24h=block.find(class_='sc-1ow4cwt-0 iosgXe').text
            item_circulsupp=block.find(class_='sc-1eb5slv-0 kZlTnE').text
            cryptocurrency.append({
                'name': item_name,
                'prise': item_prise,
                'marketcap': item_marketcap,
                'circulsupp': item_circulsupp,
                'volume24h': item_volume24h
                })
        # items_percent24h=block.find_all('span',class_='sc-15yy2pl-0 kAXKAX')
        # items_percent7d=block.find_all('span',class_='sc-15yy2pl-0 hzgCfk')
        # for item_percent24h in items_percent24h:
        #     cryptocurrency.append({
        #         'percent24h': item_percent24h.text
        #     })
        # for item_percent7d in items_percent7d:
        #     cryptocurrency.append({
        #         'percent7d': item_percent7d.text
        #     })

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html)
    else:
        ("Ошибка! Не удалось получить данные сайта =(")

def create_json():
    with open ('data.json', 'a', encoding='utf-8') as file:
        json.dump(cryptocurrency,file,indent=4, ensure_ascii='False')

parse()
create_json()