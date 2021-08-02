''' Ejemplo para saltar entre ventanas 
'''
import os
import sys
#****** para que agrege la ruta de tu proyecto y encuentre src ***************
# sys.path.insert( '~/Documentos/Selenium_testing_framework_python')
# sys.path.append("/home/infinity/Documentos/Selenium_testing_framework_python")
sys.path.append(os.path.abspath(os.path.join(__file__, "../../..")))
from src.functions.Functions import Functions as Selenium
import unittest
import time


class test_005(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self, URL="https://listado.mercadolibre.com.ar/")
        time.sleep(2)


    def test_005(self):
        
        Selenium.new_window(self, "https://www.mercadolibre.com.ar/ofertas#nav-header")
        time.sleep(2)
        
        Selenium.switch_to_windows_name(self, "ofertas")
        time.sleep(2)

        Selenium.new_window(self, "https://www.mercadolibre.com.ar/ofertas/supermercado#nav-header")
        time.sleep(2)

        Selenium.switch_to_windows_name(self, "supermercado")
        time.sleep(2)

        Selenium.switch_to_windows_name(self, "Principal")
        time.sleep(2)
        
        Selenium.switch_to_windows_name(self, "ofertas")
        time.sleep(2)

        Selenium.switch_to_windows_name(self, "supermercado")
        time.sleep(2)

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()