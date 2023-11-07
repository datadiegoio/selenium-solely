from selenium import webdriver
from selenium.webdriver.common.by import By 
# ^ ---- 
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--headless')

partida = "fortaleza, ce"
chegada = "ipaumirim, ce"

driver = webdriver.Chrome(options)

URL = f"https://www.google.com.br/maps/dir/{partida}/{chegada}"

driver.get(URL)

driver.save_screenshot(f"{partida}-{chegada}.png")

print(driver.title)