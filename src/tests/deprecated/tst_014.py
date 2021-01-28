# -*- coding: utf-8 -*-
'''
Javascript – Selenium
execute_script
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException



class Test_014(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # INGRESO A LA APP
        self.driver.get("https://www.amazon.es/")

        time.sleep(5)
    def test_014(self):
        # Click
        time.sleep(5)
        localizador = self.driver.find_element(By.XPATH, "//a[@id='nav-hamburger-menu']")
        self.driver.execute_script("arguments[0].click();", localizador) # escroll y hace click

        time.sleep(5)
        localizador = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[1]/div/div[1]/ul/li[2]")
        self.driver.execute_script("arguments[0].click();", localizador)

        time.sleep(5)
        assert "Sobre Amazon" ==  self.driver.title,  "No son iguales"




    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()