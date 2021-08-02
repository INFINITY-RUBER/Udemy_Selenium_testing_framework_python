import os
import sys
# sys.path.append("/home/infinity/Documentos/Selenium_testing_framework_python")
#****** para que agrege la ruta de tu proyecto y encuentre src ***************
# sys.path.insert( '~/Documentos/Selenium_testing_framework_python')
sys.path.append(os.path.abspath(os.path.join(__file__, "../../..")))
from src.functions.Functions import Functions as Selenium
from src.pages.Spotify_registro import Registro
import unittest
import time


class test_004(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)

    def test_004(self):
        #carga el json con los valores
        Selenium.get_json_file(self,'Spotify_registro')
        # acede a los valores de json
        Selenium.get_entity(self, 'Logo')
        assert Selenium.get_elements(self, 'Titulo').text == 'Registrarte con tu correo electrónico'
        assert Selenium.get_text(self, 'Titulo') == 'Registrarte con tu correo electrónico'
        Selenium.get_elements(self, 'Email').send_keys('ruber@gmail.com')

        Selenium.esperar_elemento(self, 'Email')
        Selenium.get_elements(self, 'Email Confirmacion').send_keys('ruber@gmail.com')
        
        Selenium.esperar_elemento(self, 'Email Confirmacion')
        
        Selenium.get_elements(self, 'Pass').send_keys('ruber12345')
        Selenium.get_elements(self, 'Nombre').send_keys('ruberhe')

        Selenium.esperar_elemento(self, 'Dia')
        Selenium.get_elements(self, 'Dia').send_keys('25')

        # Selenium.get_select_elements(self, 'Mes de nacimiento').select_by_visible_text('Febrero')
        Selenium.select_by_text(self,'Mes de nacimiento', 'Febrero')

        Selenium.esperar_elemento(self, 'Año')
        Selenium.get_elements(self, 'Año').send_keys('2018')

        # get_select_elements
        time.sleep(2)
        

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()