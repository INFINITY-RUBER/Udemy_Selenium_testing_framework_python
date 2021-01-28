from src.functions.Inicializar import Inicializar
from selenium import webdriver
from selenium.webdriver.ie.options import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as OpcionesChrome


class Functions(Inicializar):
#######################################################
    ######   -=_INICIALIZAR DRIVERS_=-   #######
    def abrir_navegador(self, URL=Inicializar.URL, navegador=Inicializar.NAVEGADOR):
        print("Directorio Base: " + Inicializar.basedir)
        self.ventanas = {}
        print("----------------")
        print(navegador)
        print("---------------")

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
            self.driver = webdriver.Chrome(chrome_options=options,
                                           executable_path=Inicializar.basedir + "/drivers/chromedriver") #en linux
            self.driver.implicitly_wait(10) 
            self.driver.get(URL)
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            return self.driver

    def tearDown(self):
        print("Se cerrará  el DRIVER")
        self.driver.quit()
