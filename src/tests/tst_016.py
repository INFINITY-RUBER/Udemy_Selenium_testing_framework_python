''' Funcion para capturar pantalla
'''
import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, "../../..")))
from src.functions.Functions import Functions as Selenium
import unittest



class test_016(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, "https://www.google.com/")
        Selenium.get_json_file(self, "Google")

    def test_016(self):
        date = Selenium.textDateEnvironmentReplace(self, "Last Month")
        Selenium.get_elements(self, "txt_busqueda").send_keys(date)
        Selenium.send_especific_keys(self, "txt_busqueda",'Enter')
        Selenium.capturar_pantalla(self)
        

        Selenium.esperar(self, 5)


    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
