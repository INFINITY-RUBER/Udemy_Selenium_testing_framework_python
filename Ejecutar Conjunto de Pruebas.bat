echo. ##################### ACTIVACION DEL ENTORNO VIRTUAL #####################
D:\udemy.python.SeleniumFramework\environment\Scripts\activate.bat

echo. ##################### TEST PATH #####################
cd /d D:\udemy.python.SeleniumFramework\src\tests

@echo off

echo. ##################### PRUEBAS #####################


python -m pytest tst_001.py tst_002.py tst_003.py --junitxml=results.xml





pause