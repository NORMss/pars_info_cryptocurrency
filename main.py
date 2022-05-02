import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import requests

URL = "https://coinmarketcap.com/"
HEADERS = {
    "user-agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}

cryptocurrency = []


def get_html(url, params=None):
    # page = requests.get(URL, headers=HEADERS, params=params)

    driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
    driver.get(url)
    time.sleep(2)

    # # heig_d=500
    # # while heig_d < 10000:
    # #     driver.execute_script("0,window.scrollTo(0, {heig_d});")
    # #     heig_d += 500
    # #     time.sleep(0.5)

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
            item_name = block.find(class_='sc-1eb5slv-0 iworPT').text
            item_prise = block.find(class_='sc-131di3y-0 cLgOOr').text
            items_percent24h = block.find_all(class_='sc-15yy2pl-0 kAXKAX')
            items_percent7d = block.find_all(class_='sc-15yy2pl-0 hzgCfk')
            item_marketcap = block.find(class_='sc-1ow4cwt-0 iosgXe').text
            item_volume24h = block.find(class_='sc-1ow4cwt-0 iosgXe').text
            item_circulsupp = block.find(class_='sc-1eb5slv-0 kZlTnE').text

            # items_percent24h=block.find_all('span',class_='sc-15yy2pl-0 kAXKAX')
            # items_percent7d=block.find_all('span',class_='sc-15yy2pl-0 hzgCfk')

            # str_percent24h=[]
            # str_percent7d=[]

            # for item_percent24h in items_percent24h:
            #     str_percent24h.append(item_percent24h.text)
            # for item_percent7d in items_percent7d:
            #     str_percent7d.append(item_percent7d.text)

            cryptocurrency.append({
                'name': item_name,
                'prise': item_prise,
                # 'percent24h':str_percent24h,
                # 'percent7d': str_percent7d,
                'marketcap': item_marketcap,
                'circulsupp': item_circulsupp,
                'volume24h': item_volume24h
            })


def parse():
    html = get_html(URL)
    get_content(html)


def create_json(data):
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii='False')


def create_csv(data):
    dataframe = pd.DataFrame(data)
    dataframe.to_csv('data.csv', index=False, sep=';')


def search_list(data, key):
    # sm = set(key)
    # return[a for a in sm if a in data['name']]

    try:
        return list(filter(lambda item: item['name'] == key, data))
    except Exception:
        return "Not found"

    # dataframe = pd.DataFrame(data)
    # return dataframe[dataframe['name'].str.contains(key)]


def search_json(data,key):
    items = json.loads(data)

    # Input the item name that you want to search
    item = input("Enter an item name:\n")

    # Define a function to search the item
    for keyval in items:
        if key.lower() == keyval['name'].lower():
            return keyval


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
                parse()
                flag = True
            except Exception:
                print("Please try again")
                flag = False
        elif cmd == "2" and flag == True:
            key = input("Enter (name): ")
            print(search_list(cryptocurrency, key))
        elif cmd == "3" and flag == True:
            create_json(cryptocurrency)
        elif cmd == "4" and flag == True:
            create_csv(cryptocurrency)
        elif cmd == "0":
            print()
            break
        else:
            print("You entered an invalid value")


# menu()