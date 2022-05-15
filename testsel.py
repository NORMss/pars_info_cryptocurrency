import json
import time
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

URL = "https://coinmarketcap.com/"

cryptocurrency = []

def getcontent(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    l = driver.find_elements_by_xpath ("//tbody/tr")
    print(len(l))
    for item in l:
        print(item.text)
    driver.quit()

getcontent(URL)