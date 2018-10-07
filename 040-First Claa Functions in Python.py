'''
    #### First Class Function in PYthon ####

    ## Properties of first class functions:
        -A function is an instance of the Object type.
        -You can store the function in a variable.
        -You can pass the function as a parameter to another function.
        -You can return the function from a function.
        -You can store them in data structures such as hash tables, lists, …

'''
# 1. Functions are objects
def up(text):
    return text.upper()

print(up('me'))
yes=up
print(yes('me and you'))

# 2. Functions can be passed as arguments to other functions
def do(text):
    return text.upper()
def whisper(text):
    return text.lower()
def greet(func):
    take=func('it is useful for upper and lower')
    print(take)

greet(do)
greet(whisper)

# 3. Functions can return another function
def create_new(x):
    def add(y):
        return x+y

    return add
add_more=create_new(40)
print(add_more(10))
