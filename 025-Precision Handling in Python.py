'''
#### Precision Handling ####
Python in its definition allows to handle precision of floating point numbers
in several ways using different functions.
Most of them are defined under the “math” module.


'''
# importing "math" for precision function
import math

# initializing value
a = 3.4536

# 1-using trunc() to print integer after truncating
print ("The integral value of number is : ",end="")
print (math.trunc(a))

# 2-using ceil() to print number after ceiling
print ("The smallest integer greater than number is : ",end="")
print (math.ceil(a))

# 3-using floor() to print number after flooring
print ("The greatest integer smaller than number is : ",end="")
print (math.floor(a))

# 4-using "%" to print value till 2 decimal places
print ("The value of number till 2 decimal place(using %) is : ",end="")
print ('%.2f'%a)

# 5-using format() to print value till 2 decimal places
print ("The value of number till 2 decimal place(using format()) is : ",end="")
print ("{0:.2f}".format(a))

# 6-using round() to print value till 2 decimal places 
print ("The value of number till 2 decimal place(using round()) is : ",end="")
print (round(a,2))
