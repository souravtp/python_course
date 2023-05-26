import sys

print(sys.maxsize)
"""In Python, sys.maxsize returns the maximum value a variable of the int type can take.
It represents the largest positive integer that can be used on the current platform
and is dependent on the system's memory architecture. The value of sys.maxsize is typically 231 - 1
on a 32-bit system and 263 - 1 on a 64-bit system. It's important to note that
sys.maxsize is not the maximum value that can be stored in an integer variable in Python;
it is rather the maximum value that can be used for certain purposes, such as array indexing or
defining the size of a range."""