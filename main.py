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
    items = soup.find_all('tr')
    cryptocurrency=[]
    for item in items:
        items2=item.find_all('p',class_ = 'sc-1eb5slv-0 iworPT')
        for item2 in items2:
            cryptocurrency.append({
                'name': item2.text
            })
    print(cryptocurrency)

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html)
    else:
        print("Ошибка! Не удалось получить данные сайта =(")


parse()