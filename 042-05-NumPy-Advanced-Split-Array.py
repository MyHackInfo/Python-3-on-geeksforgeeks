'''
### Splitting:>> For splitting, we have these functions:
        1-> np.hsplit:-> Split array along horizontal axis.
        2-> np.vsplit:-> Split array along vertical axis.
        3-> np.array_split:-> Split array along specified axis.

'''
import numpy as np

a = np.array([[1, 3, 5, 7, 9, 11],
              [2, 4, 6, 8, 10, 12]])

# horizontal splitting
print("Splitting along horizontal axis into 2 parts:\n", np.hsplit(a, 2))

# vertical splitting
print("\nSplitting along vertical axis into 2 parts:\n", np.vsplit(a, 2))
