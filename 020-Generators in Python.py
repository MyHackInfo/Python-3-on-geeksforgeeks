'''
#### Generators in Python ####
    1-Generator-Function:
                A generator-function is defined like a normal function,
                but whenever it needs to generate a value, it does so with
                the yield keyword rather than return. If the body of a def
                contains yield, the function automatically becomes a generator function.

    1-Generator-Object:
                Generator functions return a generator object. Generator objects are
                used either by calling the next method on the generator object.

'''
'''
# A generator-function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)
'''

'''
# A Python program to demonstrate use of
# generator object with next()
# A generator function
def simpleGeneratorFuns():
    yield 1
    yield 2
    yield 3

# x is a generator object
x = simpleGeneratorFuns()
# Iterating over the generator object using next
print(x.next()); # In Python 3, __next__()
print(x.next());
print(x.next());
'''
