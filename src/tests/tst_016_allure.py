# -*- coding: utf-8 -*-
''' Funcion para capturar pantalla
'''
import os
import sys
sys.path.append("/home/infinity/Documentos/Selenium_testing_framework_python")
from src.functions.Functions import Functions as Selenium
import unittest
import allure


@allure.feature(u'Test Udemy 1')
@allure.story(u'015: caturar pantalla')
@allure.testcase(u"Caso de Prueba 015", u'http://my.tms.org/browse/TESTCASE-39')
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Se requiere visitar el sitio googole:</br>
Deseamos ingresar texto en el recuadro de busqueda de google </br>
 </br></br>""")


class test_016(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1: Ingresar a Google'):
            Selenium.abrir_navegador(self, "https://www.google.com/")
            Selenium.get_json_file(self, "Google")

    def test_016(self):
        with allure.step(u'PASO 2: captura pantalla '):
            Selenium.captura(self, 'Google')      
            Selenium.esperar(self, 5)


    def tearDown(self):
        with allure.step(u'PASO 3: Cerramos el navegador'):
            Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
