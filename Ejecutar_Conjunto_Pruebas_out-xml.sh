#!/bin/sh

cd src/tests
python3 -m pytest tst_001.py tst_002.py tst_003.py --junit-xml=../results/results.xml 



