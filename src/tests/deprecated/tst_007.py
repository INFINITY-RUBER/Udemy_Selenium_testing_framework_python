
'''
seleccionar un conjunto de elementos
find_elements_by_xpath(“xpath”)
find_elements(By.XPATH,"")
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



class Test_007(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.NOMBRE = "Mervin Alberto"
        self.APELLIDO = "Diaz Lugo"
        self.USERNAME = "MervinUdemytest2019"
        self.PASSWORD = "Udemytest2019-A"

    def test_007(self):
        
        #INGRESO A LA APP DE REGISTRO
        self.driver.get("https://listado.mercadolibre.com.ar/sedan#D[A:sedan]")
        
        time.sleep(1)
        
        # self.LISTADO = self.driver.find_elements_by_xpath("//*[contains(@class, 'ui-search-item__title')]")
        self.LISTADO = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'ui-search-item__title')]")
        self.LISTADO2 = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'price-tag-fraction')]")
        
        print ("listado de elementos encontrados:")
        
        self.count = 0
        
        for self.lista in self.LISTADO:            
            print(self.lista.text)
            
        for self.lista2 in self.LISTADO2:
            print(self.lista2.text)
            
            
            
            
        

        
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()