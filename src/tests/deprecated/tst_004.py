import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_004(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome() # self >> hace la variable Global
        self.driver.implicitly_wait(15)# espera implicita segun el tiempo
        self.driver.maximize_window() # maximizo ventana
        self.NOMBRE = "Ruber "
        self.APELLIDO = "Hernandez Liebano"
        self.USERNAME = "MervinUdemytest2019"
        self.PASSWORD = "Udemytest2019-A"

    def test_004(self):
        
        #INGRESO A LA APP DE REGISTRO
        self.driver.get("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
        
        #COLOCAR NOMBRE
        self.driver.find_element_by_id("firstName").clear()# identifica un elemento
        #self.driver.find_element_by_id("firstName").send_keys(self.NOMBRE)
        self.driver.find_element(By.ID, "firstName").send_keys(self.NOMBRE)
        
        #COLOCAR APELLIDO
        self.driver.find_element_by_xpath("//INPUT[@id='lastName']").clear()
        self.driver.find_element_by_xpath("//INPUT[@id='lastName']").send_keys(self.APELLIDO)

        #COLOCAR USERNAME
        self.driver.find_element_by_name("Username").clear()
        self.driver.find_element_by_name("Username").send_keys(self.USERNAME)

        #COLOCAR PASSWORD
        self.driver.find_element_by_xpath("(//*[@name='Passwd'])").clear()
        self.driver.find_element_by_xpath("(//*[@name='Passwd'])").send_keys(self.PASSWORD)
        time.sleep(10)
        #COLOCAR CONFIRMACION DE  PASSWORD
        self.driver.find_element_by_xpath("(//*[@name='ConfirmPasswd'])").clear()
        self.driver.find_element_by_xpath("(//*[@name='ConfirmPasswd'])").send_keys(self.PASSWORD)

        #BOTON NEXT
        self.driver.find_element_by_xpath("//*[@id='accountDetailsNext']").click()

        

        #MENSAJE DE VALIDACION
        MENSAJE_ERROR = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[1]/div/h1").text

        print(MENSAJE_ERROR)

        assert MENSAJE_ERROR == "Verificar tu número", "No coinciden"
        
    def tearDown(self):
        self.driver.quit()
        


if __name__ == "__main__":
    unittest.main()