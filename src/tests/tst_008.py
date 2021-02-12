''' Ventana de Alertas
'''
import os
import sys
sys.path.append("/home/infinity/Documentos/Selenium_testing_framework_python")
#****** para que agrege la ruta de tu proyecto y encuentre src ***************
# sys.path.insert( '~/Documentos/Selenium_testing_framework_python')
from src.functions.Functions import Functions as Selenium
import unittest
import time


class test_008(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, URL= "https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
        Selenium.get_json_file(self, "frames")
        time.sleep(1)


    def test_008(self):
        Selenium.page_has_loaded(self)
        Selenium.switch_to_iframe(self, "Frame4 Alerta")
        Selenium.get_elements(self, "Alert").click()
        Selenium.alert_windows(self, "accept")
        Selenium.esperar(self, 4)     
                
        time.sleep(2)

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()