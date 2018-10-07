'''
        #### Function Decorator ####

@ Following are important facts about functions in Python that are useful to understand decorator functions. @

    1-In Python, we can define a function inside another function.
    2-In Python, a function can be passed as parameter to another function (a function can also return another function).



'''
# Function inside function
'''
# Adds a welcome message to the string
def messageWithWelcome(str):
    # Nested function
    def addWelcome():
        return "Welcome to "
    # Return concatenation of addWelcome()
    # and str.
    return  addWelcome() + str
# To get site name to which welcome is added
def site(site_name):
    return site_name
print(messageWithWelcome(site("Python3 With Me")))
'''

# Decorator function
'''
        A decorator is a function that takes a function as its only parameter and returns a function.
        This is helpful to “wrap” functionality with the same code over and over again.
        For example, above code can be re-written as following.

        We use @func_name to specify a decorator to be applied on another function.

        Decorators can also be useful to attach data (or add attribute) to functions.
'''


'''
def text(name):

    def full(fullname):
        return "My name is " + fullname

    return full

@text
def name(put):
    return put

print(name("narsi"))


'''

'''
# A decorator function to attach
# data to func
def attach_data(func):
       func.data = 'Narsi'
       return func

@attach_data
def add (x, y):
       return x + y

# Driver code
# This call is equivalent to attach_data()
# with add() as parameter
print(add(2, 3))
print(add.data)
'''
