'''
# Inplace vs Standard Operators in Python
  -Normal operators do the simple assigning job. On other hand, Inplace operators behave
  -similar to normal operators except that they act in a different manner in case of
  -mutable and Immutable targets.

  Immutable=> such as numbers, strings and tuples. >>Updation But not Assignment.
  Mutable  => such as list and dictionaries.       >>Updation and Assignment both.

'''
# 1-Immutable :
# importing operator to handle operator operations
import operator

# Initializing values
x = 5
y = 6
a = 5
b = 6

# using add() to add the arguments passed
z = operator.add(a,b)

# using iadd() to add the arguments passed
p = operator.iadd(x,y)
print ("Value after adding using normal operator : ",end="")
print (z)
print ("Value after adding using Inplace operator : ",end="")
print (p)
print ("Value of first argument using normal operator : ",end="")
print (a)
print ("Value of first argument using Inplace operator : ",end="")
print (x)


# 2-Mutable

# Initializing list
a = [1, 2, 4, 5]

# using add() to add the arguments passed
z = operator.add(a,[1, 2, 3])
print ("Value after adding using normal operator : ",end="")
print (z)
print ("Value of first argument using normal operator : ",end="")
print (a)

# using iadd() to add the arguments passed
# performs a+=[1, 2, 3]
p = operator.iadd(a,[1, 2, 3])
print ("Value after adding using Inplace operator : ",end="")
print (p)
print ("Value of first argument using Inplace operator : ",end="")
print (a)
