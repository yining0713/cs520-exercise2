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

##python.exe command works for windows system. Use only python if you are working on a UNIX system.


# Check the operating system
if [ "$(expr substr $(uname -s) 1 5)" = "Linux" ]; then
    # Linux
    PYTHON_EXECUTABLE="python3"
elif [ "$(expr substr $(uname -s) 1 10)" = "MINGW32_NT" ]; then
    # Windows
    PYTHON_EXECUTABLE="python3.exe"
fi

$PYTHON_EXECUTABLE mut.py --target isTriangle --unit-test test_triangle -m 
$PYTHON_EXECUTABLE mut.py --target isTriangle --unit-test test_triangle -m --report-html initial_mutation_report.html 
