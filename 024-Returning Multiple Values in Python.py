'''
In Python, we can return multiple values from a function. Following are different ways.
    1) Using Object.
    2) Using Tuple.
    3) Using a list.
    4) Using a Dictionary.


'''
#### 1) Using Object: ####
# A Python program to to return multiple
# values from a method using class
class Test:
    def __init__(self):
        self.str = "Python3 With Me "
        self.x = 100

# This function returns an object of Test
def fun():
    return Test()

# Driver code to test above method
t = fun()
print(t.str)
print(t.x)


#### 2) Using Tuple: ####
# A Python program to to return multiple
# values from a method using tuple

# This function returns a tuple
def fun():
    str = "myhackinfo"
    x   = 20
    return str, x;  # Return tuple, we could also
                    # write (str, x)

# Driver code to test above method
str, x = fun() # Assign returned tuple
print(str)
print(x)


#### 3) Using a list ####
# A Python program to to return multiple
# values from a method using list

# This function returns a list
def fun():
    str = "Python3 With Me"
    x = 200
    return [str, x];

# Driver code to test above method
list = fun()
print(list)


#### 4) Using a Dictionary ####
# A Python program to to return multiple
# values from a method using dictionary

# This function returns a dictionary
def fun():
    d = dict();
    d['str'] = "myhackinfo"
    d['x']   = 20
    return d

# Driver code to test above method
d = fun()
print(d)
