from asyncore import write
import requests
url = "https://coinmarketcap.com/"
page = requests.get(url)
with open('mainpage.txt', 'w',encoding='utf-8') as f:
    f.write(page.text)