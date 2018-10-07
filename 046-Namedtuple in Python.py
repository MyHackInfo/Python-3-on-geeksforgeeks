'''
    ### Namedtuple in Python ###
    -Python supports a type of container like dictionaries called “namedtuples()” present in module,
    -“collection“. Like dictionaries they contain keys that are hashed to a particular value.
    -But on contrary, it supports both access from key value and iteration, the functionality that dictionaries lack.


 ## Operations on namedtuple():>>
    1. Access by index : The attribute values of namedtuple() are ordered and can be accessed using the index number unlike dictionaries which are not accessible by index.
    2. Access by keyname : Access by keyname is also allowed as in dictionaries.
    3. using getattr() :- This is yet another way to access the value by giving namedtuple and key value as its argument.
    4. _make() :- This function is used to return a namedtuple() from the iterable passed as argument.
    5. _asdict() :- This function returns the OrdereDict() as constructed from the mapped values of namedtuple().
    6. using “**” (double star) operator :- This function is used to convert a dictionary into the namedtuple().




'''
import collections
Student=collections.namedtuple('Student',['name','age','dob'])
S=Student("Narsi",'20','1998-04-05')

## Access Operations
print("Student age using index:",S[1])
print("Student name using keyname:",S.name)
print("Student dob using getattr() is:",getattr(S,'dob'))

## Conversion Operations

li=['Jeetu','19','1999-10-06'] # iterable
di={'name':'rock','age':25,'dob':'1995-09-12'} # dictionary

print("namedtuple instance using iterable:",Student._make(li))
print("OrdereDict instance using namedtuple is :",S._asdict())
print("namedtuple instace from dict is :",Student(**di))

## Additional Operations
print("All the fields of Student are:",S._fields)
print("The modified namedtuple is :",S._replace(name = 'Mankrit'))
