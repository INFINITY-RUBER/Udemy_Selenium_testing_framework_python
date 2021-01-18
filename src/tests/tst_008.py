'''
seleccionar un conjunto de elementos
find_elements_by_xpath(“xpath”)
find_elements(By.XPATH,"")
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



class Test_008(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.NOMBRE = "Mervin Alberto"
        self.APELLIDO = "Diaz Lugo"
        self.USERNAME = "MervinUdemytest2019"
        self.PASSWORD = "Udemytest2019-A"

    def test_008(self):
        
        #INGRESO A LA APP DE REGISTRO
        self.driver.get("https://www.mercadolibre.com.ar")
        
        time.sleep(3)
        
        #self.LISTADO = self.driver.find_elements_by_xpath("//*[contains(@class, 'main-title')]")
        self.PAYMENTS = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'payment-data-title')]")

        for self.lista in self.PAYMENTS:            
            print(self.lista.text)
        self.count = 0
        
        for self.PAY in self.PAYMENTS:
            
            RESULTADO_ESPERADO= ['Tarjeta de crédito', 'Tarjeta de débito', 'Efectivo', 'Más medios de pago']
            
            assert RESULTADO_ESPERADO[self.count] == self.PAY.text, "No coinciden"
            
            self.count = self.count + 1
            
        

            
            
        

        
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()