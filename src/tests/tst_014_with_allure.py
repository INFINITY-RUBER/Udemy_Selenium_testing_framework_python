# -*- coding: utf-8 -*-
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
import allure
import pytest

@allure.feature(u'Test Udemy 1')
@allure.story(u'015: Visitamos google y colocamos una fecha')
@allure.testcase(u"Caso de Prueba 015", u'http://my.tms.org/browse/TESTCASE-39')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Se requiere visitar el sitio googole:</br>
Deseamos ingresar texto en el recuadro de busqueda de google </br>
 </br></br>""")


class test_014(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1: Ingresar a Google'):
            Selenium.abrir_navegador(self, 'https://www.google.com/')
            Selenium.get_json_file(self, "Google")

    def test_014(self):
        with allure.step(u'PASO 2: Ingresar termino de Busqueda'):
            texto = Selenium.textDateEnvironmentReplace(self,'Last Month')
            
            Selenium.send_key_text(self,'txt_busqueda', texto)

            Selenium.esperar(self, 3)



    def tearDown(self):
        with allure.step(u'PASO 3: Cerramos el navegador'):
            Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()