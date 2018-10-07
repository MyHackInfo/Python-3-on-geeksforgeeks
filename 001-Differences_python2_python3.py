'''
 Important differences between Python 2.x and Python 3.x
 1-Division operator
 2-print function
 3-Unicode
 4-xrange or range
 5-Error Handling
 6-_future_ module


'''
        # # 1-division
        # print 7 / 5
        # print -7 / 5
        #
        # # 2-print
        # print 'Hello, Geeks'
        # print('Hope You like these facts')
        #
        # # 3-Unicode
        # print(type('default string '))
        # print(type(b'string with b '))
        #
        #
        # # 4-xrange
        # for x in xrange(1, 5):
        #     print(x)
        # for x in range(1, 5):
        #     print(x)
        #
        #
        # # 5-Error Handling
        # try:
        #      trying_to_check_error
        # except NameError as err: # 'as' is needed in Python 3.x
        #      print (err, 'Error Caused')
        #
        # # 6- _future_ module
        # # In below python 2.x code, division works
        # # same as Python 3.x because we use  __future__
        # from __future__ import division
        # print 7 / 5
        # print -7 / 5
