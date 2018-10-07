'''
    #### calendar Function in python ####
    1.calendar(year,w,l,c)=>This function displays the year, width of characters, no. of lines per week and column separations.
    2.firstweekday()
    3.isleap(year)
    4-leapdays(year1,year2)
    5-month(year,month,w,l)
    5-monthrange(year, month)=>This function returns two integers, first, the starting day number of week(0 as monday) ,
                                second, the number of days in the month.
    6-prcal(year, w, l, c) :- This function also prints the calendar of specific year but there is
                                no need of “print” operation to execute this.
    7-prmonth(year, month, w, l) :- This function also prints the month of specific year but there is no need of “print” operation to execute this.
    8-setfirstweekday(num) :- This function sets the day start number of week.
    9-weekday(year, month, date) :- This function returns the week day number(0 is Monday) of the date specified in its arguments.


'''

import calendar
print(calendar.calendar(2018,2,1,6))
print(calendar.firstweekday())
print(calendar.isleap(2018))
print(calendar.leapdays(2000,2018))
print(calendar.month(2018,5,2,1))
print(calendar.monthrange(2008,2))
calendar.prcal(2020,2,1,6)

calendar.prmonth(2019,5,2,1)
calendar.setfirstweekday(3)
print(calendar.weekday(2018,8,10))
