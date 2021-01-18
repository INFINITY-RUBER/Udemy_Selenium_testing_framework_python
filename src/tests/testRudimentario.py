###### IMPORTANDO LIBRERIAS DE SELENIUM
from selenium import webdriver
import time


###### INICIALIZO EL DRIVER
driver = webdriver.Chrome() # se debe colocar chromedriver en el binario del entorno virtual o de lo contrario asi:
# webdriver.Chrome(executable_path=r'./chromedriver')

### VOY HOST DE LA APLICACION
driver.get("http://www.python.org")

#SE VERIFICA QUE EL TITULO DE LA APLICACION
assert "Python" in driver.title

time.sleep(10)

###### ALMACENO EN UNA VARIABLE EL OBJETO CON QUE VOY A INTERACTUAR
elem = driver.find_element_by_id("id-search-field")

###lIMPIO LA CAJA DE TEXTO
elem.clear()

###ESCRIBE EN LA CAJA
elem.send_keys("RUBER HERNANDEZ ESCRIBE:pycon")

time.sleep(10)

#CIEROO EL DRIVER
driver.close()