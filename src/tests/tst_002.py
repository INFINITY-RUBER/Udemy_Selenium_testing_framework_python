# -*- coding: utf-8 -*-
import os
import sys
#sys.path.append("/home/infinity/Documentos/Selenium_testing_framework_python")
#****** para que agrege la ruta de tu proyecto y encuentre src ***************
# sys.path.insert( '~/Documentos/Selenium_testing_framework_python')
from src.functions.Functions import Functions as Selenium
import unittest


class test_002(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self,'https://www.spotify.com/py/signup/',"FIREFOX")

    def test_002(self):
        pass

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()