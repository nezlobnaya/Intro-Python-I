"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE

for x in sys.argv:
    print("Argument", x)
    print("It has a length of %i arguments" % (len(sys.argv)))
    print(sys.argv)
    
arguments = len(sys.argv)
print ("The script is called with %i arguments" % (arguments))  
    
# Print out the OS platform you're using:
# YOUR CODE HERE
print("the OS platform I' am using:" , sys.platform)
# Print out the version of Python you're using:
# YOUR CODE HERE
print("the version of Python I'am using:", sys.version_info)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print("current working directory:" , os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print(os.getlogin())
print(os.geteuid())

import getpass

print(getpass.getuser())
# print(getpass.getpass())

