# 1.reverse a number
# x = int(input("Enter the number:"))
# y = str(x)
# rev = ""
# for i in range(len(y)):
#     rev += y[-i-1]
# print(int(rev))

# greatest common divisor
# num = []
# n = int(input("enter number of items to find gcd:"))
# for i in range(n):
#     x = int(input(f'enter number {i}:'))
#     num.append(x)
# gcd = 1
# for j in range(1, min(num)+1):
#     counter = 0
#     for k in num:
#         if k % j == 0:
#             counter += 1
#     if counter == len(num):
#         gcd = j
# print(gcd)


# x = input("enter numbers separated with commas:")
# 2.frequency of characters in a string
# x = input("Enter the sentence:")
# y = input("Enter the letter to count:")
# x_lower = x.lower()
# y_lower = y.lower()
# counter = 0
# for i in x_lower:
#     if i == y.lower():
#         counter += 1
# print(f'the frequency of letter in the string is {counter}')

# or

# z = x_lower.count(y_lower)
# print(f'the count of the letter {y} in string is {z}')

# 3. Leap year or not
# y = int(input("Enter a year:"))
# if y % 4 != 0:
#     print(f'{y} is not a leap year')
# elif y % 100 != 0:
#     print(f'{y} is a leap year')
# elif y % 400 != 0:
#     print(f'{y} is not a leap year')
# else:
#     print(f'{y} is a leap year')

#anoter method
# if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
#     print(f'{y} is a leap year.')
# else:
#     print(f'{y} is a common year.')

# vowels or consonant
# x = input("enter the letter:")
# vowels = ["a", "e", "i", "o", "u"]
# if x.lower() in vowels:
#     print(f'{x} is a vowel')
# else:
#     print(f'{x} is a consonant')

# non-repeating characters in a string
# x = input("enter the string:")
# x_lower = x.lower()
# for i in x.lower():
#     if i.isalnum():
#         if x_lower.count(i) == 1:
#             print(i)

# dictionary of numbers and squares

# n = int(input("Enter the number of elements in the dictionary:"))
# dict1 = {}
# for i in range(n):
#     dict1.update({i+1: (i+1)**2})
# print(dict1)

# or

# for i in range(1, n+1):
#     dict1[i] = i*i

# count letters and numbers
# str1 = input("enter the sentence:")
# num_count = 0
# let_count = 0
# for i in str1:
#     if i.isnumeric():
#         num_count += 1
#     elif i.isalpha():
#         let_count += 1
# print(f"the number of numbers is {num_count} and number of letters is {let_count}")

# dict1 = {"a": 10, "b": 20, "c": 30}
# dsum = 0
# dprod= 1
# for i in dict1:
#     dsum += dict1[i]
#     dprod *= dict1[i]
# print(f'sum = {dsum}, product = {dprod}')

# sort list with element length
# list1 = ["VW", "Suzuki", "Mitsubishi", "BMW", "Hyundai", "Mercedes"]
# list1.sort(reverse=True, key=len)
# print(list1)

# pgm to check for sublist in list
# list1 = [6, 78, 54, 65, 21, 13, 9, 88]
# sublist = input("enter sublist elements separated with commas:").split(",")
# sublist = [int(i) for i in sublist]
# if set(sublist).issubset(set(list1)):
#     print(f'sublist exist')
# else:
#     print(f'sublist does not exist')

# pgm to find numbers between 100 and 400 where each digit is even
# for i in range(100, 401):
#     if (i%10)%2 == 0 and ((i%100)//10)%2 == 0 and (i//100)%2 == 0:
#         print(i)