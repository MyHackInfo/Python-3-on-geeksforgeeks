'''
### Linear algebra in NumPy:->> The Linear Algebra module of NumPy offers various methods to apply linear algebra on any numpy array.

 # You can find:
#################
    1-> rank, determinant, trace, etc. of an array.
    2-> eigen values of matrices
    3-> matrix and vector products (dot, inner, outer,etc. product), matrix exponentiation
    4-> solve linear or tensor equations and much more!

'''

import numpy as np

A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])

print("Rank of A:", np.linalg.matrix_rank(A))

print("\nTrace of A:", np.trace(A))

print("\nDeterminant of A:", np.linalg.det(A))

print("\nInverse of A:\n", np.linalg.inv(A))

print("\nMatrix A raised to power 3:\n", np.linalg.matrix_power(A, 3))
