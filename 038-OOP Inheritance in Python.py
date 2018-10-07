'''
    #### Inheritance in Python ####
    -One of the major advantages of Object Oriented Programming is re-use.
    -Inheritance is one of the mechanisms to achieve the same. In inheritance,
    -a class (usually called superclass) is inherited by another class (usually called subclass).
    -The subclass adds some attributes to superclass.


'''

'''
#############################
# Inheritance class
# SuperClass->
class Person(object):

    def __init__(self,name):
        self.name=name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False

# Inheritance SubClass
class Employee(Person):

    def isEmployee(self):
        return True

# Create Object
emp = Person("You")
print(emp.getName(),emp.isEmployee())

emp2 = Employee("Me")
print(emp2.getName(),emp2.isEmployee())


########################################
# How to check if a class is subclass and Instance of another?
# -Python provides a function issubclass() and isinstance()
# -that directly tells us if a class is subclass of another class.

class Base(object):
    pass
class Derived(Base):
    pass

print(issubclass(Derived,Base))
print(issubclass(Base,Derived))

d=Derived()
b=Base()
# b is not an instance of Derived
print(isinstance(b,Derived))
# But d is an instance of Base
print(isinstance(d,Base))

##############################

###############################
# Python support Multiple Inheritance
# -Unlike Java and like C++, Python supports multiple inheritance.
# -We specify all parent classes as comma separated list in bracket.

###############################
'''

'''
##############################
# Access parent members in a subclass
# Two way use ->
# 1- Using Parent class name
# 2- Using super()

class Top(object):
    def __init(self,x):
        self.x=x
class Down(Top):
    def __init__(self,x,y):
        Top.x=x
        self.y=y

    def printall(self):
        print(Top.x,self.y)


u=Down(100,200)
u.printall()

# super()
class B(object):
    def __init__(self,j):
        self.j=j
class D(B):
    def __init__(self,j,k):

        super(D,self).__init__(j)
        self.k=k
    def printalls(self):
        print(self.j,self.k)
z=D(10,20)
z.printalls()
###########################
'''
