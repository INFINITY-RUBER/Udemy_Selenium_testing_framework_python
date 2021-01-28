
import os
import sys
sys.path.insert(0, '../src')
from src.functions.Functions import Functions as Selenium
import unittest


class test_001(Selenium, unittest.TestCase):

    def setUp(self):
        Selenium.abrir_navegador(self)

    def test_001(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()