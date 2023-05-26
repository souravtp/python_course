""" to find max of three numbers"""


# def max_of_three(n1, n2, n3):
#     def inner_max():
#         if n2 > n3:
#             return n2
#         elif n3 > n2:
#             return n3
#         else:
#             return n2
#     if inner_max() > n1:
#         return inner_max()
#     elif inner_max() < n1:
#         return n1
#     else:
#         return n1
#
#
# print(max_of_three(1500, 1500, 1500))


# another method
# def max_3(x, y, z):
#     def max_2(y, z):
#         if y > z:
#             return y
#         elif y < z:
#             return z
#         else:
#             return y
#     return max_2(x, max_2(y, z))
#
#
# print(max_3(25, 30, 27))


# factorial of a number
# def factorial(n):
#     if n < 0:
#         return f'number should be 0 or higher'
#     def inner_factorial():
#         prod = 1
#         for i in range(1, n+1):
#             prod *= i
#         return prod
#     return inner_factorial()
#
#
# print(factorial(-5))

