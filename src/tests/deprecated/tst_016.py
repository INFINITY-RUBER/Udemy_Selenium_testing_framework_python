
'''
Capturas de Pantalla
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException

horaGlobal = time.strftime("%H%M%S") # la hora global

class Test_016(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # INGRESO A LA APP
        self.driver.get("https://www.amazon.es/")

        time.sleep(5)

    def test_016(self):
        localizador = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[5]/div[1]/div/div[1]/ul/li[2]")
        self.driver.execute_script("arguments[0].click();", localizador)

        time.sleep(5)
        #self.driver.get_screenshot_as_png()
        title = "Sobre Amazon"
        # toma de patalla
        self.driver.get_screenshot_as_file(f"../data/capturas/{title}-{horaGlobal}.png")
        
        assert title == self.driver.title, "No son iguales"



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()