'''
    #### Time Functions in Python ####

    ## Operations on Time :
        1-time()->This function is used to count the number of seconds.
        2-gmtime(sec)->This function returns a structure with 9 values each representing a time attribute in sequence.
        3-asctime("time")->This function takes a time attributed string produced by gmtime() and returns a 24 character string denoting time.
        4-ctime(sec)->This function returns a 24 character time string but takes seconds as argumentself.
        5-sleep(sec)->This method is used to hault the program execution for the time specified in the arguments.


'''
import time

ti=time.gmtime()

print('1-time time method',time.time())
print('2-time gmtime method',time.gmtime())
print('3-time asctime method',time.asctime(ti))
print('4-time ctime method',time.ctime())
print('5-time sleep method',time.sleep(1))
