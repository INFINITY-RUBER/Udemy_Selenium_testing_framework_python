''' Assertion de texto y elementos
'''
import os
import sys
sys.path.append("/home/infinity/Documentos/Selenium_testing_framework_python")
from src.functions.Functions import Functions as Selenium
import unittest
import pytest
import time


class test_021(unittest.TestCase, Selenium):

    def setUp(self):
        Selenium.abrir_navegador(self)
        Selenium.get_json_file(self, "Spotify_registro")

    def test_021(self):
        Selenium.get_elements(self, "Email").send_keys("mervindiazlugo@gmail.com")
        Selenium.get_elements(self, "Email Confirmacion").click()

        Mensaje_Email_Obj = Selenium.validar_elemento(self, "Mensaje Email")
        Captcha = Selenium.validar_elemento(self, "Contenedor Captcha")

        Mensaje_Email_texto = Selenium.get_text(self, "Mensaje Email")


        assert Mensaje_Email_Obj == True, "No se visualizo el mensaje de error email duplicado"
        
        assert Captcha == True, "No se visualizo el captcha"

        assert Mensaje_Email_texto == "Este correo electrónico ya está conectado a una cuenta. Inicia sesión.", f"El mensaje esperado es: 'Este correo electrónico ya está conectado a una cuenta. Inicia sesión.',  el mensaje obtenido fue: {Mensaje_Email_texto}"

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
