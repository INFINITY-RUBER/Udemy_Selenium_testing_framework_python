import os

class Inicializar():
# Directorio Base
    basedir = os.path.abspath(os.path.join(__file__, "../.."))# sube 2 carpetas
    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    # JsonData
    Json = basedir + u"/pages"
    print(basedir)
    print(Json)
    
    Environment = 'Test'

    # BROWSER DE PRUEBAS
    NAVEGADOR = u'CHROME'

    # DIRECTORIO DE LA EVIDENCIA
    Path_Evidencias = basedir + u'/data/capturas'

    # HOJA DE DATOS EXCEL
    Excel = basedir + u'/data/DataTest.xlsx'

    if Environment == 'Dev':
        URL = 'https://www.spotify.com/py/signup/'


    if Environment == 'Test':
        URL = 'https://www.despegar.com.ar/'