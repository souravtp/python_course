""" to find sum of list elements using recursion"""
# def suml(list1):
#     if len(list1) == 0:
#         return 0
#     else:
#         x = list1.pop(0)
#         return x + suml(list1)
#
#
# my_list = [0, 1, 2, 3, 4, 5, 6]
# print(suml(my_list))

# or

# def list_sum(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + list_sum(lst[1:])
#
#
# print(list_sum(my_list))


"""Write a Python program to convert an integer to a string in any base"""

# def to_string(n, base):
#     conver_tstring = "0123456789ABCDEF"
#     if n < base:
#         return conver_tstring[n]
#     else:
#         return to_string(n//base, base) + conver_tstring[n % base]
#
#
# print(to_string(2835, 2))

"""fibonacci series using recursion"""


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


nterms = 12

if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(fib(i))

