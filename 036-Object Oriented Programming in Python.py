'''
    #### Object Oriented Programming in Python ####
    # Class, Object and Members #

    * The __init__ method:>>
        The __init__ method is similar to constructors in C++ and Java.
        It is run as soon as an object of a class is instantiated.
        The method is useful to do any initialization you want to do with your object.

    * Class and Instance Variables:>>
        In Python, instance variables are variables whose value is assigned inside a constructor or method with self.




'''
########################
# A simple example class
class Test:

    # A sample method
    def fun(self):
        print("Hello")

# Create Object
obj = Test()
obj.fun()

#######################

#######################
# A Sample class with init method
class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)

# Create Object
p = Person('Narsi')
p.say_hi()
#########################


#########################
# Python program to show that the variables with a value
# assigned in class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.

# Class for Computer Science Student
class CSStudent:

    # Class Variable
    stream = 'cse'

    # The init method or constructor
    def __init__(self, roll):

        # Instance Variable
        self.roll = roll

# Objects of CSStudent class
a = CSStudent(101)
b = CSStudent(102)

print(a.stream)  # prints "cse"
print(b.stream)  # prints "cse"
print(a.roll)    # prints 001

# Class variables can be accessed using class
# name also
print(CSStudent.stream) # prints "cse"



##############################
# How to create an empty class?
# An empty class
class Test:
    pass
