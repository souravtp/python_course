# to find sum of n natural numbers
# def sumofnat(n):
#     try:
#         sumn = 0
#         for i in range(n+1):
#             sumn += i
#         return sumn
#     except NameError:
#         print("only enter numbers")


# to find maximum of three numbers
# def num_max(numbers):
#     largest = 0
#     for i in numbers:
#         if i > largest:
#             largest = i
#     return largest
#
#
# x = input("enter numbers separated with commas:")
# list1 = x.split(",")
# list1 = [int(i) for i in list1]
# print(num_max(list1))


# define a function which counts vowels and consonants in a word
# def vowel_consonant(str1):
#     vowels = ["a", "e", "i", "o", "u"]
#     str1 = str1.lower()
#     cons = 0
#     vow = 0
#     for i in str1:
#         if i.isalpha():
#             if i in vowels:
#                 vow += 1
#             elif i not in vowels:
#                 cons += 1
#     return f'number of vowels in the given word is {vow}, number of consonants is {cons}'
#
#
# my_str = input("enter the word")
# print(vowel_consonant(my_str))


# pgm to accept two numbers and returns the sum
# def sum1(x, y):
#     return x+y
#
#
# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# print(sum1(a, b))


# a function that accepts different values as parameters and returns a list
# def make_list(*x):
#     return list(x)
#
# print(make_list("name2", 5, "hello", True))
#
#
# function accepts dictionary as parameter
# def dict_fun(**elem):
#     return elem
#
#
# print(dict_fun(food1='biryani', food2='dosa', food3='chapati'))


