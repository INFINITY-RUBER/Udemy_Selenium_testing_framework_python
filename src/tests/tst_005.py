import os
import sys
sys.path.append("/home/infinity/Documentos/Selenium_testing_framework_python")
#****** para que agrege la ruta de tu proyecto y encuentre src ***************
# sys.path.insert( '~/Documentos/Selenium_testing_framework_python')
from src.functions.Functions import Functions as Selenium
import unittest
import time


class test_005(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, URL="https://chercher.tech/practice/frames-example-selenium-webdriver")

    def test_005(self):
        #carga el json con los valores
        Selenium.get_json_file(self,'frames')

        Selenium.switch_to_iframe(self, 'Frame2')

        Selenium.select_by_text(self,'Frame2 select', 'Avatar')

        #VOLVER AL MAIN
        Selenium.switch_to_parentFrame(self)

        #VOLVER AL Frame1
        Selenium.switch_to_iframe(self, 'Frame1')

        Selenium.send_key_text(self, 'Frame1 input', 'Hola Chicos UDEMY por Ruber')
        time.sleep(2)

        #VOLVER AL Frame3
        Selenium.switch_to_iframe(self, 'Frame3')

        Selenium.get_elements(self, 'Frame3 input').click()

        # get_select_elements
        time.sleep(2)
        

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()