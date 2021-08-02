''' 
Funcion de la functions assert_text
para validar que salga un texto
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


class test_010(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, URL='https://www.spotify.com/py/signup/')
        Selenium.get_json_file(self, "Spotify_registro")

    def test_010(self):
        Selenium.get_elements(self,'Email').send_keys('rubergmailcom')
        Selenium.send_especific_keys(self, 'Email','Tab')

        Selenium.assert_text(self,'Email Error', 'Este correo electrónico no es válido. Asegúrate de que tenga un formato como este: ejemplo@email.com')        

        time.sleep(2)

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()