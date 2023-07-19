#!/bin/bash
# Change to the directory containing the Python script
cd "./test_suit"
python.exe mut.py --target isTriangle --unit-test test_mutationAdequate -m 
python.exe mut.py --target isTriangle --unit-test test_mutationAdequate -m --report-html mutation_report.html 
