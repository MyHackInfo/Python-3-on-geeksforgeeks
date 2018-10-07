'''
#################
4. Basic operations:
''''''''''''''''''''
        -Plethora of built-in arithmetic functions are provided in NumPy.
''''''''''''''''''''
Operations on single array:
    -We can use overloaded arithmetic operators to do element-wise operation on
    -array to create a new array.
    -In case of +=, -=, *= operators,
    -the exsisting array is modified.

'''
import numpy as np

a = np.array([1, 2, 5, 3])

# add 1 to every element
print ("Adding 1 to every element:", a+1)

# subtract 3 from each element
print ("Subtracting 3 from each element:", a-3)

# multiply each element by 10
print ("Multiplying each element by 10:", a*10)

# square each element
print ("Squaring each element:", a**2)

# modify existing array
a *= 2
print ("Doubled each element of original array:", a)

# transpose of array
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])

print ("\nOriginal array:\n", a)
print ("Transpose of array:\n", a.T)
print("\n")

#####################################
'''
## Unary operators:
    -Many unary operations are provided as a method of ndarray class.
    -This includes sum, min, max, etc.
    -These functions can also be applied row-wise or column-wise by setting an axis parameter.
'''
arr = np.array([[1, 5, 6],
                [4, 7, 2],
                [3, 1, 9]])

# maximum element of array
print ("Largest element is:", arr.max())
print ("Row-wise maximum elements:",
                    arr.max(axis = 1))

# minimum element of array
print ("Column-wise minimum elements:",
                        arr.min(axis = 0))

# sum of array elements
print ("Sum of all array elements:",
                            arr.sum())

# cumulative sum along each row
print ("Cumulative sum along each row:\n",
                        arr.cumsum(axis = 1))

##############################
'''
### Binary operators:
    -These operations apply on array elementwise and a new array is created.
    -You can use all basic arithmetic operators like +, -, /, , etc.
    -In case of +=, -=, = operators, the exsisting array is modified.
'''
d = np.array([[1, 2],
            [3, 4]])
b = np.array([[4, 3],
            [2, 1]])

# add arrays
print ("Array sum:\n", d + b)

# multiply arrays (elementwise multiplication)
print ("Array multiplication:\n", d*b)

# matrix multiplication
print ("Matrix multiplication:\n", d.dot(b))

#######################################
'''
## Universal functions (ufunc):
        -NumPy provides familiar mathematical functions
        -such as sin, cos, exp, etc.
        -These functions also operate elementwise on an array,
        -producing an array as output.

'''
# create an array of sine values
x = np.array([0, np.pi/2, np.pi])
print ("Sine values of array elements:", np.sin(x))

# exponential values
x = np.array([0, 1, 2, 3])
print ("Exponent of array elements:", np.exp(x))

# square root of array values
print ("Square root of array elements:", np.sqrt(x))
