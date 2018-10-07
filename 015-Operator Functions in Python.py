'''
#-Python has predefined functions for many mathematical,
#-logical, relational, bitwise etc operations under the module “operator”.

1. add(a, b)
2. sub(a, b)
3. mul(a, b)
4. truediv(a,b)
5. floordiv(a,b)
6. pow(a,b)
7. mod(a,b)
8. lt(a, b)
9. le(a, b)
10. eq(a, b)
11. gt(a,b)
12. ge(a,b)
13. ne(a,b)
'''

# importing operator module
import operator

#Initializing variables
a = 5
b = 2

# using truediv() to divide two numbers
print ("The true division of numbers is : ",end="");
print (operator.truediv(a,b))

# using floordiv() to divide two numbers
print ("The floor division of numbers is : ",end="");
print (operator.floordiv(a,b))

# using pow() to exponentiate two numbers
print ("The exponentiation of numbers is : ",end="");
print (operator.pow(a,b))

# using mod() to take modulus of two numbers
print ("The modulus of numbers is : ",end="");
print (operator.mod(a,b))


# using lt() to check if a is less than b
if(operator.lt(a,b)):
       print ("3 is less than 3")
else : print ("3 is not less than 3")

# using le() to check if a is less than or equal to b
if(operator.le(a,b)):
       print ("3 is less than or equal to 3")
else : print ("3 is not less than or equal to 3")

# using eq() to check if a is equal to b
if (operator.eq(a,b)):
       print ("3 is equal to 3")
else : print ("3 is not equal to 3")



# using gt() to check if a is greater than b
if (operator.gt(a,b)):
       print ("4 is greater than 3")
else : print ("4 is not greater than 3")

# using ge() to check if a is greater than or equal to b
if (operator.ge(a,b)):
       print ("4 is greater than or equal to 3")
else : print ("4 is not greater than or equal to 3")

# using ne() to check if a is not equal to b
if (operator.ne(a,b)):
       print ("4 is not equal to 3")
else : print ("4 is equal to 3")
