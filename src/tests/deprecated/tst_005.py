import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_005(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.NOMBRE = "Ruber Hernandez"
        self.APELLIDO = "Hernandez"
        self.USERNAME = "MervinUdemytest2019"
        self.PASSWORD = "Udemytest2019-A"

    def test_005(self):
        
        #INGRESO A LA APP DE REGISTRO
        self.driver.get("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
        
        #COLOCAR NOMBRE
        # find_element_by_name
        # driver.find_element(By.{TIPO DE LOCALIZADOR}, localizador)
        self.driver.find_element_by_name("firstName").clear()
        self.driver.find_element(By.NAME, "firstName").send_keys(self.NOMBRE)
        
        #COLOCAR APELLIDO
        # find_element_by_css_selector
        # driver.find_element(By.{TIPO DE LOCALIZADOR}, localizador)
        self.driver.find_element_by_css_selector("#lastName").clear()
        self.driver.find_element(By.NAME, "lastName").send_keys(self.APELLIDO)
        
        
        # self.driver.find_element_by_partial_link_text("Ayuda").click()
        print(self.driver.find_element_by_partial_link_text("Ayuda").text)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Ayuda").click()
        time.sleep(5)        
        #Sign in instead
        

        #self.driver.find_elements_by_xpath("").clear()
        # self.driver.find_element_by_id("firstName").send_keys(self.NOMBRE)
        #self.driver.find_element(By.ID, "firstName").send_keys(self.NOMBRE)
        #MENSAJE DE VALIDACION
        #MENSAJE_ERROR = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[1]/div/h1").text
        #print(MENSAJE_ERROR)

        #assert MENSAJE_ERROR == "Verificar tu número", "No coinciden"
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()