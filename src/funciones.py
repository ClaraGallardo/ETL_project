import asyncio

def asincrono(funcion):
    
    def eventos(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, funcion, *args, **kwargs)
    
    return eventos

import time

import warnings
warnings.filterwarnings('ignore')

import asyncio

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def extraer(url):
    
    global tabla

    # paso 1
    # inicia un driver
    driver = webdriver.Chrome()
    driver.get(url)
    
    time.sleep(2)
    
    
    # paso 2, cookies:
    
    time.sleep(2)

    try:
        aceptar=driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')

        aceptar.click()
    
    except:
        print('Ya')

    # paso 3 obtener tabla:

    time.sleep(3)
 
    try:

        tarjetas=[]
        for e in range(len(driver.find_elements(By.TAG_NAME,'header'))):
                
            box=driver.find_elements(By.TAG_NAME,'header')[e].text.split('\n')
            tarjetas.append(box)
    except:

        print('Algo fallo en la obtención de las tablas')
            

    # paso 4 concatenamos las tablas:

    tabla+=tarjetas



