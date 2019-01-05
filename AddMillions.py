#  Test script that adds in a for loop from 0 to a specified maximum

import PyFarm

# arguments from Sheets:
countTo = int(PyFarm.input(0))

# function to run:
y = int(0)
for x in range (0, countTo):
    y += 1
    

# result output:
PyFarm.output(y)




