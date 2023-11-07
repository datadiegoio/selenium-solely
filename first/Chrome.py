from selenium import webdriver
from selenium.webdriver.common.by import By 

class Chrome:
    def driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        options.add_argument('--headless')
        return webdriver.Chrome(options)