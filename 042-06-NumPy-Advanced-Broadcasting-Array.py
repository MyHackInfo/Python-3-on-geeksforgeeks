'''
## Broadcasting:
     In order to broadcast, the size of the trailing axes for
     both arrays in an operation must either be the same size or one of them must be one.
'''
import numpy as np

a = np.array([1.0, 2.0, 3.0])

# Example 1
b = 2.0
print(a * b)

# Example 2
c = [2.0, 2.0, 2.0]
print(a * c)
print("\n")

#############


c = np.array([0.0, 10.0, 20.0, 30.0])
d = np.array([0.0, 1.0, 2.0])

print(c[:, np.newaxis] + d)

print("\n")
####################
## Working with datatime
today = np.datetime64('2017-02-12')
print("Date is:", today)
print("Year is:", np.datetime64(today, 'Y'))

# sorting dates
a = np.array(['2017-02-12', '2016-10-13', '2019-05-22'], dtype='datetime64')
print("\nDates in sorted order:", np.sort(a))
