#!/bin/bash

cd src/tests
python -m pytest tst_012.py tst_013.py tst_011.py --html=../results/results.html --self-contained-html
