'''
#### Stacking:>> Several arrays can be stacked together along different axes.
    1-> np.vstack:-> To stack arrays along vertical axis.
    2-> np.hstack:-> To stack arrays along horizontal axis.
    3-> np.column_stack:-> To stack 1-D arrays as columns into 2-D arrays.
    4-> np.concatenate:-> To stack arrays along specified axis (axis is passed as argument).
'''
import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

# vertical stacking
print("Vertical stacking:\n", np.vstack((a, b)))

# horizontal stacking
print("\nHorizontal stacking:\n", np.hstack((a, b)))

c = [5, 6]

# stacking columns
print("\nColumn stacking:\n", np.column_stack((a, c)))

# concatenation method
print("\nConcatenating to 2nd axis:\n", np.concatenate((a, b), 1))
