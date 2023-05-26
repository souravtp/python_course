# multiply all numbers in a list by using function
# def multiply_elem(list1):
#     prod = 1
#     for i in list1:
#         prod *= i
#     return prod
#
#
# my_list = [1, 2, 3, 4, 5]
# print(multiply_elem(my_list))


# python program to reverse a string
# def reverse(str1):
#     rev = ""
#     for i in range(len(str1)):
#         rev += str1[-i-1]
#     return rev
#
#
# str1 = input("enter string:")
# print(reverse(str1))


# python function to calculate the factorial of a number
# def factorial(n):
#     if n < 0:
#         return None
#     elif n < 2:
#         return 1
#     prod = 1
#     for i in range(1, n+1):
#         prod *= i
#     return prod
#
#
# print(factorial(0))


# function to check if a number is prime or not
# def is_prime(n):
#     counter = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             counter += 1
#     if counter == 2:
#         return f'{n} is prime'
#     else:
#         return f'{n} is not prime'
#
#
# print(is_prime(7))
#
# for j in range(1, 100):
#     print(is_prime(j))


# generate a python list of all even numbers between 4 and 30
# def even_num(m=4, n=30):
#     list1 = []
#     for i in range(m, n):
#         if i % 2 == 0:
#             list1.append(i)
#     return list1
#
#
# print(even_num(5, 30))
