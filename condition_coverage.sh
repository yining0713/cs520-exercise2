#!/bin/bash
# Change to the directory containing the Python script
cd "./test_suit"
coverage run --branch test_conditionCoverage.py
coverage report -m --include="test_conditionCoverage.py"
coverage html --skip-covered
