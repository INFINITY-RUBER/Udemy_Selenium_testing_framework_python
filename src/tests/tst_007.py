''' Ejemplo para la funcion scrolback
arguments[0].scrollIntoView()
arguments[0].click()
'''
import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, "../../..")))
#****** para que agrege la ruta de tu proyecto y encuentre src ***************
# sys.path.insert( '~/Documentos/Selenium_testing_framework_python')
from src.functions.Functions import Functions as Selenium
import unittest
import time


class test_007(Selenium, unittest.TestCase):

    def setUp(self):        
        Selenium.abrir_navegador(self, URL="https://www.amazon.es")
        time.sleep(2)


    def test_007(self):
        Selenium.get_json_file(self,'Amazon') # cargo valores json
        Selenium.scroll_to(self, 'Sobre Amazon')
        Selenium.esperar(5)
        Selenium.js_clic(self, 'Sobre Amazon')
        Selenium.page_has_loaded(self)
        
        time.sleep(2)

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()