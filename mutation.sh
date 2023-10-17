#!/bin/bash
# Change to the directory containing the Python script
# cd "./test_suit"
# python.exe mut.py --target isTriangle --unit-test test_mutationAdequate -m 
# python.exe mut.py --target isTriangle --unit-test test_mutationAdequate -m --report-html mutation_report.html 


#!/bin/bash
# Change to the directory containing the Python script
cd "./test_suit"

# Define the output file for both stdout and stderr
output_file="mutation_output.log"

# Use tee to capture both stdout and stderr and save them to the file
{
    python.exe mut.py --target isTriangle --unit-test test_mutationAdequate -m 
    python.exe mut.py --target isTriangle --unit-test test_mutationAdequate -m --report-html mutation_report.html 
} 2>&1 | tee "$output_file"
