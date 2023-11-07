from Chrome import Chrome
from selenium.webdriver.common.by import By

class PegaData:
    def pega(self, partida, chegada):
        driver = Chrome().driver()
        URL = f"https://www.google.com.br/maps/dir/{partida}/{chegada}"
        driver.get(URL)

        driver.save_screenshot(f"{partida}-{chegada}.png")

        

print(PegaData().pega('colosso', 'tauá'))