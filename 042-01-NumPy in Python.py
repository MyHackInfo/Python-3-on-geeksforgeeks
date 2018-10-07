'''
    ###########################################
    #### NumPy in Python Basic to Advanced ####
    ############################################

'''
'''
#####@ What is NumPy ###########
    :>>NumPy is a general-purpose array-processing package.
       It provides a high-performance multidimensional array object,
       and tools for working with these arrays.

    # It is the fundamental package for scientific computing with Python.
      It contains various features including these important ones:

        >1-A powerful N-dimensional array object
        >2-Sophisticated (broadcasting) functions
        >3-Tools for integrating C/C++ and Fortran code
        >4-Useful linear algebra, Fourier transform, and random number capabilities
'''
###################### ############################################################################################
#1. Arrays in NumPy:#####                                                                                        ##
##                                                                                                               ##
##  NumPy’s main object is the homogeneous multidimensional array.                                               ##
##  1->It is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers.#
##  2->In NumPy dimensions are called axes. The number of axes is rank.                                          ##
##  3->NumPy’s array class is called ndarray. It is also known by the alias array.                               ##
###################################################################################################################

import numpy as np
arr =  np.array([[1,2,4],
                [4,2,5]])
print("Array is of type",type(arr))
print("NO. of Dimensions:",arr.ndim)
print("Shape of array:", arr.shape)
print("Size of array:",arr.size)
print("Array stores elements of type:",arr.dtype)


##################################################################################################################
# 2. Array creation:>                                                                                           ##
#   ->There are various ways to create arrays in NumPy.                                                         ##
#       1->arange: returns evenly spaced values within a given interval. step size is specified.                ##
#       2->linspace: returns evenly spaced values within a given interval. num no. of elements are returned     ##
#       3->Reshaping array: We can use reshape method to reshape an array.                                      ##
#       4->Flatten array: We can use flatten method to get a copy of array collapsed into one dimension.        ##
##################################################################################################################

print("\nHere start Array Creation.")
a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float')
print("Array created using passed list:\n",a)

# Creating array from tuple
b = np.array((1 , 3, 2))
print ("\nArray created using passed tuple:\n", b)

# Creating a 3X4 array with all zeros
c = np.zeros((3, 4))
print ("\nAn array initialized with all zeros:\n", c)

# Create a constant value array of complex type
d = np.full((3, 3), 6, dtype = 'complex')
print ("\nAn array initialized with all 6s."
            "Array type is complex:\n", d)

# Create an array with random values
e = np.random.random((2, 2))
print ("\nA random array:\n", e)

# Create a sequence of integers
# from 0 to 30 with steps of 5
f = np.arange(0, 30, 5)
print ("\nA sequential array with steps of 5:\n", f)

# Create a sequence of 10 values in range 0 to 5
g = np.linspace(0, 5, 10)
print ("\nA sequential array with 10 values between"
                                        "0 and 5:\n", g)

# Reshaping 3X4 array to 2X2X3 array
arr = np.array([[1, 2, 3, 4],
                [5, 2, 4, 2],
                [1, 2, 0, 1]])

newarr = arr.reshape(2, 2, 3)

print ("\nOriginal array:\n", arr)
print ("Reshaped array:\n", newarr)

# Flatten array
arr = np.array([[1, 2, 3], [4, 5, 6]])
flarr = arr.flatten()

print ("\nOriginal array:\n", arr)
print ("Fattened array:\n", flarr)
