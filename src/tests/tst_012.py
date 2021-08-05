''' 
Funcion de guardar variables de esernario 
copiado de texto de los elementos xpath_
'''
import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, "../../..")))
#****** para que agrege la ruta de tu proyecto y encuentre src ***************
# sys.path.insert( '~/Documentos/Selenium_testing_framework_python')
from src.functions.Functions import Functions as Selenium
from src.pages.Spotify_registro import Registro
import unittest
import time


class test_012(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.get_json_file(self, "Spotify_registro")

    def test_012(self):
        Selenium.save_variable_scenary(self,'Already', 'already') 
        Selenium.save_variable_scenary(self,'Titulo', 'titulo')  

        Selenium.new_window(self, 'https://www.google.com/')
        Selenium.get_json_file(self, 'Google')

        Selenium.switch_to_windows_name(self, 'google') # cambio de pestaña

        texto = Selenium.get_variable_scenary(self, 'titulo')
        Selenium.get_elements(self, 'txt_busqueda').send_keys(texto)
        Selenium.send_especific_keys(self, 'txt_busqueda','Enter')
        Selenium.esperar(self, 3)

        Selenium.new_window(self, 'https://www.google.com/')
        Selenium.switch_to_windows_name(self, 'google_2') # cambio de pestaña y la nombra google_2
 
        texto2 = Selenium.get_variable_scenary(self, 'already')
        Selenium.send_key_text(self,'txt_busqueda', texto2)
        Selenium.send_especific_keys(self, 'txt_busqueda','Enter')

        Selenium.esperar(self, 3)


    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()