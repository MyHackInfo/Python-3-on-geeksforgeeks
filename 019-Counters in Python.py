# A Python program to show different ways to create
# Counter

from collections import Counter

# With sequence of items
print(Counter(['a','a','a','b','b','d','g']))

# with dictionary
print (Counter({'A':3, 'B':5, 'C':2,'g':6}))

# with keyword arguments
print (Counter(A=3, B=5, C=2,f=2))
