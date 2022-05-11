import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests


URL = "https://coinmarketcap.com/"
HEADERS = {
    "user-agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}

cryptocurrency = []


def get_html_req(url, params=None):
    page = requests.get(url, headers=HEADERS, params=params)
    return page


def get_html(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    for heig_d in range(0,driver.execute_script("return document.body.scrollHeight"),500):
        driver.execute_script(f"0,window.scrollTo(0, {heig_d});")
        time.sleep(0.5)

    page = driver.page_source

    return page


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    blocks = soup.find(class_="h7vnx2-1 bFzXgL").find_all('tr')
    for block in blocks:
        if (block.find(class_="sc-1eb5slv-0 iworPT") != None):
            item_name = block.find(class_='sc-1eb5slv-0 iworPT').text
            items_priсe = block.find_all(class_='sc-131di3y-0 cLgOOr')
            items_percent7d24=block.find_all(class_='hzgCfk')
            item_marketcap = block.find(class_='sc-1ow4cwt-0 iosgXe').text
            item_volume24h = block.find(class_='sc-1ow4cwt-0 iosgXe').text
            item_circulsupp = block.find(class_='sc-1eb5slv-0 kZlTnE').text

            str_priсe=''
            str_percent7d24h=''

            for item_priсe in items_priсe:
                str_priсe+=item_priсe.text
            for item_percent7d24 in items_percent7d24:
                str_percent7d24h+=item_percent7d24.text

            cryptocurrency.append({
                'name': item_name,
                'price': str_priсe,
                'percent24h7d':str_percent7d24h,
                'marketcap': item_marketcap,
                'circulsupp': item_circulsupp,
                'volume24h': item_volume24h
            })


def parse():
    html = get_html(URL,)
    get_content(html)


def create_json(data):
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii='False')


def create_csv(data):
    dataframe = pd.DataFrame(data)
    dataframe.to_csv('data.csv', index=False, sep=';')


def search_list(data, key):
    try:
        return list(filter(lambda item: item['name'] == key, data))
    except Exception:
        return "Not found"

def search_upper(data, key):
    items = []
    for item in data:
        if item.get("name").upper().startswith(key.upper()):
            items.append(item)
    if not items:
        return "Not found"
    else:
        return items

def menu():
    flag = False
    while True:
        print("1. Parsing")
        if flag == True:
            print("2. Search")
            print("3. Create JSON")
            print("4. Create CSV")
        print("0. Exit")
        cmd = input("Select: ")

        if cmd == "1":
            try:
                cryptocurrency.clear()
                parse()
                flag = True
            except Exception:
                cryptocurrency.clear()
                print("Please try again")
                flag = False
        elif cmd == "2" and flag == True:
            key = input("Enter (name): ")
            print(search_upper(cryptocurrency,key))
        elif cmd == "3" and flag == True:
            create_json(cryptocurrency)
        elif cmd == "4" and flag == True:
            create_csv(cryptocurrency)
        elif cmd == "0":
            print()
            break
        else:
            print("You entered an invalid value")


menu()