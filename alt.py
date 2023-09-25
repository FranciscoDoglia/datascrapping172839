from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pandas as pd

import time

options = webdriver.ChromeOptions()
options.add_argument('--headless') # sin interfaz grafica
options.add_argument('--no-sandbox') # Seguridad
# options.add_argument('--disable-dev-shm-usage') # configuracion de linux
options.add_argument('--disable-gpu')
options.add_argument('--user-agent=""Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36""')

driver = webdriver.Chrome(options= options)


def scrape_goog(palabra):
    url = "http://google.com.ar"
    driver.get(url)
    input = driver.find_element(by=By.XPATH, value='//textarea[1]')
    input.send_keys(palabra + Keys.ENTER)
    time.sleep(5)
    # driver.save_screenshot("prueba.png")
    search_results_name = driver.find_elements(By.CLASS_NAME, 'VuuXrf')
    search_results_link = driver.find_elements(By.CLASS_NAME, 'byrV5b')
    # competitors_brands = [element.text for element in search_results_name]
    # competitors_links = [element.text for element in search_results_link]
    # print(competitors_brands, competitors_links)
    # Crear un diccionario vacío
    competitors_list = [(name.text, link.text) for name, link in zip(search_results_name, search_results_link)]
    # Crear un DataFrame a partir del diccionario
    df = pd.DataFrame(competitors_list, columns=['Competitor', 'Link'])
    # Imprimir el DataFrame
    df.to_excel(f'Competidores {palabra} Data Scrapping.xlsx', index=False, engine='openpyxl')

    return f'Excel guardado como: "Competidores {palabra} Data Scrapping.xlsx"'

