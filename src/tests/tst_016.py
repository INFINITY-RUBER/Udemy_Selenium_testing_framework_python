''' Funcion para capturar pantalla
'''
import os
import sys
sys.path.append("/home/infinity/Documentos/Selenium_testing_framework_python")
from src.functions.Functions import Functions as Selenium
import unittest



class test_016(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, "https://www.google.com/")
        Selenium.get_json_file(self, "Google")

    def test_016(self):
        Selenium.capturar_pantalla(self)
        

        Selenium.esperar(self, 5)


    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
