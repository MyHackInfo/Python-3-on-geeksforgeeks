'''
    #### Python Modules ####

    -A module is a file containing Python definitions and statements.
    -A module can define functions, classes and variables.
    -A module can also include runnable code.
    -Grouping related code into a module makes the code easier to understand and use.

    ## Two Ways use Module ##
    1-The import statement.
    2-The from import Statement.

    ## The dir() function

'''

# 1-The import statement.
import cal
print(cal.add(4,3))
print(cal.sub(500,230))
print(cal.mul(3,5))


# 2-The from import Statement.
from cal import add,sub
print(add(200,500))
print(sub(200,123))


# dir() function
print(dir(cal))
print(dir(sub))
