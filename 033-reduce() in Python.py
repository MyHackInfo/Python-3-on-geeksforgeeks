'''
    #### reduce() in Python ####
    -The reduce(fun,seq) function is used to apply a particular function passed in its
    -argument to all of the list elements mentioned in the sequence passed along.
    -This function is defined in “functools” module.



'''
import functools

li=[1,3,4,6,8,2]
# using reduce to compute sum of list
print ("The sum of the list elements is : ",end="")
print (functools.reduce(lambda a,b : a+b,li))

# using reduce to compute maximum element from list
print ("The maximum element of the list is : ",end="")
print (functools.reduce(lambda a,b : a if a > b else b,li))


'''
#### Using Operator Functions ####
-reduce() can also be combined with operator functions to achieve the
-similar functionality as with lambda functions and makes the code more readable.
'''
import operator

print ("The sum of the list elements is : ",end="")
print (functools.reduce(operator.add,li))

print ("The product of list elements is : ",end="")
print (functools.reduce(operator.mul,li))


'''
#### reduce() vs accumulate()  ####
-Both reduce() and accumulate() can be used to calculate the summation of a sequence elements.
-But there are differences in the implementation aspects in both of these.

    # reduce() is defined in “functools” module, accumulate() in “itertools” module.
    # reduce(fun,seq) takes function as 1st and sequence as 2nd argument.
      In contrast accumulate(seq,fun) takes sequence as 1st argument and function as 2nd argument.
'''

import itertools

# priting summation using accumulate()
print ("The summation of list using accumulate is :",end="")
print (list(itertools.accumulate(li,lambda x,y : x+y)))

# priting summation using reduce()
print ("The summation of list using reduce is :",end="")
print (functools.reduce(lambda x,y:x+y,li))
