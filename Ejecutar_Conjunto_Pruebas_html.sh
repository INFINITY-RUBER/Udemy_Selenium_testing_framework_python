#!/bin/bash

cd src/tests
python -m pytest tst_001.py tst_002.py tst_016.py --html=../results/results.html --self-contained-html
