import json
import time
from math import hypot
from re import I
from tracemalloc import start
from unicodedata import name
from wsgiref import headers
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import fileinput
URL = "https://coinmarketcap.com/"
HEADERS = {
    "user-agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
cryptocurrency=[]

# data = "".join(fileinput.input(openhook=fileinput.hook_encoded("utf-8")))
# presidents = json.loads(data)

def get_html(url, params=None):
    #page = requests.get(URL, headers=HEADERS, params=params)
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
    driver.get(url)
    time.sleep(2)
    driver.execute_script("0,window.scrollTo(0, 500);")
    time.sleep(0.5)
    driver.execute_script("0,window.scrollTo(0, 1000);")
    time.sleep(0.5)
    driver.execute_script("0,window.scrollTo(0, 1500);")
    time.sleep(0.5)
    driver.execute_script("0,window.scrollTo(0, 2000);")
    time.sleep(0.5)
    driver.execute_script("0,window.scrollTo(0, 2500);")
    time.sleep(0.5)
    driver.execute_script("0,window.scrollTo(0, 3000);")
    time.sleep(0.5)
    driver.execute_script("0,window.scrollTo(0, 3500);")
    time.sleep(0.5)
    driver.execute_script("0,window.scrollTo(0, 4000);")
    time.sleep(0.5)
    driver.execute_script("0,window.scrollTo(0, 4500);")
    time.sleep(0.5)
    driver.execute_script("0,window.scrollTo(0, 5000);")
    time.sleep(0.5)
    driver.execute_script("0,window.scrollTo(0, 5500);")
    time.sleep(0.5)
    driver.execute_script("0,window.scrollTo(0, 6000);")
    time.sleep(0.5)
    driver.execute_script("0,window.scrollTo(0, 6500);")
    time.sleep(0.5)
    driver.execute_script("0,window.scrollTo(0, 7000);")
    time.sleep(0.5)
    driver.execute_script("0,window.scrollTo(0, 7500);")
    time.sleep(0.5)
    page = driver.page_source
    return page

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
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
    get_content(html)
    # if html.status_code == 200:
    #    get_content(html)
    # else:
    #     print("Ошибка! Не удалось получить данные сайта =(")

def create_json():
    with open ('data.json', 'a', encoding='utf-8') as file:
        json.dump(cryptocurrency,file,indent=4, ensure_ascii='False')

parse()
create_json()