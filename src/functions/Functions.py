from src.functions.Inicializar import Inicializar
from selenium import webdriver
from selenium.webdriver.ie.options import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as OpcionesChrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, NoSuchWindowException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.ie.options import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as OpcionesChrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

import pytest
import json


class Functions(Inicializar):
#######################################################
    ######   -=_INICIALIZAR DRIVERS_=-   #######
    def abrir_navegador(self, URL=Inicializar.URL, navegador=Inicializar.NAVEGADOR):
        print("Directorio Base: " + Inicializar.basedir)
        self.ventanas = {}
        print("-"*20)
        print(navegador)
        print("-"*20)

        if navegador == ("IExplorer"):
            caps = DesiredCapabilities.INTERNETEXPLORER.copy() # config de interne exp
            caps["platform"] = "WINDOWS"
            caps["browserName"] = "internet explorer"
            caps["ignoreZoomSetting"] = True
            caps["requireWindowFocus"] = True
            caps["nativeEvents"] = True
            self.driver = webdriver.Ie(Inicializar.basedir + "\\drivers\\IEDriverServer.exe", caps)
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.ventanas = {'Principal':self.driver.window_handles[0]}
            print(self.ventanas)
            return self.driver

        if navegador == ("CHROME"):
            options = OpcionesChrome()
            options.add_argument('start-maximized')# hace que las opciones este maximizado 
            # self.driver = webdriver.Chrome(chrome_options=options, executable_path=Inicializar.basedir + "\\drivers\\chromedriver.exe") PARA WINDOWS
            self.driver = webdriver.Chrome(chrome_options=options,executable_path=Inicializar.basedir + "/drivers/chromedriver") #en linux
            self.driver.implicitly_wait(10) 
            self.driver.get(URL)
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            return self.driver

        if navegador == ("FIREFOX"):
            self.driver = webdriver.Firefox(executable_path=Inicializar.basedir + "/drivers/geckodriver") #en linux
            # self.driver = webdriver.Firefox() windows
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.ventanas = {'Principal':self.driver.window_handles[0]}
            return self.driver

    def tearDown(self):
        print("Se cerrará  el DRIVER")
        self.driver.quit()

##########################################################################
##############       -=_lOCATORS   HANDLE _=-              ###############
##########################################################################

    def xpath_element(self, XPATH):
        elements = self.driver.find_element_by_xpath(XPATH)
        print("Xpath_Elements: Se interactuo con el elemento " + XPATH)
        return elements

    def _xpath_element(self, XPATH):
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.visibility_of_element_located((By.XPATH, XPATH)))
            elements = self.driver.find_element_by_xpath(XPATH)
            print(u"Esperar_Elemento: Se visualizo el elemento " + XPATH)
            return True

        except TimeoutException:
            print(u"Esperar_Elemento: No presente " + XPATH)
            Functions.tearDown(self)
        except NoSuchElementException:
            print(u"Esperar_Elemento: No presente " + XPATH)
            Functions.tearDown(self)

#******* ID ******************************
    def id_element(self, ID):
        elements = self.driver.find_element_by_id(ID)
        print("Xpath_Elements: Se interactuo con el elemento " + ID)
        return elements

    def _id_element(self, ID):
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.visibility_of_element_located((By.ID, ID)))
            elements = self.driver.find_element_by_id(ID)
            print(u"Esperar_Elemento: Se visualizo el elemento " + ID)
            return elements

        except TimeoutException:
            print(u"Esperar_Elemento: No presente " + ID)
            Functions.tearDown(self)
        except NoSuchElementException:
            print(u"Esperar_Elemento: No presente " + ID)
            Functions.tearDown(self)

#******* NAME ******************************
    def name_element(self, name):
        elements = self.driver.find_element_by_id(name)
        print("Xpath_Elements: Se interactuo con el elemento " + name)
        return elements

    def _name_element(self, name):
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.visibility_of_element_located((By.ID, name)))
            elements = self.driver.find_element_by_id(name)
            print(u"Esperar_Elemento: Se visualizo el elemento " + name)
            return elements

        except TimeoutException:
            print(u"Esperar_Elemento: No presente " + name)
            Functions.tearDown(self)
        except NoSuchElementException:
            print(u"Esperar_Elemento: No presente " + name)
            Functions.tearDown(self)

##########################################################################
##############       -=_JSON     HANDLE _=-              #################
##########################################################################
 
    def get_json_file(self, file):
        json_path = Inicializar.Json + "/" + file + '.json'
        try:
            with open(json_path, "r") as read_file:
                self.json_strings = json.loads(read_file.read())
                print ("get_json_file: "+ json_path)
        except FileNotFoundError:
            self.json_strings = False
            pytest.skip(u"get_json_file: No se encontro el Archivo " + file)
            Functions.tearDown(self)

    def get_entity(self, entity):
        if self.json_strings is False:
            print ("Define el DOM para esta prueba")
        else:
            try:
                self.json_ValueToFind = self.json_strings[entity]["ValueToFind"]
                self.json_GetFieldBy = self.json_strings[entity]["GetFieldBy"]
                print (self.json_ValueToFind,"---;-- ",self.json_GetFieldBy)

                return True

            except KeyError:
                pytest.skip(u"get_entity: No se encontro la key a la cual se hace referencia: " + entity)
                #self.driver.close()
                Functions.tearDown(self)
                return None

############## ############################## ##############################
    def get_elements(self, entity, MyTextElement = None):
            Get_Entity = Functions.get_entity(self, entity)

            if Get_Entity is None:
                print("No se encontro el valor en el Json definido")
            else:
                try:
                    if self.json_GetFieldBy.lower() == "id":
                        elements = self.driver.find_element_by_id(self.json_ValueToFind)

                    if self.json_GetFieldBy.lower() == "name":
                        elements = self.driver.find_element_by_name(self.json_ValueToFind)

                    if self.json_GetFieldBy.lower() == "xpath":
                        if MyTextElement is not None:
                            self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                            print (self.json_ValueToFind)
                        elements = self.driver.find_element_by_xpath(self.json_ValueToFind)

                    if self.json_GetFieldBy.lower() == "link":
                        elements = self.driver.find_element_by_partial_link_text(self.json_ValueToFind)

                    if self.json_GetFieldBy.lower() == "css":
                        elements = self.driver.find_element_by_css_selector(self.json_ValueToFind)

                    print("get_elements: " + self.json_ValueToFind)
                    return elements

                except NoSuchElementException:
                    print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                    Functions.tearDown(self)
                except TimeoutException:
                    print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                    Functions.tearDown(self)

    def get_text(self, entity, MyTextElement = None):
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element_by_id(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element_by_name(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print (self.json_ValueToFind)
                    elements = self.driver.find_element_by_xpath(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element_by_partial_link_text(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_element_by_css_selector(self.json_ValueToFind)

                print("get_text: " + self.json_ValueToFind)
                print("Text Value : " + elements.text)
                return elements.text

            except NoSuchElementException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)
            except TimeoutException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)

    def select_by_text(self, entity, text):
        Functions.get_select_elements(self, entity).select_by_visible_text(text)

    def send_key_text(self, entity, text): # funcion par aenviar texto
        Functions.get_elements(self, entity).clear()
        Functions.get_elements(self, entity).send_keys(text)

    def esperar_elemento(self, locator, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            return print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.ID, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.ID, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.NAME, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.NAME, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 20)
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)

                    wait.until(EC.visibility_of_element_located((By.XPATH, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.XPATH, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

            except TimeoutException:
                print(u"Esperar_Elemento: No presente " + locator)
                Functions.tearDown(self)
            except NoSuchElementException:
                print(u"Esperar_Elemento: No presente " + locator)
                Functions.tearDown(self)
        
    
    def get_select_elements(self, entity):
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    select = Select(self.driver.find_element_by_id(self.json_ValueToFind))

                if self.json_GetFieldBy.lower() == "name":
                    select = Select(self.driver.find_element_by_name(self.json_ValueToFind))

                if self.json_GetFieldBy.lower() == "xpath":
                    select = Select(self.driver.find_element_by_xpath(self.json_ValueToFind))

                if self.json_GetFieldBy.lower() == "link":
                    select = Select(self.driver.find_element_by_partial_link_text(self.json_ValueToFind))

                print("get_select_elements: " + self.json_ValueToFind)
                return select

            # USO
            #       select by visible text  #       select.select_by_visible_text('Banana')
            #       select by value  #       select.select_by_value('1')

            except NoSuchElementException:
                print("No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)

            except TimeoutException:
                print("No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)

    def switch_to_iframe(self, Locator):
        iframe = Functions.get_elements(self, Locator)
        self.driver.switch_to.frame(iframe)
        print (f"Se realizó el switch a {Locator}")

    def switch_to_parentFrame(self):
        self.driver.switch_to.parent_frame()

    def switch_to_windows_name(self, ventana):
        if ventana in self.ventanas:
            self.driver.switch_to.window(self.ventanas[ventana])
            Functions.page_has_loaded(self)
            print ("volviendo a " + ventana + " : " + self.ventanas[ventana])
        else:
            self.nWindows = len(self.driver.window_handles) - 1
            self.ventanas[ventana] = self.driver.window_handles[int(self.nWindows)]
            self.driver.switch_to.window(self.ventanas[ventana])
            self.driver.maximize_window()
            print(self.ventanas)
            print ("Estas en " + ventana + " : " + self.ventanas[ventana])
            Functions.page_has_loaded(self)

    def new_window(self, URL):
        self.driver.execute_script(f'''window.open("{URL}","_blank");''')
        Functions.page_has_loaded(self)

    def page_has_loaded(self):
        driver = self.driver
        print("Checking if {} page is loaded.".format(self.driver.current_url))
        page_state = driver.execute_script('return document.readyState;')
        yield
        WebDriverWait(driver, 30).until(lambda driver: page_state == 'complete')
        assert page_state == 'complete', "No se completo la carga"