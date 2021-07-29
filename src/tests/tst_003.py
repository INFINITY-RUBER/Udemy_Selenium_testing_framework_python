
import os
import sys
#****** para que agrege la ruta de tu proyecto y encuentre src ***************
# sys.path.append("/home/infinity/Documentos/Selenium_testing_framework_python")
# sys.path.insert( '~/Documentos/Selenium_testing_framework_python')
sys.path.append(os.path.abspath(os.path.join(__file__, "../../..")))
from src.functions.Functions import Functions as Selenium
from src.pages.Spotify_registro import Registro
import unittest
import time


class test_003(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)

    def test_003(self):
        assert Selenium.xpath_element(self,Registro.lbl_titulo_xpath).text == 'Registrarte con tu correo electrónico'
        print(Selenium.xpath_element(self,Registro.lbl_titulo_xpath).text)
        Selenium.xpath_element(self,Registro.txt_email_xpath).send_keys('ruber@gmail.com')
        Selenium.xpath_element(self,Registro.txt_email_confirm_xpath).send_keys('ruber@gmail.com')

        Selenium._id_element(self, Registro.txt_password_id).send_keys('password')
        Selenium._id_element(self, Registro.txt_nombre_id).send_keys('Infinity')

        time.sleep(2)

    def tearDown(self):
        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()