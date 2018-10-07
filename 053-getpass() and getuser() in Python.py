'''
    ### getpass() and getuser() in Python ###
    -getpass() prompts the user for a password without echoing.
    -The getpass module provides a secure way to handle the password
    -prompts where programs interact with the users via the terminal.

'''
# 1-getpass()
# -The getpass() function is used to prompt to users using the string prompt and reads the
# -input from the user as Password. The input read deafults to “Password: ” is returned to the caller as a string.

import getpass

try:
    p = getpass.getpass()
except Exception as error:
    print('ERROR', error)
else:
    print('Password entered:', p)


# 2-getuser()
# -The getuser() function displays the login name of the user. This function checks the environment
# -variables LOGNAME, USER, LNAME and USERNAME, in order, and returns the value of the first non-empty string.

user = getpass.getuser()

while True:
    pwd = getpass.getpass("User Name : %s" % user)

    if pwd == 'abcd':
        print ("Welcome!!!")
        break
    else:
        print ("The password you entered is incorrect.")
        
