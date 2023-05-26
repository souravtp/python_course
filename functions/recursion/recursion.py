# factorial of a number
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         x = n*factorial(n-1)  # when python reaches this point it finds call for 'factorial(n-1)'. So, it returns
#         # to the definition of factorial(). It will continue to do this until factorial(n-1) == factorial(2-1).
#         # here x = 2*factorial(2-1), n is still 2. and factorial(2-1) returns 1. now x is calculated, x = 2*1=2
#         # so, it prints number 2 first.
#         print(x)
#     return x


# print(factorial(5))

"""Python keeps track of the previous values of n for each recursive call. When a recursive function is called,
 a new instance of the function is created and added to the call stack. The current state of the function,
  including the value of its local variables, is stored on this stack. When a function returns,
   the topmost instance of the function is removed from the call stack and its state is restored."""

"""tail recursion example. Here the function called recursively and the last value calculated is f(n-1)
function is not returning to find value of f(n). Tail recursion is faster than normal recursion."""


# def prints(n):
#     if (n < 0):
#         return
#     print(str(n), end=' ')
#
#     # The last executed statement is recursive call
#     prints(n - 1)
#
#
# prints(5)


"""factorial using tail recursion"""


def facto(n, a=1):
    if n <= 1:
        return a
    return facto(n-1, n*a)


print(facto(5))

"""sum of n natural numbers"""


# def tri_recursion(k):
#     if k > 0:
#         result = k + tri_recursion(k-1)
#         print(result)
#     else:
#         result = 0
#     return result
#
#
# print(tri_recursion(5))


"""python program to find LCM of two numbers using recursion"""


# def lcm(a, b):
#     t = a % b
#     if t == 0:
#         return a
#     return a * lcm(b, t) / t
#
#
# print(lcm(12, 5))

# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)
#
# def lcm(a, b):
#     return a * b // gcd(a, b)
#
# print(lcm(12, 5))
"""to find product of two numbers using recursion"""


# def prod(x, y):
#     if y == 0:
#         return 0
#     else:
#         return x + prod(x, y-1)
#
#
# print(prod(10, 1))


"""reverse a string using recursion"""


# def reverse(string):
#     if len(string) == 0:
#         return string
#     else:
#         return reverse(string[1:]) + string[0]
#
#
# a = str(input("Enter the string to be reversed: "))
# print(reverse(a))
