'''
#### Class or Static Variables in Python ####

-The Python approach is simple, it doesn’t require a static keyword.
-All variables which are assigned a value in class declaration are class variables.
-And variables which are assigned values inside class methods are instance variables.

# We Chnage class Variable Value
    1- Use Object Name
    2- Use Claa Name

'''

class Student:
    age=18                  # Class Variable

    def __init__(self,name,roll):
        self.name=name      # Instance Variable
        self.roll=roll      # Instance Variable

# Create object of Student class
a = Student('Narsi', 101)
b = Student('Jeetu', 102)

print(a.age)
print(a.roll)
print(a.name)
print(a.roll)
print(b.name)
print(b.roll)

# We change class variable.
# Use Object help
#a.age=20
print(a.age)

# Use class name
# Student.age=25
print(a.age)
