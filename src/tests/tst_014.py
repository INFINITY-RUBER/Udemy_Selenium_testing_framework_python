''' Funcion de textDateEnvironmentReplace para restar fechas
'''
import os
import sys
sys.path.append("/home/infinity/Documentos/Selenium_testing_framework_python")
#****** para que agrege la ruta de tu proyecto y encuentre src ***************
# sys.path.insert( '~/Documentos/Selenium_testing_framework_python')
from src.functions.Functions import Functions as Selenium
from src.pages.Spotify_registro import Registro
import unittest
import time


class test_014(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, 'https://www.google.com/')
        Selenium.get_json_file(self, "Google")

    def test_014(self):

        texto = Selenium.textDateEnvironmentReplace(self,'Last Month')
        
        Selenium.send_key_text(self,'txt_busqueda', texto)

        Selenium.esperar(self, 3)


    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()