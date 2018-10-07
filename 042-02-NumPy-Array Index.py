'''
##################
3. Array Indexing:
##################
    Knowing the basics of array indexing is important for analysing and manipulating the array object.
    NumPy offers many ways to do array indexing.
''''''''''''''''''''''''''''''''''''''''''''''''
    1->Slicing:
        -Just like lists in python, NumPy arrays can be sliced.
        -As arrays can be multidimensional, you need to specify a slice for each dimension of the array.
    2->Integer array indexing:
        -In this method, lists are passed for indexing for each dimension.
        -One to one mapping of corresponding elements is done to construct a new arbitrary array.
    3->Boolean array indexing:
        -This method is used when we want to pick elements from array which satisfy some condition.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
import numpy as np
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

# Slicing array
temp = arr[:4, ::2]
print ("Array with first 2 rows and alternate"
                    "columns(0 and 2):\n", temp)

# Integer array indexing example
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]]
print ("\nElements at indices (0, 3), (1, 2), (2, 1),"
                                    "(3, 0):\n", temp)

# boolean array indexing example
cond = arr > 0 # cond is a boolean array
temp = arr[cond]
print ("\nElements greater than 0:\n", temp)
