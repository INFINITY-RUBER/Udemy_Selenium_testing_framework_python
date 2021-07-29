

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(__file__, "../../..")))
# sys.path.append("/home/infinity/Documentos/Selenium_testing_framework_python")
# ****** para que agrege la ruta de tu proyecto y encuentre src ***************
# sys.path.insert( '~/Documentos/Selenium_testing_framework_python')
from src.functions.Functions import Functions as Selenium


class test_001(Selenium, unittest.TestCase):

    def setUp(self):        
        Selenium.abrir_navegador(self)

    def test_001(self):
        pass

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
