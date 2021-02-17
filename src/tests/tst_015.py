''' Funcion para conecion de base datos y querys
'''
import os
import sys
sys.path.append("/home/infinity/Documentos/Selenium_testing_framework_python")
from src.functions.Functions import Functions as Selenium
import unittest



class test_015(Selenium, unittest.TestCase):

    def setUp(self):
        self.CURSOR = Selenium.pyodbc_query(self, 'SELECT * FROM alert_alert;')

        Selenium.abrir_navegador(self, "https://www.google.com/")
        Selenium.get_json_file(self, "Google")

    def test_015(self):
        print(self.CURSOR)
        date = Selenium.textDateEnvironmentReplace(self, "Last Month")

        Selenium.get_elements(self, "txt_busqueda").send_keys(date)

        Selenium.crear_path(self) # crea la carpeta de pantallazo

        Selenium.esperar(self, 5) 


    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
