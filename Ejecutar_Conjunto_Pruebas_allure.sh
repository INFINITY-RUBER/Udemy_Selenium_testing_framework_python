#!/bin/bash

cd src/tests
python3 -m pytest tst_014_with_allure.py --alluredir ../allure-results
python3 -m pytest tst_016_allure.py --alluredir ../allure-results
python3 -m pytest tst_015_with_allure.py --alluredir ../allure-results
