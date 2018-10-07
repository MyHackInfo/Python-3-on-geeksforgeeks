'''
    #### Datetime Functions in Python ####
    -Date manipulation can also be performed using Python using “datetime” module and using “date” class in it.

    Operations on Date:
    1-MINYEAR->It displays the minimum year that can be represented using date class.
    2-MAXYEAR->It displays the maximum year that can be represented using date class.
    3-date(yyyy-mm-dd)-> This function returns a string with passed arguments in order of year, months and date.
    4-today()-> Returns the date of present day in the format yyyy-mm-dd.
    5-fromtimestamp(sec)-> It returns the date calculated from the seconds elapsed since epoch mentioned in arguments.
    6-min()-> This returns the minimum date that can be represented by date class.
    7-max()-> This returns the maximum date that can be represented by date class.

'''
import datetime
from datetime import date

print('datetime MINYEAR',datetime.MINYEAR)
print('datetime MAXYEAR',datetime.MAXYEAR)

print('datetime date',datetime.date(2018,8,11))
print('date class today',date.today())

print('date class fromtimestamp',date.fromtimestamp(9999978196))
print('date class min',date.min)
print('date class max',date.max)
