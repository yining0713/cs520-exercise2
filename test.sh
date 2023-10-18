#!/bin/sh
# Change to the directory containing the Python script
cd "./test_suit"
coverage run -m pytest test_triangle.py
coverage report -m --include="test_triangle.py"
coverage html -d initial_statement_html


#!/bin/bash
# Change to the directory containing the Python script

coverage run --branch test_triangle.py
coverage report -m --include="test_triangle.py"
coverage html -d initial_decision_html


python3 mut.py --target isTriangle --unit-test test_triangle -m 
python3 mut.py --target isTriangle --unit-test test_triangle -m --report-html initial_mutation_report.html 
