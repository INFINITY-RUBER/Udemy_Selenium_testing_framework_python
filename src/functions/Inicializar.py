import os

class Inicializar():
# Directorio Base
    basedir = os.path.abspath(os.path.join(__file__, "../.."))# sube 2 carpetas
    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    # JsonData
    Json = basedir + u"/pages"
    # print(basedir)
    # print(Json)
    
    Environment = 'Dev'

    # BROWSER DE PRUEBAS
    # NAVEGADOR = u'IExplorer'
    NAVEGADOR = u'CHROME'
    # NAVEGADOR = u'FIREFOX'



    # DIRECTORIO DE LA CATURA PANTALLAS
    Path_Evidencias = basedir + u'/data/capturas'

    # HOJA DE DATOS EXCEL
    Excel = basedir + u'/data/DataTest.xlsx'

    if Environment == 'Dev':
        URL = 'https://www.spotify.com/py/signup/'
        User = 'mdiaz'
        Pass = 'Mm121666'
        DB_HOST = '127.0.0.1'
        DB_PORT = '3306'
        DB_DATABASE = 'djangochannels'
        DB_USER = 'djruber'
        DB_PASS = 'Ericsson2018@'


    if Environment == 'Test':
        URL = 'https://www.despegar.com.ar/'