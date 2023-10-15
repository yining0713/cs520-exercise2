# IE2-Triangle
Template code for the In-Class Exercise 2 on Unit Testing, an exercise that focuses on unit testing and
test effectiveness, using code coverage and mutation analysis.

# Installation
1. Run ```pip3 install -r requirements.txt.```
2. Test the setup by running 
  ```
   cd test_suit
   python -m test_isTriangle
   ```


# Control Flow Diagram
We will use the ```py2cfg``` package (https://pypi.org/project/py2cfg/) to generate control flow diagram from the file ```isTriangle.py```. Note: Windows users may find that py2cfg has a specific dependency that only works in Unix system. In that case, please execute it in a UNIX virtual machine.

1. Use the following command to install the py2cfg library: ```pip3 install py2cfg --user```
2. Install graphviz for visualizing the generated CFG. In Ubuntu, you can use the following command:
```sudo apt install graphviz```. 
Link to the Graphviz download: https://graphviz.org/download/
3. If you have installed it, then the default command is:
```py2cfg isTriangle.py```. You should find a generated SVG file in the same directory. 


# Testing

You will need to create three test suites and place the files in test_suit folder. The names of the files should be the following:
```
test_statementCoverage.py
test_conditionCoverage.py 
test_mutationAdequate.py 
```

The following shell scripts will be used for unit testing using mutation analysis and code coverage. 

```
mutation: run './mutation.sh'
line coverage: run './statement_coverage.sh'
branch coverage: run ./condition_coverage.sh'
```

NB: python.exe command works for windows system. Use only python if you are working on a UNIX system. 

# Troubleshooting
If you encounter an error with ```if self.isAlive():``` from mutpy, do the following:
1. Open ```utils.py``` shown in the error message from the "mutpy" scripts in the installed directory. 
2. Go to the line ```if self.isAlive():```, shown in the error message
3. Make the following change: if self.isAlive(): becomes ```if self.is_alive():```

