from Chrome import Chrome
from selenium.webdriver.common.by import By

class PegaData:
    def pega(self, partida, chegada):
        driver = Chrome().driver()
        URL = f"https://www.google.com.br/maps/dir/{partida}/{chegada}"
        driver.get(URL)
        resultado = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div/div[1]/div[2]/div')
        driver.save_screenshot(f"{partida}-{chegada}.png")
        return resultado.text

        

# print(PegaData().pega('fortaleza', 'praia do presidio'))