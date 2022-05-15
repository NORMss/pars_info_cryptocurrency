from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
import json

URL = "https://coinmarketcap.com/"

cryptocurrency = []


def get_html(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    for heig_d in range(0, driver.execute_script("return document.body.scrollHeight"), 500):
        driver.execute_script(f"0,window.scrollTo(0, {heig_d});")
        time.sleep(0.2)

    page = driver.page_source
    return page


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    blocks = soup.find(class_="h7vnx2-1 bFzXgL").find_all('tr')
    for block in blocks:
        if (block.find(class_="sc-1eb5slv-0 iworPT") != None):
            item_name = block.find(class_='sc-1eb5slv-0 iworPT').text
            items_priсe = block.find_all(class_='sc-131di3y-0 cLgOOr')
            items_percent24h = block.find_all(class_='kAXKAX')
            items_percent7d24 = block.find_all(class_='hzgCfk')
            item_marketcap = block.find(class_='sc-1ow4cwt-0 iosgXe').text
            item_volume24h = block.find(
                class_='sc-1eb5slv-0 hykWbK font_weight_500').text
            item_circulsupp = block.find(class_='sc-1eb5slv-0 kZlTnE').text

            str_priсe = ''
            str_percent24h = ''
            str_percent7d = ''

            for item_priсe in items_priсe:
                str_priсe += item_priсe.text
            for item_percent24h in items_percent24h:
                str_percent24h += item_percent24h.text
            for item_percent7d24 in items_percent7d24:
                str_percent7d += item_percent7d24.text

            cryptocurrency.append({
                'name': item_name,
                'price': str_priсe,
                'percent24h': str_percent24h,
                'percent7d': str_percent7d,
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


def search_upper(data, key):
    items = []
    for item in data:
        if item.get("name").upper().startswith(key.upper()):
            items.append(item)
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
            if not search_upper(cryptocurrency, key):
                print('Not found')
            else:
                for item in search_upper(cryptocurrency, key):
                    print(
                        f"{item['name']:30} {item['price']:20} {item['percent24h']:10} {item['percent7d']:10} {item['marketcap']:10} {item['circulsupp']:15} {item['volume24h']:5}")
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