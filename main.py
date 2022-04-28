from math import hypot
from re import I
from wsgiref import headers
import requests
from bs4 import BeautifulSoup
URL = "https://coinmarketcap.com/"
HEADERS = {
    "user-agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}


def get_html(url, params=None):
    page = requests.get(URL, headers=HEADERS, params=params)
    return page

def get_content(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    blocks = soup.find_all('tr')
    cryptocurrency=[]
    for block in blocks:
        items_name=block.find_all('p',class_ = 'sc-1eb5slv-0 iworPT')
        items_prise=block.find_all('div',class_ = 'sc-131di3y-0 cLgOOr')
        items_percent24h=block.find_all('span',class_='sc-15yy2pl-0 kAXKAX')
        items_percent7d=block.find_all('span',class_='sc-15yy2pl-0 hzgCfk')
        items_marketcap=block.find_all('span',class_='sc-1ow4cwt-0 iosgXe')
        items_volume24h=block.find_all('p',class_='sc-1ow4cwt-0 iosgXe')
        items_circulsupp=block.find_all('p',class_='sc-1eb5slv-0 kZlTnE')
        for item_name in items_name:
            cryptocurrency.append({
                'name': item_name.text
            })
        for item_prise in items_prise:
            cryptocurrency.append({
                'prise': item_prise.text
            })
        for item_percent24h in items_percent24h:
            cryptocurrency.append({
                'percent24h': item_percent24h.text
            })
        for item_percent7d in items_percent7d:
            cryptocurrency.append({
                'percent7d': item_percent7d.text
            })
        for item_marketcap in items_marketcap:
            cryptocurrency.append({
                'marketcap': item_marketcap.text
            })
        for item_marketcap in items_marketcap:
            cryptocurrency.append({
                'marketcap': item_marketcap.text
            })
        for item_volume24h in items_volume24h:
            cryptocurrency.append({
                'volume24h': item_volume24h.text
            })
        for item_circulsupp in items_circulsupp:
            cryptocurrency.append({
                'circulsupp': item_circulsupp.text
            })
        
    print(cryptocurrency)

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html)
    else:
        print("Ошибка! Не удалось получить данные сайта =(")


parse()