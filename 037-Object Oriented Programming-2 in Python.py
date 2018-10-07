'''
#### Object Oriented Programming-2 in Python ####
# Data Hiding and Object Printing #

'''
######################
# Data Hinding
# - In Python, we use double underscore (Or __) before the attributes name and those attributes will not be directly visible outside.
class MyClass:

    # Hidden member of MyClass
    __hiddenVariable = 10

    # A member method that changes
    # __hiddenVariable
    def add(self, increment):
        self.__hiddenVariable += increment
        print (self.__hiddenVariable)

# Create Object
myObject = MyClass()
myObject.add(2)
#myObject.add(5)

# This line causes error
#print (myObject.__hiddenVariable)

# How can asscess the __hiddenVariable
# use single _ before class name-
print(myObject._MyClass__hiddenVariable)

#############################################

##########################################
# Printing Objects
# -uses __repr__
class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __repr__(self):
        return "Test a:%s b:%s" % (self.a,self.b)

t = Test(123,124)
print(t)
