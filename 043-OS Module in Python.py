'''
## OS Module in PYthon ##
#########################
    -The OS module in python provides functions for interacting with the operating system.
    -OS, comes under Python’s standard utility modules.
    -This module provides a portable way of using operating system dependent functionality.
    -The *os* and *os.path* modules include many functions to interact with the file system.

# Functions of OS Module:>
    1. os.name:->
            This function gives the name of the operating system dependent module imported.
            The following names have currently been registered: ‘posix’, ‘nt’, ‘os2’, ‘ce’, ‘java’ and ‘riscos’
    2. os.getcwd():->
            Function os.getcwd(), returns the Current Working Directory(CWD) of the file used to execute the code,
            can vary from system to system.
    4. os.popen():->
            This method opens a pipe to or from command.
            The return value can be read or written depending on whether mode is ‘r’ or ‘w’.

    5. os.close():->
            Close file descriptor fd. A file opened using open(), can be closed by close()only.
            But file opened through os.popen(), can be closed with close() or os.close().
            If we try closing a file opened with open(), using os.close(),
            Python would throw TypeError.

    6. os.rename():->
            A file old.txt can be renamed to new.txt, using the function os.rename().
            The name of the file changes only if,
            the file exists and user has sufficient privilege permission to change the file.
'''
print("")

import os
print('os name:',os.name)
print("\nGetcwd() method.")

print('Current working Directory',os.getcwd())


print('\nPopen() method.')

fd = "GFG.txt"
# popen() is similar to open()
file = open(fd, 'w')
file.write("Hello")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)
# popen() provides a pipe/gateway and accesses the file directly
file = os.popen(fd, 'w')
file.write("Hello")
file.close



print("\nClose() method")
import os
fd = "GFG.txt"
file = open(fd, 'r')
text = file.read()
print(text)
os.close(file)

print("\nRename() method.")
fd = "GFG.txt"
os.rename(fd,'New.txt')
os.rename(fd,'New.txt')
