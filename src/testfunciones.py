from selenium.common.exceptions import WebDriverException

import asyncio
import time

import warnings
warnings.filterwarnings('ignore')

import asyncio

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException

def extraer(url):

    global tabla

    while True:
        # paso 1: inicia un driver
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(2)

        # paso 2: cookies
        time.sleep(2)

        try:
            aceptar = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
            aceptar.click()
        except:
            print('Ya')

        # paso 3: obtener tabla
        time.sleep(3)

        tarjetas = []

        try:
            for e in range(len(driver.find_elements(By.TAG_NAME, 'header'))):
                box = driver.find_elements(By.TAG_NAME, 'header')[e].text.split('\n')
                tarjetas.append(box)
        except:
            print('Algo falló en la obtención de las tablas')

        # paso 4: concatenamos las tablas
        if tarjetas:
            tabla += tarjetas
            break  # Salir del bucle si se ha obtenido alguna información
        else:
            print('La lista "tarjetas" está vacía, volviendo a abrir la URL.')

    # Cerrar el controlador después de haber terminado
    driver.quit()


